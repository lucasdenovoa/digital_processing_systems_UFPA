import matplotlib.pyplot as plt
import numpy as np
import time


from PIL import Image

img = Image.open('./4.2.07.tiff')
plt.figure(figsize=(9, 6))
plt.imshow(img)

imggray = img.convert('LA')

imggray.save('converted_4.2.07.tiff')

plt.figure(figsize=(9,6))
plt.imshow(imggray)

imgmat = np.array(list(imggray.getdata(band=0)), float)

imgmat.shape = (imggray.size[1], imggray.size[0])

imgmat = np.matrix(imgmat)

plt.figure(figsize=(9,6))
plt.imshow(imgmat, cmap='gray')

#imgmat.save('mat.tiff')

