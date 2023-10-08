# 21UCS061         DEVANSH SRIVASTAVA
# 21UCS068         DHRUV PATEL

import cv2
import numpy as np
# Only if you using the google colab
# from google.colab.patches import cv2_imshow 
# #importing the imshow function to display the image.

print()
print("------->Welcome<-------")
print()
# Reading the image in the grayscale and saving it in img variable

img = cv2.imread('lena_color.tif', 0)
print("Showing the original image in Grayscale")
print()


cv2.namedWindow('Display')
cv2.imshow('Display', img)
print(" Note : Close the window to see the next image ")
cv2.waitKey(0)

# Setting the height and width of the image into variables

height = int(img.shape[0])
width = int(img.shape[1])

# Making a list of 8 images such that all the pixel values are set to zero
bit_plane = list()
for i in range(8):
    bit_plane.append(np.zeros((height, width, 1), np.uint8))

# This section of code will not set the proper values of 8 images created beforehand
for k in range(8):
    for i in range(height):
        for j in range(width):
            # Converting the pixel value into the binary and saving it as a form of string in temp variable
            temp = np.binary_repr(img[i][j], width=8)

            # Now if the bit value is 0 then that bit plane pixel value will be set to 0 otherwise appropriate value will be given
            if int(temp[7-k]) == 0:
                bit_plane[k][i][j] = 0
            else:
                bit_plane[k][i][j] = int(pow(2, k))

# Here showing all the bit_plane images individually
for i in range(8):
    print()
    print("Opened image is the image of bit plane " + str(i+1))
    # cv2.namedWindow('Display')
    cv2.imshow('Display', bit_plane[i])
    print(" Note : Close the window to see the next image ")

    cv2.waitKey(0)
    print()

# Now creating another image which will be used to print the Final result.
final = np.zeros((height, width, 1), np.uint8)

# Now casewise showing the image in the output
print()
print("Case 1 : Resultant image obtained by the addition of 8th and 7th Plane : ")

for i in range(height):
    for j in range(width):
        final[i][j] = bit_plane[7][i][j] + bit_plane[6][i][j]
# cv2.namedWindow('Display')
cv2.imshow('Display', final)
print(" Note : Close the window to see the next image ")
cv2.waitKey(0)
print()


print("Case 2 : Resultant image obtained by the addition of 8th,7th and 6th Plane : ")

for i in range(height):
    for j in range(width):
        final[i][j] = bit_plane[7][i][j] + \
            bit_plane[6][i][j] + bit_plane[5][i][j]
# cv2.namedWindow('Display')
cv2.imshow('Display', final)
print(" Note : Close the window to see the next image ")
cv2.waitKey(0)

print()
print("Case 3 : Resultant image obtained by the addition of 8th,7th,6th and 5th Plane : ")

for i in range(height):
    for j in range(width):
        final[i][j] = bit_plane[7][i][j] + bit_plane[6][i][j] + \
            bit_plane[5][i][j] + bit_plane[4][i][j]

# cv2.namedWindow('Display')
cv2.imshow('Display', final)
print(" Note : Close the window to see the next image ")

cv2.waitKey(0)
cv2.destroyAllWindows
