def camer():
    import cv2  # Import OpenCV library for computer vision tasks

    # Load the Haar Cascade Classifier for face detection
    # This XML file contains the pre-trained model for face detection
    cascade_face = cv2.CascadeClassifier('haarcascade_default.xml')

    # Initialize video capture from the default camera (index 0)
    # VideoCapture(0) means use the first available camera
    cap = cv2.VideoCapture(0)

    while True:  # Continuous loop to capture frames
        # Read a frame from the video capture
        # '_' ignores the return value (success/failure)
        # img contains the actual image frame
        _, img = cap.read()

        # Convert the color image to grayscale
        # Face detection works better on grayscale images
        # Reduces processing overhead as color isn't needed for detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        # Parameters:
        # - gray: input grayscale image
        # - 1.3: scale factor (how much the image size is reduced at each image scale)
        # - 5: minNeighbors (how many neighbors each candidate rectangle should have)
        # - minSize=(30, 30): minimum possible face size
        # - flags=cv2.CASCADE_SCALE_IMAGE: detection algorithm flag
        faces = cascade_face.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), 
                                            flags=cv2.CASCADE_SCALE_IMAGE)

        # Draw rectangles around detected faces
        # faces contains arrays of [x, y, width, height] for each detected face
        for (a, b, c, d) in faces:
            # Parameters:
            # - img: image to draw on
            # - (a,b): top-left corner of rectangle
            # - (a+c, b+d): bottom-right corner
            # - (10,159,255): BGR color values (orange)
            # - 2: thickness of rectangle border
            cv2.rectangle(img, (a, b), (a + c, b + d), (10,159,255), 2)

        # Display the processed image in a window named 'Webcam Check'
        cv2.imshow('Webcam Check', img)

        # Check for key press event
        # cv2.waitKey(1): wait for 1ms between frames
        # & 0xFF: bitwise AND operation to get last 8 bits
        # ord('q'): ASCII value of 'q'
        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up resources
    # Release the camera device
    cap.release()
    # Close all OpenCV windows
    cv2.destroyAllWindows()
