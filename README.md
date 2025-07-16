# AttendEase - Smart Attendance Management System

## Overview
AttendEase is a facial recognition-based attendance management system built with Python and OpenCV. It automates the attendance tracking process by capturing, training, and recognizing faces in real-time.

## Tech Stack
- **Python 3.x**
- **OpenCV** - For image processing and facial recognition
- **NumPy** - For numerical computations
- **PIL (Python Imaging Library)** - For image handling
- **Threading** - For concurrent operations
- **LBPH Face Recognizer** - For face recognition algorithms

## Features
- Camera testing functionality
- Face capture and registration
- Face recognition training
- Automated attendance marking
- CSV-based attendance records
- Real-time face detection

## Project Structure
```
AttendEase/
├── Attendance/              # Stores attendance records
├── StudentDetails/          # Contains student information
├── TrainingImage/          # Stores captured face images
├── TrainingImageLabel/     # Contains trained model data
├── capture_image.py        # Image capture module
├── check_camera.py         # Camera testing module
├── recognize.py            # Face recognition module
├── train_image.py         # Model training module
└── main.py                # Main application entry point
```

## Installation
1. Clone the repository or download the ZIP file
2. Install required dependencies:
```bash
pip install opencv-python
pip install numpy
pip install pillow
```

## How to Use
1. Run `main.py` to start the application
2. Choose from the following options:
   - Test Camera: Verify camera functionality
   - Capture Faces: Register new students/employees
   - Train Images: Train the system with captured faces
   - Recognize & Attendance: Start attendance marking
3. Attendance records are automatically saved in CSV format

## Requirements
- Python 3.x
- Webcam
- Minimum 512MB RAM
- 1GB free disk space
