import cv2 as cv
import sys
import numpy as np

from marker_detection import MarkerDetector
from marker_identification import MarkerIdentifier
from sword_render import SwordRenderer


def capture_video():
    camera = cv.VideoCapture(0)
    detector = MarkerDetector()

    # TODO: Move this to configuration file or arguments parameters
    identifier = MarkerIdentifier(
        cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_250), 94, 99
    )

    while True:
        # Capture frame-by-frame
        check, frame = camera.read()

        if not check:
            print("Can't receive frame. Exiting ...", file=sys.stderr)

        # Detect marker corners
        corners = detector.detect(frame)

        if corners is not None:
            rotated_marker, marker_id = identifier.identify(detector._threshold(frame), corners)

            if marker_id != -1:
                # Draw detected marker
                corners = (np.array([rotated_marker.astype(np.float32)]),)

                cv.aruco.drawDetectedMarkers(frame, corners, np.array([marker_id]))

        cv.imshow("Video", frame)

        key = cv.waitKey(1)

        # Press ESC to exit
        if key == 27:
            break

    camera.release()
    cv.destroyAllWindows()


def draw_sword(image):
    marker_detector = MarkerDetector()
    contours = marker_detector.detect(image)

    if len(contours) == 0:
        return image

    cv.drawContours(image, contours, -1, (0, 255, 0), 10)

    # Draw a sword wireframe on top of detected AruCo marker
    image = SwordRenderer.draw(image, contours[0])

    return image


if __name__ == "__main__":
    # image = cv.imread('../data/images/camera.png')

    capture_video()
