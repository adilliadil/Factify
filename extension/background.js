const API_URL = "http://localhost:8000";

chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "factify_check",
    title: "Fact This",
    contexts: ["selection"],
  });

  chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true });
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId === "factify_check" && info.selectionText) {
    await chrome.sidePanel.open({ tabId: tab.id });
    runFactCheck(info.selectionText);
  }
});

chrome.commands.onCommand.addListener(async (command) => {
  if (command === "fact-check") {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab) return;

    await chrome.sidePanel.open({ tabId: tab.id });

    const results = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => window.getSelection().toString(),
    });
    const text = results?.[0]?.result;
    if (text) runFactCheck(text);
  }
});

async function runFactCheck(text) {
  const trimmed = text.trim();
  if (!trimmed) return;

  await chrome.storage.local.set({
    factify_state: "loading",
    factify_text: trimmed,
    factify_result: null,
    factify_error: null,
    factify_loading_step: "extracting",
  });

  try {
    const response = await fetch(`${API_URL}/factcheck/stream`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: trimmed }),
    });

    if (!response.ok) {
      const err = await response.json().catch(() => ({}));
      throw new Error(err.detail || err.error || `Server error ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const parts = buffer.split("\n\n");
      buffer = parts.pop();

      for (const part of parts) {
        const lines = part.trim().split("\n");
        let eventType = "";
        let eventData = "";
        for (const line of lines) {
          if (line.startsWith("event: ")) eventType = line.slice(7);
          if (line.startsWith("data: ")) eventData = line.slice(6);
        }
        if (!eventType || !eventData) continue;

        const parsed = JSON.parse(eventData);

        if (eventType === "step") {
          await chrome.storage.local.set({
            factify_loading_step: parsed.step,
            factify_step_meta: parsed,
          });
        } else if (eventType === "result") {
          await chrome.storage.local.set({
            factify_state: "done",
            factify_result: parsed,
            factify_error: null,
            factify_loading_step: null,
            factify_step_meta: null,
          });
        }
      }
    }
  } catch (e) {
    await chrome.storage.local.set({
      factify_state: "error",
      factify_result: null,
      factify_error: e.message || "Something went wrong",
      factify_loading_step: null,
      factify_step_meta: null,
    });
  }
}
