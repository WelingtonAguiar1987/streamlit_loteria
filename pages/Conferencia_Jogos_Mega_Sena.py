import pandas as pd
import streamlit as st
import openpyxl


# CONFIGURAÇÃO DE PÁGINA:
st.set_page_config(page_title='CONFERÊNCIA DOS JOGOS',
                   page_icon='🎱 ', layout='wide')
st.sidebar.header(
    'Conferência dos Jogos Realizados: ', divider='rainbow')
st.sidebar.image('imagem_megasena.JPG')

df_meus_jogos = pd.read_excel(r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\CONTROLE PAGAMENTO JOGOS.xlsx",
                              header=0, sheet_name='DEZENAS APOSTADAS-MEGA SENA')

df_dados_historicos = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\Mega-Sena.xlsx", header=0, sheet_name='MEGA SENA')


# Definir função para conferir jogos
ultimo_jogo = df_dados_historicos.tail(1)


def conferir_jogos(df, meus_numeros):
    # Verificar acertos
    df['TOTAL DE ACERTOS'] = df.apply(lambda row: sum(
        [1 for num in meus_numeros if num in row[2:].values]), axis=1)

    # Criar DataFrame apenas com as colunas desejadas e a coluna "Total de Acertos"
    df_conferencia = df[['CONCURSOS', 'DATA DO JOGO', 'BOLA 1', 'BOLA 2',
                         'BOLA 3', 'BOLA 4', 'BOLA 5', 'BOLA 6', 'TOTAL DE ACERTOS']]

    # Destacar números sorteados

    def highlight_acertos(val):
        color = 'green' if val in meus_numeros else 'black'
        return f'color: {color}'

    # Aplicar estilo ao DataFrame
    df_conferencia_estilo = df_conferencia.style.applymap(
        highlight_acertos, subset=[f'BOLA {i}' for i in range(1, 7)])

    return df_conferencia_estilo


# DATAFRAME ÚLTIMO SORTEIOS:
st.header('Dezenas do Último Sorteio: ')
st.dataframe(ultimo_jogo)

# Seleção dos números para conferência
meus_numeros = st.multiselect('Selecione as 6 dezenas Sorteadas:', list(
    range(1, 61)), default=[])

# Conferir jogos se 15 números foram selecionados
if len(meus_numeros) == 6:
    df_conferencia_estilo = conferir_jogos(df_meus_jogos, meus_numeros)
    st.header('Resultado dos Jogos: ')
    st.dataframe(df_conferencia_estilo)
else:
    st.warning('Por favor, selecione exatamente 6 dezenas.')

# Exibir DataFrame original para referência
st.header('Jogos para Conferir: ')
st.dataframe(df_meus_jogos.set_index(['CONCURSOS']))

# Conferir jogos se 15 números foram selecionados
if len(meus_numeros) == 6:
    df_conferencia_estilo = conferir_jogos(df_meus_jogos, meus_numeros)

else:
    st.warning('Por favor, selecione exatamente 6 dezenas.')
