# SupportLLM

Fine-tune a small instruction-tuned LLM for customer support response generation.

This project demonstrates:
- synthetic instruction dataset creation
- LoRA/QLoRA fine-tuning
- response quality and safety evaluation
- a Streamlit customer-support demo

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Prepare data

```bash
python scripts/prepare_dataset.py --input data/sample_support.jsonl --output data/processed/train.jsonl
```

## Train

```bash
python scripts/train_qlora.py --config configs/qlora_config.yaml --train_file data/processed/train.jsonl
```

## Inference

```bash
python scripts/inference.py --message "I was charged twice this month. Can you help?"
```

## Demo

```bash
streamlit run app/streamlit_app.py
```
