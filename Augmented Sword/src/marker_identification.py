import cv2 as cv
import numpy as np

class MarkerIdentifier:
    MARKER_SIZE = 250
    dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)

    @classmethod
    def identify(self, source_marker):
        def squares_grid(marker, marker_size):
            marker_length = marker.shape[0]
            square_length = marker_length // marker_size

            grid = np.zeros((marker_size, marker_size))

            for y in range(0, marker_length, square_length):
                for x in range(0, marker_length, square_length):
                    square = marker[y:y + square_length, x:x + square_length]    
                    num_white_pixels = np.sum(square == 255)

                    if num_white_pixels > square_length ** 2 / 2:
                        grid[y // square_length, x // square_length] = 1

            return grid
        
        def get_marker_image(dictionary, marker_id):
            return cv.aruco.generateImageMarker(dictionary, marker_id, self.MARKER_SIZE)

        # Get the number of markers in the dictionary
        num_markers = 250
        source_grid = squares_grid(source_marker, 8)

        for id in range(num_markers):
            target_marker = get_marker_image(self.dictionary, id)

            # Get four orientations of the target marker
            rotated_markers = [
                cv.rotate(target_marker, cv.ROTATE_90_CLOCKWISE),
                cv.rotate(target_marker, cv.ROTATE_180),
                cv.rotate(target_marker, cv.ROTATE_90_COUNTERCLOCKWISE),
                target_marker
            ]

            for rotated_marker in rotated_markers:
                rotated_grid = squares_grid(rotated_marker, 8)

                if np.array_equal(source_grid, rotated_grid):
                    return id
                
        return -1
