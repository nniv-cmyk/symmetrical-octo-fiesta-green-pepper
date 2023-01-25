import os
import exifread
from pathlib import Path
from datetime import datetime

folder = r"D:\Research\Manganji2\23.12.2022\color2"

# Create a list of image files
images = [f for f in os.listdir(folder) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]

# Create a list of tuples containing the image file path and the creation date
images_creation_date = []
for image in images:
    with open(os.path.join(folder, image), 'rb') as f:
        tags = exifread.process_file(f)
        creation_date = tags.get('EXIF DateTimeOriginal')
        if creation_date:
            creation_date = datetime.strptime(str(creation_date), '%Y:%m:%d %H:%M:%S')
            images_creation_date.append((image, creation_date))
        else:
            #if the image does not contain the 'EXIF DateTimeOriginal' tag, use the last modified time
            images_creation_date.append((image, os.path.getmtime(os.path.join(folder, image))))

# sort the list of tuples by the second element (the creation date)
images_creation_date.sort(key=lambda x: x[1])

# rename the files in the sorted order
for i, image_tuple in enumerate(images_creation_date):
    os.rename(os.path.join(folder, image_tuple[0]), os.path.join(folder, f"{i:03d}_{image_tuple[0]}"))
