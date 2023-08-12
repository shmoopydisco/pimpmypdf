import streamlit as st
import ocrmypdf


def main():
    # streamlit app that recieves a pdf and runs OCRMypdf on it
    st.title("Pimp My PDF")
    st.write("This app uses OCRmyPDF to convert your PDF to a searchable PDF.")
    st.write("Please upload your PDF below.")
    uploaded_file = st.file_uploader("Choose a file", type="pdf")
    if uploaded_file is not None:
        st.write("Your PDF is being processed. Please wait...")
        ocrmypdf.ocr(
            uploaded_file.name,
            "output.pdf",
            deskew=True,
            clean=True,
            rotate_pages=True,
            remove_background=True,
            optimize=3,
            force_ocr=True,
        )
        st.write("Your PDF has been processed. Please download it below.")
        st.download_button(
            label="Download your processed PDF",
            data="output.pdf",
            file_name="output.pdf",
            mime="application/pdf",
        )


if __name__ == "__main__":
    main()
