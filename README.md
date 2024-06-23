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
