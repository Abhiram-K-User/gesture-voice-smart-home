# gesture_control.py
import cv2
import mediapipe as mp
import time
from serial_handler import init_serial, send_serial
from voice_control import start_voice_listener

current_mode = "fan"

def handle_voice_command(text):
    """Update mode based on detected keywords."""
    global current_mode
    if "fan" in text:
        current_mode = "fan"
        print("🎐 Switched to FAN mode.")
    elif "light" in text:
        current_mode = "light"
        print("💡 Switched to LIGHT mode.")
    elif "door" in text:
        current_mode = "servo"
        print("🚪 Switched to DOOR mode.")

def start_gesture_control():
    """Main Mediapipe + OpenCV control loop."""
    ser = init_serial()
    start_voice_listener(handle_voice_command)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils
    fingertips_ids = [4, 8, 12, 16, 20]

    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Gesture Control", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Gesture Control", 960, 720)

    last_speed = 0
    finger_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
                lm = hand_landmarks.landmark
                fingers = []

                # Thumb
                if handedness.classification[0].label == "Right":
                    fingers.append(1 if lm[4].x > lm[3].x else 0)
                else:
                    fingers.append(1 if lm[4].x < lm[3].x else 0)

                # Remaining fingers
                for id in range(1, 5):
                    fingers.append(1 if lm[fingertips_ids[id]].y < lm[fingertips_ids[id]-2].y else 0)

                finger_count = sum(fingers)
                last_speed = [0, 80, 120, 160, 200, 255][finger_count]

                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # === SERIAL ===
        if ser:
            if current_mode == "servo":
                val = 180 if finger_count == 1 else 0
                send_serial(ser, "servo", val)
            else:
                send_serial(ser, current_mode, last_speed)
        time.sleep(0.05)

        # === UI Overlay ===
        cv2.rectangle(frame, (10, 620), (350, 710), (0, 0, 0), -1)
        cv2.putText(frame, f'Mode: {current_mode.upper()}', (20, 650),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.putText(frame, f'Fingers: {finger_count}', (20, 685),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Gesture Control", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("👋 Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()
    if ser:
        ser.close()
