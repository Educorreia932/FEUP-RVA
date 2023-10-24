import sys
import numpy as np
import cv2 as cv

if (len(sys.argv) < 2):
    print(f"Usage: {sys.argv[0]} <file_to_save(.npz format)>")
    exit()

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((4 * 5, 3), np.float32)
objp[:, :2] = np.mgrid[0:4, 0:5].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

cv.namedWindow("img")

# Capture video from webcam
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Can't open stream")
    exit()

img_count = 0
while img_count < 11:
    ret, img = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        exit()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('img', img)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (4, 5), None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv.drawChessboardCorners(img, (4, 5), corners2, ret)
        cv.imshow('img', img)

        img_count += 1

        # Freeze image to allow for the rotation of the chessboard
        cv.waitKey(2000)

    cv.waitKey(50)

ret, camera_matrix, distort_coeff, rvecs, tvecs = cv.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None)

print(f"Camera matrix: {camera_matrix}")
print(f"Distortion coefficients: {distort_coeff.ravel()}")

mean_error = 0

for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], camera_matrix, distort_coeff)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2) / len(imgpoints2)
    mean_error += error

print(f"Total error: {mean_error / len(objpoints)}")

# Saving the intrinsic parameters
np.savez(sys.argv[1], camera_matrix=camera_matrix, distortion_coefficients=distort_coeff)

cv.waitKey(0)
cv.destroyAllWindows()