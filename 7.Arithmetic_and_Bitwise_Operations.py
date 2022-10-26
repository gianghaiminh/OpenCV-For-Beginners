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

# Increasing Brightness

image = cv2.imread("images/liberty.jpeg",0)
imshow("Grayscaled Image", image)
print(image)

M = np.ones(image.shape, dtype="uint8") * 100

added = cv2.add(image, M)
imshow("Increasing Brightness", added )

added2 = image + M
imshow("Simple Numpy Adding Results in Clipping", added2)

# Decreasing Brightness

subtracted = cv2.subtract(image, M)
imshow("Subtracted", subtracted)

subtracted2 = image - M
imshow("Subtracted 2", subtracted2)

# Bitwise Operations and Masking

square = np.zeros((300,300), np.uint8)
cv2.rectangle(square, (50,50), (250,250), 255, -2)
imshow("quare", square)

ellipse = np.zeros((300,300), np.uint8)
cv2.ellipse(ellipse, (150,150), (150,150), 30 , 0, 180, 255, -1)
imshow("ellipse", ellipse)

# Experimenting with some bitwise operations such as AND, OR, XOR and NOT

And = cv2.bitwise_and(square,ellipse)
imshow("AND", And)

bitwiseOr = cv2.bitwise_or(square, ellipse)
imshow("bitwiseOr", bitwiseOr)

bitwiseXOR = cv2.bitwise_xor(square, ellipse)
imshow("bitwiseXOR", bitwiseXOR)

bitwiseNot_sq = cv2.bitwise_not(square)
imshow("bitwiseNot_square", bitwiseNot_sq)









