# This app still has a problem with the font that I'm trying to solve. The 'arial/times.ttf' isn't working.

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def text_on_image(image, text, font_size, color):
    """
    Função que faz a operação de adicionar marca d'água.
    Uma vez definido todas as variáveis necessárias.

    Args:
        image (file): Imagem que terá uma nova marca d'água
        text (string): Texto da marca d'água
        font_size (int): Tamanho da fonte da marca d'água
        color (string?): Cor da marca d'água

    Returns:
        Não retorna nada.

    Raises:
        Exception: Levanta um erro, caso não seja possível fazer a operação.
    """
    try:
        img = Image.open(image)
        font = ImageFont.truetype('times.ttf', size=font_size)
        draw = ImageDraw.Draw(img)
        iw, ih = img.size
        fw, fh = font.getsize(text)
        draw.text(
            ((iw - fw) / 2, (ih - fh) / 2),
            text,
            fill = color,
            font=font,
        )
        img.save('last_image.jpg')
    except Exception as e:
        st.warning('Não foi possível completar a tarefa devido ao seguinte error: \n {}'.format(e))

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