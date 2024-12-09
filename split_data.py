import os
import random
import shutil
from itertools import islice

output = "Dataset/SplitData"
input = "Dataset/All"


try:
    shutil.rmtree(output)
except OSError as e:
    os.mkdir(output)
    
# Directories to Create
os.makedirs(f"{output}/train/images", exist_ok = True)
os.makedirs(f"{output}/train/labels", exist_ok = True)
os.makedirs(f"{output}/val/images", exist_ok = True)
os.makedirs(f"{output}/val/labels", exist_ok = True)
os.makedirs(f"{output}/test/images", exist_ok = True)
os.makedirs(f"{output}/test/labels", exist_ok = True)

# Get the names
listNames = os.listdir(input)

uniqueNames = []

for name in listNames:
    uniqueNames.append(name.split('.')[0])
uniqueNames = list(set(uniqueNames))

# Shuffle 
random.shuffle(uniqueNames)

# Find the number of images for each folder
lenData = len(uniqueNames)
print(f'Total Images:{uniqueNames}') 
