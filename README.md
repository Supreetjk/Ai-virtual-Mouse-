# Ai-virtual-Mouse
Ai virtual mouse using hand gestures
🖱️ AI Virtual Mouse Using Hand Gestures

📌 Overview

The AI Virtual Mouse Using Hand Gestures is a computer vision-based project that allows users to control mouse functions using hand gestures instead of a physical mouse.
It uses a webcam to track hand movements in real time and performs actions like cursor movement, clicking, scrolling, and more.

This project enhances Human-Computer Interaction (HCI) by providing a touchless, intuitive, and cost-effective solution.

---

🚀 Features

- 🎯 Real-time hand tracking using MediaPipe
- 🖱️ Cursor movement with finger gestures
- 👆 Left click & right click using gestures
- 🔄 Scroll up & down
- 🤏 Drag and drop functionality
- ⚡ Smooth and responsive cursor control
- 💻 Works with standard webcam (no extra hardware required)

---

🛠️ Technologies Used

- Python 3.x
- OpenCV – Image processing
- MediaPipe – Hand tracking & landmark detection
- PyAutoGUI / AutoPy – Mouse control
- NumPy – Numerical operations

---

📂 Project Structure

AI_Virtual_Mouse/
│
├── VirtualMouse.py          # Main program
├── HandTrackingModule.py    # Hand detection module
├── README.md                # Project documentation

---

⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/your-username/AI_Virtual_Mouse.git
cd AI_Virtual_Mouse

---

2️⃣ Create Virtual Environment (Recommended)

python -m venv .venv
.venv\Scripts\activate   # Windows

---

3️⃣ Install Dependencies

pip install opencv-python mediapipe pyautogui autopy numpy

---

4️⃣ Run the Project

python VirtualMouse.py

---

🎮 Gesture Controls

Gesture| Action
☝️ Index finger up| Move cursor
✌️ Index + Middle| Left click
🤟 Index + Pinky| Right click
✋ All fingers up| Scroll up
✊ Closed fist| Scroll down
🤏 Thumb + Index close| Drag

---

⚠️ Requirements

- Python 3.7 – 3.11 (MediaPipe compatibility)
- Webcam (built-in or external)
- Minimum 4GB RAM recommended

---

🧪 Applications

- Assistive technology for physically challenged users
- Touchless systems (hospitals, kiosks)
- Smart classrooms and presentations
- Gaming and AR/VR interaction

---

⚡ Advantages

- No physical mouse required
- Cost-effective solution
- Hygienic (touchless interaction)
- Easy to use and portable

---

❗ Limitations

- Sensitive to lighting conditions
- Requires clear background
- Accuracy depends on camera quality
- Fast hand movement may reduce accuracy

---

🔮 Future Enhancements

- Deep learning-based gesture recognition
- Multi-hand support
- Custom gesture configuration UI
- Integration with AR/VR systems

---

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit pull requests.

---

📜 License

This project is for educational purposes.

---

🙌 Acknowledgement

Developed as part of a Final Year Engineering Project in Computer Science & Engineering.

---