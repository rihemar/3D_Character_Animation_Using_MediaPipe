# 🕺 3D GLB Character Animation with Three.js & MediaPipe Pose Recognition

An interactive project that brings a **3D GLB character** to life using **Three.js** for rendering and **MediaPipe Pose** for real-time body tracking.
Your webcam movements are mapped onto the 3D character, allowing it to mimic human gestures and poses seamlessly.

---

## ✨ Features

* 🎭 **GLB Character Rendering**: Load and display 3D character models in `.glb` format with realistic lighting and animations.
* 🧍 **Pose Recognition**: Track 33 body landmarks in real time using **MediaPipe Pose**.
* 🔗 **Skeleton Mapping**: Map MediaPipe joints to the 3D character’s bones.
* 🎥 **Webcam Integration**: Real-time control of character movements through your webcam.
* ⚡ **Smooth Animation**: Frame-by-frame updates with interpolation for fluid motion.

---

## 🛠️ Tech Stack

* **[Three.js](https://threejs.org/)** → WebGL-based 3D rendering engine.
* **[MediaPipe Pose](https://developers.google.com/mediapipe/solutions/vision/pose)** → Machine learning model for real-time human pose detection.
* **JavaScript (ES6)** → Core project logic.
* **GLTFLoader** (from Three.js) → Load `.glb` character assets.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/rihemar/3D_Character_Animation_Using_MediaPipe
cd .\3D_Character_Animation_Using_MediaPipe\
```

### 2️⃣ Run the Python MediaPipe server

```bash
python websock.py
```

### 3️⃣ Serve the project

```bash
npx serve .
```

### 4️⃣ Open in Browser

Navigate to:

```
http://localhost:3000
```

---


## 📌 Notes

* Ensure you allow **camera permissions** in your browser.
* A **GLB model with a humanoid skeleton** (rigged) works best.
* Performance may vary depending on your device and browser.

---

## 📜 License

This project is licensed under the **MIT License**.
