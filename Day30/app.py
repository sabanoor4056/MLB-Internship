
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.set_page_config(
    page_title="Image Segmentation Tool",
    page_icon="🖼️"
)

st.title("Image Segmentation Tool")
st.write(
    "Upload an image and apply different "
    "image segmentation techniques."
)

# Upload image
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

method = st.selectbox(
    "Select Segmentation Method",
    [
        "Grayscale",
        "Binary Thresholding",
        "Adaptive Thresholding",
        "Otsu Thresholding",
        "Background Removal"
    ]
)

if uploaded_file is not None:

    # Read uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    image_array = np.array(image)

    # Convert RGB to OpenCV BGR
    original = cv2.cvtColor(
        image_array,
        cv2.COLOR_RGB2BGR
    )

    # Convert to grayscale
    gray = cv2.cvtColor(
        original,
        cv2.COLOR_BGR2GRAY
    )

    # Select method
    if method == "Grayscale":
        result = gray

    elif method == "Binary Thresholding":
        _, result = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )

    elif method == "Adaptive Thresholding":
        result = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

    elif method == "Otsu Thresholding":
        _, result = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

    else:
        blurred = cv2.GaussianBlur(
            gray, (5, 5), 0
        )

        _, mask = cv2.threshold(
            blurred,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        result = cv2.bitwise_and(
            original,
            original,
            mask=mask
        )

    # Display original and processed images
    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    st.subheader("Segmented Result")

    if len(result.shape) == 2:
        st.image(
            result,
            channels="GRAY",
            use_container_width=True
        )
    else:
        result_rgb = cv2.cvtColor(
            result, cv2.COLOR_BGR2RGB
        )
        st.image(
            result_rgb,
            use_container_width=True
        )

    # Prepare download image
    if len(result.shape) == 2:
        output_image = Image.fromarray(result)
    else:
        output_image = Image.fromarray(
            cv2.cvtColor(
                result, cv2.COLOR_BGR2RGB
            )
        )

    buffer = io.BytesIO()
    output_image.save(buffer, format="PNG")

    st.download_button(
        label="Download Segmented Image",
        data=buffer.getvalue(),
        file_name="segmented_output.png",
        mime="image/png"
    )
