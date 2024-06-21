# YOLOv5su-based Object Detection App

## Introduction
Welcome, This is an object detection application built using YOLOv5su. We have chosen YOLOv5su for its excellent balance of speed and accuracy, making it a reasonable choice for high-quality results in real-time object detection tasks.

The user should only upload an image and press (Analyze Image) button and it will return the names of the objects in the image.
![image](https://github.com/a5medashraf/Image-Component-Detector/assets/72763763/ac5b8d70-c74a-41da-8902-464f858e2354)

## How to Use

### 1. Create and Activate a Conda Environment
First, create a new Conda environment with Python 3.10:
```bash
conda create -n SlashAiEnv python=3.10
```

Activate the environment:
```bash
conda activate SlashAiEnv
```
### 2. Install Required Dependencies
Install the necessary dependencies using the provided requirements.txt file:
```bash
pip install -r requirements.txt
```
### 3. Run the Application
Finally, run the application using Streamlit:
```bash
streamlit run {path}\app.py
```

Replace {path} with the appropriate path to the app.py file.
Enjoy using the project for your object detection tasks! If you encounter any issues or have any questions, feel free to open an issue in the GitHub repository.
