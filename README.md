# Hand Gesture Volume Control App

A real-time hand gesture-based volume control application using **OpenCV**, **MediaPipe**, and **PyAutoGUI**. The app detects hand landmarks from your webcam and controls your system volume based on the distance between your thumb and index finger.

---

## Features

* Real-time hand detection using **MediaPipe**.
* Gesture-based volume control:

  * Increase volume when fingers are far apart.
  * Decrease volume when fingers are close together.
* Visual feedback:

  * Draws hand landmarks.
  * Shows a line connecting the thumb and index finger.
* Simple and lightweight implementation.

---

## Requirements

* Python: 3.x <= 3.12
* Packages:

  * `opencv-python`
  * `mediapipe`
  * `pyautogui`

Install dependencies using:

```bash
pip install opencv-python mediapipe pyautogui
```

---

## How It Works

1. Capture video from your webcam using **OpenCV**.
2. Detect hands and landmarks using **MediaPipe Hands**.
3. Track the index finger tip (ID 8) and thumb tip (ID 4).
4. Calculate the distance between the two fingertips.
5. Map the distance to system volume:

   * Distance > 50 → increase volume
   * Distance ≤ 50 → decrease volume
6. Visualize the landmarks and distance line on the video frame.
7. Exit the program by pressing the `ESC` key.

---

## Usage

1. Clone or download this repository.
2. Run the script:

```bash
python hand_volume_control.py
```

3. Make a hand gesture in front of your webcam.
4. Adjust the volume by moving your thumb and index finger closer or farther apart.
5. Press `ESC` to quit the application.

---

## Notes

* Ensure your webcam is functional and accessible.
* The app works best in a well-lit environment.
* You may need to adjust the distance threshold (`50`) depending on your screen size or webcam placement.
