import cv2 as cv
import sys
import numpy as np

from marker_detection import MarkerDetector
from marker_identification import MarkerIdentifier
from render import SwordRenderer


def capture_video():
    camera = cv.VideoCapture(0)
    detector = MarkerDetector()

    # TODO: Move this to configuration file or arguments parameters
    identifier = MarkerIdentifier(
        cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_250), 88, 93
    )

    while True:
        # Capture frame-by-frame
        check, frame = camera.read()

        if not check:
            print("Can't receive frame. Exiting ...", file=sys.stderr)

        # Detect marker corners
        detected_corners = detector.detect(frame)

        if detected_corners is not None:
            cv.drawContours(frame, [detected_corners], -1, (0, 255, 0), 3)

            marker_corners, marker_id = identifier.identify(detector._threshold(frame), detected_corners)

            if marker_corners is not None:
                # Draw detected marker
                corners = (np.array([marker_corners.astype(np.float32)]),)

                cv.aruco.drawDetectedMarkers(frame, corners, np.array([marker_id]))

                # Draw sword
                renderer = SwordRenderer()
                frame = renderer.draw(frame, marker_corners, marker_id)

        cv.imshow("Video", frame)

        key = cv.waitKey(10)

        # Press ESC to exit
        if key == 27:
            break

    camera.release()
    cv.destroyAllWindows()

def debug():
    image = cv.imread("../data/images/photo.jpg")
    detector = MarkerDetector()
    identifier = MarkerIdentifier(
        cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_250), 94, 99
    )

    # Detect marker corners
    detected_corners = detector.detect(image)

    if detected_corners is not None:
        marker_corners, marker_id = identifier.identify(detector._threshold(image), detected_corners)

        if marker_corners is not None:
            # Draw detected marker
            corners = (np.array([marker_corners.astype(np.float32)]),)

            cv.aruco.drawDetectedMarkers(image, corners, np.array([marker_id]))

            # Draw sword
            image = render_sword(image, marker_id, marker_corners)

    cv.imshow("Augmented Sword", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def render_sword(image, marker_id, marker_corners):
    # Draw a sword wireframe on top of detected AruCo marker
    renderer = SwordRenderer()
    image = renderer.draw(image, marker_corners, marker_id)

    return image

if __name__ == "__main__":
    capture_video()