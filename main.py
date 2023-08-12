import streamlit as st
import ocrmypdf


@st.cache_data
def run_ocr(input_file, output_file):
    ocrmypdf.ocr(
        input_file=input_file,
        output_file=output_file,
        rotate_pages=True,
        force_ocr=True,
        progress_bar=False,
    )


def main():
    # streamlit app that recieves a pdf and runs OCRMypdf on it
    st.title("Pimp My PDF")
    st.write("This app uses OCRmyPDF to convert your PDF to a searchable PDF.")
    st.write("Please upload your PDF below.")
    uploaded_file = st.file_uploader("Choose a file", type="pdf")
    if uploaded_file is not None:
        st.write("Your PDF is being processed. Please wait...")
        run_ocr(uploaded_file, "output.pdf")
        st.write("Your PDF has been processed. Please download it below.")
        with open("output.pdf", "rb") as f:
            st.download_button(
                label="Download your processed PDF",
                data=f,
                file_name=f"{uploaded_file.name.rstrip('.pdf')}_ocr.pdf",
                mime="application/pdf",
            )


if __name__ == "__main__":
    main()
