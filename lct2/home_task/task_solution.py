import numpy as np
import cv2

def detect_objects(frame, lower_black, upper_black, min_size, max_size):
    answer = []
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, lower_black, upper_black)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        if area >= min_size and area <= max_size:
            answer.append((x, y, w, h))
    
    return answer

def draw_answer(frame, bboxes):
    for b in bboxes:
        l, t, w, h = b
        
        cv2.rectangle(frame, (l, t), (l + w, t + h), (123, 34, 125), 3)
    
    return frame

answers = []

video_name = "home_task/black_objects.mp4"

cam = cv2.VideoCapture(video_name)

cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.resizeWindow("mask", 600, 900)

cv2.createTrackbar("hb", "mask", 128, 255, lambda i: 1)
cv2.createTrackbar("lb", "mask", 93, 255, lambda i: 1)
cv2.createTrackbar("hg", "mask", 178, 255, lambda i: 1)
cv2.createTrackbar("lg", "mask", 108, 255, lambda i: 1)
cv2.createTrackbar("hr", "mask", 77, 255, lambda i: 1)
cv2.createTrackbar("lr", "mask", 50, 255, lambda i: 1)
cv2.createTrackbar("min_size", "mask", 4001, 5000, lambda i: 1)  # Трекбар для минимального размера детектируемого объекта
cv2.createTrackbar("max_size", "mask", 8004, 10000, lambda i: 1)  # Трекбар для максимального размера детектируемого объекта

while(True):
    succ, frame = cam.read()
    
    if not succ:
        print("не удалось считать кадр, выход")
        break
    
    hb = cv2.getTrackbarPos("hb", "mask")
    lb = cv2.getTrackbarPos("lb", "mask")
    hg = cv2.getTrackbarPos("hg", "mask")
    lg = cv2.getTrackbarPos("lg", "mask")
    hr = cv2.getTrackbarPos("hr", "mask")
    lr = cv2.getTrackbarPos("lr", "mask")
    min_size = cv2.getTrackbarPos("min_size", "mask")
    max_size = cv2.getTrackbarPos("max_size", "mask")
    
    lower_black = np.array([lb, lg, lr])
    upper_black = np.array([hb, hg, hr])
    
    answer = detect_objects(frame, lower_black, upper_black, min_size, max_size)
    answers.append(answer)
    
    marked = draw_answer(frame, answer)
    
    cv2.imshow("result", marked)
    
    key = cv2.waitKey(30) & 0xFF
    
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()