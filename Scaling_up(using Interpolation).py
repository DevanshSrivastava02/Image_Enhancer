# 21UCS061         DEVANSH SRIVASTAVA
# 21UCS068         DHRUV PATEL

import numpy as np
import cv2 as cv


def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        points.append([y, x])
        if (len(points) == 2):
            cv.namedWindow('interpolated_display', cv.WINDOW_AUTOSIZE)
            copy_img = img[points[0][0]:points[1]
                           [0], points[0][1]:points[1][1]]
            width = 2*int(copy_img.shape[1])
            height = 2*int(copy_img.shape[0])
            frame = np.zeros((height, width, 3), np.uint8)

            for i in range(0, height, 2):
                for j in range(0, width, 2):
                    frame[i][j] = copy_img[i//2][j//2]

            for i in range(0, height, 2):
                for j in range(1, width, 2):
                    if j != width-1:
                        frame[i][j] = (frame[i][j-1]+frame[i][j+1])//2
                    else:
                        frame[i][j] = frame[i][j-1]//2

            for i in range(1, height, 2):
                for j in range(width):
                    if i != height-1:
                        frame[i][j] = (frame[i-1][j]+frame[i+1][j])//2
                    else:
                        frame[i][j] = frame[i-1][j]//2
            cv.imshow("interpolated_display", frame)


points = []
img = cv.imread("lena_color.tif", 3)
if img is None:
    print("Wrong image")
else:
    print("Image read successfully")
    cv.imshow('image', img)
    cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()
