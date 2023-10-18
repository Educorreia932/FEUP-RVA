import cv2 as cv
import sys

def capture_video():
    camera = cv.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        check, frame = camera.read()

        if not check:
            print("Can't receive frame. Exiting ...", file=sys.stderr)

        cv.imshow('video', frame)

        key = cv.waitKey(1)
        
        if key == 27:
            break

    camera.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    capture_video()