import pandas as pd
import streamlit as st
import openpyxl


# CONFIGURAÇÃO DE PÁGINA:
st.set_page_config(page_title='CONFERÊNCIA DOS JOGOS',
                   page_icon='🎱 ', layout='wide')
st.sidebar.header(
    'Conferência dos Jogos Pessoais Realizados: ', divider='rainbow')
st.sidebar.image('imagem_lotofacil.JPG')

df_meus_jogos = pd.read_excel(r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\CONTROLE PAGAMENTO JOGOS.xlsx",
                              header=0, sheet_name='JOGOS PESSOAIS APOSTA-LOTOFÁCIL')

df_dados_historicos = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\Lotofácil.xlsx", header=0, sheet_name='LOTOFÁCIL')

opcao_conferencia = ['Automática', 'Manual']
st.sidebar.selectbox(
    'Selecione o Método de Conferência das Apostas: ', opcao_conferencia)


# Definir função para conferir jogos
ultimo_jogo = df_dados_historicos.tail(1)
tabela_ultimo_sorteio = ultimo_jogo[['Concurso', 'Data Sorteio', 'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6',
                                     'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']]


def conferir_jogos(df, meus_numeros):
    # Verificar acertos
    df['TOTAL DE ACERTOS'] = df.apply(lambda row: sum(
        [1 for num in meus_numeros if num in row[2:].values]), axis=1)

    # Criar DataFrame apenas com as colunas desejadas e a coluna "Total de Acertos"
    df_conferencia = df[['CONCURSOS', 'DATA DO JOGO', 'BOLA 1', 'BOLA 2', 'BOLA 3', 'BOLA 4', 'BOLA 5', 'BOLA 6', 'BOLA 7', 'BOLA 8',
                         'BOLA 9', 'BOLA 10', 'BOLA 11', 'BOLA 12', 'BOLA 13', 'BOLA 14', 'BOLA 15', 'TOTAL DE ACERTOS']]

    # Destacar números sorteados

    def highlight_acertos(val):
        color = 'green' if val in meus_numeros else 'black'
        return f'color: {color}'

    # Aplicar estilo ao DataFrame
    df_conferencia_estilo = df_conferencia.style.applymap(
        highlight_acertos, subset=[f'BOLA {i}' for i in range(1, 16)])

    return df_conferencia_estilo


# DATAFRAME ÚLTIMO SORTEIOS:
st.header('Dezenas do Último Sorteio: ')
st.dataframe(tabela_ultimo_sorteio)


# Seleção dos números para conferência
meus_numeros = st.multiselect('Selecione as 15 dezenas Sorteadas:', list(
    range(1, 26)), default=[])

# Conferir jogos se 15 números foram selecionados
if len(meus_numeros) == 15:
    df_conferencia_estilo = conferir_jogos(df_meus_jogos, meus_numeros)
    st.header('Resultado dos Jogos: ')
    st.dataframe(df_conferencia_estilo)
else:
    st.warning('Por favor, selecione exatamente 15 dezenas.')

# Exibir DataFrame original para referência
st.header('Jogos para Conferir: ')
st.dataframe(df_meus_jogos.set_index(['CONCURSOS']))

# Conferir jogos se 15 números foram selecionados
if len(meus_numeros) == 15:
    df_conferencia_estilo = conferir_jogos(df_meus_jogos, meus_numeros)

else:
    st.warning('Por favor, selecione exatamente 15 dezenas.')
