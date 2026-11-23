
import cv2
from ultralytics import YOLO

def track_video(video_path, output_path,
                tracker="bytetrack.yaml",
                confidence=0.25):

    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError("Could not open video")

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if fps <= 0:
        fps = 25

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    if not writer.isOpened():
        cap.release()
        raise ValueError("Could not create output video")

    unique_ids = set()

    try:
        while True:

            success, frame = cap.read()

            if not success:
                break

            results = model.track(
                frame,
                persist=True,
                tracker=tracker,
                conf=confidence,
                imgsz=480,
                device="cpu",
                verbose=False
            )

            result = results[0]

            if result.boxes is not None:
                if result.boxes.id is not None:

                    ids = result.boxes.id.int().cpu().tolist()

                    for object_id in ids:
                        unique_ids.add(object_id)

            annotated = result.plot(
                labels=True,
                conf=True
            )

            cv2.putText(
                annotated,
                f"Unique Objects: {len(unique_ids)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            writer.write(annotated)

    finally:
        cap.release()
        writer.release()

    return len(unique_ids)
