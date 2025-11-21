import cv2
import time
from ultralytics import YOLO

def main():
    # Path to your trained YOLOv11 weights
    model_path = "best.pt"

    # Load the YOLOv11 model
    model = YOLO(model_path)

    # Open webcam (0 = default camera; change if needed)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    # For FPS calculation
    prev_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Run inference on the frame
        # stream=True gives generator of results; good for live video
        results = model(frame, verbose=False)

        # Take first (and only) result for this frame
        result = results[0]

        # Current time for FPS
        curr_time = time.time()
        fps = 1.0 / (curr_time - prev_time) if prev_time != 0 else 0.0
        prev_time = curr_time

        # Get detections: boxes, class IDs, confidences
        if result.boxes is not None:
            boxes = result.boxes.xyxy.cpu().numpy()      # [x1, y1, x2, y2]
            confs = result.boxes.conf.cpu().numpy()      # confidence scores
            clss = result.boxes.cls.cpu().numpy().astype(int)  # class IDs

            for box, conf, cls in zip(boxes, confs, clss):
                x1, y1, x2, y2 = box.astype(int)
                class_name = model.names[cls] if hasattr(model, "names") else str(cls)
                label = f"{class_name} {conf:.2f}"

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Draw label background
                (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                cv2.rectangle(frame, (x1, y1 - th - 6), (x1 + tw, y1), (0, 255, 0), -1)

                # Put label text
                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 4),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 0, 0),
                    2,
                    cv2.LINE_AA,
                )

        # Draw FPS on the frame
        fps_text = f"FPS: {fps:.2f}"
        cv2.putText(
            frame,
            fps_text,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

        # Show the result
        cv2.imshow("YOLOv11 Live Detection (FER2025)", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
