# Import required libraries
import datetime  # For handling date and time operations
import os       # For file and directory operations
import time     # For timestamp operations
import cv2      # OpenCV for computer vision tasks
import pandas as pd  # For handling CSV data and DataFrame operations

def recognize_attendence():
    # Initialize the LBPH Face Recognizer
    # Local Binary Patterns Histograms (LBPH) is effective for face recognition
    recognizer = cv2.face.LBPHFaceRecognizer_create()  
    
    # Load the trained model
    # The model contains the trained facial patterns of registered students
    recognizer.read("TrainingImageLabel"+os.sep+"Trainner.yml")
    
    # Load Haar Cascade Classifier for face detection
    harcascadePath = "haarcascade_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    
    # Read student details from CSV file into pandas DataFrame
    # Contains mapping of student IDs to their names
    df = pd.read_csv("StudentDetails"+os.sep+"StudentDetails.csv")
    
    # Set font style for OpenCV text
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Initialize attendance DataFrame with columns
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)

    # Initialize video capture
    # CAP_DSHOW is DirectShow (Windows) video input
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    # Set video resolution
    cam.set(3, 640)  # Width
    cam.set(4, 480)  # Height
    
    # Calculate minimum face size based on video dimensions
    # 10% of frame width and height
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        # Read frame from video stream
        ret, im = cam.read()
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        # Parameters: image, scale factor, min neighbors, min size, flags
        faces = faceCascade.detectMultiScale(gray, 1.2, 5,
                minSize = (int(minW), int(minH)),
                flags = cv2.CASCADE_SCALE_IMAGE)

        # Process each detected face
        for(x, y, w, h) in faces:
            # Draw rectangle around face
            # Parameters: image, top-left point, bottom-right point, color (BGR), thickness
            cv2.rectangle(im, (x, y), (x+w, y+h), (10, 159, 255), 2)
            
            # Predict the ID of the face
            # conf is the confidence level (lower is better)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

            # Handle recognition results
            if conf < 100:
                # Get name corresponding to the ID
                aa = df.loc[df['Id'] == Id]['Name'].values
                confstr = "  {0}%".format(round(100 - conf))
                tt = str(Id)+"-"+aa
            else:
                # If confidence is low, mark as unknown
                Id = '  Unknown  '
                tt = str(Id)
                confstr = "  {0}%".format(round(100 - conf))

            # Record attendance if confidence is high enough (>67%)
            if (100-conf) > 67:
                # Get current timestamp
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = str(aa)[2:-2]  # Clean up name string
                # Add new attendance record
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            # Display name and confidence
            tt = str(tt)[2:-2]
            if(100-conf) > 67:
                tt = tt + " [Pass]"
                cv2.putText(im, str(tt), (x+5,y-5), font, 1, (255, 255, 255), 2)
            else:
                cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

            # Display confidence with color coding
            # Green: High confidence (>67%)
            # Yellow: Medium confidence (>50%)
            # Red: Low confidence
            if (100-conf) > 67:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font,1, (0, 255, 0),1 )
            elif (100-conf) > 50:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1)
            else:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1)

        # Remove duplicate entries keeping first occurrence
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        
        # Display the processed frame
        cv2.imshow('Attendance', im)
        
        # Break loop if 'q' is pressed
        if (cv2.waitKey(1) == ord('q')):
            break

    # Generate unique filename with timestamp
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance"+os.sep+"Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    
    # Save attendance records to CSV file
    attendance.to_csv(fileName, index=False)
    print("Attendance Successful")
    
    # Release resources
    cam.release()
    cv2.destroyAllWindows()