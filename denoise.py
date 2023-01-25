import cv2

# Load the image
img = cv2.imread("IMG_0913.jpg")

# Apply the Non-local Means denoising algorithm
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

# Save the denoised image
cv2.imwrite("IMG_0913_denoised_image.jpg", dst)
