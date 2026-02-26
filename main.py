import cv2
from hand_tracking import HandTracker

cap = cv2.VideoCapture(0)

tracker = HandTracker()
while True:
    success, frame = cap.read()
    results = tracker.detect(frame)
    frame = tracker.draw_landmarks(frame, results)

    cv2.imshow("Virtual Writer - Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

