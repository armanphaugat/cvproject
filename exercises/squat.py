from utils.angle import calculate_angle
class Squat:
    def __init__(self):
        self.stage = None
        self.counter = 0

    def analyze(self, landmarks):

        hip = [landmarks[23].x, landmarks[23].y]
        knee = [landmarks[25].x, landmarks[25].y]
        ankle = [landmarks[27].x, landmarks[27].y]

        angle = calculate_angle(hip, knee, ankle)

        feedback = ""

        if angle > 160:
            self.stage = "up"

        if angle < 90 and self.stage == "up":
            self.stage = "down"
            self.counter += 1

        if angle > 120 and angle < 160:
            feedback = "Go Lower"

        return angle, feedback, self.counter