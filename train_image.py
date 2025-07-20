# Import required libraries
import os       # For file and directory operations
import time     # For time-related functions
import cv2      # OpenCV for computer vision
import numpy as np  # For numerical operations
from PIL import Image  # For image processing
from threading import Thread  # For concurrent operations


def getImagesAndLabels(path):
    """
    Processes training images and extracts faces with corresponding IDs
    Args:
        path: Directory path containing training images
    Returns:
        tuple: (faces array, IDs array)
    """
    # Get paths of all files in the specified folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []  # List to store face images
    Ids = []    # List to store corresponding IDs
    
    # Process each image file
    for imagePath in imagePaths:
        try:
            # Open image and convert to grayscale
            pilImage = Image.open(imagePath).convert('L')
            # Convert PIL image to numpy array
            imageNp = np.array(pilImage, 'uint8')
            # Extract ID from filename (format: name.ID.samplenumber.jpg)
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # Add face image and ID to respective lists
            faces.append(imageNp)
            Ids.append(Id)
        except Exception as e:
            # Handle any errors during image processing
            print(f"Skipping file {imagePath}: {e}")
            continue
    return faces, Ids


def TrainImages():
    """
    Trains the face recognition model using collected images
    - Creates LBPH face recognizer
    - Loads and processes training images
    - Trains the model
    - Saves the trained model
    """
    # Initialize LBPH Face Recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Path to Haar cascade classifier
    harcascadePath = "haarcascade_default.xml"
    # Initialize face detector
    detector = cv2.CascadeClassifier(harcascadePath)
    
    # Get processed faces and their IDs
    faces, Id = getImagesAndLabels("TrainingImage")
    
    # Start training in a separate thread
    Thread(target = recognizer.train(faces, np.array(Id))).start()
    # Start progress counter in a separate thread
    Thread(target = counter_img("TrainingImage")).start()
    
    # Save the trained model
    recognizer.save("TrainingImageLabel"+os.sep+"Trainner.yml")
    print("All Images")


def counter_img(path):
    """
    Displays training progress
    Args:
        path: Directory path containing training images
    Provides visual feedback during training process
    """
    # Initialize counter
    imgcounter = 1
    # Get all image paths
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    
    # Display progress for each image
    for imagePath in imagePaths:
        # Print counter with carriage return for dynamic update
        print(str(imgcounter) + " Images Trained", end="\r")
        # Small delay for visible progress
        time.sleep(0.008)
        # Increment counter
        imgcounter += 1