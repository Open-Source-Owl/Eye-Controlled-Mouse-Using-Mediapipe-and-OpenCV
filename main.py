import cv2  # OpenCV library for real-time computer vision
import mediapipe as mp  # Mediapipe library for face landmark detection
import pyautogui  # PyAutoGUI library for controlling the mouse

# Initialize webcam capture
cam = cv2.VideoCapture(0)

# Initialize Mediapipe FaceMesh with refined landmarks (for detailed tracking)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Get the screen resolution to map face coordinates to screen coordinates
screen_w, screen_h = pyautogui.size()

# Infinite loop for continuously processing the webcam feed
while True:
    # Read a frame from the webcam
    _, frame = cam.read()

    # Flip the frame horizontally (creates a mirror-like effect)
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB (as Mediapipe works with RGB images)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with FaceMesh to detect landmarks
    output = face_mesh.process(rgb_frame)

    # Retrieve the list of face landmarks detected in the frame
    landmark_points = output.multi_face_landmarks

    # Get the dimensions of the frame (height, width, and channels)
    frame_h, frame_w, _ = frame.shape

    # Check if any face landmarks are detected
    if landmark_points:
        # Get the landmarks for the first detected face
        landmarks = landmark_points[0].landmark

        # Loop through a subset of landmarks (474 to 478) to focus on the right eye
        for id, landmark in enumerate(landmarks[474:478]):
            # Convert normalized landmark coordinates to pixel coordinates
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)

            # Draw a green circle at each landmark point
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

            # Use the second landmark (id == 1) to control the mouse cursor
            if id == 1:
                # Map the pixel coordinates to screen coordinates
                screen_x = 1.5 * screen_w / frame_w * x
                screen_y = 1.5 * screen_h / frame_h * y

                # Move the mouse cursor to the mapped coordinates
                pyautogui.moveTo(screen_x, screen_y)

        # Detect blinking by analyzing the distance between two eye landmarks
        left = [landmarks[145], landmarks[159]]

        # Draw yellow circles on the landmarks used for blinking detection
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        # Calculate the difference in y-coordinates between the two landmarks
        print(left[0].y - left[1].y)
        if (left[0].y - left[1].y) < 0.004:  # Threshold for blink detection
            print('click')
            pyautogui.click()  # Simulate a mouse click
            pyautogui.sleep(0.1)  # Short delay to prevent rapid clicks

    # Display the current frame with drawn landmarks
    cv2.imshow('eye mouse', frame)

    # Add a delay and check if the user presses a key to exit
    cv2.waitKey(1)
