import cv2 
import numpy as np 

def main():
    cap = cv2.VideoCapture(0) 
    while True: 
        ret,frame = cap.read()
        if not ret:
            break 
        into_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 
        L_limit = np.array([98,50,50]) 
        U_limit = np.array([139,255,255])
        b_mask=cv2.inRange(into_hsv,L_limit,U_limit) 
        blue=cv2.bitwise_and(frame,frame,mask=b_mask) 
        cv2.imshow('Original',frame) 
        cv2.imshow('Blue Detector',blue) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release() 
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()