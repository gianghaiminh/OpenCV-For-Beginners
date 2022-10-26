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

image =cv2.imread('images/opencv_inv.png',0)
#imshow('Original', image)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(image, kernel, iterations=1)
#imshow("Erosion", erosion)

dilation = cv2.dilate(image, kernel, iterations=1)
#imshow("Dilation", dilation)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
#imshow('Open', opening)

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
#imshow('Closing', closing)

# Candy Edge Detection

image = cv2.imread("images/londonxmas.jpeg", 0)
#imshow('Original', image)

canny = cv2.Canny(image, 50, 120)
#imshow('Canny 1', canny)

canny = cv2.Canny(image, 10, 200)
#imshow('Canny Wide', canny)

canny = cv2.Canny(image, 200, 240)
#imshow('Canny Narrow', canny)

canny = cv2.Canny(image, 60, 110)
#imshow('Canny 4', canny)

# Auto Canny

def autoCanny(image):
    blurred_img = cv2.blur(image, ksize=(5,5))
    med_val = np.median(image)
    lower = int(max(0, 0.66 * med_val))
    upper = int(min(255, 1.33 * med_val))
    edges = cv2.Canny(image=image, threshold1= lower, threshold2=upper)
    return edges

auto_Canny = autoCanny(image)
imshow('Auto Canny', auto_Canny)







