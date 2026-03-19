from utils.angle import calculate_angle
class BicepCurl:
    def __init__(self):
        self.counter = 0
        self.stage = None
    def analyze(self, landmarks):
        shoulder = [landmarks[11].x, landmarks[11].y]
        elbow = [landmarks[13].x, landmarks[13].y]
        wrist = [landmarks[15].x, landmarks[15].y]
        angle = calculate_angle(shoulder, elbow, wrist)
        feedback = ""
        if angle > 160:
            self.stage = "down"

        if angle < 40 and self.stage == "down":
            self.stage = "up"
            self.counter += 1

        if angle > 90:
            feedback = "Curl higher"

        return angle, feedback, self.counter