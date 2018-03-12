#!/usr/bin/ python3
#
# img2csv.py
# ~~~~~~~~~~
# python script to convert an image of a csv file
# back into a csv file

from PIL import Image

import sys
import argparse

import pyocr
import pyocr.builders

# parse args
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="input image to run OCR on")
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done on image before OCR")
args = vars(ap.parse_args())

# set path to image from args
image_path = args['image']

# set tools
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    print("Try installing tesseract or another OCR")
    sys.exit(1)

tool = tools[0]
print("OCR Installed; Using {}".format(tool.get_name()))

# set language
langs = tool.get_available_languages()
print("Available languages: {}".format(langs), end="")
lang = langs[0]
print(" (using {})".format(lang), end="\n\n")

# text from image
txt = tool.image_to_string(
    Image.open(image_path),
    lang=lang,
    builder=pyocr.builders.TextBuilder())

print("Text from image:\n{}".format(txt), end="\n\n")

""" example of how to save to pdf format
pyocr.libtesseract.image_to_pdf(
    Image.open(image_path),
    "test_pdf_file"
) """

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

