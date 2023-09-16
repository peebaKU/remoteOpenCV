import cv2
import os
from flask import Flask, Response
import threading



app = Flask(__name__)

class ThreadCamera:
    def __init__(self,src):
        self.ret = False
        self.frame = None
        self.cap = cv2.VideoCapture(src)
        self.thread = threading.Thread(target=self.mthread_reading)
        self.thread.daemon = True
        self.thread.start()


    def read(self):
        return self.ret, self.frame

    def mthread_reading(self):
        self.ret, self.frame = self.cap.read()

camera = cv2.VideoCapture(2)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.1.101', port=8080)


 
