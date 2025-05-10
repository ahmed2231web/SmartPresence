<div align="center">

# 🎭 Face Recognition Attendance System 🎭

![Face Recognition Banner](https://img.shields.io/badge/Face%20Recognition-Attendance%20System-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6+-green?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-red?style=for-the-badge&logo=opencv)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?style=for-the-badge&logo=sqlite)

</div>

<p align="center">✨ A modern, user-friendly face recognition system for automated attendance tracking, built with Python and OpenCV ✨</p>

<p align="center">
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="Python" width="40" height="40"/>
<img src="https://opencv.org/wp-content/uploads/2020/07/OpenCV_logo_black-2.png" alt="OpenCV" width="40" height="40"/>
<img src="https://www.sqlite.org/images/sqlite370_banner.gif" alt="SQLite" width="80" height="40"/>
</p>

## ✨ Features ✨

- 🖥️ **User-Friendly GUI**: Simple and intuitive interface built with Tkinter
- 👨‍🎓 **Student Management**: Add and manage student details easily
- 📸 **Face Detection**: Capture and process facial images for recognition
- 🧠 **Training System**: Train the recognition model on captured faces
- ✅ **Automated Attendance**: Mark attendance automatically using facial recognition
- 🗄️ **Local Database**: Store all data securely in a local SQLite database
- 🔊 **Voice Feedback**: Text-to-speech notifications for important actions

## 📋 Requirements 📋

- 🐍 Python 3.6+
- 👁️ OpenCV (with contrib modules)
- 🖼️ Pillow
- 🔢 NumPy
- 💾 SQLite3 (built into Python)
- 🔊 pyttsx3 (for text-to-speech)

## 🚀 Installation 🚀

1. 📥 Clone this repository:
   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. 📦 Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. 🏃‍♂️ Run the application:
   ```bash
   python main.py
   ```

## 📱 Usage Guide 📱

<div align="center">
<table>
<tr>
<td>

### 1️⃣ Student Registration

- 🖱️ Click on "Student Details" button
- 📝 Fill in the student information (Name, ID, Department, etc.)
- 💾 Click "Enter data" to save to the database

</td>
<td>

### 2️⃣ Face Capture

- 🖱️ Click on "Face Detector" button
- 📸 Click "Photos!!!" to start capturing face images
- 🤖 The system will automatically detect and save face images
- ⏱️ Press Enter or wait until 100 images are captured

</td>
</tr>
<tr>
<td>

### 3️⃣ Train the Model

- 🖱️ Click on "Train Data" button
- 🧠 The system will process all captured face images
- 📊 A progress window will show training status
- 💿 The trained model will be saved as "classifier.xml"

</td>
<td>

### 4️⃣ Attendance Marking

- 🖱️ Click on "Attendance" button
- 📹 The system will open your camera and recognize faces
- 👤 Recognized students will have their names and departments displayed
- ⌨️ Press 'q' to exit the attendance mode

</td>
</tr>
</table>
</div>

## 🏗️ Project Structure 🏗️

```
Face-Recognition-Project/
├── main.py                     # Main application entry point
├── student.py                  # Student registration module
├── face_detector.py            # Face detection and image capture
├── train_data.py               # Model training module
├── attandance.py               # Attendance tracking module
├── result.py                   # Database query utilities
├── all.json                    # Configuration data
├── haarcascade_frontalface_default.xml  # Face detection model
├── classifier.xml              # Trained face recognition model
├── database/                   # SQLite database directory
├── Faces/                      # Directory for storing captured face images
└── __pycache__/                # Python bytecode cache
```

**Project Root**
- `requirements.txt` - Project dependencies
- `README.md` - Project documentation
- `.gitignore` - Git ignore file

## 🔧 Technical Details 🔧

<div align="center">

| 🧩 Component | 🛠️ Technology Used |
|-------------|-------------------|
| 👁️ **Face Detection** | Haar Cascade Classifier |
| 🧠 **Face Recognition** | LBPH (Local Binary Patterns Histograms) algorithm |
| 🗄️ **Database** | SQLite3 for lightweight, serverless data storage |
| 🖥️ **GUI Framework** | Tkinter for cross-platform compatibility |
| 🔊 **Voice Feedback** | pyttsx3 text-to-speech engine |

</div>

## 🤝 Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact 📞

If you have any questions or suggestions, please open an issue or contact me at codefiles47@gmail.com.

---

<div align="center">

### 🌟 Star this repository if you find it useful! 🌟

<p align="center">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="Built with Love">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="Made with Python">
</p>

<p align="center">
  Made with ❤️ by Ahmed
</p>

</div>
