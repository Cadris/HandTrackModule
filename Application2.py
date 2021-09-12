import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

#FPS
pTime = 0
cTime = 0
# camera selector
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img,draw=False)
    lmList = detector.findPosition(img)        

    if(len(lmList) != 0):
        print(lmList[4])

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)