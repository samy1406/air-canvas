import cv2
import mediapipe as mp

# --- MediaPipe setup ---
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# --- Webcam setup ---
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip so it acts like a mirror
    frame = cv2.flip(frame, 1)

    # MediaPipe needs RGB, OpenCV gives BGR
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    # If hand detected, draw landmarks
    if result.multi_hand_landmarks:
        # Inside the `if result.multi_hand_landmarks:` block
# AFTER the draw_landmarks line, add this:

        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get frame dimensions
            h, w, _ = frame.shape

            # Landmark 8 = index fingertip
            index_tip = hand_landmarks.landmark[8]

            # Convert normalized (0-1) coords to pixel coords
            cx = int(index_tip.x * w)
            cy = int(index_tip.y * h)

            # Draw a red dot on the fingertip
            cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)

            # Print to terminal
            print(f"Index tip: ({cx}, {cy})")

    cv2.imshow("Air Canvas - Step 1", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()