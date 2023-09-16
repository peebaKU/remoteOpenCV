import redis
import base64
import cv2



cam = cv2.VideoCapture(0)

r = redis.Redis(host="192.168.1.105",port=6379)

while True:
    try:
        ret, frame = cam.read()
        encoded, buf = cv2.imencode('.jpg', frame)
        image = base64.b64encode(buf)
        r.set("image",image)
    except KeyboardInterrupt:
        cam.release()
        cv2.destroyAllWindows()
        break;
