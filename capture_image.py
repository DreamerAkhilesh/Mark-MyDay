# Import required libraries
import csv      # For handling CSV file operations
import cv2      # OpenCV for computer vision tasks
import os      # For file and directory operations

def is_number(s):
    """
    Validates if a string is a valid number
    Handles both float and unicode numeric values
    Args:
        s: String to validate
    Returns:
        bool: True if string is a valid number, False otherwise
    """
    try:
        # Try converting to float
        float(s)
        return True
    except ValueError:
        pass
    try:
        # Try converting unicode characters (like ½)
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def takeImages():
    """
    Captures and saves facial images for training
    - Gets user ID and name
    - Validates input
    - Captures multiple face images
    - Saves images and user details
    """
    # Get user input for identification
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    # Debug information for input validation
    print(f"Debug: Id={Id}, name={name}")
    print(f"is_number(Id): {is_number(Id)}, name.isalpha(): {name.isalpha()}")

    # Validate inputs: ID must be numeric, name must be alphabetic
    if(is_number(Id) and name.isalpha()):
        print("Validation passed, opening camera...")
        # Initialize video capture from default camera
        cam = cv2.VideoCapture(0)

        # Check if camera opened successfully
        if not cam.isOpened():
            print("Error: Could not open camera")
            return

        # Load Haar Cascade Classifier for face detection
        harcascadePath = "haarcascade_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        
        # Counter for number of samples
        sampleNum = 0

        # Main capture loop
        while(True):
            # Read frame from camera
            ret, img = cam.read()
            if not ret:
                print("Failed to grab frame")
                break

            # Convert to grayscale for face detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces in the frame
            # Parameters:
            # - gray: grayscale image
            # - 1.3: scale factor
            # - 5: minimum neighbors
            # - minSize: minimum face size
            faces = detector.detectMultiScale(
                gray, 1.3, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

            # Process each detected face
            for(x,y,w,h) in faces:
                # Draw rectangle around face
                # Parameters: image, start point, end point, color (BGR), thickness
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                
                # Increment sample counter
                sampleNum += 1
                
                # Save the captured face
                # Format: name.ID.samplenumber.jpg
                cv2.imwrite("TrainingImage" + os.sep + name + "."+ Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                
                # Display the frame
                cv2.imshow('frame', img)

            # Check for exit conditions
            # 'q' key press or 100 samples collected
            if cv2.waitKey(100) & 0xFF == ord('q'):
                print("Exit requested by user")
                break
            elif sampleNum > 100:
                print("Collected 100 samples, exiting loop")
                break

        # Clean up resources
        cam.release()
        cv2.destroyAllWindows()
        
        # Save user details to CSV file
        res = "Images Saved for ID : " + Id + " Name : " + name
        print(res)
        row = [Id, name]
        
        # Append user details to StudentDetails.csv
        with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        # Input validation error messages
        if(is_number(Id)):
            print("Enter Alphabetical Name")
        if(name.isalpha()):
            print("Enter Numeric ID")
