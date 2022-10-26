import cv2
import numpy as np
from matplotlib import pyplot as plt

def imshow(title="Image", image = None, size =10):
    w,h = image.shape[:2]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
# Blurring using Convolutions
image = cv2.imread('images/flowers.jpeg')
imshow('Original Image', image)

kernel_3x3 = np.ones((3,3), np.float32) / 9

blurred = cv2.filter2D(image, -1, kernel_3x3)
imshow('3x3 Kernel Blurring', blurred)

kernel_7x7 = np.ones((7,7), np.float32) /49

blurred2 = cv2.filter2D(image, -1, kernel_7x7)
imshow('7x7 Kernel Blurring', blurred2)

# Other commonly used blurring methods in OpenCV

blur = cv2.blur(image, (5,5))
imshow('Averaging', blur)

Gaussian = cv2.GaussianBlur(image, (5,5), 0)
imshow('Gaussian Blurring', Gaussian)

median = cv2.medianBlur(image, 5)
imshow('Median Blurring', median)

# Bilateral Filter
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
imshow('Bilateral Blurring', bilateral)

image = cv2.imread('images/hilton.jpeg')
imshow('Original', image)

dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)
imshow('fastNlMeansDenoisingColored', dst)

# Sharpening Images
 
image = cv2.imread('images/hilton.jpeg')
imshow('Original', image)

# Sharpening Images
kernel_sharpening = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])

sharpened = cv2.filter2D(image, -1, kernel_sharpening)
imshow('Sharpened Image', sharpened)


