import unittest
import cv2
import numpy as np
import src.cleaning.fourier as fourier
import src.cleaning.masks as masks


import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class TestGroup32(unittest.TestCase):
    def test_RPf_00262_obj(self):
        img_path = "images/input/RPf_00154.png"
        img_bgr = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
        
        r,g,b = cv2.split(img_rgb)
        shift_col = 400
        shift_row = 0
        height =  800
        width =  300
        rows,cols = r.shape
        crow,ccol = rows//2,cols//2
        channels = [r,g,b]
        channels_masks = [masks.two_rectangles(ch,crow,ccol,height,width,shift_row,shift_col) for ch in [r,g,b]]

        fourier_img = fourier.transform_color_img(channels,channels_masks)
        
        #plt.imshow((fourier_img*255).astype(np.uint8))
        #plt.savefig("Zeus.png")
        fourier_img_255 = (fourier_img*255).astype(np.uint8)
        # cv2.imshow("Cleaned_image",cv2.cvtColor(fourier_img_255,cv2.COLOR_RGB2BGR))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cv2.imwrite("images/zeus.png",cv2.cvtColor(fourier_img_255,cv2.COLOR_RGB2BGR))