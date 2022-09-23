import cv2 
import numpy as np
import matplotlib.pyplot as plt
import src.cleaning.fourier as fourier
import src.cleaning.masks as masks

if __name__ == "__main__":
    img_path = "images/input/RPf_00155.png"
    img_bgr = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
    
    r,g,b = cv2.split(img_rgb)
    shift_col = 30
    shift_row = 0
    height = 20 #  300
    width = 20 # 400
    rows,cols = r.shape
    crow,ccol = rows//2,cols//2
    channels = [r,g,b]
    channels_masks = [masks.two_rectangles(ch,crow,ccol,height,width,shift_row,shift_col) for ch in [r,g,b]]
    fourier_img = fourier.transform_color_img(channels,channels_masks)
    
    #plt.imshow((fourier_img*255).astype(np.uint8))
    #plt.savefig("Zeus.png")
    fourier_img_255 = (fourier_img*255).astype(np.uint8)
    cv2.imshow("Cleaned_image",cv2.cvtColor(fourier_img_255,cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("images/zeus.png",cv2.cvtColor(fourier_img_255,cv2.COLOR_RGB2BGR))