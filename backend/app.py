from flask import Flask, render_template, Response
from flask_cors import CORS  # Import CORS
import cv2
import numpy as np
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def create_background(cap, num_frames=30):
    print("Capturing background. Please move out of frame.")
    backgrounds = []
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret:
            backgrounds.append(frame)
        else:
            print(f"Warning: Could not read frame {i+1}/{num_frames}")
        time.sleep(0.1)
    if backgrounds:
        return np.median(backgrounds, axis=0).astype(np.uint8)
    else:
        raise ValueError("Could not capture any frames for background")

def create_mask(frame, lower_color, upper_color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
    return mask

def apply_cloak_effect(frame, mask, background):
    mask_inv = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg = cv2.bitwise_and(background, background, mask=mask)
    return cv2.add(fg, bg)

def gen_frames():
    cap = cv2.VideoCapture(0)  # Open the camera

    if not cap.isOpened():
        raise Exception("Could not open video capture")

    background = create_background(cap)  # Capture the background

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")  # Log if the frame capture fails
            break

        mask = create_mask(frame, lower_blue, upper_blue)  # Create mask
        result = apply_cloak_effect(frame, mask, background)  # Apply effect

        ret, buffer = cv2.imencode('.jpg', result)  # Encode frame
        frame = buffer.tobytes()  # Convert to bytes

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Yield frame

    cap.release()


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

# Route to start the cloak effect (connects with React button)
@app.route('/start_cloak', methods=['POST'])
def start_cloak():
    return {"status": "cloak started"}

if __name__ == '__main__':
    app.run(debug=True)
