import cv2
from matplotlib import pyplot as plt

#Convert a color image to grayscale
def imshow(title="Image", image = None, size = 5):
    w,h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread("./images/castara.jpeg")

imshow("Castara, Tobago", image,size=5)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imshow("Converted to grayscale", gray_image)

print(image.shape)
print(gray_image.shape)


