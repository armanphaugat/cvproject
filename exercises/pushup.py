from utils.angle import calculate_angle
class Pushup:
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
            self.stage = "up"
        if angle < 90 and self.stage == "up":
            self.stage = "down"
            self.counter += 1
        if angle > 120 and angle < 160:
            feedback = "Go Lower"

        return angle, feedback, self.counter