import numpy as np

def circle(img,crow,ccol,radius):
    circle_mask = np.zeros_like(img)

    for i in range(crow-radius, crow+radius):
            for j in range(ccol-radius, ccol + radius):
                if (crow - i) ** 2 + (ccol - j) ** 2 <= radius**2:
                    circle_mask[i,j]=1
    return circle_mask

def rectangle_white_list(img,crow,ccol,height,width):
    zeros = np.zeros_like(img)
    zeros[crow-height//2:crow+height//2,ccol-width//2:ccol+width//2] = 1
    return zeros

def rectangle_black_list(img,crow,ccol,height,width):
    ones = np.ones_like(img)
    ones[crow-height//2:crow+height//2,ccol-width//2:ccol+width//2] = 0
    return ones

def two_rectangles(img,crow,ccol,height,width,shift_row,shift_col):
    return np.bitwise_not(
                np.bitwise_xor(
                    rectangle_black_list(img,crow-shift_row,ccol+shift_col,height,width),
                    rectangle_black_list(img,crow+shift_row,ccol-shift_col,height,width)))