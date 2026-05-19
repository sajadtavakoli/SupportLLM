import argparse
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from supportllm.prompts import build_prompt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="Qwen/Qwen2.5-1.5B-Instruct")
    parser.add_argument("--message", required=True)
    parser.add_argument("--category", default="general")
    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(args.model, device_map="auto", trust_remote_code=True)
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    output = generator(build_prompt(args.message, args.category), max_new_tokens=180, do_sample=False)[0]["generated_text"]
    print(output.split("### Response:")[-1].strip())

if __name__ == "__main__":
    main()
