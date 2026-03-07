const states = {
  empty: document.getElementById("empty-state"),
  loading: document.getElementById("loading-state"),
  result: document.getElementById("result-state"),
  error: document.getElementById("error-state"),
};

function showState(name) {
  Object.entries(states).forEach(([key, el]) => {
    el.hidden = key !== name;
  });
}

function getScoreColor(score) {
  if (score <= 20) return "#ef4444";
  if (score <= 40) return "#f97316";
  if (score <= 60) return "#eab308";
  if (score <= 80) return "#84cc16";
  return "#22c55e";
}

const VERDICT_LABELS = {
  false: "False",
  mostly_false: "Mostly False",
  mixed: "Mixed",
  mostly_true: "Mostly True",
  true: "True",
  unverifiable: "Unverifiable",
};

function renderResult(result) {
  const color = getScoreColor(result.score);

  const ring = document.getElementById("score-ring");
  ring.style.borderColor = color;
  document.getElementById("score-value").textContent = result.score;

  const badge = document.getElementById("verdict-badge");
  badge.textContent = VERDICT_LABELS[result.verdict] || result.verdict;
  badge.style.backgroundColor = color;

  const claimsList = document.getElementById("claims-list");
  claimsList.innerHTML = "";
  result.claims.forEach((claim) => {
    const li = document.createElement("li");
    li.textContent = claim;
    claimsList.appendChild(li);
  });

  document.getElementById("explanation").textContent = result.explanation;

  const sourcesList = document.getElementById("sources-list");
  sourcesList.innerHTML = "";
  result.sources.forEach((source) => {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = source.url;
    a.target = "_blank";
    a.rel = "noopener";
    a.textContent = source.title || source.url;
    li.appendChild(a);
    sourcesList.appendChild(li);
  });

  showState("result");
}

function render() {
  chrome.storage.local.get(
    ["factify_state", "factify_text", "factify_result", "factify_error"],
    (data) => {
      const { factify_state, factify_text, factify_result, factify_error } = data;

      if (!factify_state || factify_state === "idle") {
        showState("empty");
        return;
      }

      if (factify_state === "loading") {
        document.getElementById("loading-claim").textContent =
          factify_text?.length > 120
            ? factify_text.substring(0, 120) + "..."
            : factify_text || "";
        showState("loading");
        return;
      }

      if (factify_state === "done" && factify_result) {
        renderResult(factify_result);
        return;
      }

      if (factify_state === "error") {
        document.getElementById("error-text").textContent =
          factify_error || "Something went wrong";
        showState("error");
        return;
      }

      showState("empty");
    }
  );
}

chrome.storage.onChanged.addListener((changes, area) => {
  if (area === "local" && changes.factify_state) {
    render();
  }
});

render();
