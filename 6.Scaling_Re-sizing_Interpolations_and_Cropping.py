import cv2
from matplotlib import pyplot as plt
import numpy as np

def imshow(title="Image", image=None, size=10):
    w,h = image.shape[:2]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
# Re-sizing
# cv2.resize(image, dsize(output image size), x scale, y scale, interpolation)
image = cv2.imread('images/oxfordlibrary.jpeg')
imshow("Scaling - Linear Interpolation", image)

image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
imshow("0.75x Scaling - Linear Interpolation", image_scaled)

image_scaled2 = cv2.resize(image, None, fx=2, fy=2, interpolation= cv2.INTER_CUBIC)
imshow("2x Scaling - Inter Cubic", image_scaled2)

image_scaled3 = cv2.resize(image, None, fx=2, fy=2, interpolation= cv2.INTER_NEAREST)
imshow("2x Scaling - Inter Nearest", image_scaled3)

image_scaled4 = cv2.resize(image, (900,400), interpolation=cv2.INTER_AREA)
imshow("Scaling - Inter Area", image_scaled4)

# Cropping

image = cv2.imread('images/oxfordlibrary.jpeg')

height, width = image.shape[:2]

start_row, start_col = int(height * .25), int(width * .25)

end_row, end_col = int(height * .75), int(width * .75)

cropped = image[start_row:end_row, start_col:end_col]

imshow("Original Image", image)

copy = image.copy()
cv2.rectangle(copy, (start_col, start_row), (end_col, end_row), (0,255,255), 10 )
imshow("Area we are cropping", copy)
imshow("Cropped Image", cropped)

# Image Pyraminds

image = cv2.imread("images/oxfordlibrary.jpeg")

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)
even_smaller = cv2.pyrDown(smaller)

imshow("Original", image)
imshow("Smaller", smaller)
imshow("Larger", larger)
imshow("Even Smaller", even_smaller)


