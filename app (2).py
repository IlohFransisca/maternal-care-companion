import streamlit as st
import requests
import os

# Hugging Face Inference API
key = st.secrets.get("HUGGINGFACE_API_KEY", None)
HUGGINGFACE_HEADERS = {"Authorization": f"Bearer {key}"} if key else {}


def query_huggingface(payload):
    response = requests.post(HUGGINGFACE_API_URL, headers=HUGGINGFACE_HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"❌ Error: {response.status_code} - {response.json()}"

# Streamlit UI
st.set_page_config(page_title="MobiMum: Maternal Care Companion")
st.title("🤰 MobiMum: Maternal Care Companion")
st.markdown("Empowering expectant mothers with safe, friendly, AI-powered maternal health advice.")

with st.form("input_form"):
    user_question = st.text_area("📝 Ask a question about maternal health:")
    submitted = st.form_submit_button("Get Advice")

if submitted and user_question:
    with st.spinner("Thinking..."):
        prompt = f"You are MobiMum, an empathetic AI maternal health advisor. Answer clearly and respectfully:\n\nUser: {user_question}\nMobiMum:"
        result = query_huggingface({"inputs": prompt})
        st.success("💡 MobiMum Advice:")
        st.write(result)
else:
    st.info("Enter a question to get started.")

st.markdown("---")
st.caption("🚀 Built with ❤️ using Streamlit and Hugging Face.")
