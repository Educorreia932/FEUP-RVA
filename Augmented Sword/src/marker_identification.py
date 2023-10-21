import cv2 as cv
import numpy as np


class MarkerIdentifier:
    SIDE_PIXELS = 250

    def __init__(self, markers_dict, min_id, max_id):
        self.markers_dict = markers_dict
        self.id_range = range(min_id, max_id + 1)

    def identify(self, image, corners):
        def get_marker_from_dict(marker_id):
            return cv.aruco.generateImageMarker(self.markers_dict, marker_id, self.SIDE_PIXELS)

        def get_marker_from_image(image, corners, marker_size):
            # Define the dimensions of the target image
            width, height = marker_size, marker_size

            # Define the target points
            target_points = np.array(
                [
                    [0, height],
                    [width, height],
                    [width, 0],
                    [0, 0],
                ],
                dtype=np.float32,
            )

            # Get the transformation matrix
            transformation_matrix, _ = cv.findHomography(corners, target_points)

            # Apply the transformation matrix to the source image
            warped = cv.warpPerspective(image, transformation_matrix, (width, height))

            _, marker = cv.threshold(warped, 127, 255, cv.THRESH_BINARY)

            return marker

        source_marker = get_marker_from_image(image, corners, self.SIDE_PIXELS)

        # Get four orientations of the target marker
        rotated_markers = [
            source_marker,
            cv.rotate(source_marker, cv.ROTATE_90_COUNTERCLOCKWISE),
            cv.rotate(source_marker, cv.ROTATE_180),
            cv.rotate(source_marker, cv.ROTATE_90_CLOCKWISE),
        ]

        for id in self.id_range:
            target_marker = get_marker_from_dict(id)

            for i, rotated_marker in enumerate(rotated_markers):
                # Subtract the two markers
                subtracted = np.subtract(target_marker, rotated_marker)

                # Count number of white pixels
                num_white_pixels = np.count_nonzero(subtracted == 255)

                # Rotate corners according to the marker orientation
                rotated_corners = np.roll(corners, i, axis=0)

                # If the number of white pixels is less than 1500, then we have a match
                if num_white_pixels < 1500:
                    return rotated_corners, id

        return None, -1
