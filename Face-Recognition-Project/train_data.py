import os
import pyttsx3
import cv2 as cv
import numpy as np
from tkinter import *
from PIL import Image
from tkinter import messagebox

class Train_data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x100+500+200")
        self.root.title("Face Recognition System")
        self.root.configure(bg="lightpink")

        main_frame = Frame(self.root, borderwidth=4, relief="ridge", bg="lightgray")
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        def speak():
            # Initialize the text-to-speech engine
            engine = pyttsx3.init()

            engine.say("Your data is trained successfully")
            engine.runAndWait()
            engine.stop()

            messagebox.showinfo("Info", "Your data is trained successfully")

            # Close the current window and go back to the previous window
            self.root.destroy()

        def training_data():
            # Check if Faces directory exists
            faces_dir = 'Faces'
            if not os.path.exists(faces_dir):
                messagebox.showerror("Error", "No faces directory found. Please capture faces first.")
                return
                
            # Check if there are any images in the directory
            files = os.listdir(faces_dir)
            if len(files) == 0:
                messagebox.showerror("Error", "No face images found. Please capture faces first.")
                return
            
            path = [os.path.join(faces_dir, file) for file in files if file.endswith('.jpg')]
            
            if len(path) == 0:
                messagebox.showerror("Error", "No valid face images found. Please capture faces first.")
                return

            faces = []
            user_ids = []
            
            # Create a progress window
            progress_window = Toplevel(self.root)
            progress_window.title("Training Progress")
            progress_window.geometry("300x100")
            
            progress_label = Label(progress_window, text=f"Processing image 0/{len(path)}")
            progress_label.pack(pady=10)

            # Process each image
            for i, image in enumerate(path):
                try:
                    img = Image.open(image).convert('L')
                    imageNp = np.array(img, 'uint8')
                    
                    # Extract the user ID from the filename
                    id = int(os.path.split(image)[1].split('.')[1])
                    
                    faces.append(imageNp)
                    user_ids.append(id)
                    
                    # Show training progress
                    progress_label.config(text=f"Processing image {i+1}/{len(path)}")
                    progress_window.update()
                    
                    # Display the current image briefly without waiting for key press
                    cv.imshow("Training", imageNp)
                    cv.waitKey(1)  # Wait just 1ms instead of indefinitely
                except Exception as e:
                    messagebox.showerror("Error", f"Error processing image {image}: {str(e)}")
            
            # Close the progress window
            progress_window.destroy()
            
            if len(faces) == 0:
                messagebox.showerror("Error", "No valid faces could be processed.")
                cv.destroyAllWindows()
                return
                
            # Convert to numpy array for training
            user_ids = np.array(user_ids)
            
            # Train the face recognition model
            try:
                algo = cv.face.LBPHFaceRecognizer_create()
                algo.train(faces, user_ids)
                algo.write("classifier.xml")
                messagebox.showinfo("Success", f"Training completed with {len(faces)} images!")
            except Exception as e:
                messagebox.showerror("Error", f"Training failed: {str(e)}")
            
            cv.destroyAllWindows()

        def combined_task():
            training_data()
            speak()

        button = Button(main_frame, text="Train Data!!!", font=("times new roman", 12, "bold"), cursor="hand2", command=combined_task)

        button.place(x=20, y=17, width=120, height=40)

if __name__ == "__main__":
    root = Tk()
    obj = Train_data(root)
    root.mainloop()
