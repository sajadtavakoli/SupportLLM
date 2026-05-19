import argparse
import json
from pathlib import Path

def format_example(row):
    text = f"""### Instruction:
{row.get('instruction', 'Write a helpful customer support response.')}

### Category:
{row.get('category', 'general')}

### Customer message:
{row['message']}

### Response:
{row['response']}"""
    return {"text": text, **row}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.input, encoding="utf-8") as fin, open(args.output, "w", encoding="utf-8") as fout:
        for line in fin:
            fout.write(json.dumps(format_example(json.loads(line))) + "\n")

if __name__ == "__main__":
    main()
