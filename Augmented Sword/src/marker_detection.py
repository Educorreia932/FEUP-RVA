import cv2 as cv
import math
import numpy as np


class MarkerDetector:
    def __init__(self) -> None:
        pass

    def detect(self, image):
        thresholded = self._threshold(image)
        corners = self._corners(thresholded)

        return corners

    def _threshold(self, image):
        # Converting to grayscale and applying Gaussian blur
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (5, 5), 0)

        # Applying CLAHE histogram equalization
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        equalized = clahe.apply(blur)

        _, thresholded = cv.threshold(
            equalized, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU
        )

        return thresholded

    def _corners(self, image):
        # Get contours
        contours, _ = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Remove borders with a small length
        contours = [c for c in contours if len(c) > 40]

        # Polygonal approximation
        contours = [cv.approxPolyDP(c, 3, True) for c in contours]

        # Check if contour has 4 sides
        contours = [c for c in contours if len(c) == 4]

        # Sort corners
        corners = [c.reshape(-1, 2) for c in contours]
        corners = np.array(list(map(self._sort_corners, corners)))

        # Remove close rectangles
        corners = self._remove_close_rectangles(corners)

        # Remove rectangles that have a big length ratio
        corners = [
            c
            for c in corners
            if 4 * math.pi * cv.contourArea(c) / (cv.arcLength(c, True) ** 2) > 0.7
        ]

        # Get the biggest rectangle
        if len(corners) == 0:
            return None

        corners = max(corners, key=lambda c: cv.contourArea(c))

        return corners

    def _sort_corners(self, corners):
        def angle_with_reference(point, reference_point):
            x, y = point[0] - reference_point[0], point[1] - reference_point[1]

            return math.atan2(y, x)

        # Find the centroid as a reference point
        reference_point = (
            sum(x for x, _ in corners) / len(corners),
            sum(y for _, y in corners) / len(corners),
        )

        # Sort corners based on angles with respect to the reference point
        corners = sorted(
            corners,
            key=lambda point: angle_with_reference(point, reference_point),
            reverse=True,  # Sorting in anti-clockwise order
        )

        return corners

    def _remove_close_rectangles(self, rectangles):
        def is_too_close(rect1, rect2):
            return np.linalg.norm(rect1 - rect2) < 100

        filtered_rectangles = []

        for rectangle in rectangles:
            if not any(is_too_close(rectangle, r) for r in filtered_rectangles):
                filtered_rectangles.append(rectangle)

        return filtered_rectangles

    def _get_marker_image(self, image, marker_corners, marker_size):
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
        transformation_matrix, _ = cv.findHomography(marker_corners, target_points)

        # Apply the transformation matrix to the source image
        warped = cv.warpPerspective(image, transformation_matrix, (width, height))

        _, marker = cv.threshold(warped, 127, 255, cv.THRESH_BINARY)

        return marker
