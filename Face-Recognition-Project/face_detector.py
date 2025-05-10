import sqlite3
import os
import cv2 as cv
from tkinter import *
from tkinter import messagebox

class Face_detector:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x100+500+200")
        self.root.title("Face Recognition System")
        self.root.configure(bg="lightpink")

        main_frame = Frame(self.root, borderwidth=4, relief="ridge", bg="lightgray")
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

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

        # Count the number of users in the database
        cursor.execute('SELECT COUNT(*) FROM User')
        id_count = cursor.fetchone()[0]
        
        # If no users, set id_count to 0
        if id_count is None:
            id_count = 0

        face_classifier = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            
            faces = face_classifier.detectMultiScale(gray, 1.3, 4)
            
            for (x, y, w, h) in faces:
                face_cropped = img[y:y+h, x:x+w]
                return face_cropped
            
        def capture_images():
            # Create Faces directory if it doesn't exist
            if not os.path.exists('Faces'):
                os.makedirs('Faces')
                
            cap = cv.VideoCapture(0)
            img_id = 0

            while True:
                ret, my_frame = cap.read()
                if not ret:
                    messagebox.showerror("Camera Error", "Could not access the camera")
                    break

                cropped_face = face_cropped(my_frame)
                
                # Only process if a face is detected
                if cropped_face is not None:
                    img_id += 1
                    
                    # We already have the cropped face, no need to call face_cropped again
                    face = cv.resize(cropped_face, (450, 450))
                    face = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
                    
                    file_name_path = f"Faces/user.{id_count}.{img_id}.jpg"
                     
                    cv.imwrite(file_name_path, face)
                    
                    cv.putText(face, str(img_id), (50, 50), cv.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    
                    cv.imshow("Cropped Face", face)
                else:
                    # Display the original frame with a message if no face is detected
                    cv.putText(my_frame, "No face detected", (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                    cv.imshow("Camera Feed", my_frame)

                if cv.waitKey(1) == 13 or int(img_id) == 100:
                    break
            
            cap.release()
            cv.destroyAllWindows()
            messagebox.showinfo("Result", "Images Taken")

        b5 = Button(main_frame, text="Photos!!!", font=("times new roman", 12, "bold"), cursor="hand2", command=capture_images)
        b5.place(x=20, y=17, width=120, height=40)



if __name__ == "__main__":
    root = Tk()
    obj = Face_detector(root)
    root.mainloop()
