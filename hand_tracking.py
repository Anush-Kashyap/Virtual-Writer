import cv2
import mediapipe as mp

class HandTracker:
    
    def __init__ (self, max_hands=2):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=max_hands)
        self.mp_draw = mp.solutions.drawing_utils
    
    def detect(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        return results
    
    def draw_landmarks(self, frame, results):
        finger_points = [4,8,12,16,20]
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for ac_point in finger_points:
                    index_tip = hand_landmarks.landmark[ac_point]
                    h, w, c = frame.shape
                    cx = int(index_tip.x * w)
                    cy = int(index_tip.y * h)
                    cv2.circle(frame, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

                '''# Print landmark coordinates
                for id, lm in enumerate(hand_landmarks.landmark):
                    print(id, lm.x, lm.y)'''

            # Draw landmarks
            self.mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                self.mp_hands.HAND_CONNECTIONS
            )

        return frame
