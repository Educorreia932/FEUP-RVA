import cv2 as cv
import sys
import numpy as np

from marker_detection import MarkerDetector
from marker_identification import MarkerIdentifier
from sword_render import SwordRenderer

def capture_video():
    camera = cv.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        check, frame = camera.read()

        if not check:
            print("Can't receive frame. Exiting ...", file=sys.stderr)

        corners = list(MarkerDetector.detect(frame))

        if corners:
            for contours in corners:
                pass
                # cv.drawContours(frame, contours, -1, (0, 255, 0), 20)
                # frame = overlay_marker(frame, marker_corners)

        cv.imshow('Video', frame)

        key = cv.waitKey(1)
        
        # Press ESC to exit
        if key == 27:
            break

    camera.release()
    cv.destroyAllWindows()

def draw_sword():
    image = cv.imread('../data/images/camera.png')

    contours = MarkerDetector.detect(image)

    cv.drawContours(image, contours, -1, (0, 255, 0), 10)

    # Draw a sword wireframe on top of detected AruCo marker
    image = SwordRenderer.draw(image, contours[0])

    cv.imshow("Augmented Sword", image)
    cv.waitKey(0)

if __name__ == "__main__":
    draw_sword()
