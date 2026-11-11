
import cv2
import streamlit as st
import tempfile
import os

# App title
st.title("Day 26 - Video Processing Tool")

st.write(
    "Upload a video to apply Grayscale, "
    "Gaussian Blur and Canny Edge Detection."
)

# Upload video
video = st.file_uploader(
    "Upload your video",
    type=["mp4", "avi", "mov"]
)

if video is not None:

    # Save uploaded video temporarily
    temp_input = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp4"
    )

    temp_input.write(video.read())
    temp_input.close()

    # Display original video
    st.subheader("Original Video")
    st.video(temp_input.name)

    if st.button("Process Video"):

        cap = cv2.VideoCapture(temp_input.name)

        if not cap.isOpened():
            st.error("Cannot open video!")

        else:

            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(
                cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            )
            height = int(
                cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            )

            if fps <= 0:
                fps = 20

            st.write("FPS:", fps)
            st.write("Width:", width)
            st.write("Height:", height)

            # Create output video
            output_path = tempfile.mktemp(
                suffix=".mp4"
            )

            fourcc = cv2.VideoWriter_fourcc(
                *"mp4v"
            )

            out = cv2.VideoWriter(
                output_path,
                fourcc,
                fps,
                (width * 2, height)
            )

            while True:

                ret, frame = cap.read()

                if not ret:
                    break

                # Grayscale
                gray = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2GRAY
                )

                # Gaussian Blur
                blur = cv2.GaussianBlur(
                    gray,
                    (5, 5),
                    0
                )

                # Canny Edge Detection
                edges = cv2.Canny(
                    blur,
                    100,
                    200
                )

                # Convert edges to color
                edges_color = cv2.cvtColor(
                    edges,
                    cv2.COLOR_GRAY2BGR
                )

                # Join original and processed frames
                combined = cv2.hconcat(
                    [frame, edges_color]
                )

                # Save processed frame
                out.write(combined)

            cap.release()
            out.release()

            if os.path.exists(output_path):

                st.success(
                    "Video processed successfully!"
                )

                st.subheader(
                    "Processed Video"
                )

                st.video(output_path)

                with open(output_path, "rb") as file:

                    st.download_button(
                        label="Download Processed Video",
                        data=file,
                        file_name="processed_video.mp4",
                        mime="video/mp4"
                    )

            else:
                st.error("Output video was not created!")

    os.unlink(temp_input.name)
