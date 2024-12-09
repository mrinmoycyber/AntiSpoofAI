# SpoofShield 🛡️🤖

## Project Goal 🎯
The goal of this project is to develop an AI-powered face spoofing detection system using YOLO-based real-time face detection and computer vision techniques. The system is designed to differentiate between real and fake faces, detecting whether an individual in front of the camera is authentic or a spoof (e.g., a photograph, video, or mask). The project aims to provide a robust solution for face recognition security by identifying potential spoofing attempts in real-time.

## Features ✨
- **Real-time Face Detection** 🕵️‍♂️: Detects faces in video streams using YOLOv5 for accurate and fast results.
- **Spoof Detection** 🚫📸: Differentiates between real faces and spoofed attempts (e.g., photos or videos) to prevent unauthorized access.
- **Confidence Scoring** 💯: Each detection is accompanied by a confidence score that helps assess the accuracy of the detection.
- **Bounding Box Visualization** 📦: Draws bounding boxes around detected faces, making it easier to see which faces are being recognized.
- **Customizable Detection Threshold** ⚙️: Adjustable confidence threshold to filter out low-confidence detections.

## Project Structure 📁
```plaintext
├── SpoofShield
|   ├── Code/
│   ├── data.py
│   ├── main.py
│   ├── split_data.py
│   └──train.py                                
│   ├── Datasets/
│   │   ├── All                   
│   │   ├── DataCollection
│   │   ├── Real
│   │   ├── Fake                     
│   │   └── SplitData
│   ├── Test/
│   │   ├── face_detector_test.py
│   │   ├── test.txt
│   │   ├── text_file_test.py
│   │   └── yolo_test.py  
│   ├── models/
│   └──l_version_1_300.pt
├── .gitignore                                                   
├── LICENSE                                   
└── README.md                                    
```
## Video Output 🎥
Watch the project demo here: 

https://github.com/user-attachments/assets/9428f5e2-379b-4454-a23e-a24aedf3b956

## Technologies Used 🚀
- **YOLOv5** for real-time face detection
- **OpenCV** for image processing and computer vision tasks
- **Python** for scripting and automation
- **cvzone** for simplifying OpenCV tasks like bounding box drawing


