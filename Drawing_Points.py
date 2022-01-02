import cv2
import numpy as np


def mousePoint(event, x, y, flage, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(img, (x, y), 3, (110, 50, 50), -1)
        cv2.imshow("Orginal Image", img)


img = cv2.imread("7.jpeg")
cv2.imshow("Orginal image", img)
cv2.setMouseCallback("Orginal image", mousePoint)

cv2.waitKey(0)