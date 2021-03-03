import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

img = mpimg.imread("gray.png")


fig = plt.figure()
ax = fig.add_subplot(1,2,1)
imgplot = plt.imshow(img)
ax.set_title('Before')
plt.colorbar(ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0], orientation='horizontal')
ax = fig.add_subplot(1,2,2)
imgplot = plt.imshow(img)
imgplot.set_clim(0.0,0.15)
print(imgplot)
ax.set_title('After')
plt.colorbar(ticks=[0.05,0.10,0.15], orientation='horizontal')
#imgplot.set_cmap('binary')
plt.show()
