from json import loads
import streamlit as st
import pandas as pd
import sys

st.title('App0 - O começo!')
with st.sidebar:
    st.subheader(' Usarei da barra lateral para fazer meus comentários :sunglasses:.')
    versao = sys.version
    st.write('Versão do Python: {}'.format(versao))
    st.write('Versão do Streamlit: {}'.format(st.__version__))
    with st.expander("Mais informações aqui"):
        st.markdown(
            """
            O arquivo que eu que estou me baseando está vídeo que coloquei como referência no README.md, está no tempo
            de 36 minutos e 40 segundos.

            ---

            O formato match/case que o Eduardo utiliza é para versões do Python que estejam com versões de 3.10 para cima. No meu caso, estou me baseando no meu 3.8.10 :thumbsup:. 
            Depois adicionarei o python 3.10+ para fazer essa mudança.

            Acredito que o mais prático do streamlit é pode fazer o código e checar o que você está fazendo.
            É muito prático ver o que está bom e ir alterando e dando prioridade de acordo como está ficando.

        """)


st.markdown(
    """
# Exibidor de Arquivos

## Suba um arquivo e vejamos o que acontece :smile: 
"""

)

arquivo = st.file_uploader(
    "Suba um arquivo", type=['png', 'csv', 'json', 'py', 'mp3']
)

if arquivo:
    type_arquivo =  arquivo.type.split('/')
    if type_arquivo == ['image', 'png']:
            st.image(arquivo)
    elif type_arquivo == ['text', 'csv']:
        df = pd.read_csv(arquivo)
        st.dataframe(df)
        st.line_chart(df)
    elif type_arquivo == ['application', _ ]:
        st.json(loads(arquivo.read()))
    elif type_arquivo == ['text', 'x-python']:
        st.code(arquivo.read().decode())
    elif type_arquivo == ['audio', _]:
        st.audio(arquivo)
else:
    st.error('Arquivo ainda não carregado!')




