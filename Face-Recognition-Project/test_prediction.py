import os
import cv2 as cv
import numpy as np
import sqlite3
from PIL import Image

def test_model_prediction():
    print("\n===== Face Recognition Model Prediction Test =====\n")
    
    # Check if classifier exists
    if not os.path.exists("classifier.xml"):
        print("Error: classifier.xml not found. Please train the model first.")
        return
    
    # Check if Faces directory exists
    if not os.path.exists("Faces"):
        print("Error: Faces directory not found. Please capture faces first.")
        return
    
    # Get list of face images
    face_files = [f for f in os.listdir("Faces") if f.endswith('.jpg')]
    if not face_files:
        print("Error: No face images found in Faces directory.")
        return
    
    # Load the face classifier
    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.read("classifier.xml")
    
    # Connect to the database
    db_dir = os.path.dirname(os.path.abspath(__file__)) + '/database'
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    conn = sqlite3.connect(db_dir + '/face_recognition.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
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
    
    # Test prediction on a few sample images
    print("Testing prediction on sample images from Faces directory:\n")
    
    # Take up to 5 sample images for testing
    sample_files = face_files[:5]
    
    for i, file in enumerate(sample_files):
        print(f"Image {i+1}: {file}")
        
        # Extract user ID from filename
        try:
            user_id = file.split('.')[1]
        except:
            print(f"  - Could not extract user ID from filename: {file}")
            continue
        
        # Get user details from database
        cursor.execute('SELECT Name, Department FROM User WHERE id = ?', (user_id,))
        user_data = cursor.fetchone()
        
        if user_data:
            name, department = user_data
            print(f"  - Database record: Name={name}, Department={department}")
        else:
            print(f"  - No database record found for user ID: {user_id}")
        
        # Load and process the image
        try:
            img_path = os.path.join("Faces", file)
            test_img = cv.imread(img_path)
            
            if test_img is None:
                print(f"  - Could not load image: {img_path}")
                continue
                
            gray_img = cv.cvtColor(test_img, cv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
            
            if len(faces) == 0:
                print("  - No face detected in the image")
                continue
                
            for (x, y, w, h) in faces:
                face_crop = gray_img[y:y+h, x:x+w]
                id_pred, confidence = recognizer.predict(face_crop)
                
                confidence_percentage = 100 - int(confidence)
                print(f"  - Prediction: User ID={id_pred}, Confidence={confidence_percentage}%")
                
                # Get predicted user details
                cursor.execute('SELECT Name, Department FROM User WHERE id = ?', (str(id_pred),))
                pred_user = cursor.fetchone()
                
                if pred_user:
                    pred_name, pred_dept = pred_user
                    print(f"  - Predicted person: Name={pred_name}, Department={pred_dept}")
                    
                    # Check if prediction matches actual user
                    if str(id_pred) == user_id:
                        print("  - ✅ CORRECT PREDICTION")
                    else:
                        print("  - ❌ INCORRECT PREDICTION")
                else:
                    print(f"  - No database record found for predicted ID: {id_pred}")
        except Exception as e:
            print(f"  - Error processing image: {str(e)}")
        
        print("")  # Empty line between images
    
    # Close the database connection
    conn.close()
    
    print("===== Test Complete =====")

if __name__ == "__main__":
    test_model_prediction()
