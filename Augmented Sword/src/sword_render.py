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
                # TODO: Can be calculated using rotation matrixes
                [
                    # Front face
                    [
                        [-0.325, -0.325, -0.5],
                        [-0.325, 0.325, -0.5],
                        [0.325, 0.325, -0.5],
                        [0.325, -0.325, -0.5],
                    ],
                    # Right face
                    [
                        [-0.5, -0.325, 0.325],
                        [-0.5, 0.325, 0.325],
                        [-0.5, 0.325, -0.325],
                        [-0.5, -0.325, -0.325],
                    ],
                    # Back face
                    [
                        [0.325, -0.325, 0.5],
                        [0.325, 0.325, 0.5],
                        [-0.325, 0.325, 0.5],
                        [-0.325, -0.325, 0.5],
                    ],
                    # Left face
                    [
                        [0.5, -0.325, -0.325],
                        [0.5, 0.325, -0.325],
                        [0.5, 0.325, 0.325],
                        [0.5, -0.325, 0.325],
                    ],
                    # Top face
                    [
                        [-0.325, 0.5, -0.325],
                        [-0.325, 0.5, 0.325],
                        [0.325, 0.5, 0.325],
                        [0.325, 0.5, -0.325],
                    ],
                    # Bottom face
                    [
                        [-0.325, -0.5, 0.325],
                        [-0.325, -0.5, -0.325],
                        [0.325, -0.5, -0.325],
                        [0.325, -0.5, 0.325],
                    ],
                ],
                dtype=np.float32,
            )
            * self.scale
        )

        # Rotation and translation vectors
        _, rvec, tvec = cv.solvePnP(
            model_points[5],
            image_points,
            self.camera_matrix,
            self.distortion_coefficient,
        )

        self.draw_sword(image, rvec, tvec)

        return image

    def draw_referential(self, image, rvec, tvec):
        ar_verts = (
            np.array(
                [[0, 0, 0], [0.5, 0, 0], [0, 0.5, 0], [0, 0, 0.5]],
                dtype=np.float32,
            )
            * self.scale
        )

        ar_edges = [[0, 1], [0, 2], [0, 3]]

        # X - Blue
        # Y - Green
        # Z - Red

        return self.draw_wireframe(
            image,
            rvec,
            tvec,
            ar_verts,
            ar_edges,
            [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
        )

    def draw_sword(self, image, rvec, tvec):
        self.load_object("../data/models/sword")

        ar_verts, ar_faces = self.load_object("../data/models/sword")

        ar_verts *= self.scale

        return self.draw_wireframe(image, rvec, tvec, ar_verts, ar_faces)

    def draw_wireframe(self, image, rvec, tvec, ar_verts, ar_faces):
        # Project 3D points to image plane
        verts, _ = cv.projectPoints(
            ar_verts,
            rvec,
            tvec,
            self.camera_matrix,
            self.distortion_coefficient,
        )

        for face in ar_faces:
            points = verts[face.astype(np.int32)].astype(np.int32)

            cv.drawContours(image, [points], -1, (0, 0, 255), 2)

        return image

    def load_object(self, path):

        with open(f"{path}/vertices.txt", "r") as file:
            vertices = np.array([np.array([float(x) for x in line.split()]) for line in file.readlines()])

        with open(f"{path}/faces.txt", "r") as file:
            faces = np.array([np.array([int(x) - 1 for x in line.split()]) for line in file.readlines()])
        
        return vertices, faces