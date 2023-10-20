import numpy as np
import cv2 as cv


class SwordRenderer:
    @classmethod
    def draw(cls, image, corners):
        def translateXY(x):
            x[0] -= 0.5
            x[1] -= 0.5

            return x

        files = np.load("camera.npz")
        camera_matrix = files["camera_matrix"]
        distortion_coefficient = files["distortion_coefficients"]

        image_points = corners.astype(np.double)

        model_points = np.array(
            [
                [0, 0, 0],
                [0, 250, 0],
                [250, 250, 0],
                [250, 0, 0],
            ],
            dtype="double",
        )

        # Rotation and translation vectors
        _, rvec, tvec = cv.solvePnP(
            model_points, image_points, camera_matrix, distortion_coefficient, flags=0
        )

        verts, _ = cv.projectPoints(
            np.array([(0.0, 0.0, 1000.0)]),
            rvec,
            tvec,
            camera_matrix,
            distortion_coefficient,
        )

        # Draw corners
        for p in image_points:
            cv.circle(image, (int(p[0]), int(p[1])), 5, (0, 0, 255), -1)

        for image_point in image_points:
            point1 = image_point.astype(np.int32)
            point2 = (int(verts[0][0][0]), int(verts[0][0][1]))

            cv.line(image, point1, point2, (0, 0, 255), 2)

        return image
