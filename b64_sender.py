import redis
import base64
import cv2



camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
camera.set(cv2.CAP_PROP_FPS, 30)

r = redis.Redis(host="192.168.1.105",port=6379)

while True:
    try:
        ret, frame = camera.read()
        encoded, buf = cv2.imencode('.jpg', frame)
        image = base64.b64encode(buf)
        r.set("image",image)
    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break;
