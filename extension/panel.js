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

const CLAIM_VERDICT_COLORS = {
  supported: "#22c55e",
  contradicted: "#ef4444",
  mixed: "#eab308",
  unverifiable: "#9ca3af",
};

const CLAIM_VERDICT_LABELS = {
  supported: "Supported",
  contradicted: "Contradicted",
  mixed: "Mixed",
  unverifiable: "Unverifiable",
};

const ACTION_MAP = {
  safe: {
    label: "Safe to share",
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
    cls: "action-safe",
  },
  caution: {
    label: "Needs caution",
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    cls: "action-caution",
  },
  false: {
    label: "Likely false",
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
    cls: "action-false",
  },
  unknown: {
    label: "Can\u2019t verify yet",
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    cls: "action-unknown",
  },
};

function getAction(score, verdict) {
  if (verdict === "unverifiable") return ACTION_MAP.unknown;
  if (score <= 40) return ACTION_MAP.false;
  if (score <= 60) return ACTION_MAP.caution;
  return ACTION_MAP.safe;
}

const CONFIDENCE_LABELS = { high: "High confidence", medium: "Medium confidence", low: "Low confidence" };

function getDomain(url) {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return url;
  }
}

function animateScore(target, color) {
  const CIRCUMFERENCE = 2 * Math.PI * 34;
  const fill = document.getElementById("donut-fill");
  const valueEl = document.getElementById("score-value");

  fill.style.stroke = color;
  fill.style.strokeDasharray = `${CIRCUMFERENCE}`;
  fill.style.strokeDashoffset = `${CIRCUMFERENCE}`;

  requestAnimationFrame(() => {
    const offset = CIRCUMFERENCE - (target / 100) * CIRCUMFERENCE;
    fill.style.strokeDashoffset = `${offset}`;
  });

  const wrapper = document.querySelector(".donut-wrapper");
  if (wrapper) {
    wrapper.style.filter = `drop-shadow(0 0 24px ${color}40)`;
  }

  const duration = 800;
  const start = performance.now();
  function step(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    valueEl.textContent = Math.round(eased * target);
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

function renderResult(result, originalText) {
  const color = getScoreColor(result.score);

  const quoteEl = document.getElementById("original-text");
  quoteEl.textContent = originalText || "";
  quoteEl.hidden = !originalText;

  const action = getAction(result.score, result.verdict);
  const actionEl = document.getElementById("action-verdict");
  actionEl.className = `action-verdict ${action.cls}`;
  document.getElementById("action-icon").innerHTML = action.icon;
  document.getElementById("action-label").textContent = action.label;

  const confLevel = document.getElementById("confidence-level");
  const confReason = document.getElementById("confidence-reason");
  const conf = result.confidence || "low";
  confLevel.textContent = CONFIDENCE_LABELS[conf] || CONFIDENCE_LABELS.low;
  confLevel.className = `confidence-level conf-${conf}`;
  confReason.textContent = result.confidence_reason ? ` \u00B7 ${result.confidence_reason}` : "";

  animateScore(result.score, color);

  document.getElementById("tldr").textContent = result.tldr || "";

  const claimsList = document.getElementById("claims-list");
  claimsList.innerHTML = "";
  result.claims.forEach((claim) => {
    const li = document.createElement("li");

    const text = typeof claim === "string" ? claim : claim.text;
    const verdict = typeof claim === "string" ? "unverifiable" : claim.verdict;

    const textSpan = document.createElement("span");
    textSpan.className = "claim-text";
    textSpan.textContent = text;

    const label = document.createElement("span");
    label.className = `claim-verdict-label claim-verdict-${verdict}`;
    label.textContent = CLAIM_VERDICT_LABELS[verdict] || "Unknown";

    li.appendChild(textSpan);
    li.appendChild(label);
    claimsList.appendChild(li);
  });

  document.getElementById("claims-count").textContent = result.claims.length;

  document.getElementById("explanation").textContent = result.explanation;

  const STANCE_ORDER = { supporting: 0, contradicting: 1, neutral: 2 };
  const STANCE_LABELS = { supporting: "Supporting", contradicting: "Contradicting", neutral: "Neutral" };

  const sortedSources = [...(result.sources || [])].sort(
    (a, b) => (STANCE_ORDER[a.stance] ?? 2) - (STANCE_ORDER[b.stance] ?? 2)
  );

  const sourcesList = document.getElementById("sources-list");
  sourcesList.innerHTML = "";
  sortedSources.forEach((source) => {
    const domain = getDomain(source.url);
    const stance = source.stance || "neutral";

    const card = document.createElement("a");
    card.className = "source-card";
    card.href = source.url;
    card.target = "_blank";
    card.rel = "noopener";
    const favicon = document.createElement("img");
    favicon.className = "source-favicon";
    favicon.src = `https://www.google.com/s2/favicons?sz=16&domain=${domain}`;
    favicon.alt = "";
    favicon.width = 16;
    favicon.height = 16;

    const info = document.createElement("div");
    info.className = "source-info";

    const domainRow = document.createElement("span");
    domainRow.className = "source-domain";
    domainRow.textContent = domain;

    const domainLine = document.createElement("span");
    domainLine.className = "source-domain-line";
    domainLine.appendChild(domainRow);

    const stanceTag = document.createElement("span");
    stanceTag.className = `source-stance stance-tag-${stance}`;
    stanceTag.textContent = STANCE_LABELS[stance] || "Neutral";
    domainLine.appendChild(stanceTag);

    const titleEl = document.createElement("span");
    titleEl.className = "source-title";
    titleEl.textContent = source.title || source.url;

    info.appendChild(domainLine);
    info.appendChild(titleEl);
    card.appendChild(favicon);
    card.appendChild(info);
    sourcesList.appendChild(card);
  });

  document.getElementById("sources-count").textContent = result.sources.length;

  document.querySelectorAll(".collapsible").forEach((el) => el.classList.remove("open"));

  const checkedAt = document.getElementById("checked-at");
  const now = new Date();
  checkedAt.textContent = `Checked ${now.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" })}`;

  showState("result");
}

function resetState() {
  chrome.storage.local.set({
    factify_state: "idle",
    factify_text: null,
    factify_result: null,
    factify_error: null,
  });
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
        updateLoadingSteps();
        return;
      }

      if (factify_state === "done" && factify_result) {
        renderResult(factify_result, factify_result.original_text || factify_text);
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

const STEP_ORDER = ["extracting", "searching", "analyzing"];

function updateLoadingSteps() {
  chrome.storage.local.get(["factify_loading_step", "factify_step_meta"], (data) => {
    const current = data.factify_loading_step || "extracting";
    const meta = data.factify_step_meta || {};
    const currentIdx = STEP_ORDER.indexOf(current);

    document.querySelectorAll(".loading-step").forEach((el) => {
      const step = el.dataset.step;
      const stepIdx = STEP_ORDER.indexOf(step);
      el.classList.remove("active", "done", "pending");

      if (stepIdx < currentIdx) {
        el.classList.add("done");
      } else if (stepIdx === currentIdx) {
        el.classList.add("active");
      } else {
        el.classList.add("pending");
      }
    });

    document.querySelectorAll(".step-connector").forEach((el, i) => {
      el.classList.toggle("filled", i < currentIdx);
    });

    const progressFill = document.getElementById("loading-progress-fill");
    if (progressFill) {
      const pct = ((currentIdx + 1) / STEP_ORDER.length) * 100;
      progressFill.style.width = `${Math.min(pct, 95)}%`;
    }

    const searchMeta = document.getElementById("step-meta-searching");
    const analyzeMeta = document.getElementById("step-meta-analyzing");
    if (meta.claims_found && currentIdx >= 1) {
      searchMeta.textContent = `${meta.claims_found} claim${meta.claims_found > 1 ? "s" : ""} found`;
    } else {
      searchMeta.textContent = "";
    }
    if (meta.sources_found && currentIdx >= 2) {
      analyzeMeta.textContent = `${meta.sources_found} source${meta.sources_found > 1 ? "s" : ""} found`;
    } else {
      analyzeMeta.textContent = "";
    }
  });
}

document.addEventListener("click", (e) => {
  const toggle = e.target.closest(".collapsible-toggle");
  if (!toggle) return;
  const section = toggle.closest(".collapsible");
  section.classList.toggle("open");
});

document.getElementById("check-another").addEventListener("click", resetState);
document.getElementById("error-check-another").addEventListener("click", resetState);

chrome.storage.onChanged.addListener((changes, area) => {
  if (area !== "local") return;
  if (changes.factify_state) render();
  if (changes.factify_loading_step) updateLoadingSteps();
});

render();
