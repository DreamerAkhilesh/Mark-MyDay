import csv
import cv2
import os


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False



def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    print(f"Debug: Id={Id}, name={name}")
    print(f"is_number(Id): {is_number(Id)}, name.isalpha(): {name.isalpha()}")

    if(is_number(Id) and name.isalpha()):
        print("Validation passed, opening camera...")
        cam = cv2.VideoCapture(0)

        if not cam.isOpened():
            print("Error: Could not open camera")
            return

        harcascadePath = "haarcascade_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while(True):
            ret, img = cam.read()
            if not ret:
                print("Failed to grab frame")
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(
                gray, 1.3, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                sampleNum += 1
                # saving the captured face
                cv2.imwrite("TrainingImage" + os.sep + name + "."+ Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                print("Exit requested by user")
                break
            elif sampleNum > 100:
                print("Collected 100 samples, exiting loop")
                break

        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        print(res)
        row = [Id, name]
        with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        if(is_number(Id)):
            print("Enter Alphabetical Name")
        if(name.isalpha()):
            print("Enter Numeric ID")
