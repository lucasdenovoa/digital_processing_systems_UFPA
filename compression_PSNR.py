from math import log10, sqrt
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import os

MAX_PIXEL=255.0

'''
def read_image():
    y = Image.open('./images/4.2.07.tiff')

    if os.path.exists('./images/gray_4.2.07.tiff'):
        pepper_image = Image.open('./images/4.2.07.tiff')
    elif os.path.exists('./images/gray_4.2.01.tiff'):
        splash_image = Image.open('./images/4.2.01.tiff')
    elif os.path.exists('./images/gray_4.2.03.tiff'):
        baboon_image = Image.open('./images/4.2.03.tiff')
    
    
    plt.figure(2)
    plt.imshow(y, 'gray', clim=(0, 255))

    y2 = 2*np.floor_divide(y,2)
    
    plt.figure(3), plt.imshow(y2, 'gray', clim=(0, 255))

    plt.show()
'''

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):
        return 100

    psnr = 20 * log10(MAX_PIXEL / sqrt(mse))
    
    return psnr
  
def main():
    pepper_original = cv2.imread("./images/4.2.07.tiff")

    if os.path.exists('./images/gray_4.2.07.tiff'):
        pepper_original = cv2.imread('./images/4.2.07.tiff')
        pepper_compressed = cv2.imread('./images/gray_4.2.07.tiff')
        
        value = PSNR(pepper_original, pepper_compressed)
        print(f"PSNR value for Pepper image is {value} dB")

    if os.path.exists('./images/gray_4.2.01.tiff'):
        splash_original = cv2.imread('./images/4.2.01.tiff')
        splash_compressed = cv2.imread('./images/gray_4.2.01.tiff')

        value = PSNR(splash_original, splash_compressed)
        print(f"PSNR value for Splash image is {value} dB")

    if os.path.exists('./images/gray_4.2.03.tiff'):
        baboon_original = cv2.imread('./images/4.2.03.tiff')
        baboon_compressed = cv2.imread('./images/gray_4.2.03.tiff')

        value = PSNR(baboon_original, baboon_compressed)
        print(f"PSNR value for Baboon image is {value} dB")
       
if __name__ == "__main__":
    main()
