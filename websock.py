from flask import Flask, jsonify
import threading
import cv2
import mediapipe as mp
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)


mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

latest_keypoints = []

def capture_pose():
    global latest_keypoints
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            lm = results.pose_landmarks.landmark
            latest_keypoints = {'LeftShoulder': calculate_angle(lm[12], lm[11], lm[13]),
                                'RightShoulder': calculate_angle(lm[11], lm[12], lm[14]),
                                'LeftElbow': calculate_angle(lm[11], lm[13], lm[15]),
                                'RightElbow': calculate_angle(lm[12], lm[14], lm[16]),
                                'LeftKnee': calculate_angle(lm[23], lm[25], lm[27]),
                                'RightKnee': calculate_angle(lm[24], lm[26], lm[28]),
                                'LeftHip': calculate_angle(lm[24], lm[23], lm[25]),
                                'RightHip': calculate_angle(lm[23], lm[24], lm[26]),
                                }
        else:
            latest_keypoints = []

        # Show the webcam with landmarks for debugging
        mp.solutions.drawing_utils.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow('Pose Capture', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def calculate_angle(a, b, c):
    """
    Calculates the directed angle (in degrees) between points a, b, c at point b.
    Result is in range [-180, 180], positive counter-clockwise.
    """
    a = [a.x, a.y]
    b = [b.x, b.y]
    c = [c.x, c.y]
    
    ab = [a[0] - b[0], a[1] - b[1]]
    cb = [c[0] - b[0], c[1] - b[1]]
    
    angle_ab = math.atan2(ab[1], ab[0])
    angle_cb = math.atan2(cb[1], cb[0])
    
    angle_rad = angle_cb - angle_ab
    angle_deg = math.degrees(angle_rad)
    
    # Normalize angle to [-180, 180]
    while angle_deg > 180:
        angle_deg -= 360
    while angle_deg < -180:
        angle_deg += 360

    return angle_deg



@app.route('/pose')
def get_pose():
    return jsonify(latest_keypoints)

if __name__ == '__main__':
    # Start the camera capture loop in a separate thread
    thread = threading.Thread(target=capture_pose, daemon=True)
    thread.start()

    # Run Flask server
    app.run(host='0.0.0.0', port=5000)



# 0 - nose
# 1 - left eye (inner)
# 2 - left eye
# 3 - left eye (outer)
# 4 - right eye (inner)
# 5 - right eye
# 6 - right eye (outer)
# 7 - left ear
# 8 - right ear
# 9 - mouth (left)
# 10 - mouth (right)
# 11 - left shoulder
# 12 - right shoulder
# 13 - left elbow
# 14 - right elbow
# 15 - left wrist
# 16 - right wrist
# 17 - left pinky
# 18 - right pinky
# 19 - left index
# 20 - right index
# 21 - left thumb
# 22 - right thumb
# 23 - left hip
# 24 - right hip
# 25 - left knee
# 26 - right knee
# 27 - left ankle
# 28 - right ankle
# 29 - left heel
# 30 - right heel
# 31 - left foot index
# 32 - right foot index