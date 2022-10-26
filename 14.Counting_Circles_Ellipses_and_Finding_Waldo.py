import cv2
import numpy as np
from matplotlib import pyplot as plt

def imshow(title='Image', image=None, size=10):
    w,h = image.shape[:2]
    aspect_ratio = w/h
    plt.figure(figsize=(aspect_ratio * size, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread('images/blobs.jpg',0)
#imshow('Original Image', image)

detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(image)

blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255),
                                    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = 'Number of Circular Blobs: ' + str(len(keypoints))
cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1, (0,100,255),2)

#imshow("Filtering Circular Blobs Only", blobs)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

params.filterByCircularity = True 
params.minCircularity = 0.9

params.filterByConvexity = False
params.minConvexity = 0.2

params.filterByInertia = True
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(image)

blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,0),
                                    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = 'Number of Circular Blobs: ' + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX,1, (0,100,255), 2)

#imshow('Filtering Circular Blobs Only', blobs)

# Finding Waldo Using Template Matching

template = cv2.imread('images/waldo.jpg')
imshow('Template', template)

image = cv2.imread('images/WaldoBeach.jpg')
imshow('Where is Waldo?', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('images/waldo.jpg', 0)

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 5)

imshow('Where is Waldo?', image)

