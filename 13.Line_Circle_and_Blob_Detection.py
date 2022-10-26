import cv2
from cv2 import circle
import numpy as np
from matplotlib import pyplot as plt

def imshow(title='Image', image= None, size =10):
    w,h = image.shape[:2]
    aspect_ratio = w/h
    plt.figure(figsize=(aspect_ratio * size, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
'''
image = cv2.imread('images/soduku.jpg')
imshow('Original', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize= 3)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, 3, 25)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image, (x1, y1), (x2,y2), (255,0,0), 2)

imshow('Hough Line', image)
'''
image = cv2.imread('images/soduku.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize= 3)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, 3, 25)

print(lines.shape)

for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(image, (x1,y1), (x2,y2), (0,255,0),2)

imshow('Probabilistic Hough Lines', image)       

# Circle Detection - Hough Cirlces

image = cv2.imread('images/Circles_Packed_In_Square_11.jpeg')
imshow('Circles', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2, 25)

cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1.2, 100)

circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.circle(image, (i[0], i[1]), i[2], (0,0,255), 5)
    cv2.circle(image, (i[0], i[1]), 2, (0,0,255), 8)

imshow('Detected circles', image)







