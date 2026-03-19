import cv2
import mediapipe as mp

from utils.pose_detector import PoseDetector
from exercises.squat import Squat
from exercises.pushup import Pushup
from exercises.bicep_curl import BicepCurl

mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

detector = PoseDetector()

squat = Squat()
pushup = Pushup()
curl = BicepCurl()

exercise_mode = "curl"

while cap.isOpened():

    ret, frame = cap.read()

    results = detector.detect(frame)

    if results.pose_landmarks:

        landmarks = results.pose_landmarks.landmark

        if exercise_mode == "squat":
            angle, feedback, counter = squat.analyze(landmarks)

        elif exercise_mode == "pushup":
            angle, feedback, counter = pushup.analyze(landmarks)

        else:
            angle, feedback, counter = curl.analyze(landmarks)

        cv2.putText(frame, f"Exercise: {exercise_mode}",
                    (50,30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,255,255),
                    2)

        cv2.putText(frame, f"Reps: {counter}",
                    (50,70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2)

        cv2.putText(frame, feedback,
                    (50,110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    2)

    detector.draw_landmarks(frame, results)

    cv2.imshow("Gym AI Trainer", frame)

    key = cv2.waitKey(10)

    if key == ord('q'):
        break
    elif key == ord('1'):
        exercise_mode = "squat"
    elif key == ord('2'):
        exercise_mode = "pushup"
    elif key == ord('3'):
        exercise_mode = "curl"

cap.release()
cv2.destroyAllWindows()