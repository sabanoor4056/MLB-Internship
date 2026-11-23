
import streamlit as st
import tempfile
import os

from tracking import track_video

st.set_page_config(
    page_title="Smart Object Tracking",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Smart Object Tracking System")

st.write(
    "Upload a video and track multiple objects "
    "using YOLO and ByteTrack or BoT-SORT."
)

st.sidebar.header("Tracking Settings")

tracker = st.sidebar.selectbox(
    "Select Tracking Algorithm",
    ["bytetrack.yaml", "botsort.yaml"]
)

confidence = st.sidebar.slider(
    "Detection Confidence",
    min_value=0.1,
    max_value=0.9,
    value=0.25,
    step=0.05
)

uploaded_video = st.file_uploader(
    "Upload your video",
    type=["mp4", "avi", "mov", "mkv"]
)

if uploaded_video is not None:

    st.subheader("Input Video")
    st.video(uploaded_video)

    if st.button("Start Tracking"):

        with tempfile.TemporaryDirectory() as temp_dir:

            input_path = os.path.join(
                temp_dir,
                uploaded_video.name
            )

            output_path = os.path.join(
                temp_dir,
                "tracked_output.mp4"
            )

            with open(input_path, "wb") as file:
                file.write(uploaded_video.getbuffer())

            try:

                with st.spinner(
                    "Processing video on CPU. Please wait..."
                ):

                    total_objects = track_video(
                        input_path,
                        output_path,
                        tracker=tracker,
                        confidence=confidence
                    )

                st.success("Tracking completed!")

                st.metric(
                    "Total Unique Objects",
                    total_objects
                )

                st.subheader("Processed Video")

                with open(output_path, "rb") as file:
                    video_bytes = file.read()

                st.video(video_bytes)

                st.download_button(
                    "Download Processed Video",
                    data=video_bytes,
                    file_name="tracked_output.mp4",
                    mime="video/mp4"
                )

            except Exception as error:
                st.error(f"Something went wrong: {error}")

else:
    st.info("Please upload a video to start tracking.")
