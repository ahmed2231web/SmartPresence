import sqlite3
import os
import cv2 as cv
from tkinter import *

class Attandance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x100+500+200")
        self.root.title("Face Recognition System")

        # Set the background color of the main window
        self.root.configure(bg="lightblue")

        # Create and place the main frame
        main_frame = Frame(self.root, borderwidth=3, relief="ridge", bg="lightgray")
        
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        def face_recog():
            def attandance(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []

                for (x,y,w,h) in features:
                    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
                    
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    
                    confidence = int((100*(1-predict/300)))


                    # Database
                    # Create database directory if it doesn't exist
                    db_dir = os.path.dirname(os.path.abspath(__file__)) + '/database'
                    if not os.path.exists(db_dir):
                        os.makedirs(db_dir)
                    
                    # Connect to SQLite database
                    conn = sqlite3.connect(db_dir + '/face_recognition.db')
                    cursor = conn.cursor()
                    
                    # Ensure the User table exists
                    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS User (
                        id TEXT PRIMARY KEY,
                        Name TEXT,
                        Department TEXT,
                        Teacher TEXT,
                        Email TEXT,
                        Phone TEXT
                    )
                    ''')
                    conn.commit()

                    id = str(id)

                    # Query the database
                    cursor.execute('SELECT Name, Department FROM User WHERE id = ?', (id,))
                    result = cursor.fetchone()

                    # Initialize with default values
                    name = "Unknown"
                    department = "Unknown"

                    if result:
                        name, department = result
                        # Print prediction details to terminal
                        confidence_percentage = int(100 * (1 - predict/300))
                        print(f"\n===== Face Recognition Prediction =====")
                        print(f"Detected User ID: {id}")
                        print(f"Name: {name}")
                        print(f"Department: {department}")
                        print(f"Confidence: {confidence_percentage}%")
                        print(f"{'✅ HIGH CONFIDENCE' if confidence_percentage > 80 else '⚠️ LOW CONFIDENCE'}")
                        print("======================================\n")
                    else:
                        print(f"\n⚠️ User ID {id} not found in database")
                        
                    # Close the database connection
                    conn.close()
                        
                    if confidence>75:
                        # Display ID on top
                        cv.putText(img, f"ID: {id}", (x,y-80), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,0), 3)
                        
                        # Display name
                        cv.putText(img, f"Name: {name}", (x,y-55), cv.FONT_HERSHEY_COMPLEX, 0.8, (0,255,255), 3)
                        
                        # Display department
                        cv.putText(img, f"Department: {department}", (x,y-30), cv.FONT_HERSHEY_COMPLEX, 0.8, (0,255,255), 3)
                        
                        # Display confidence
                        confidence_percentage = int(100 * (1 - predict/300))
                        cv.putText(img, f"Confidence: {confidence_percentage}%", (x,y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
                    
                    else:
                        cv.rectangle(img,(x,y), (x+w, y+h), (0,0,255), 3)
                        
                        cv.putText(img, "Unknown Face", (x,y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    
                    coord = [x,y,w,y]
                
                return coord
            
            def recognize(img,clf,faceCascade):
                coord = attandance(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)

                return img

            faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

            clf = cv.face.LBPHFaceRecognizer_create()

            clf.read("classifier.xml")

            video_cap = cv.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                
                img = recognize(img, clf, faceCascade)
                
                cv.imshow("Welcome to Face Recognizer", img)

                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            
            video_cap.release()
            cv.destroyAllWindows()


        button = Button(main_frame, text="Attandance", font=("times new roman", 20, "bold"), cursor="hand2",bg=None , fg='gray', command=face_recog)

        button.place(x=10, y=17, width=150, height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Attandance(root)
    root.mainloop()