import cv2
import numpy as np
from matplotlib import pyplot as plt

def imshow(title='Image', image = None, size=10):
    w,h = image.shape[:2]
    aspect_ratio = w/h
    plt.figure(figsize=(aspect_ratio * size, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread('images/scan.jpeg',0)
imshow('Original', image)

ret, thresh1 = cv2.threshold(image, 127,255,cv2.THRESH_BINARY)
imshow('1 Threshold Binary @ 127', thresh1)

ret, thresh2 = cv2.threshold(image, 127, 255,cv2.THRESH_BINARY_INV)
imshow('2 Threshold Binary Inverse @ 127', thresh2)

ret, thresh3 = cv2.threshold(image, 127, 255,cv2.THRESH_TRUNC)
imshow('3 THRESH TRUNC @ 127', thresh3)

ret, thresh4 = cv2.threshold(image, 127, 255,cv2.THRESH_TOZERO)
imshow('4 THRESH TOZERO @ 127', thresh4)

ret, thresh5 = cv2.threshold(image, 127, 255,cv2.THRESH_TOZERO_INV)
imshow('5 THRESH TOZERO IVN @ 127', thresh5)

# Adaptive Thresholding
# cv2.adaptiveThreshold**(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) → dst

thresh = cv2.adaptiveThreshold(image, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3,5)
imshow("Adaptive Mean Thresholding", thresh)

_, th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
imshow("Otsu's Thresholding", th2)

blur = cv2.GaussianBlur(image, (5,5), 0)
_, th3 = cv2.threshold(blur,0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
imshow("Guassian Otsu's Thresholding", th3)








