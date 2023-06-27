import cv2
import numpy as np
#from yolov3.yolov3_detector import YOLOv3Detector

def main():
    # Load YOLOv3 detector
    detector = YOLOv3Detector()

    # Load the video
    video_path = "C:\\Users\\DEPTEC\\Documents\\ABEJA\\videos\\Bees-Cajica-1.MOV"
    video = cv2.VideoCapture(video_path)

    # Get video properties
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_rate = video.get(cv2.CAP_PROP_FPS)

    # Create output video writer
    output_path = "output/video_output.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, frame_rate, (frame_width, frame_height))

    while video.isOpened():
        # Read a frame from the video
        ret, frame = video.read()

        if not ret:
            break

        # Perform circle detection using YOLO
        detections = detector.detect(frame)

        # Filter detections to keep only circles
        circles = [d for d in detections if d["class_id"] == 0]

        # Draw circles on the frame
        for circle in circles:
            x, y, w, h = circle["bbox"]
            cv2.circle(frame, (int(x + w / 2), int(y + h / 2)), int(w / 2), (0, 255, 0), 2)

        # Write the frame with circles to the output video
        output_video.write(frame)

        # Display the frame (optional)
        cv2.imshow("Circle Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    video.release()
    output_video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
