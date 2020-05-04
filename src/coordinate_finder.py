#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

__author__ = "Mohd Hafizuddin Bin Kamilin"

# load the binary image in a single channel mode
img = Image.open("test.png").convert("L")
# convert the image into a numpy array
img = np.array(img)

# get the image size
imgWidth = img.shape[0]
imgHeight = img.shape[1]

# initialize up coordinate
up_x = None
up_y = None
# initialize down coordinate
down_x = None
down_y = None
# initialize left coordinate
left_x = None
left_y = None
# initialize right coordinate
right_x = None
right_y = None

# temporarily store the values for comparison
temp_x = None
temp_y = None

# scanning the y-axis from top to bottom
for y in range(imgHeight):

    # scanning the x-axis from left to right
    for x in range(imgWidth):

        # if white dot was found
        if (img[y][x] == 255):

            # the first white dot that was found represent the top section of the object
            if ((up_x is None) and (up_y is None)):

                # so we record the coordinate of where the white dot was found
                up_x = x
                up_y = y

            # after the first white dot was found and we are not at the end of the picture
            elif ((x != imgWidth) and (y != imgHeight)):

                # keep on recording the latest white dot's coordinate that we found
                temp_x = x
                temp_y = y

    # finally we write the last white dot recorded on temporary variable to their respective variable
    down_x = temp_x
    down_y = temp_y

# reset the temporary variable
temp_x = None
temp_y = None

# scanning the x-axis from left to right
for x in range(imgWidth):

    # scanning the y-axis from top to bottom
    for y in range(imgHeight):

        # if white dot was found
        if (img[y][x] == 255):

            # the first white dot was found represent the left section for the object
            if ((left_x is None) and (left_y is None)):

                # so we record the coordinate of where the white dot was found
                left_x = x
                left_y = y

            # after the first white dot was found and we are not at the end of the picture
            elif ((x != imgWidth) and (y != imgHeight)):

                # keep on recording the latest white dot's coordinate that we found
                temp_x = x
                temp_y = y

    # finally we write the last white dot recorded on temporary variable to their respective variable
    right_x = temp_x
    right_y = temp_y

print("\n\nPixel coordinate for the:")
print("  ↑ point of object (%d, %d)" % (up_x, up_y))
print("  ↓ point of object (%d, %d)" % (down_x, down_y))
print("  ← point of object (%d, %d)" % (left_x, left_y))
print("  → point of object (%d, %d)" % (right_x, right_y))

print("\nGraph coordinate for the:")
print("  ↑ point of object (%d, %d)" % (imgWidth - up_x, imgHeight - up_y))
print("  ↓ point of object (%d, %d)" % (imgWidth - down_x, imgHeight - down_y))
print("  ← point of object (%d, %d)" % (imgWidth - left_x, imgHeight - left_y))
print("  → point of object (%d, %d)" % (imgWidth - right_x, imgHeight - right_y))
