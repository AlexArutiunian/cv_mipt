import cv2

cam = cv2.VideoCapture(0)

i = 0

while(True):
    success, frame = cam.read()
    
    print(frame.shape, type(frame[100, 300, 2]))
    
    frame[100:400, 300:500, :] = 30
    i += 1
    
    cv2.imshow("frame_lalalalala", frame)
    
    key = cv2.waitKey(30) & 0xFF
    
    if (key == ord('q')):
        break

cam.release() 
cv2.destroyAllWindows()
cv2.waitKey(10)