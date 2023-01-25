import os
from os.path import getctime

path = r'D:\Research\Manganji2\23.12.2022\color2'

# Get all files in the folder
files = [f for f in os.listdir(path) if f.endswith('.JPG')]

# Sort files by creation time
files.sort(key=lambda x: getctime(os.path.join(path, x)))

# Rename files
for i, f in enumerate(files):
    new_name = '{:03d}_IMG{}_{}.jpg'.format(i+1, (i+1)//2, (i+1)%2)
    os.rename(os.path.join(path, f), os.path.join(path, new_name))



