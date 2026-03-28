# 🚗 Driver Drowsiness Detection System

A real-time AI-based system that detects driver drowsiness using Computer Vision and alerts the driver with a voice warning.

---

## 🔥 Features

* 👁️ Real-time face and eye detection
* 🧠 Eye Aspect Ratio (EAR) based drowsiness detection
* 🔊 Voice alert system when drowsiness is detected
* 🟢 Live status display (Awake / Drowsy)
* 🎯 Smooth and responsive UI dashboard

---

## 🖥️ Demo

![Demo](assets/demo.png)

---

## ⚙️ How It Works

1. Webcam captures live video feed
2. Face landmarks are detected using MediaPipe
3. Eye landmarks are extracted
4. EAR (Eye Aspect Ratio) is calculated
5. If EAR drops below threshold → Driver is drowsy
6. Voice alert is triggered

---

## 🛠️ Tech Stack

* Python 🐍
* OpenCV
* MediaPipe
* NumPy

---

## 📂 Project Structure

```
driver-drowsiness-detection/
│
├── Detection/
│   ├── face_detector.py
│   ├── eye_detector.py
│   └── haarcascade_frontalface_default.xml
│
├── models/
│   └── face_landmarker.task
│
├── main.py
├── voice.wav
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/driver-drowsiness-detection.git
cd driver-drowsiness-detection
```

### 2️⃣ Install dependencies

```bash
pip install opencv-python mediapipe numpy
```

### 3️⃣ Run the project

```bash
python main.py
```

---

## 📌 Future Improvements

* 📊 Fatigue level indicator
* 📱 Mobile app integration
* 🚗 Integration with car systems
* 🤖 Advanced AI models

---

## 🙌 Acknowledgements

* MediaPipe for face landmark detection
* OpenCV for computer vision

---

## 👨‍💻 Author

**Parth (Parth-Coder5)**
🚀 Passionate about AI, ML & building real-world projects

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
