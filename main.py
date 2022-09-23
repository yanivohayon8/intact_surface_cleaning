import cv2 
import numpy as np
import matplotlib.pyplot as plt
import fourier


if __name__ == "__main__":
    img_path = "images/RPf_00262_obj.png"
    img_bgr = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
    
    r,g,b = cv2.split(img_rgb)
    shift_col = 200
    shift_row = 0
    height_ = 800 # 300
    width_ = 400 # 400
    shift_col = 200
    rows,cols = r.shape
    crow,ccol = rows//2,cols//2
    channels = [r,g,b]
    channels_masks = [np.bitwise_not(
                                np.bitwise_xor(
                                    fourier.build_rectangle_high_pass(ch,crow-shift_row,ccol+shift_col,height_,width_),
                                    fourier.build_rectangle_high_pass(ch,crow+shift_row,ccol-shift_col,height_,width_)))
                                for ch in [r,g,b]]
    fourier_img = fourier.transform_color_img(channels,channels_masks)
    
    plt.imshow((fourier_img*255).astype(np.uint8))
    plt.savefig("Zeus.png")

    #cv2.imshow("Cleaned_image",(fourier_img*255).astype(np.uint8))
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()