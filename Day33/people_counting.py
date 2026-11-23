
import cv2
import os
from ultralytics import YOLO

# 1. PROJECT FOLDER


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 2. YOLO MODEL


MODEL_PATH = os.path.join(BASE_DIR, "yolo11n.pt")

print("Loading YOLO model...")

if not os.path.exists(MODEL_PATH):
    print("Downloading YOLO model...")
    downloaded_model = YOLO("yolo11n.pt")
    downloaded_model.save(MODEL_PATH)

model = YOLO(MODEL_PATH)

print("YOLO model loaded successfully!")


# 3. INPUT AND OUTPUT FOLDERS


INPUT_VIDEO_FOLDER = os.path.join(
    BASE_DIR, "input_videos"
)

OUTPUT_VIDEO_FOLDER = os.path.join(
    BASE_DIR, "output_videos"
)

INPUT_IMAGE = os.path.join(
    BASE_DIR, "input_images", "image1.jpg"
)

OUTPUT_IMAGE = os.path.join(
    BASE_DIR, "output_images", "processed_image.jpg"
)

os.makedirs(OUTPUT_VIDEO_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(OUTPUT_IMAGE), exist_ok=True)



# 4. PEOPLE COUNTING FUNCTION


def process_video(input_path, output_path, show_window=False):

    if not os.path.isfile(input_path):
        raise FileNotFoundError(
            f"Video not found: {input_path}"
        )

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    # Reset tracker for a new video
    if hasattr(model, "predictor") and model.predictor is not None:

        if hasattr(model.predictor, "trackers"):

            for tracker in model.predictor.trackers:
                tracker.reset()

    # Open video
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        raise ValueError(
            "Unable to open video. Check video format."
        )

    # Video details
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if fps <= 0:
        fps = 25

    if width <= 0 or height <= 0:
        cap.release()
        raise ValueError("Invalid video dimensions.")

    print("\nVideo opened successfully!")
    print("Width:", width)
    print("Height:", height)
    print("FPS:", fps)

    # Create output video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    if not out.isOpened():
        cap.release()
        raise ValueError(
            "Unable to create output video."
        )

    # Counting variables
    total_unique_people = set()
    peak_occupancy = 0
    frame_number = 0

    print("\nPeople detection started...\n")

    try:

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            frame_number += 1

            # YOLO DETECTION AND TRACKING
            results = model.track(
                frame,
                persist=True,
                tracker="bytetrack.yaml",
                classes=[0],
                conf=0.25,
                verbose=False
            )

            result = results[0]

            visible_count = 0

            if result.boxes is not None and len(result.boxes) > 0:

                boxes = result.boxes

                coordinates = (
                    boxes.xyxy.int().cpu().tolist()
                )

                confidences = (
                    boxes.conf.cpu().tolist()
                )

                visible_count = len(coordinates)

                if boxes.id is not None:

                    track_ids = (
                        boxes.id.int().cpu().tolist()
                    )

                else:

                    track_ids = [None] * visible_count

                # DRAW BOUNDING BOXES
                for box, track_id, confidence in zip(
                    coordinates,
                    track_ids,
                    confidences
                ):

                    x1, y1, x2, y2 = box

                    # Store unique IDs
                    if track_id is not None:
                        total_unique_people.add(track_id)

                    # Draw rectangle
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    # Display ID and confidence
                    label = (
                        f"ID: {track_id} "
                        f"Confidence: {confidence:.2f}"
                    )

                    cv2.putText(
                        frame,
                        label,
                        (x1, max(y1 - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

            # PEOPLE COUNTING
            peak_occupancy = max(
                peak_occupancy,
                visible_count
            )

            # Display visible people
            cv2.putText(
                frame,
                f"Visible People: {visible_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

            # Display unique people
            cv2.putText(
                frame,
                f"Unique People: {len(total_unique_people)}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

            # Display peak occupancy
            cv2.putText(
                frame,
                f"Peak Occupancy: {peak_occupancy}",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

            # SAVE PROCESSED VIDEO
            out.write(frame)

            # Show progress
            if frame_number % 30 == 0:

                print(
                    f"Processed frames: {frame_number} | "
                    f"Visible people: {visible_count}"
                )

    finally:

        cap.release()
        out.release()

    # FINAL VIDEO RESULTS
    print("\n=================================")
    print("VIDEO PROCESSING COMPLETED!")
    print("=================================")

    print(
        "Total unique tracked people:",
        len(total_unique_people)
    )

    print(
        "Peak occupancy:",
        peak_occupancy
    )

    print(
        "Total frames processed:",
        frame_number
    )

    print("Output video saved:", output_path)

    if not os.path.exists(output_path):
        raise FileNotFoundError(
            "Output video was not created."
        )

    if os.path.getsize(output_path) == 0:
        raise ValueError("Output video is empty.")

    print(
        "Output video size:",
        round(
            os.path.getsize(output_path) / (1024 * 1024),
            2
        ),
        "MB"
    )

    return {
        "unique_people": len(total_unique_people),
        "peak_occupancy": peak_occupancy,
        "frames": frame_number,
        "output_path": output_path
    }


# 5. IMAGE DETECTION FUNCTION


def process_image(input_path, output_path):

    if not os.path.isfile(input_path):
        raise FileNotFoundError(
            f"Image not found: {input_path}"
        )

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    image = cv2.imread(input_path)

    if image is None:
        raise ValueError("Could not read image.")

    results = model.predict(
        image,
        classes=[0],
        conf=0.25,
        verbose=False
    )

    result = results[0]

    people_count = 0

    if result.boxes is not None and len(result.boxes) > 0:

        people_count = len(result.boxes)

        boxes = result.boxes.xyxy.int().cpu().tolist()
        confidences = result.boxes.conf.cpu().tolist()

        for box, confidence in zip(boxes, confidences):

            x1, y1, x2, y2 = box

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            label = f"Person: {confidence:.2f}"

            cv2.putText(
                image,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Display count
    cv2.putText(
        image,
        f"Total People: {people_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    success = cv2.imwrite(output_path, image)

    if not success:
        raise ValueError("Could not save processed image.")

    print("\nIMAGE PROCESSING COMPLETED!")
    print("People detected:", people_count)
    print("Image saved:", output_path)

    return people_count



# 6. PROCESS ALL FIVE VIDEOS


def process_all_videos():

    print("\n=================================")
    print("SMART PEOPLE COUNTING SYSTEM")
    print("PROCESSING ALL VIDEOS")
    print("=================================")

    if not os.path.isdir(INPUT_VIDEO_FOLDER):
        raise FileNotFoundError(
            "input_videos folder not found."
        )

    # Find all video files
    video_files = sorted([
        file for file in os.listdir(INPUT_VIDEO_FOLDER)
        if file.lower().endswith(
            (".mp4", ".avi", ".mov", ".mkv")
        )
    ])

    print("\nTotal videos found:", len(video_files))

    if len(video_files) != 5:
        print(
            f"WARNING: Your assignment requires 5 videos. "
            f"Currently found: {len(video_files)}"
        )

    if len(video_files) == 0:
        print("No videos found!")
        return

    all_results = []

    # Process each video
    for index, video_name in enumerate(video_files, start=1):

        print("\n=================================")
        print(f"PROCESSING VIDEO {index} OF {len(video_files)}")
        print("Video name:", video_name)
        print("=================================")

        input_path = os.path.join(
            INPUT_VIDEO_FOLDER,
            video_name
        )

        name_without_extension = os.path.splitext(
            video_name
        )[0]

        output_name = name_without_extension + "_processed.mp4"

        output_path = os.path.join(
            OUTPUT_VIDEO_FOLDER,
            output_name
        )

        try:

            result = process_video(
                input_path,
                output_path
            )

            all_results.append({
                "video": video_name,
                "unique_people": result["unique_people"],
                "peak_occupancy": result["peak_occupancy"],
                "frames": result["frames"],
                "status": "Success"
            })

        except Exception as error:

            print("\nERROR:", error)

            all_results.append({
                "video": video_name,
                "status": "Failed",
                "error": str(error)
            })

    # FINAL REPORT
    print("\n=================================")
    print("FINAL FIVE VIDEO REPORT")
    print("=================================")

    for item in all_results:

        print("\nVideo:", item["video"])
        print("Status:", item["status"])

        if item["status"] == "Success":

            print("Unique People:", item["unique_people"])
            print("Peak Occupancy:", item["peak_occupancy"])
            print("Frames Processed:", item["frames"])

        else:

            print("Error:", item["error"])

    successful = sum(
        1 for item in all_results
        if item["status"] == "Success"
    )

    print("\n=================================")
    print("TOTAL VIDEOS PROCESSED:", successful)
    print("TOTAL VIDEOS FOUND:", len(video_files))
    print("=================================")

    return all_results



# 7. RUN PROGRAM


if __name__ == "__main__":

    print("\nTesting Image Detection...")

    if os.path.isfile(INPUT_IMAGE):

        count = process_image(
            INPUT_IMAGE,
            OUTPUT_IMAGE
        )

        print("Image people count:", count)

    else:

        print("Image not found. Skipping image detection.")

    # Process all five videos
    results = process_all_videos()

    print("\nPROGRAM FINISHED!")
