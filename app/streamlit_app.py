import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from supportllm.prompts import build_prompt

st.set_page_config(page_title="SupportLLM", page_icon="💬")
st.title("SupportLLM")
st.write("Generate polite customer support responses.")

model_name = st.text_input("Model", "Qwen/Qwen2.5-1.5B-Instruct")
category = st.selectbox("Category", ["general", "billing", "account", "technical", "shipping", "refund"])
message = st.text_area("Customer message", "I was charged twice this month. Can you help?")

if st.button("Generate response"):
    with st.spinner("Loading model and generating response..."):
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
        generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
        output = generator(build_prompt(message, category), max_new_tokens=180, do_sample=False)[0]["generated_text"]
        st.write(output.split("### Response:")[-1].strip())
