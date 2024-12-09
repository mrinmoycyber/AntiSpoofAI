import os
import random
import shutil
from itertools import islice

outputFile = "Dataset/SplitData"
inputFile = "Dataset/All"
splitRatio = {"train":0.7, "val":0.2, "test":0.1}
classes = ["fake", "real"]


try:
    shutil.rmtree(outputFile)
except OSError as e:
    os.mkdir(outputFile)
    
# Directories to Create
os.makedirs(f"{outputFile}/train/images", exist_ok = True)
os.makedirs(f"{outputFile}/train/labels", exist_ok = True)
os.makedirs(f"{outputFile}/val/images", exist_ok = True)
os.makedirs(f"{outputFile}/val/labels", exist_ok = True)
os.makedirs(f"{outputFile}/test/images", exist_ok = True)
os.makedirs(f"{outputFile}/test/labels", exist_ok = True)

# Get the names
listNames = os.listdir(inputFile)

uniqueNames = []

for name in listNames:
    uniqueNames.append(name.split('.')[0])
uniqueNames = list(set(uniqueNames))

# Shuffle 
random.shuffle(uniqueNames)

# Find the number of images for each folder
lenData = len(uniqueNames)
lenTrain = int(lenData * splitRatio['train'])
lenVal = int(lenData * splitRatio['val'])
lenTest = int(lenData * splitRatio['test'])

# Put remaining images in Training
if lenData != lenTrain + lenTest + lenVal:
    remaining = lenData - (lenTrain+lenTest+lenVal)
    lenTrain += remaining

# Split the list
lenToSplit = [lenTrain, lenVal, lenTest]
Input = iter(uniqueNames)
Output = [list(islice(Input, elem)) for elem in lenToSplit]
print(f'Total Images: {lenData} \nSplit: {len(Output[0])} {len(Output[1])} {len(Output[2])}')

# Copy the files
sequence  = ['train', 'val', 'test']
for i, out in enumerate(Output):
    for fileName in out:
        shutil.copy(f'{inputFile}/{fileName}.jpg', f'{outputFile}/{sequence[i]}/images/{fileName}.jpg')
        shutil.copy(f'{inputFile}/{fileName}.txt', f'{outputFile}/{sequence[i]}/labels/{fileName}.txt')
print("Split Process Completed")

# Creating Data.yaml file
dataYaml = f'path: ../Data\n\
train: ../train/images\n\
val: ../val/images\n\
test: ../test/images\n\
\n\
nc: {len(classes)}\n\
names: {classes}'


f = open(f"{outputFile}/data.yaml", 'a')
f.write(dataYaml)
f.close()
