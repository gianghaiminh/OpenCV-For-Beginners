import cv2
print(cv2.__version__)

# Loading images
image = cv2.imread("./images/flowers.jpeg")

# Displaying images
from matplotlib import pyplot as plt
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
# Let's create a simple function to make displaying our images simpler and easier
def imshow(title="", image = None):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
imshow("Displaying Our First Image", image)

# Saving Images
cv2.imwrite("output.jpg", image)
# cv2.imwrite("output.png", image)

# Displaying Image Dimensions
import numpy as np
print(image.shape)
print(image.shape[0])

print("Height of Image: {} pixels".format(int(image.shape[0])))
print("Width of Image: {} pixels".format(int(image.shape[1])))
print("Depth of Image: {} pixels".format(int(image.shape[2])))


