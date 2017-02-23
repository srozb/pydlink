import os
import sys
from fabulous import image


def AnsiRender(camera_image):
    cols = int(os.popen('stty size', 'r').read().split()[1])
    print(image.Image(camera_image, width=cols))
