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

        model_points = np.array(
            [
                [0, 0, 0],
                [0, 250, 0],
                [250, 250, 0],
                [250, 0, 0],
            ],
            dtype="double",
        )

        image_points = corners.astype(np.double)

        # Rotation and translation vectors
        _, rvec, tvec = cv.solvePnP(
            model_points, image_points, camera_matrix, distortion_coefficient
        )

        ar_verts = np.array(
            [
                [0, 0, 0],
                [0, 1, 0],
                [1, 1, 0],
                [1, 0, 0],
                [0, 0, 1],
                [0, 1, 1],
                [1, 1, 1],
                [1, 0, 1],
            ]
        )

        ar_edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
        ]

        scale = 1
        ar_verts = np.array(list(map(translateXY, ar_verts)), dtype=np.float32)
        ar_verts *= scale

        verts = cv.projectPoints(
            ar_verts, rvec, tvec, camera_matrix, distortion_coefficient
        )[0].reshape(-1, 2)

        for i, j in ar_edges:
            (x0, y0), (x1, y1) = verts[i], verts[j]
            cv.line(image, (int(x0), int(y0)), (int(x1), int(y1)), (0, 0, 255), 10)

        return image
