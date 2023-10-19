import cv2 as cv
import sys

from marker_detection import MarkerDetector

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

    for marker in MarkerDetector.detect_markers(image):
        cv.imshow('marker', marker)
        cv.waitKey(0)

if __name__ == "__main__":
    detect_markers()
