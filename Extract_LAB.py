import os
import csv
import cv2
from skimage import color
import numpy as np

import time

start_time = time.time()

folder_path = r'D:\Research\Manganji2\23.12.2022\UV2'

folder_name = os.path.basename(folder_path) # get the folder name

# Create an empty list to store the mean values
mean_values = []

image_count = 0

# Loop through the files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is an image file
    if file_name.endswith('.JPG') or file_name.endswith('.jpg'):
        # Load the image
        image = cv2.imread(os.path.join(folder_path, file_name))
        image_gray = cv2.imread(os.path.join(folder_path, file_name), cv2.IMREAD_GRAYSCALE)
        # Apply Otsu's thresholding
        ret, thresholded_img = cv2.threshold(image_gray, 10, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #  convert the thresholded image into a binary image, where the pixels that
        #meet the threshold criteria are set to 1 and the pixels that do not meet the criteria are set to 0.
        mask = thresholded_img.astype(np.uint8) 
        # you can use the binary mask to extract specific information or features from the original image.
        original_image = image.copy()
        masked_image = cv2.bitwise_and(original_image, original_image, mask = mask)
        
        # Convert the image from RGB to LAB
        image_lab = color.rgb2lab(masked_image)
        # Calculate the mean values of the L, a, and b channels
        l_mean = np.mean(image_lab[:, :, 0])
        a_mean = np.mean(image_lab[:, :, 1])
        b_mean = np.mean(image_lab[:, :, 2])
        # Append the mean values to the list
        mean_values.append([file_name, l_mean, a_mean, b_mean])

        image_count += 1

        print(f'{image_count} processed!')

base_csv_path = r'D:\Research\Manganji2\23.12.2022\csv'

print(base_csv_path)

csv_file_path = f'{base_csv_path}\{folder_name}.csv'


# Write the mean values to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the headers
    csv_writer.writerow(['File Name', 'L Mean', 'A Mean', 'B Mean'])
    # Write the data
    csv_writer.writerows(mean_values)

end_time = time.time()

elapsed_time = end_time - start_time

print(f'Elapsed time: {elapsed_time:.2f} seconds')
print(f'Number of processed images: {image_count}')


