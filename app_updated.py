
import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="MobiMum: Maternal Care Companion")
st.title("🤰 MobiMum: Maternal Care Companion")
st.markdown("Empowering expectant mothers with safe, friendly, AI-powered maternal health advice.")

with st.form("input_form"):
    user_question = st.text_area("📝 Ask a question about maternal health:")
    submitted = st.form_submit_button("Get Advice")

if submitted and user_question:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "You are MobiMum, an AI maternal health companion. "
                        "Give caring, accurate, culturally respectful, and medically sound advice. "
                        "Always encourage seeing a qualified healthcare provider if needed."
                    )},
                    {"role": "user", "content": user_question}
                ],
                temperature=0.7,
                max_tokens=500
            )
            answer = response.choices[0].message.content
            st.success("💡 MobiMum Advice:")
            st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Enter a question to get started.")

st.markdown("---")
st.caption("🚀 Built with ❤️ using Streamlit and OpenAI.")
