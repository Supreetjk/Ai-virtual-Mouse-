import cv2
import numpy as np
import HandTrackingModule as htm
import autopy
import pyautogui
import time

# Camera settings
wCam, hCam = 640, 480
frameR = 100
smoothening = 7

# Initialize
pTime = 0
plocX, plocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector()

wScr, hScr = autopy.screen.size()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]   # index finger
        x2, y2 = lmList[12][1:]  # middle finger

        fingers = detector.fingersUp(lmList)

        # Draw rectangle
        cv2.rectangle(img, (frameR, frameR),
                      (wCam-frameR, hCam-frameR), (255,0,255), 2)

        # ================= Cursor Movement =================
        if fingers[1] == 1 and fingers[2] == 0:

            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            autopy.mouse.move(wScr - clocX, clocY)

            cv2.circle(img, (x1, y1), 10, (255,0,255), cv2.FILLED)

            plocX, plocY = clocX, clocY

        # ================= Left Click =================
        if fingers[1] == 1 and fingers[2] == 1:
            length, img = detector.findDistance(8, 12, lmList, img)

            if length < 40:
                cv2.circle(img, (x1, y1), 10, (0,255,0), cv2.FILLED)
                autopy.mouse.click()

        # ================= Right Click =================
        if fingers[1] == 1 and fingers[4] == 1:
            autopy.mouse.click(button=autopy.mouse.Button.RIGHT)
            time.sleep(0.3)

        # ================= Scroll =================
        if sum(fingers) == 5:
            pyautogui.scroll(200)
        elif sum(fingers) == 0:
            pyautogui.scroll(-200)

    # FPS
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20,50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

    cv2.imshow("AI Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()