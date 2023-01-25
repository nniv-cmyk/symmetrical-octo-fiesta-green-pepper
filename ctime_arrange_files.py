import os
import datetime
from pathlib import Path

folder = r"D:\Research\Manganji2\23.12.2022\UV2"

# Create a list of image files
images = [f for f in os.listdir(folder) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]

# Sort the list of images by the date created
images.sort(key=lambda x: os.path.getctime(os.path.join(folder, x)))

# Rename the files in the sorted order
for i, image in enumerate(images):
    os.rename(os.path.join(folder, image), os.path.join(folder, f"{i:03d}_{image}"))
