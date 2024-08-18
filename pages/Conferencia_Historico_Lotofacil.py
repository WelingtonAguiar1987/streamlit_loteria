import pandas as pd
import streamlit as st
import openpyxl
import numpy as np

# CONFIGURAÇÃO DE PÁGINA:
st.set_page_config(page_title='CONFERÊNCIA DOS JOGOS',
                   page_icon='🎱 ', layout='wide')
st.sidebar.header(
    'Conferência dos Jogos em Dados Históricos: ', divider='rainbow')
st.sidebar.image('imagem_lotofacil.JPG')

# Carregar dados da planilha Excel
df_lotofacil = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\Lotofácil.xlsx",
    header=0,
    sheet_name='LOTOFÁCIL'
)

# Transformar a coluna Concurso de Float para String
df_lotofacil['Concurso'] = df_lotofacil['Concurso'].astype(str)


ultimo_jogo = df_lotofacil.tail(1)

# Definir função para conferir jogos


def conferir_jogos(df, meus_numeros):
    # Verificar acertos
    df['Total de Acertos'] = df.apply(lambda row: sum(
        [1 for num in meus_numeros if num in row[2:].values]), axis=1)

    # Criar DataFrame apenas com as colunas desejadas e a coluna "Total de Acertos"
    df_conferencia = df[['Concurso', 'Data Sorteio', 'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8',
                         'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15', 'Total de Acertos']]

    # Destacar números sorteados

    def highlight_acertos(val):
        color = 'green' if val in meus_numeros else 'black'
        return f'color: {color}'

    # Aplicar estilo ao DataFrame
    df_conferencia_estilo = df_conferencia.style.applymap(
        highlight_acertos, subset=[f'Bola{i}' for i in range(1, 16)])

    return df_conferencia_estilo


# DATAFRAME ÚLTIMO SORTEIOS:
st.header('Dezenas do Último Sorteio: ')
st.dataframe(ultimo_jogo)

# Seleção dos números para conferência
meus_numeros = st.multiselect('Selecione suas 15 dezenas:', list(
    range(1, 26)), default=[])

# Conferir jogos se 15 números foram selecionados
if len(meus_numeros) == 15:
    df_conferencia_estilo = conferir_jogos(df_lotofacil, meus_numeros)
    st.dataframe(df_conferencia_estilo)
else:
    st.warning('Por favor, selecione exatamente 15 dezenas.')

# Exibir DataFrame original para referência
st.dataframe(df_lotofacil.set_index(['Concurso']))
