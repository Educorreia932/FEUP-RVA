import numpy as np
import cv2 as cv


class SwordRenderer:
    @classmethod
    def draw(cls, image, marker_corners, marker_id):
        files = np.load("camera.npz")
        camera_matrix = files["camera_matrix"]
        distortion_coefficient = files["distortion_coefficients"]

        scale = 250

        image_points = marker_corners.astype(np.double)
        model_points = (
            np.array(
                [
                    [-0.5, 0.5, 0],
                    [-0.5, -0.5, 0],
                    [0.5, -0.5, 0],
                    [0.5, 0.5, 0],
                ],
                dtype="double",
            )
            * scale
        )

        # Rotation and translation vectors
        _, rvec, tvec = cv.solvePnP(
            model_points, image_points, camera_matrix, distortion_coefficient
        )

        # Project 3D points to image plane
        ar_verts = (
            np.array(
                [
                    [-0.5, 0.5, 0.0],
                    [-0.5, -0.5, 0.0],
                    [0.5, -0.5, 0.0],
                    [0.5, 0.5, 0.0],
                    [-0.5, 0.5, 1.0],
                    [-0.5, -0.5, 1.0],
                    [0.5, -0.5, 1.0],
                    [0.5, 0.5, 1.0],
                ],
                dtype=np.float32,
            )
            * scale
        )

        ar_edges = [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [4, 5],
            [5, 6],
            [6, 7],
            [0, 4],
            [1, 5],
            [2, 6],
            [3, 7],
        ]

        verts, _ = cv.projectPoints(
            ar_verts,
            rvec,
            tvec,
            camera_matrix,
            distortion_coefficient,
        )

        for ar_edge in ar_edges:
            start_point = verts[ar_edge[0]][0].astype(np.int32)
            end_point = verts[ar_edge[1]][0].astype(np.int32)

            image = cv.line(
                image,
                start_point,
                end_point,
                (0, 255, 0),
                2,
            )

        return image
