import cv2
import numpy as np
from matplotlib import pyplot as plt

# Drawing images and shapes using OpenCV
def imshow(title=" ", image =None, size =10):
    w,h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(aspect_ratio * size, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
# Create a black image using numpy to create and array of black 
image = np.zeros((512,512,3), np.uint8)

image_gray = np.zeros((512,512), np.uint8)

imshow("Black Canvas - RGB Color", image)
imshow("Black Canvas - Grayscale", image_gray)

# Let's draw a line over our black square
# cv2.line(image, starting cordinates, ending cordinates, color, thickness)
cv2.line(image, (0,0), (512,512), (255,127,0), 5)
imshow("Black Canvas With Diagonal Line",image)

# Drawing Rectangles
# cv2.rectangle(image, starting vertex, opposite vertex, color, thickness)```
image = np.zeros((512,512,3), np.uint8)
cv2.rectangle(image, (100,100), (300,250), (127,50,127),10)
imshow("Black Canvas With Pink Rectangle", image)

# Now let's draw some cirlcles?
# cv2.cirlce(image, center, radius, color, fill)
image = np.zeros((512,512,3), np.uint8)
cv2.circle(image, (350,350),100, (15,150,50), -1)
imshow("Black Canvas With Green Circle", image)

# Polygons
# cv2.polylines(image, points, Closed?, color, thickness)
image = np.zeros((512,512,3), np.uint8)

pts = np.array([[10,50],[400,50], [90,200], [50,500]])

pts.reshape((-1,1,2))

cv2.polylines(image, [pts], True, (0,0,255), 3)
imshow("Black Canvas With Red Polygon",image)


# And now for adding text with cv2.putText
# cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, Color, Thickness)

image = np.zeros((1000,1000,3), np.uint8)
ourString = "Hello World"
cv2.putText(image, ourString, (155,290), cv2.FONT_HERSHEY_COMPLEX, 3, (40,200, 0), 4)
imshow("Messing With Some Text", image)


