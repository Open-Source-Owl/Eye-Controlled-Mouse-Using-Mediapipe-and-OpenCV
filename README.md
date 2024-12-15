# Eye-Controlled Mouse Using Mediapipe and OpenCV

This project demonstrates an eye-controlled mouse system that uses a webcam to track facial landmarks and simulate mouse movements and clicks based on eye position and blinking. It leverages **Mediapipe** for face landmark detection, **OpenCV** for video processing, and **PyAutoGUI** for mouse control.

## Features
- **Eye Tracking**: Tracks eye movements to control the mouse pointer.
- **Blink Detection**: Simulates mouse clicks when a blink is detected.
- **Real-Time Performance**: Processes video frames in real-time for smooth interaction.

## Prerequisites
Before running the project, ensure you have the following:
- Python 3.x installed.
- A working webcam.

### Required Libraries
Install the required Python libraries using pip:

```bash
pip install opencv-python mediapipe pyautogui
```

## How It Works
1. The program captures video frames from your webcam using **OpenCV**.
2. It uses **Mediapipe FaceMesh** to detect facial landmarks, focusing on the eyes.
3. The detected eye coordinates are mapped to your screen's resolution to control the mouse pointer.
4. Blinking is detected based on the vertical distance between specific eye landmarks, and a mouse click is simulated if the distance falls below a threshold.

## How to Run
1. Clone the repository or download the project files.
2. Run the script in your Python environment:
   ```bash
   python eye_controlled_mouse.py
   ```
3. A window will open showing the webcam feed with tracked landmarks. Use your eye movements to move the mouse, and blink to click.

## Code Explanation
### Main Components
- **Face Landmark Detection**: Uses Mediapipe to identify key facial features, focusing on eye landmarks.
- **Mouse Movement**: Maps the coordinates of detected eye landmarks to screen dimensions using PyAutoGUI.
- **Blink Detection**: Calculates the distance between two vertical eye landmarks to detect blinking and simulate clicks.

### Key Sections
1. **Webcam Setup**: Captures live video feed.
2. **FaceMesh Initialization**: Detects and processes facial landmarks.
3. **Mouse Control Logic**: Maps eye landmarks to screen coordinates.
4. **Blink Detection Logic**: Detects blinks to simulate mouse clicks.

## Controls
- **Mouse Movement**: Move your eyes to control the cursor.
- **Mouse Click**: Blink to simulate a left mouse click.

## Known Issues
- Performance may vary depending on lighting conditions and webcam quality.
- Slight delays in detection may occur on lower-end systems.

## Future Enhancements
- Add support for drag-and-drop functionality.
- Enable right-click detection using a specific gesture.

## License
This project is licensed under the MIT License.

---
