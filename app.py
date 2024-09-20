# app.py
import os
from flask import Flask, render_template, Response
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import DepthwiseConv2D

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the Flask app and set the template folder
app = Flask(__name__, template_folder=os.path.join(current_dir, 'templates'))

# Custom DepthwiseConv2D layer
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        groups = kwargs.pop('groups', 1)
        super().__init__(*args, **kwargs)

# Register the custom layer
tf.keras.utils.get_custom_objects()['DepthwiseConv2D'] = CustomDepthwiseConv2D

# Load the Teachable Machine model
model = load_model('keras_model.h5', compile=False)

# Load the labels
with open('labels.txt', 'r') as file:
    class_names = [line.strip() for line in file.readlines()]

def generate_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Preprocess the frame for the model
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (224, 224))
            img_array = np.asarray(img)
            normalized_image_array = (img_array.astype(np.float32) / 127.5) - 1
            data = np.expand_dims(normalized_image_array, axis=0)

            # Make prediction
            prediction = model.predict(data)
            index = np.argmax(prediction)
            class_name = class_names[index]
            confidence_score = prediction[0][index]

            # Add text to the frame
            cv2.putText(frame, f"{class_name}: {confidence_score:.2f}", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
