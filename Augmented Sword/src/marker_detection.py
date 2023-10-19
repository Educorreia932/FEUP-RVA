import cv2 as cv
import math
import numpy as np

class MarkerDetector:
    MARKER_SIZE = 250

    @classmethod
    def detect_markers(self, image):
        thresholded = self._threshold(image)
        corners = self._corners(thresholded)

        for marker_corners in corners:
            yield self._get_marker_image(thresholded, marker_corners)

    @classmethod
    def _threshold(self, image):
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        _, thresholded = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) # Use Adaptative Thresholding

        return thresholded

    @classmethod
    def _corners(self, image):
        # TODO: Use adaptive thresholding
        # Get contours
        contours, _ = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Remove borders with a small length
        contours = [c for c in contours if len(c) > 70]

        # Polygonal approximation
        contours = [cv.approxPolyDP(c, 3, True) for c in contours]
        contours = [c for c in contours if len(c) == 4]

        # Sort corners
        corners = [c.reshape(-1, 2) for c in contours]
        corners = np.array(list(map(self._sort_corners, corners)))

        # Remove close rectangles
        corners = self._remove_close_rectangles(corners)

        # TODO: Sub-pixel approximation to smooth out rough edges

        return corners

    @classmethod
    def _sort_corners(self, corners):
        def angle_with_reference(point, reference_point):
            x, y = point[0] - reference_point[0], point[1] - reference_point[1]
            
            return math.atan2(y, x)
    
        # Find the centroid as a reference point
        reference_point = (
            sum(x for x, _ in corners) / len(corners),
            sum(y for _, y in corners) / len(corners)
        )
        
        # Sort corners based on angles with respect to the reference point
        corners = sorted(
            corners,
            key=lambda point: angle_with_reference(point, reference_point),
            reverse=True  # Sorting in anti-clockwise order
        )

        return corners

    @classmethod
    def _remove_close_rectangles(self, rectangles):
        def is_too_close(rect1, rect2):
            return np.linalg.norm(rect1 - rect2) < 100

        filtered_rectangles = []
        
        for rectangle in rectangles:
            if not any(is_too_close(rectangle, r) for r in filtered_rectangles):
                filtered_rectangles.append(rectangle)
        
        return filtered_rectangles

    @classmethod
    def _get_marker_image(self, image, marker_corners):
        # Define the dimensions of the target image
        width, height = self.MARKER_SIZE, self.MARKER_SIZE
        
        # Define the target points
        target_points = np.array([
            [0, height],
            [width, height],
            [width, 0],
            [0, 0],
        ], dtype=np.float32)
        
        # Get the transformation matrix
        transformation_matrix, _ = cv.findHomography(marker_corners, target_points)
        
        # Apply the transformation matrix to the source image
        warped = cv.warpPerspective(image, transformation_matrix, (width, height))

        _, marker = cv.threshold(warped, 127, 255, cv.THRESH_BINARY)

        return marker

    