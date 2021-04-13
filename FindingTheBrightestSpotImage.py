from PIL import Image
import numpy as np
Stars = Image.open('star.jpg')
print(Stars.size)
print(Stars.mode)
greyscale = Stars.convert('L')
print(greyscale.mode)
greyscaleArray = np.array(greyscale)
pixel = greyscale.load()
stars = []
for row in range(greyscale.size[0]):
    for column in range(greyscale.size[1]):
        if pixel[row, column] !=0:
            stars.append([row, column])
print(np.array(greyscale))
print(stars)








