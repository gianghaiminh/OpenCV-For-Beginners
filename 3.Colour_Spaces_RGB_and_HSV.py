import cv2
import numpy as np
from matplotlib import pyplot as plt

# View the individual channels of an RGB Image
def imshow(title="", image = None, size =10):
    w,h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread("./images/castara.jpeg")

B, G, R = cv2.split(image)
print(B.shape)
print(G.shape)
print(R.shape)

imshow("Blue Channel Only", B)







