import shutil
from PIL import Image
import os



import os

path = r'D:\Research\Manganji2\23.12.2022\color2'
counter = 1

# Iterating through all the files in the specified directory
for filename in os.listdir(path):
    if filename.endswith(".jpg"):
        try:
            # Opening the image file
            with Image.open(os.path.join(path, filename)) as im:
                # Extracting the exif data from the image file
                exif_data = im._getexif()
                date_time = exif_data[36867] # 36867 is an Exif tag key that represents the "DateTime" field. unique identifier
                i = date_time.split(":")[0]
                j = date_time.split(":")[1]
                # Creating the new file name
                new_filename = os.path.join(path, '{:03d}_IMG{}_{}.jpg'.format(counter, i, j))
                # Renaming the file
                os.rename(os.path.join(path, filename), new_filename)
                counter += 1
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

