import cv2
import numpy as np

# Load the image and the template
image = cv2.imread('piman2.png')
template = cv2.imread('piman2_template.png')

# Convert the images to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Perform the template matching
result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Get the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw a rectangle around the best match
top_left = max_loc
bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# Show the result
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

