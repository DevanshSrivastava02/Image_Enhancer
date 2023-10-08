# 21UCS061         DEVANSH SRIVASTAVA
# 21UCS068         DHRUV PATEL

import cv2 as cv
import numpy as np


# callback function to implement replicated image
def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print()
        print('Select coordinates of the top left corner and bottom right corner of the desired window size')
        print()
        print(x, ',', y)
        points.append([y, x])
        if (len(points) == 2):
            # Create window to capture the desired window size
            cv.namedWindow('replicated_image', cv.WINDOW_AUTOSIZE)
            copy_img = img[points[0][0]:points[1]
                           [0], points[0][1]:points[1][1]]

            width = 2*int(copy_img.shape[1])
            height = 2*int(copy_img.shape[0])
            frame = np.zeros((height, width, 3), np.uint8)

            for i in range(height):   # Looping through complete image
                for j in range(width):
                    if i % 2 == 0:
                        if j % 2 != 0:
                            frame[i, j] = frame[i, j-1]
                        else:
                            frame[i, j] = copy_img[i//2, j//2]
                    else:
                        frame[i, j] = frame[i-1, j]
            cv.imshow("replicated_image", frame)


points = []
img = cv.imread("lena_color.tif", 3)  # Reading original image file
if img is None:
    print("Error:Image cannot be loaded")
    exit(0)
else:
    print("Image loaded succesfully")
    # Display original image to compare with the selected window
    cv.imshow('original_image', img)
    # This function will track the coordinates of the top left and bottom right limit of the desired window size to display the replicated image
    cv.setMouseCallback('original_image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()
