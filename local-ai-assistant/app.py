import streamlit as st
from llm_client import call_llm
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="Local AI Assistant", layout="centered")

st.title("🧠 Local AI Assistant")

# ── Sidebar: Inference Settings ─────────────────────────
st.sidebar.header("Inference Settings")

model = st.sidebar.selectbox(
    "Model",
    ["tinyllama", "gemma:4b"]
)

temperature = st.sidebar.slider(
    "Temperature",
    0.0, 1.0, 0.6, 0.05
)

top_p = st.sidebar.slider(
    "Top-P (nucleus sampling)",
    0.1, 1.0, 0.9, 0.05
)

top_k = st.sidebar.slider(
    "Top-K",
    1, 100, 40, 1
)

# Advanced setting (optional)
with st.sidebar.expander("Advanced"):
    min_p = st.slider(
        "Min-P (stability)",
        0.0, 0.2, 0.0, 0.01
    )

max_tokens = st.sidebar.slider(
    "Max Tokens",
    50, 512, 200, 25
)

# ── Main UI ─────────────────────────────────────────────
user_input = st.text_area("Ask something...")

if st.button("Generate Response"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}"

            output = call_llm(
                prompt=full_prompt,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                top_k=top_k,
                min_p=min_p
            )

        st.markdown("### Response")
        st.write(output)