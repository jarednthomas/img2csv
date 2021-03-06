#!/usr/bin/ python3
#
# img2csv.py
# ~~~~~~~~~~
# python script to convert an image of a csv file
# back into a csv file

from PIL import Image

import os
import sys
import argparse

import pyocr
import pyocr.builders

# Parse Args
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="input image to run OCR on")
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done on image before OCR")
args = vars(ap.parse_args())

# Define Image and path from Args
image_path = args['image']
image = Image.open(image_path)
image.save("temp.png", dpi=(300,300))
image = Image.open("temp.png")
print(image.format, image.size, image.mode)

# Define OCR Tools
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    print("Try installing tesseract-ocr or another OCR")
    sys.exit(1)

tool = tools[0]
langs = tool.get_available_languages()
lang = langs[0]
print("OCR Installed; Using {}".format(tool.get_name()))
print("Available languages: {}".format(langs), end="")
print(" (using {})".format(lang), end="\n\n")

#########################
## OCR text from image ##
#########################
txt = tool.image_to_string(
    image,
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)

print("Text from image:\n{}".format(txt), end="\n\n")

# example of how to save to pdf format
# pyocr.libtesseract.image_to_pdf(
#    Image.open(image_path),
#    "test_pdf_file"
#)

# Word Boxes
word_boxes = tool.image_to_string(
    Image.open(image_path),
    lang="eng",
    builder=pyocr.builders.WordBoxBuilder())

#print("Word Boxes:\n{}".format(word_boxes), end="\n\n")

# Line and Word Boxes
line_and_word_boxes = tool.image_to_string(
    Image.open('example.png'),
    lang="eng",
    builder=pyocr.builders.LineBoxBuilder())

#print("Line and Word Boxes:\n{}".format(line.content))

# Digits
digits = tool.image_to_string(
    Image.open('example.png'),
    lang="eng",
    builder=pyocr.tesseract.DigitBuilder())



os.remove("temp.png")
