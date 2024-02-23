import cv2
from matplotlib import pyplot as plt

# Load the image using OpenCV
img = cv2.imread("lct2/object.jpg")

# Convert the image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image using matplotlib
plt.imshow(img_rgb)
plt.axis('off')  # Turn off axis numbers
plt.show()