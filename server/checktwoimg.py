import cv2
import numpy as np


def isTwoImageEqual(img1path,img2path):
    original = cv2.imread(img1path)
    duplicate = cv2.imread(img2path)

    if original.shape == duplicate.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely Equal")
            return True
    else:
        print("images are different")
        return False