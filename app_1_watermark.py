# This app still has a problem with the font that I'm trying to solve. The 'arial.ttf' isn't working.

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def text_on_image(image, text, font_size, color):
    img = Image.open(image)
    font = ImageFont.truetype('arial.ttf', font=font_size)
    draw = ImageDraw.Draw(img)
    iw, ih = img.size
    fw, fh = font.getsize(text)
    draw.text(
        ((iw - fw) / 2, (ih - fh) / 2),
        text,
        fill = color,
        font=font,
    )
    img.save('last_image.png')

image = st.file_uploader('Uma imagem!', type=['jpeg', 'jpg', 'png'])
text = st.text_input("Sua Marca d'água")
color = st.color_picker('Escolha uma cor:') # st.selectbox('Cor do fonte', ['black', 'white', 'red', 'green'])
font_size = st.number_input('Tamanho da fonte', min_value=50)

if image:
    result = st.button(
        'Aplicar',
        type = 'primary',
        on_click=text_on_image,
        args=(image, text, font_size, color)
    )
    if result:
        st.image('last_image.jpg')
        with open('last_image.jpg', 'rb') as file:
            st.download_button(
                'Baixar',
                file_name='image.jpg',
                data=file,
                mime='image/jpg'
            )
else:
    st.warning('Ainda não temos imagem!')