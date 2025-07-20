import os  # For operating system operations (clear screen, etc.)
import check_camera    # Module for camera testing
import capture_image   # Module for capturing face images
import train_image     # Module for training the face recognition model
import recognize       # Module for face recognition and attendance


def title_bar():
    """
    Clears the console and displays the application title
    Uses cls command for Windows systems
    """
    os.system('cls')  # Clear console screen
    print("\t***** Face Recognition Attendance System *****")


def mainMenu():
    """
    Displays and handles the main menu of the application
    Features:
    - Camera testing
    - Face capture
    - Model training
    - Attendance recognition
    - Exit option
    Includes input validation and error handling
    """
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    # Display menu options
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Quit")

    # Input handling loop
    while True:
        try:
            # Get user choice with validation
            choice = int(input("Enter Choice: "))
            if choice == 1:
                checkCamera()     # Test camera functionality
                break
            elif choice == 2:
                CaptureFaces()   # Capture new face images
                break
            elif choice == 3:
                Trainimages()    # Train the model
                break
            elif choice == 4:
                recognizeFaces() # Start recognition
                break
            elif choice == 5:
                print("Thank You")
                break
            else:
                # Handle invalid numeric input
                print("Invalid Choice. Enter 1-5")
                mainMenu()
        except ValueError:
            # Handle non-numeric input
            print("Invalid Choice. Enter 1-5\n Try Again")
    exit


def checkCamera():
    """
    Initiates camera test functionality
    - Calls camera test function from check_camera module
    - Returns to main menu after completion
    """
    check_camera.camer()
    key = input("Enter any key to return main menu ")
    mainMenu()


def CaptureFaces():
    """
    Initiates face capture process
    - Calls image capture function from capture_image module
    - Returns to main menu after completion
    """
    capture_image.takeImages()
    key = input("Enter any key to return main menu")
    mainMenu()


def Trainimages():
    """
    Initiates model training process
    - Calls training function from train_image module
    - Returns to main menu after completion
    """
    train_image.TrainImages()
    key = input("Enter any key to return main menu")
    mainMenu()


def recognizeFaces():
    """
    Initiates face recognition and attendance marking
    - Calls recognition function from recognize module
    - Returns to main menu after completion
    """
    recognize.recognize_attendence()
    key = input("Enter any key to return main menu")
    mainMenu()


# Application entry point
# Starts the main menu when the script is run
mainMenu()

