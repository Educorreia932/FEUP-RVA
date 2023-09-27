import cv2 as cv

image = cv.imread("test.jpg")

cv.imshow('img', image)
cv.waitKey(0)