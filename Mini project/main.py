import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 680)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

while True:
    success, img = cap.read()

    imgBackground[162:162+480, 58:55+640] = img
    cv2.imshow("Face Attendence", imgBackground)
    cv2.waitKey(1)
