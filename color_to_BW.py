import matplotlib.pyplot as plt
import numpy as np
import time

import sys
import argparse


from PIL import Image

parser = argparse.ArgumentParser(description="Convert color image into B&W")

parser.add_argument(
            "-i",
            "--image",
            type=str,
            help="run with pepper splash and baboon argumments",
)

args = parser.parse_args()

if args.images:
    if args.images == "pepper":
        gray_image = './images/gray_4.2.07.tiff'
        color_image = './images/4.2.07.tiff'
    elif args.images == "splash":
        gray_image = './images/gray_4.2.01.tiff'
        color_image = './images/4.2.01.tiff'
    elif args.images == "baboon":
        gray_image = './images/gray_4.2.03.tiff'
        color_image = './images/4.2.03.tiff'
        
    else:
        print("invalid argumment: ", args.images)
        print("Use pepper splash and baboon argumments")

def color_to_bw():
    img = Image.open(color_image)
    plt.figure(figsize=(9, 6))
    plt.imshow(img)
    
    imggray = img.convert('LA')

    imggray.save(gray_image)

def main():
    color_to_bw()

if __name__ == "__main__":
    main()

