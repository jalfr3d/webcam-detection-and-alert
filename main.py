import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None

while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    cv2.imshow("My video", gray_frame_gau)
    if first_frame is None:
        first_frame = gray_frame_gau
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()

