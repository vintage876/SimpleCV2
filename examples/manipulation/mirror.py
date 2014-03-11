from simplecv import *

c = Camera()

while True:
    img = c.getImage()
    split = img.split(2, 1)
    left = split[0][0]
    mirrorred = img.blit(left.flip_horizontal(),(left.width + 1, 0))
    mirrorred.show()
