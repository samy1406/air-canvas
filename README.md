# 🎨 Air Canvas: Real-Time Gesture-Based Drawing

Air Canvas is a Computer Vision-based application that allows users to draw digitally by moving their fingers in the air. By leveraging **OpenCV** and **MediaPipe**, the system tracks hand landmarks in real-time and maps coordinates to a virtual canvas, providing a seamless and touchless drawing experience.

This project is part of my **Edge AI Portfolio**, focusing on real-time computer vision, low-latency interaction, and intelligent edge processing.

---

## 🚀 Features

* **Real-Time Tracking:** High-speed hand landmark detection using Google's MediaPipe framework.
* **Dynamic Drawing:** Draw on the screen using your index finger as a virtual pen.
* **Color Palette:** Switch between different colors (Blue, Green, Red, Yellow) using on-screen interactive buttons.
* **Clear Canvas:** Reset the drawing area by hovering over the "Clear" button.
* **Edge-Ready:** Optimized for high-FPS performance on standard webcams without requiring heavy GPU compute.

## 🛠️ Technologies Used

* **Python 3.x:** Core programming language.
* **OpenCV (`cv2`):** Used for capturing webcam feeds, image processing, frame manipulation, and rendering the UI/canvas.
* **MediaPipe:** Powers the robust, ML-based hand tracking model capable of identifying 21 3D hand landmarks.
* **NumPy:** Handles efficient array manipulations and coordinate mapping for the drawing logic.

---

## 📋 Prerequisites & Installation

Ensure you have Python installed on your system. 

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/samy1406/air-canvas.git](https://github.com/samy1406/air-canvas.git)
   cd air-canvas
2. **Install the required dependencies:**
   ```bash
   pip install -r requirement.txt
3. **Run the application:**
   ```bash
   python main.py
  
## 💻 How to Use
1. **Start Drawing: Raise your hand in front of the webcam. Point your Index Finger Up to start drawing on the canvas.**

2. **Change Colors: Hover your index finger over the colored rectangular buttons at the top of the video feed to switch your brush color.**

3. **Clear Screen: Hover your index finger over the "Clear" button at the top left to wipe the canvas clean.**

## 🧠 Technical Workflow
1. **Frame Capture: Reads frames continuously from the webcam and flips them horizontally to create an intuitive "mirror" effect for the user.**

2. **Preprocessing: Converts the default BGR frames from OpenCV into RGB format, which is required by the MediaPipe pipeline.**

3. **Hand Landmark Detection: Processes the RGB frame to locate 21 hand landmarks. The application specifically isolates Landmark 8 (the tip of the index finger) to determine drawing coordinates.**

4. **Drawing Logic: Coordinates of the index finger tip are stored in collections.deque (queues) categorized by color. These coordinates are then iterated over to render lines on both the live camera feed and a separate blank white canvas.**

5. **UI Interaction: The system checks if the index finger coordinates intersect with the predefined bounding boxes of the UI elements (Color/Clear buttons) to trigger state changes.

## 📝 Learning & Challenges
1. Building this project involved overcoming several technical hurdles related to real-time processing and coordinate geometry.
2. For a deeper dive into the technical concepts learned and the challenges faced during development, check out the LEARNING.md file.

## 🤝 Contributing
Contributions are always welcome! If you have ideas for adding new features (like gesture-based thickness control, an eraser tool, or integrating a CNN for character recognition), feel free to fork the repository and submit a Pull Request.

Developed by Samy — AI & ML Engineer
