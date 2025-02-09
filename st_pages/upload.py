import os
from .page import Page
import streamlit as st


class UploadPage(Page):
    def render(self) -> None:
        st.title("AI-Powered Flash Cards!")
        st.markdown("---")
        st.html("<h2>Upload Your File 📂</h2>")
        st.write("Welcome to trash revision. Please upload a file so we can make some flash cards.")

    def upload_handler(self) -> None:
        uploaded_file = st.file_uploader("Choose a file", type=["txt"])

        if uploaded_file is not None:
            st.success("File uploaded successfully! Generating Flash Cards...")

            self.save_uploaded_file(uploaded_file)
            self.create_flashcards()
            self.switch_to_status()

    def save_uploaded_file(self, uploaded_file) -> None:
        file_path = os.path.join("uploaded_files", "questions.txt")

        with open(file_path, mode="wb") as f:
            f.write(uploaded_file.getbuffer())

    def create_flashcards(self) -> None:
        os.system("python gen_qna.py")

    def switch_to_status(self) -> None:
        st.write("Navigating to Status Page...")
        st.session_state.page = "page_2"
        st.rerun()
