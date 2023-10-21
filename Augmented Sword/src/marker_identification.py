import cv2 as cv
import numpy as np


class MarkerIdentifier:
    def __init__(self, markers_dict):
        self.markers_dict = markers_dict

    def identify(self, image, corners):
        def squares_matrix(marker, side_pixels):
            marker_size = marker.shape[0]  # Number of squares in one dimension
            square_pixels = side_pixels // marker_size  # Number of pixels in one square

            grid = np.zeros((marker_size, marker_size))

            for y in range(0, side_pixels, square_pixels):
                for x in range(0, side_pixels, square_pixels):
                    square = marker[y : y + square_pixels, x : x + square_pixels]
                    num_white_pixels = np.count_nonzero(square == 0)

                    if num_white_pixels > square_pixels**2 / 2:
                        grid[y // square_pixels, x // square_pixels] = 1

            return grid

        def get_marker_from_dict(marker_id):
            return cv.aruco.generateImageMarker(self.markers_dict, marker_id, 250)

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

        marker_size = self.markers_dict.markerSize
        source_marker = get_marker_from_image(image, corners, 250)

        # Get four orientations of the target marker
        rotated_markers = [
            cv.rotate(source_marker, cv.ROTATE_90_CLOCKWISE),
            cv.rotate(source_marker, cv.ROTATE_180),
            cv.rotate(source_marker, cv.ROTATE_90_COUNTERCLOCKWISE),
            source_marker,
        ]

        for id in range(94, 100):
            target_marker = get_marker_from_dict(id)

            for rotated_marker in rotated_markers:
                # Subtract the two markers
                subtracted = np.subtract(target_marker, rotated_marker)

                # Count number of white pixels
                num_white_pixels = np.count_nonzero(subtracted == 255)

                if num_white_pixels < 1500:
                    return id

        return -1
