import cv2
import mediapipe as mp
import numpy as np

# --- MediaPipe setup ---
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def is_index_up(hand_landmarks):
    tip = hand_landmarks.landmark[8]
    pip = hand_landmarks.landmark[6]
    return tip.y < pip.y

def is_peace_sign(hand_landmarks):
    # Index and middle up, ring and pinky down
    index_up = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
    middle_up = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
    ring_down = hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y
    pinky_down = hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y
    return index_up and middle_up and ring_down and pinky_down

# --- Webcam setup ---
cap = cv2.VideoCapture(0)

# Canvas layer — same size as frame, starts black
canvas = None
prev_x, prev_y = 0, 0
draw_color = (0, 255, 0)  # green
brush_size = 5

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Initialize canvas once we know frame size
    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_tip = hand_landmarks.landmark[8]
            cx = int(index_tip.x * w)
            cy = int(index_tip.y * h)

            cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)

            finger_up = is_index_up(hand_landmarks)
            peace = is_peace_sign(hand_landmarks)

            if peace:
                # Erase mode — draw black on canvas
                middle_tip = hand_landmarks.landmark[12]
                ex = int(middle_tip.x * w)
                ey = int(middle_tip.y * h)
                cv2.circle(canvas, (cx, cy), 20, (0, 0, 0), -1)
                status = "ERASING"
                color = (0, 165, 255)  # orange
                prev_x, prev_y = 0, 0
            elif finger_up:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = cx, cy
                cv2.line(canvas, (prev_x, prev_y), (cx, cy), draw_color, brush_size)
                prev_x, prev_y = cx, cy
                status = "DRAWING"
                color = (0, 255, 0)
            else:
                prev_x, prev_y = 0, 0
                status = "PAUSED"
                color = (0, 0, 255)

            cv2.putText(frame, status, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    # Blend canvas on top of webcam frame
    # Wherever canvas is non-black, show the drawing
    mask = canvas.astype(bool)
    frame[mask] = canvas[mask]

    cv2.imshow("Air Canvas", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros((h, w, 3), dtype=np.uint8)  # clear entire canvas

cap.release()
cv2.destroyAllWindows()