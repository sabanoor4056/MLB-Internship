
import streamlit as st
import easyocr
from PIL import Image, ImageOps, ImageEnhance
import numpy as np

# Page configuration
st.set_page_config(
    page_title="OCR Document Reader",
    page_icon="📄",
    layout="wide"
)

# Application title
st.title("📄 Simple OCR Document Reader")

st.write(
    "Upload an image and extract text using EasyOCR."
)

# Initialize EasyOCR
@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'], gpu=False)

reader = load_reader()

# Image uploader
uploaded_file = st.file_uploader(
    "Upload your document image",
    type=["jpg", "jpeg", "png"]
)

# Enhancement checkbox
enhance = st.checkbox(
    "Apply Image Enhancement",
    value=True
)

# Process image
if uploaded_file is not None:

    # Open image
    original = Image.open(uploaded_file).convert("RGB")

    # Display original image
    st.subheader("Original Image")
    st.image(original, use_container_width=True)

    # Prepare image
    processed = original

    if enhance:
        processed = ImageOps.grayscale(processed)

        processed = ImageEnhance.Contrast(
            processed
        ).enhance(1.5)

        st.subheader("Enhanced Image")
        st.image(processed, use_container_width=True)

    # Extract text button
    if st.button("Extract Text"):

        with st.spinner("Reading text from image..."):

            # OCR processing
            results = reader.readtext(
                np.array(processed),
                detail=0,
                paragraph=True
            )

            extracted_text = "\n".join(results)

        # Display extracted text
        st.subheader("Extracted Text")

        if extracted_text.strip():
            st.text_area(
                "Recognized Text",
                value=extracted_text,
                height=250
            )

            # Download text file
            st.download_button(
                label="Download Extracted Text",
                data=extracted_text,
                file_name="extracted_text.txt",
                mime="text/plain"
            )

            st.success("Text extracted successfully!")

        else:
            st.warning("No text detected in this image.")

else:
    st.info("Please upload an image to get started.")
