import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def tesxt_on_image(image, text, font_size, color):
    img = Image.open(image)
    font = ImageFont.truetype('arial.ttf', font_size)