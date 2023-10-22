import numpy as np
import cv2 as cv


class SwordRenderer:
    scale = 250
    files = np.load("camera.npz")
    camera_matrix = files["camera_matrix"]
    distortion_coefficient = files["distortion_coefficients"]

    def draw(self, image, marker_corners, marker_id):
        # Roll marker corners (DEBUG)
        marker_corners = np.roll(marker_corners, -1, axis=0)

        image_points = marker_corners.astype(np.double)

        # Faces of the cube
        model_points = (
            np.array(
                [
                    # Front face
                    [
                        [-0.325, -0.325, -0.5],
                        [-0.325, 0.325, -0.5],
                        [0.325, 0.325, -0.5],
                        [0.325, -0.325, -0.5],
                    ],
                ],
                dtype=np.float32,
            )
            * self.scale
        )

        # Rotation and translation vectors
        _, rvec, tvec = cv.solvePnP(
            model_points[0], image_points, self.camera_matrix, self.distortion_coefficient
        )

        self.draw_referential(image, rvec, tvec)

        return image

    def draw_referential(self, image, rvec, tvec):
        ar_edges = [[0, 1], [0, 2], [0, 3]]

        ar_verts = (
            np.array(
                [[0, 0, 0], [0.5, 0, 0], [0, 0.5, 0], [0, 0, 0.5]],
                dtype=np.float32,
            )
            * self.scale
        )

        return self.draw_wireframe(image, rvec, tvec, ar_verts, ar_edges)

    def draw_wireframe(self, image, rvec, tvec, ar_verts, ar_edges):
        # Project 3D points to image plane
        verts, _ = cv.projectPoints(
            ar_verts,
            rvec,
            tvec,
            self.camera_matrix,
            self.distortion_coefficient,
        )

        for i, ar_edge in enumerate(ar_edges):
            start_point = verts[ar_edge[0]][0].astype(np.int32)
            end_point = verts[ar_edge[1]][0].astype(np.int32)

            image = cv.line(
                image,
                start_point,
                end_point,
                (255, 255, 255) * abs(ar_verts[i + 1]),
                2,
            )

        return image
