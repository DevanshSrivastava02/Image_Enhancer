# 21UCS061         DEVANSH SRIVASTAVA
# 21UCS068         DHRUV PATEL


import cv2 as cv
import numpy as np


def scale_down(new_img):  # This function will remove the alternate rows and columns i.e scaling down by factor of 2
    height = new_img.shape[1]//2
    width = new_img.shape[0]//2

    frame = np.zeros((height, width, 3), np.uint8)

    for i in range(height):
        for j in range(width):
            frame[i][j] = new_img[i*2][j*2]

    # Shows the scaled down image by a factor of 2
    cv.imshow("scaled_down_image", frame)


img = cv.imread("lena_color.tif", 3)
if img is None:
    print("No image detected")
    exit(0)
else:
    print("Image read successfully")
    cv.imshow("original_image", img)  # Reads the color image
    scale_down(img)
cv.waitKey(0)
cv.destroyAllWindows()
