# Age_Detection_using_res10_300x300_ssd_iter_140000

## This repository contains a project for age detection using the res10_300x300_ssd_iter_140000 model, an SSD (Single Shot Multibox Detector) model trained for face detection. The age detection is built on top of this model to predict the age of individuals in real-time.

## Introduction
This project uses the res10_300x300_ssd_iter_140000 model for face detection and an additional pre-trained model to predict the age of detected faces. The age detection can be used for various applications, including demographic analysis, personalized services, and more.

## Features
- Real-time face detection and age prediction
- Easy to use with pre-trained models
- Supports webcam and video file inputs
- Provides age prediction for each detected face

## Installation
- Prerequisites
- Python 3.6 or higher
- OpenCV 4.0 or higher
- Git


- Clone the repository:

```
git clone https://github.com/yourusername/age-detection-res10.git
cd age-detection-res10
```
- Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
- Install the required packages:

```
pip install -r requirements.txt
```
- Download the pre-trained models:

- Res10_300x300_SSD Model
- Age Detection Model
- Place these models in a models directory within the project.

## Running the Age Detector
- To run the age detector on a webcam feed, use the following command:

```
python age_detector.py
```
## To run the age detector on a video file, use the following command:
```
python age_detector.py --input path/to/video.mp4
```
## Command Line Arguments
--input: Path to the video file. If not specified, the webcam feed will be used.
--confidence: Minimum probability to filter weak detections (default is 0.5).
Directory Structure
```
age-detection-res10/
├── models/
│   ├── res10_300x300_ssd_iter_140000.caffemodel
│   ├── deploy.prototxt
│   ├── age_net.caffemodel
│   └── age_deploy.prototxt
├── src/
│   ├── age_detector.py
│   ├── utils.py
│   └── ...
├── samples/
│   └── example_video.mp4
├── requirements.txt
└── README.md
```
#@ Dependencies
The project requires the following Python packages:
```
opencv-python
numpy
```
