import cv2 as cv
import sys

from marker_detection import MarkerDetector
from marker_identification import MarkerIdentifier

def capture_video():
    camera = cv.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        check, frame = camera.read()

        if not check:
            print("Can't receive frame. Exiting ...", file=sys.stderr)

        cv.imshow('video', frame)

        key = cv.waitKey(1)
        
        # Press ESC to exit
        if key == 27:
            break

    camera.release()
    cv.destroyAllWindows()

def detect_markers():
    image = cv.imread('../data/images/markers.jpg')

    for marker in MarkerDetector.detect(image):
        marker_id = MarkerIdentifier.identify(marker)

        print(marker_id)

if __name__ == "__main__":
    detect_markers()
