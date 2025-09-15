# 🕺 3D GLB Character Animation with Three.js & MediaPipe Pose Recognition

An interactive project that brings a **3D GLB character** to life using **Three.js** for rendering and **MediaPipe Pose** for real-time body tracking.  
Your webcam movements are mapped onto the 3D character, allowing it to mimic human gestures and poses seamlessly.

---

## ✨ Features
- 🎭 **GLB Character Rendering**: Load and display 3D character models in `.glb` format with realistic lighting and animations.
- 🧍 **Pose Recognition**: Track 33 body landmarks in real time using **MediaPipe Pose**.
- 🔗 **Skeleton Mapping**: Map MediaPipe joints to the 3D character’s bones.
- 🎥 **Webcam Integration**: Real-time control of character movements through your webcam.
- ⚡ **Smooth Animation**: Frame-by-frame updates with interpolation for fluid motion.

---

## 🛠️ Tech Stack
- **[Three.js](https://threejs.org/)** → WebGL-based 3D rendering engine.
- **[MediaPipe Pose](https://developers.google.com/mediapipe/solutions/vision/pose)** → Machine learning model for real-time human pose detection.
- **JavaScript (ES6)** → Core project logic.
- **GLTFLoader** (from Three.js) → Load `.glb` character assets.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/rihemar/3D_Character_Animation_Using_MediaPipe
cd cleanProjectTHREE

### 2️⃣ Run the python mediaPipe server
```bash
python websock.py

### 3️⃣ Serve the project 
```bash
npx serve .


### 4️⃣ Open in Browser:
Navigate to 
```browser
http://localhost:3000


## Project structure 
```bash
📦 3d-glb-mediapipe-pose
 ┣ 📂 assets
 ┃ ┗ character.glb        # Your 3D model
 ┣ 📂 src
 ┃ ┣ index.html           # Main entry HTML
 ┃ ┣ main.js              # Three.js + MediaPipe integration
 ┃ ┣ pose-mapping.js      # Maps MediaPipe joints to character bones
 ┃ ┗ style.css            # Basic styling
 ┣ package.json
 ┗ README.md


