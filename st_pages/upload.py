import os
import streamlit as st

from .page import Page



class UploadPage(Page):
    def render(self) -> None:
        st.title("Student Pilot")
        self.sep()
        st.html("<h1>Upload Your File</h1>")
        st.html("<b>Please upload a file so we can generate some notes</b>")
        self.upload_handler()

    def upload_handler(self) -> None:
        uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf"])

        if uploaded_file is not None:
            st.success("File uploaded successfully! Generating Flash Cards...")
            st.html("<br>")

            self.remove_previous_files()
            self.save_uploaded_file(uploaded_file)
            self.create_flashcards()
            self.switch_to_status()

    def remove_previous_files(self) -> None:
        for file in os.listdir("uploaded_files"):
            os.system(f"rm {os.path.join('uploaded_files', file)}")
            print(f"rm {os.path.join('uploaded_files', file)}")

    def save_uploaded_file(self, uploaded_file) -> None:
        extension = "txt"
        if "pdf" in uploaded_file.type:
            extension = "pdf"

        file_path = os.path.join("uploaded_files", f"questions.{extension}")

        with open(file_path, mode="wb") as f:
            f.write(uploaded_file.getbuffer())

    def create_flashcards(self) -> None:
        os.system("python ai_handler.py")

    def switch_to_status(self) -> None:
        st.write("Navigating to Status Page...")
        st.session_state.page = "page_2"
        st.rerun()
