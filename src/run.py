import cv2
import numpy as np
from tqdm import tqdm

def main():
    chemin_video = "C:\\Users\\DEPTEC\\Documents\\ABEJA\\videos\\Bees-Cajica-1.MOV"

    # Ouvrir la vidéo
    capture = cv2.VideoCapture(chemin_video)

    # Get the total number of frames in the video
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the frame rate (frames per second)
    fps = capture.get(cv2.CAP_PROP_FPS)

    # Get the frame dimensions
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create the VideoWriter object
    video = cv2.VideoWriter('db0.wmv', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    with tqdm(total=total_frames, desc='Processing frames') as pbar:
        while capture.isOpened():
            # Lire la frame
            ret, frame = capture.read()

            # Vérifier si la lecture de la frame a réussi
            if ret:
                # Convert to grayscale.
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Blur using 3 * 3 kernel.
                gray_blurred = cv2.blur(gray, (15, 15))

                # Apply Hough transform on the blurred image.
                detected_circles = cv2.HoughCircles(gray_blurred,
                                                    cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                                    param2=25, minRadius=5, maxRadius=50)

                # Draw circles that are detected.
                if detected_circles is not None:
                    # Convert the circle parameters a, b, and r to integers.
                    detected_circles = np.uint16(np.around(detected_circles))

                    for pt in detected_circles[0, :]:
                        a, b, r = pt[0], pt[1], pt[2]

                        # Draw the circumference of the circle.
                        cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

                        # Draw a small circle (of radius 1) to show the center.
                        cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

                # Write the processed frame to the video file
                video.write(frame)
            else:
                break

            # Update the progress bar
            pbar.update(1)

    # Release the resources
    capture.release()
    video.release()

    # Print the frame rate
    print("Frame rate:", fps)

if __name__ == "__main__":
    main()
