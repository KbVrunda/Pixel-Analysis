import numpy as np
import imageio
import matplotlib.pyplot as plt

#imread loads an image from the specified file
pic = imageio.imread("303_Lab10_P2.png")
# .show() = looks for all currently active figure objects, ones window(s) to display it
plt.show()
print(type(pic))
print(pic.shape)
#.zeros() = returns a new array of given shape and type
newArray = np.zeros(pic.shape)

for x in range(1, pic.shape[0] - 1):
    for y in range (1, pic.shape[1] - 1):
        newArray [x,y] = np.mean(pic[x-1:x+2, y-1:y+2])

#cmap means colormap; represents a change in lightness of two colors
plt.imshow(newArray, cmap = plt.cm.gray)
plt.savefig("BME303_Lab10_P2_Mean_VrundaPatel.png")

for x in range(1, pic.shape[0] - 1):
    for y in range(1, pic.shape[1] - 1):
        newArray[x,y] = np.median(pic[x-1: x+2, y-1:y+2])

plt.imshow(newArray, cmap = plt.cm.gray)
plt.savefig("BME303_Lab10_P2_Median_VrundaPatel.png")