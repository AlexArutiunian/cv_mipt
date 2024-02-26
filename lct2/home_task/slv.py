import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy

cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.resizeWindow("mask", 600, 900)

cv2.createTrackbar("hb", "mask", 255, 255, lambda i: 1)
cv2.createTrackbar("lb", "mask", 0, 255, lambda i: 1)
cv2.createTrackbar("hg", "mask", 255, 255, lambda i: 1)
cv2.createTrackbar("lg", "mask", 0, 255, lambda i: 1)
cv2.createTrackbar("hr", "mask", 255, 255, lambda i: 1)
cv2.createTrackbar("lr", "mask", 0, 255, lambda i: 1)
cv2.createTrackbar("ha", "mask", 20000, 30000, lambda i: 1)
cv2.createTrackbar("la", "mask", 0, 30000, lambda i: 1)

cap = cv2.VideoCapture('black_objects.mp4')  # Укажите путь к вашему видеофайлу
print(cap)
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't read video")
        break

    img = copy.deepcopy(frame)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hb = cv2.getTrackbarPos("hb", "mask")
    lb = cv2.getTrackbarPos("lb", "mask")
    hg = cv2.getTrackbarPos("hg", "mask")
    lg = cv2.getTrackbarPos("lg", "mask")
    hr = cv2.getTrackbarPos("hr", "mask")
    lr = cv2.getTrackbarPos("lr", "mask")

    mask = cv2.inRange(hsv, (lb, lg, lr), (hb, hg, hr))

    cv2.imshow("mask", mask)

    key = cv2.waitKey(1500) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(10)