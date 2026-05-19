import argparse
import json
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from supportllm.eval_utils import evaluate_response

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", required=True, help="JSONL with a response field")
    args = parser.parse_args()

    rows = [json.loads(line) for line in open(args.predictions, encoding="utf-8")]
    scores = [evaluate_response(row["response"]) for row in rows]
    summary = {
        "n": len(scores),
        "helpful_tone_rate": sum(s["helpful_tone"] for s in scores) / max(len(scores), 1),
        "too_short_rate": sum(s["too_short"] for s in scores) / max(len(scores), 1),
        "avg_word_count": sum(s["word_count"] for s in scores) / max(len(scores), 1),
    }

    Path("results").mkdir(exist_ok=True)
    Path("results/metrics.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
