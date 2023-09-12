import cv2

rtmp_url = "IPSENDER:8080/video"

cap = cv2.VideoCapture(rtmp_url)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Remote Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()