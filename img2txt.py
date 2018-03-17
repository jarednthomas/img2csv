#!/usr/bin python
from PIL import Image
from pytesseract import image_to_string

import argparse
import os

# parse args
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

image = args['image']
extracted = image_to_string(Image.open(image))
print extracted
