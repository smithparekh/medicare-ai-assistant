import streamlit as st


def pdf_upload():
    return st.file_uploader("Upload a PDF file", type=["pdf"],accept_multiple_files=True,
                            help="upload one or more PDF files to process.")