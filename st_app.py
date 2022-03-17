import streamlit as st
from scrap_rt import *

st.title('Scrapper de filmes usando Beautiful Soup :popcorn:')

st.write("""

Na barra de seleção, escolha o ano e será gerado a tabela dos Top filmes do ano segundo o
 Rotten Tomatoes. Por padrão, a tabela gera os 100 melhores avaliados e com maior polularidade, 
 contudo, para períodos mais antigos, apenas alguns filmes estão presentes no site, sem completar 
 100 deles.
""")

# Checkbox de seleção do ano
option = st.selectbox(
     'Selecione o ano',
     list(range(2021,1949,-1)))

st.write('You selected:', option)

# Com base no escolhido, cria o link para o scrapper
link = 'https://www.rottentomatoes.com/top/bestofrt/?year=' + str(option)


st.write('----------------------')

# Código que realiza o processo de scrapping
if st.button('Montar Dataset'):
    
    st.write('Isso pode demorar alguns minutinhos (3 no máximo, confia).....')
    df = get_dataframe(link)

    st.write('### Tabela de Filmes')
    st.dataframe(df)

    st.download_button('Download CSV',df.to_csv().encode('utf-8'), f"movies_{option}.csv",'text/csv',
    key='download csv')

else:
    st.write('----------------------')