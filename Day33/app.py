
import streamlit as st
import os
import tempfile
import uuid
import hashlib

from people_counting import process_video, process_image


# PAGE CONFIGURATION

st.set_page_config(
    page_title="PeopleVision AI | Crowd Analytics",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# SESSION STATE

if "analysis_result" not in st.session_state:
    st.session_state["analysis_result"] = None

if "upload_hash" not in st.session_state:
    st.session_state["upload_hash"] = None

if "last_input_type" not in st.session_state:
    st.session_state["last_input_type"] = "Image"


# CUSTOM CSS

st.markdown("""
<style>

.stApp {
    background: #0B1020;
    color: #F1F5F9;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

section[data-testid="stSidebar"] {
    background: #11182B;
    border-right: 1px solid #26324A;
}

section[data-testid="stSidebar"] * {
    color: #E2E8F0;
}

h1, h2, h3, h4 {
    color: #F8FAFC !important;
}

p {
    color: #B8C4D8;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #131D32;
    border: 1px solid #283651;
    border-radius: 14px;
}

div[data-testid="stMetric"] {
    background: #17243A;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #30405D;
}

div[data-testid="stMetricValue"] {
    color: #A78BFA;
}

.stButton > button {
    background: linear-gradient(90deg, #7C3AED, #6366F1);
    color: white;
    border: none;
    border-radius: 9px;
    padding: 0.65rem 1.2rem;
    font-weight: 600;
    width: 100%;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #6D28D9, #4F46E5);
    color: white;
}

.stDownloadButton > button {
    background: #17243A;
    color: #C4B5FD;
    border: 1px solid #8B5CF6;
    border-radius: 9px;
    width: 100%;
}

div[data-testid="stFileUploader"] {
    background: #131D32;
    border: 1px dashed #64748B;
    border-radius: 12px;
    padding: 15px;
}

hr {
    border-color: #283651;
}

.hero {
    background: linear-gradient(
        120deg,
        #1E1B4B,
        #172554,
        #17243A
    );
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #39466B;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 32px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}

.hero-description {
    font-size: 16px;
    color: #CBD5E1;
    line-height: 1.6;
}

.tag {
    display: inline-block;
    background: #312E81;
    color: #DDD6FE;
    padding: 6px 12px;
    border-radius: 20px;
    margin: 5px 5px 5px 0;
    font-size: 12px;
    border: 1px solid #6366F1;
}

.section-heading {
    font-size: 21px;
    font-weight: 700;
    color: #F8FAFC;
    margin-bottom: 15px;
}

.info-box {
    background: #131D32;
    border: 1px solid #283651;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 12px;
}

.footer {
    text-align: center;
    color: #94A3B8;
    font-size: 12px;
    padding: 25px 0 10px 0;
}
.hero-box {
    background: linear-gradient(120deg, #1E1B4B, #172554, #17243A);
    padding: 32px;
    border-radius: 18px;
    border: 1px solid #39466B;
    margin-bottom: 25px;
}

.hero-heading {
    font-size: 34px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 12px;
}

.hero-text {
    font-size: 16px;
    color: #CBD5E1;
    line-height: 1.7;
}

.tag {
    display: inline-block;
    background: #312E81;
    color: #DDD6FE;
    padding: 7px 13px;
    border-radius: 20px;
    margin: 5px 5px 5px 0;
    font-size: 12px;
    border: 1px solid #6366F1;
}
</style>
""", unsafe_allow_html=True)


# SIDEBAR

with st.sidebar:

    st.markdown("# 👥 PeopleVision AI")

    st.caption("INTELLIGENT CROWD ANALYTICS")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        ["Dashboard", "About Project"],
        label_visibility="visible"
    )

    st.divider()

    st.markdown("### ⚙️ System Information")

    st.markdown("""
    **AI Model:** YOLO11n

    **Tracking:** ByteTrack

    **Processing:** OpenCV

    **Interface:** Streamlit
    """)

    st.divider()

    st.markdown("### 🟢 System Status")

    st.success("Application Ready")

    st.caption("Machine Learning & Computer Vision Internship")



# DASHBOARD PAGE

if page == "Dashboard":

    # HERO SECTION

    with st.container(border=True):

        st.markdown("## 👥 PeopleVision AI")

        st.write(
            "Smart People Detection, Tracking "
            "and Crowd Analytics Dashboard"
        )

        st.caption(
            "🟣 YOLO Detection  |  "
            "🟣 ByteTrack Tracking"
        )

        st.caption(
            "🟣 Real-Time Frame Analysis  |  "
            "🟣 Crowd Analytics"
        )

    st.divider()

    # UPLOAD SECTION

    st.markdown("### 📁 Upload Your Media")

    col1, col2 = st.columns(2)

    with col1:

        input_type = st.selectbox(
            "Select Media Type",
            ["Image", "Video"],
            key="media_type"
        )

    with col2:

        if input_type == "Image":
            st.info("Supported formats: JPG, JPEG, PNG")
        else:
            st.info("Supported formats: MP4, AVI, MOV")

    # RESET OLD RESULT WHEN MEDIA TYPE CHANGES

    if input_type != st.session_state["last_input_type"]:

        st.session_state["analysis_result"] = None
        st.session_state["upload_hash"] = None
        st.session_state["last_input_type"] = input_type

    # FILE UPLOADER

    if input_type == "Image":

        uploaded_file = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"],
            key="image_upload"
        )

    else:

        uploaded_file = st.file_uploader(
            "Choose a video",
            type=["mp4", "avi", "mov"],
            key="video_upload"
        )



    # FILE PROCESSING

    if uploaded_file is not None:

        uploaded_bytes = uploaded_file.getvalue()

        file_hash = hashlib.sha256(
            uploaded_bytes
        ).hexdigest()

        current_hash = f"{input_type}_{file_hash}"

        if current_hash != st.session_state["upload_hash"]:

            st.session_state["analysis_result"] = None
            st.session_state["upload_hash"] = current_hash

        st.divider()

        st.markdown(
            '<div class="section-heading">📂 Input Preview</div>',
            unsafe_allow_html=True
        )

        preview_col, details_col = st.columns([1.5, 1])

        with preview_col:

            if input_type == "Image":

                st.image(
                    uploaded_bytes,
                    caption="Uploaded Image",
                    use_container_width=True
                )

            else:

                st.video(uploaded_bytes)

        with details_col:

            st.markdown("### File Information")

            st.write("**Filename:**", uploaded_file.name)

            st.write(
                "**File Size:**",
                f"{len(uploaded_bytes) / (1024 * 1024):.2f} MB"
            )

            st.write("**Media Type:**", input_type)

            st.write("**Status:** Uploaded successfully")

            st.success("Ready for AI Analysis")

        st.divider()


        # PROCESSING BUTTON

        if st.button(
            "🚀 Start AI Detection",
            type="primary",
            use_container_width=True
        ):

            input_path = None
            output_path = None

            try:

                suffix = os.path.splitext(
                    uploaded_file.name
                )[1]

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                ) as temp:

                    temp.write(uploaded_bytes)
                    input_path = temp.name

                os.makedirs("output_images", exist_ok=True)
                os.makedirs("output_videos", exist_ok=True)

                unique_id = uuid.uuid4().hex[:8]

                if input_type == "Image":

                    output_path = os.path.join(
                        "output_images",
                        f"processed_image_{unique_id}.jpg"
                    )

                else:

                    output_path = os.path.join(
                        "output_videos",
                        f"processed_video_{unique_id}.mp4"
                    )


                # RUN AI PROCESSING

                with st.spinner(
                    "AI is detecting and analyzing people... Please wait."
                ):

                    if input_type == "Image":

                        count = process_image(
                            input_path,
                            output_path
                        )

                        result_data = {
                            "type": "Image",
                            "count": count,
                            "output": output_path
                        }

                    else:

                        result = process_video(
                            input_path,
                            output_path,
                            show_window=False
                        )

                        result_data = {
                            "type": "Video",
                            "unique": result["unique_people"],
                            "peak": result["peak_occupancy"],
                            "output": output_path
                        }

                st.session_state["analysis_result"] = result_data

                st.success("AI Analysis Completed Successfully!")

            except Exception as e:

                st.error(f"Processing failed: {e}")

                st.session_state["analysis_result"] = None

            finally:

                if input_path and os.path.exists(input_path):

                    try:
                        os.remove(input_path)
                    except OSError:
                        pass


    # RESULTS SECTION

    result_data = st.session_state.get("analysis_result")

    if result_data is not None:

        st.divider()

        st.markdown(
            '<div class="section-heading">📊 Detection Analytics</div>',
            unsafe_allow_html=True
        )

        if result_data["type"] == "Image":

            st.metric(
                "Total People Detected",
                result_data["count"]
            )

        else:

            col1, col2 = st.columns(2)

            col1.metric(
                "Unique People Tracked",
                result_data["unique"]
            )

            col2.metric(
                "Peak Occupancy",
                result_data["peak"]
            )

        st.divider()

        st.markdown(
            '<div class="section-heading">🎯 Processed Output</div>',
            unsafe_allow_html=True
        )

        output_path = result_data["output"]

        if os.path.exists(output_path):

            if result_data["type"] == "Image":

                st.image(
                    output_path,
                    caption="AI Processed Image",
                    use_container_width=True
                )

                with open(output_path, "rb") as file:

                    st.download_button(
                        "⬇️ Download Processed Image",
                        data=file.read(),
                        file_name="processed_image.jpg",
                        mime="image/jpeg"
                    )

            else:

                st.video(output_path)

                with open(output_path, "rb") as file:

                    st.download_button(
                        "⬇️ Download Processed Video",
                        data=file.read(),
                        file_name="processed_video.mp4",
                        mime="video/mp4"
                    )

        else:

            st.warning(
                "Output file is no longer available. "
                "Please run detection again."
            )

    else:

        st.info(
            "Please upload an image or video to start people detection."
        )


# ABOUT PROJECT PAGE

# ABOUT PROJECT PAGE

elif page == "About Project":

    st.title("👥 About PeopleVision AI")

    st.write(
        "An AI-powered system for detecting, tracking and "
        "analyzing people in images and videos."
    )

    st.divider()


    # PROJECT OBJECTIVE

    st.markdown("### 🎯 Project Objective")

    st.write("""
    PeopleVision AI is designed to automatically identify
    people in images and videos, track their movement
    and provide useful crowd analytics.

    The system uses YOLO for detection, ByteTrack
    for tracking and OpenCV for image and video processing.
    """)


    # TECHNOLOGIES USED

        # TECHNOLOGIES USED

    st.markdown("### 🛠️ Technologies Used")

    with st.container(border=True):

        st.markdown("#### 🤖 YOLO")
        st.write("Detects people in images and video frames.")

        st.markdown("#### 📷 OpenCV")
        st.write("Processes images and videos and draws bounding boxes.")

        st.markdown("#### 🔄 ByteTrack")
        st.write("Tracks detected people using unique IDs.")

        st.markdown("#### 🌐 Streamlit")
        st.write("Provides the interactive web application.")


    # MAIN FEATURES

    st.markdown("### ✨ Main Features")

    st.write("""
    - YOLO-based people detection
    - ByteTrack tracking with unique IDs
    - People counting and crowd analytics
    - Bounding boxes and confidence scores
    - Processed image and video downloads
    """)


    # REAL-WORLD APPLICATIONS

    st.markdown("### 🌍 Real-World Applications")

    st.write("""
    - Shopping mall crowd monitoring
    - Office occupancy monitoring
    - Classroom and campus analytics
    - Public area crowd management
    - Building entrance monitoring
    """)


    # FUTURE IMPROVEMENTS

    st.markdown("### 🚀 Future Improvements")

    st.write("""
    - Entry and exit counting
    - Region of Interest (ROI)
    - Improved tracking accuracy
    - Real-time CCTV monitoring
    - Crowd density analysis
    """)


# FOOTER

st.markdown("""
<div class="footer">
    <p>Built with Python, YOLO, OpenCV and Streamlit</p>
    <p>Machine Learning &amp; Computer Vision Internship</p>
</div>
""", unsafe_allow_html=True)
