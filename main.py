import cv2
import mediapipe as mp
import pyautogui

webcam = cv2.VideoCapture(0)

my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

x1, y1 = 0, 0
x2, y2 = 0, 0

while True:
    _, image = webcam.read() # boolean, mat

    image = cv2.flip(image, 1)

    frame_height, frame_width,  _ = image.shape

    # convert bgr image to rgb for processing
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)

    hands = output.multi_hand_landmarks

    # take each hand and draw the landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:
                    # pointing our fore finger
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)

                    x1 = x
                    y1 = y

                if id == 4:
                    # pointing our fore finger
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    
                    x2 = x
                    y2 = y

        dist = (((x2 - x1)**2 + (y2 - y1)**2)**0.5) // 4

        # drawing line
        cv2.line(img=image, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=5)

        if dist > 50:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    # shows the video
    cv2.imshow("Hand gesture volume control app", image)

    # how to quit
    esc = cv2.waitKey(10)

    if esc == 27: # esc char is ascii
        break

webcam.release()
cv2.destroyAllWindows()