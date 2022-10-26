import cv2 
import numpy as np
from matplotlib import pyplot as plt

def imshow(title="Image", image = None, size=10):
    w,h = image.shape[:2]
    aspect_ratio = w/h
    plt.figure(figsize=(aspect_ratio * size, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread("images/LP.jpg")
#imshow('Input Image', image)

# Applying cv2.findContours()
#cv2.findContours(image, Retrieval Mode, Approximation Method)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, th2 = cv2.threshold(gray, 0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#imshow("After thresholding", th2)

contours, hierarchy = cv2.findContours(th2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0,255,0), thickness=2)
#imshow('Contours overlaid on orginal image', image)

print('Number of Contours found = ' + str(len(contours)))
print(contours[0])

# What happens if we don't threshold? Bad things

image = cv2.imread('images/LP.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#imshow('After Grayscaling', gray)

contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0,255,0), thickness=2)
#imshow('Contours overlaid on original image', image)
print('Number of Contours found = '+ str(len(contours)))

# We can use Canny Edges instead of Thresholding

image = cv2.imread('images/LP.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 30, 200)
#imshow('Canny Egges', edged)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0,255,0), thickness=2)

#imshow('Contour overlaid on orginal image', image)
print('Number of Contours found = '+ str(len(contours)))

# RETREIVAL MODES

# Retr_List
image = cv2.imread('images/LP.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
imshow('After Thresholding', th2)

contours, hierarchy = cv2.findContours(th2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0,255,0), thickness=2)
imshow('Contours overlaid on original image', image)







