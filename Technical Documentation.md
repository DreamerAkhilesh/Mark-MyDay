# AttendEase - Technical Documentation

## Code Structure and Workflow

### 1. Main Application (`main.py`)
- Serves as the entry point
- Provides menu-driven interface
- Coordinates between different modules
- Functions:
  - `mainMenu()`: Main interface
  - `checkCamera()`: Camera testing
  - `CaptureFaces()`: Image capture
  - `Trainimages()`: Training interface
  - `recognizeFaces()`: Attendance marking

### 2. Camera Testing (`check_camera.py`)
- Verifies camera functionality
- Tests video capture capabilities
- Ensures proper camera setup before main operations

### 3. Image Capture (`capture_image.py`)
- Handles new user registration
- Captures multiple face images
- Features:
  - Face detection using Haar Cascade
  - Multiple angle capture
  - Image validation
  - Student ID assignment

### 4. Training Module (`train_image.py`)
Key components:
```python
def getImagesAndLabels(path):
    # Processes training images
    # Converts images to numpy arrays
    # Returns faces and corresponding IDs
```
```python
def TrainImages():
    # Creates LBPH face recognizer
    # Trains model with processed images
    # Saves trained model as Trainner.yml
```

### 5. Recognition System (`recognize.py`)
- Real-time face recognition
- Attendance marking
- Features:
  - LBPH face recognizer implementation
  - CSV generation for attendance
  - Time-stamped entries
  - Duplicate entry prevention

### Data Flow
1. Image Capture → Training Images folder
2. Training → LBPH model generation
3. Recognition → Attendance CSV creation

### Directory Structure Explanation
- **Attendance/**: CSV files with date-time stamped attendance records
- **StudentDetails/**: Student information database
- **TrainingImage/**: Captured face images for training
- **TrainingImageLabel/**: Contains trained model file (Trainner.yml)

### File Formats
- **Images**: JPG format (faces)
- **Training Data**: YML file
- **Attendance Records**: CSV format
- **Student Records**: CSV format

### Best Practices
1. Capture at least 100 images per person
2. Ensure good lighting during capture
3. Regular model retraining for better accuracy
4. Backup attendance CSVs regularly