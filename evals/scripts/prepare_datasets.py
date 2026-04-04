"""Download and curate benchmark datasets into the unified schema.

Usage:
    python -m evals.scripts.prepare_datasets          # both datasets
    python -m evals.scripts.prepare_datasets --only politifact
    python -m evals.scripts.prepare_datasets --only averitec
"""

import argparse
import json
import random
from pathlib import Path

from datasets import load_dataset

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "datasets"

POLITIFACT_LABEL_MAP = {
    "true": {
        "expected_verdicts": ["true"],
        "expected_score_range": [80, 100],
    },
    "mostly-true": {
        "expected_verdicts": ["mostly_true", "true"],
        "expected_score_range": [60, 100],
    },
    "half-true": {
        "expected_verdicts": ["mixed", "mostly_true", "mostly_false"],
        "expected_score_range": [35, 70],
    },
    "barely-true": {
        "expected_verdicts": ["mostly_false", "mixed"],
        "expected_score_range": [20, 50],
    },
    "false": {
        "expected_verdicts": ["false", "mostly_false"],
        "expected_score_range": [0, 40],
    },
    "pants-fire": {
        "expected_verdicts": ["false"],
        "expected_score_range": [0, 20],
    },
}

AVERITEC_LABEL_MAP = {
    "Supported": {
        "expected_verdicts": ["true", "mostly_true"],
        "expected_score_range": [60, 100],
    },
    "Refuted": {
        "expected_verdicts": ["false", "mostly_false"],
        "expected_score_range": [0, 40],
    },
    "Not Enough Evidence": {
        "expected_verdicts": ["unverifiable", "mixed"],
        "expected_score_range": [30, 60],
    },
    "Conflicting Evidence/Cherrypicking": {
        "expected_verdicts": ["mixed", "mostly_true", "mostly_false"],
        "expected_score_range": [25, 75],
    },
}

LIAR_LABEL_NAMES = {
    0: "false",
    1: "half-true",
    2: "mostly-true",
    3: "true",
    4: "barely-true",
    5: "pants-fire",
}


def _stratified_sample(rows_by_label: dict[str, list], total: int, seed: int = 42) -> list:
    """Sample evenly across label categories, distributing remainder to smaller groups first."""
    rng = random.Random(seed)
    labels = sorted(rows_by_label.keys())
    per_label = total // len(labels)
    remainder = total - per_label * len(labels)

    sampled: list = []
    for i, label in enumerate(labels):
        pool = rows_by_label[label]
        n = per_label + (1 if i < remainder else 0)
        if len(pool) < n:
            sampled.extend(pool)
        else:
            sampled.extend(rng.sample(pool, n))

    rng.shuffle(sampled)
    return sampled


def prepare_politifact(total: int = 50) -> dict:
    ds = load_dataset("ucsbnlp/liar", split="test", revision="refs/convert/parquet")

    rows_by_label: dict[str, list] = {label: [] for label in POLITIFACT_LABEL_MAP}
    for row in ds:
        label = LIAR_LABEL_NAMES.get(row["label"])
        if label is None or label not in POLITIFACT_LABEL_MAP:
            continue

        statement = row.get("statement", "").strip()
        if not statement:
            continue

        rows_by_label[label].append({
            "statement": statement,
            "label": label,
            "speaker": row.get("speaker", ""),
            "context": row.get("subject", ""),
        })

    sampled = _stratified_sample(rows_by_label, total)

    samples = []
    for i, row in enumerate(sampled):
        mapping = POLITIFACT_LABEL_MAP[row["label"]]
        samples.append({
            "id": f"pf_{i + 1:03d}",
            "claim": row["statement"],
            "label": row["label"],
            "expected_verdicts": mapping["expected_verdicts"],
            "expected_score_range": mapping["expected_score_range"],
            "gold_evidence": None,
        })

    return {
        "metadata": {
            "name": "PolitiFact",
            "source": "ucsbnlp/liar",
            "description": "Real political statements from PolitiFact with 6-level verdicts",
            "sample_count": len(samples),
        },
        "samples": samples,
    }


def _extract_averitec_evidence(questions: list[dict]) -> list[dict]:
    """Convert AVeriTeC question-answer pairs into {title, url, content} source dicts."""
    sources = []
    seen_urls: set[str] = set()

    for qa in questions:
        question = qa.get("question", "")
        for ans in qa.get("answers", []):
            answer_text = ans.get("answer", "").strip()
            source_url = ans.get("source_url", "").strip()
            if not answer_text or not source_url:
                continue
            if source_url in seen_urls:
                continue
            seen_urls.add(source_url)

            sources.append({
                "title": question,
                "url": source_url,
                "content": answer_text,
            })

    return sources


def prepare_averitec(total: int = 50) -> dict:
    ds = load_dataset("pminervini/averitec", split="dev")

    rows_by_label: dict[str, list] = {label: [] for label in AVERITEC_LABEL_MAP}
    for row in ds:
        label = row.get("label", "").strip()
        if label not in AVERITEC_LABEL_MAP:
            continue

        claim = row.get("claim", "").strip()
        if not claim:
            continue

        evidence = _extract_averitec_evidence(row.get("questions", []))
        if not evidence:
            continue

        rows_by_label[label].append({
            "claim": claim,
            "label": label,
            "evidence": evidence,
            "justification": row.get("justification", ""),
        })

    sampled = _stratified_sample(rows_by_label, total)

    samples = []
    for i, row in enumerate(sampled):
        mapping = AVERITEC_LABEL_MAP[row["label"]]
        samples.append({
            "id": f"av_{i + 1:03d}",
            "claim": row["claim"],
            "label": row["label"],
            "expected_verdicts": mapping["expected_verdicts"],
            "expected_score_range": mapping["expected_score_range"],
            "gold_evidence": row["evidence"],
        })

    return {
        "metadata": {
            "name": "AVeriTeC",
            "source": "pminervini/averitec",
            "description": "Real-world claims with web-sourced evidence and 4-level verdicts",
            "sample_count": len(samples),
        },
        "samples": samples,
    }


def main():
    parser = argparse.ArgumentParser(description="Prepare benchmark datasets")
    parser.add_argument(
        "--only",
        choices=["politifact", "averitec"],
        help="Prepare only one dataset",
    )
    parser.add_argument(
        "--samples",
        type=int,
        default=50,
        help="Number of samples per dataset (default: 50)",
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.only != "averitec":
        print("Preparing PolitiFact (LIAR) dataset...")
        pf = prepare_politifact(args.samples)
        out = OUTPUT_DIR / "benchmark_politifact.json"
        out.write_text(json.dumps(pf, indent=2, ensure_ascii=False))
        label_counts: dict[str, int] = {}
        for s in pf["samples"]:
            label_counts[s["label"]] = label_counts.get(s["label"], 0) + 1
        print(f"  Written {len(pf['samples'])} samples to {out.name}")
        print(f"  Label distribution: {label_counts}")

    if args.only != "politifact":
        print("Preparing AVeriTeC dataset...")
        av = prepare_averitec(args.samples)
        out = OUTPUT_DIR / "benchmark_averitec.json"
        out.write_text(json.dumps(av, indent=2, ensure_ascii=False))
        label_counts = {}
        for s in av["samples"]:
            label_counts[s["label"]] = label_counts.get(s["label"], 0) + 1
        print(f"  Written {len(av['samples'])} samples to {out.name}")
        print(f"  Label distribution: {label_counts}")

    print("Done.")


if __name__ == "__main__":
    main()
