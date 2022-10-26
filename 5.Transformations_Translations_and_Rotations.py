import cv2
import numpy as np
from matplotlib import pyplot as plt

def imshow(title="Image", image =None, size=10):
    w,h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

# Translations
image = cv2.imread("./images/Volleyball.jpeg")
imshow("Original", image)

height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

# Our Translation
#       | 1 0 Tx |
#  T  = | 0 1 Ty |

T = np.float32([[1,0, quarter_width], [0,1,quarter_height]])

img_translation = cv2.warpAffine(image, T, (width,height))
imshow("Translated", img_translation)

print(T)
print(height, width)

# Rotations
# cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)

image = cv2.imread('images/Volleyball.jpeg')
height, width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width,height))
imshow("Rotation 90 degrees with scale = 1", rotated_image)

# Scale = 0.5
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width,height))
imshow("Rotation 90 degrees with scale = 0.5", rotated_image)

#Rotation with cv2.transpose(less flexible)
rotated_image = cv2.transpose(image)
imshow("Original", image)
imshow("Rotated using Transpose", rotated_image)

# Let's now to a horizontal flip
flipped = cv2.flip(image,1)
imshow("Horizontal Flip", flipped)




