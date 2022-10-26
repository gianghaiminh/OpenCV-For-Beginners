import cv2
import numpy as np
from matplotlib import pyplot as plt

def imshow(title = "Image", image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
'''
image = cv2.imread('images/bunchofshapes.jpg')
imshow('Original Image', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50,200)
#imshow('Canny Edges', edged)

contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#print('Number of contours found =', len(contours))

cv2.drawContours(image, contours, -1, (0,255,0), 3)
#imshow('All Contours', image)

def get_contour_areas(contours):
  all_areas = []
  for cnt in contours:
    area = cv2.contourArea(cnt)
    all_areas.append(area)
  return all_areas

image = cv2.imread('images/bunchofshapes.jpg')

#print('Contor Areas before sorting...')
#print(get_contour_areas(contours))

sorted_contours = sorted(contours, key = cv2.contourArea, reverse= True)

#print('Contor Areas after sorting...')
#print(get_contour_areas(sorted_contours))

for(i,c) in enumerate(contours):
  M = cv2.moments(c)
  cx = int(M['m10'] / M['m00'])
  cy = int(M['m01'] / M['m00'])
  cv2.putText(image, str(i+1), (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 2,(0,255,0), 3)
  cv2.drawContours(image, [c], -1, (255,0,0), 3)

#imshow('Contours by area', image)

# Define some functions we'll be using 
def x_corn_contour(contours):
  if cv2.contourArea(contours) > 10:
    M = cv2.moments(contours)
    return( int(M['m10'] / M['m00']))
  else:
    pass

def label_contour_center(image, c):
  M = cv2.moments(c)
  cx = int(M['m10'] / M['m00'])
  cy = int(M['m01'] / M['m00'])

  cv2.circle(image, (cx, cy), 10, (0,0,255), -1)
  return image


# We use Moments to Calculate the Center and then use the X Cordinate to sort from left to right

image = cv2.imread('images/bunchofshapes.jpg')
orginal_image = image.copy()

for(i,c) in enumerate (contours):
  orig = label_contour_center(image, c)

#imshow('Sorting Left to Right', image)


contour_left_to_right = sorted(contours, key = x_corn_contour, reverse=False)

for(i,c) in enumerate (contour_left_to_right):
  cv2.drawContours(orginal_image, [c] , -1, (0,0,255), 3)
  M = cv2.moments(c)
  cx = int(M['m10'] / M['m00'])
  cy = int(M['m01'] / M['m00'])
  cv2.putText(orginal_image, str(i+1), (cx,cy), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 3)
  (x,y,w,h) = cv2.boundingRect(c)

#imshow('Contours by area', orginal_image)


# Approximating Contours using ApproxPolyDP
# cv2.approxPolyDP(contour, Approximation Accuracy, Closed)

image = cv2.imread('images/house.jpg')
orig_image = image.copy()
#imshow('Original Image', orig_image)

gray = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
copy = image.copy()

for c in contours:
  x,y,w,h = cv2.boundingRect(c)
  cv2.rectangle(orig_image, (x,y), (x+w, y+h), (0,0,255), 2)
  cv2.drawContours(image, [c], 0, (0,255,0), 2)

#imshow('Drawuing of Contours', image)
#imshow('Bounding Rectangles', orig_image)

for c in contours:
  accuracy = 0.03 * cv2.arcLength(c, True)
  approx = cv2.approxPolyDP(c, accuracy, True)
  cv2.drawContours(copy, [approx], 0, (0,255,0), 2)

#imshow('Approx Poly DP', copy)

# Convex Hull

image = cv2.imread('images/hand.jpg')
orginal_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imshow('Original Image', image)

ret, thresh = cv2.threshold(gray, 176, 255, 0)

contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE )
cv2.drawContours(image, contours, 0, (0,255,0), 2)
#imshow('Contours of Hand', image)

n= len(contours) -1
contours = sorted(contours, key= cv2.contourArea, reverse= False)[:n]

for c in contours:
  hull = cv2.convexHull(c)
  cv2.drawContours(orginal_image, [hull], 0, (0,255,0), 2)

#imshow('Convex Hull', orginal_image)
'''
#Matching Contours
#cv2.matchShapes(contour template, contour, method, method parameter)

template = cv2.imread('images/4star.jpg', 0)
imshow('Template', template)

target = cv2.imread('images/shapestomatch.jpg')
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(template, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

sorted_contours = sorted(contours, key = cv2.contourArea, reverse=True)

template_contours = contours[1]

contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
  match = cv2.matchShapes(template_contours, c, 3, 0.0)
  print(match)

  if match < 0.15:
    closest_contours = c
  else:
    closest_contours = []

cv2.drawContours(target, [closest_contours], -1, (0,255,0), 3)
imshow('Output', target)














