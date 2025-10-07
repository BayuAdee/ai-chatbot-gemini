import streamlit as st
import requests

FLASK_BACKEND_URL = "https://ai-chatbot-gemini-backend.replit.dev/chat"

st.set_page_config(page_title="Asisten Belajar", layout="wide")
st.title("🤖 Asisten Belajar AI")

st.markdown("Masukkan pertanyaan di bawah ini untuk berbicara dengan chatbot Gemini:")

user_input = st.text_input("Pertanyaan:")

if st.button("Kirim"):
    if user_input:
        with st.spinner("Sedang berpikir..."):
            response = requests.post(FLASK_BACKEND_URL, json={"query": user_input})
            data = response.json()
            st.markdown("### Jawaban:")
            st.info(data.get("response", data.get("error", "Tidak ada jawaban")))
    else:
        st.warning("Tolong masukkan pertanyaan terlebih dahulu.")
