import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import datetime
import random

# NOME DO JOGO:
nome_jogo = 'LOTOFÁCIL'

# LISTA DE DADOS DOS JOGOS POR DEZENAS:
lista_dezenas = {
    'Dezenas': [15, 16, 17, 18, 19, 20],
    'Valor em R$': [3, 48, 408, 2448, 11628, 46512]
}

# LISTA DE DADOS DOS JOGOS POR TEIMOSINHA:
lista_teimosinha = {
    'Concursos': [1, 3, 6, 9, 12, 18, 24],
    'Valor em R$': [3, 9, 18, 27, 36, 54, 72]
}

# LISTA DE DADOS DOS JOGOS POR PROBABILIDADE:
lista_probabilidade = {
    'Dezenas': [15, 16, 17, 18, 19, 20],
    'Probabilidade': [3268760, 204298, 24035, 4006, 843, 211]
}

# LISTA DE DADOS DOS JOGOS POR MESES:
lista_meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# GERANDO OS DATAFRAMES COM DADOS DOS JOGOS E VALORES:
df_dezenas = pd.DataFrame(lista_dezenas)
df_teimosinha = pd.DataFrame(lista_teimosinha)
df_probabilidade = pd.DataFrame(lista_probabilidade)
df_lotofacil = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\Lotofácil.xlsx", header=0, sheet_name='LOTOFÁCIL')

df_pagamento = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\CONTROLE PAGAMENTO JOGOS.xlsx", header=0, sheet_name='LOTOFÁCIL')

df_bolas_jogadas = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\CONTROLE PAGAMENTO JOGOS.xlsx", header=0, sheet_name='DEZENAS APOSTADAS-LOTOFÁCIL')

df_saldos = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\CONTROLE PAGAMENTO JOGOS.xlsx", header=0, sheet_name='LOTOFÁCIL-SALDOS')

# TRATANDO OS DADOS NOS DATAFRAMES:
df_lotofacil['Concurso'] = df_lotofacil['Concurso'].astype(str)
df_pagamento['DATA DO PAGAMENTO'] = pd.to_datetime(
    df_pagamento['DATA DO PAGAMENTO'])
df_pagamento['DATA DOS PAGAMENTOS'] = df_pagamento['DATA DO PAGAMENTO'].dt.strftime(
    '%d/%m/%Y %H:%M:%S')
df_pagamento = df_pagamento.drop(columns='DATA DO PAGAMENTO')

df_bolas_jogadas['DATA DO JOGO'] = pd.to_datetime(
    df_bolas_jogadas['DATA DO JOGO'])
df_bolas_jogadas['DATA DO JOGO'] = df_bolas_jogadas['DATA DO JOGO'].dt.strftime(
    '%d/%m/%Y %H:%M:%S')

df1 = df_dezenas.set_index(['Dezenas'])
df2 = df_teimosinha.set_index(['Concursos'])
df3 = df_probabilidade.set_index(['Dezenas'])
df4 = df_lotofacil.set_index(['Concurso'])

# CONFIGURAÇÃO DE PÁGINA:
st.set_page_config(page_title='JOGOS DO PEZÃO',
                   page_icon='🎱 ', layout='wide')

st.title(f'JOGOS DO PEZÃO - {nome_jogo} 🎲')
st.sidebar.header('Controle dos Jogos: ')
st.sidebar.image('imagem_lotofacil.JPG')
total_numeros_aposta = st.sidebar.selectbox(
    'Selecione a Quantidade de Dezenas Desejada para este Jogo: ', list(lista_dezenas['Dezenas']))

total_concurso_teimosinha = st.sidebar.selectbox(
    'Selecione a Quantidade de Concursos que Deseja Participar Neste Jogo: ', list(lista_teimosinha['Concursos']))

quantidade_jogos_realizar = st.sidebar.number_input(
    'Digite a Quantidade de Jogos que Deseja Realizar: ', value=1)

quantidade_jogador = st.sidebar.number_input(
    'Digite a Quantidade de Jogadores: ', value=1)

valor_premio = st.sidebar.number_input(
    'Digite o Valor Total do Prêmio: ', value=0)

selecao_meses = st.sidebar.selectbox(
    'Selecione a Quantidade de Meses a Realizar os Jogos: ', list(lista_meses))

# CONDICIONAL PARA O PREÇO DAS APOSTAS SIMPLES:
if total_numeros_aposta == 15:
    valor_aposta = 3
elif total_numeros_aposta == 16:
    valor_aposta = 48
elif total_numeros_aposta == 17:
    valor_aposta = 408
elif total_numeros_aposta == 18:
    valor_aposta = 2448
elif total_numeros_aposta == 19:
    valor_aposta = 11628
elif total_numeros_aposta == 20:
    valor_aposta = 46512

# CONDICIONAL PARA O PREÇO DAS APOSTAS POR TEIMOSINHAS:
if total_concurso_teimosinha == 1:
    valor_teimosinha = 3
elif total_concurso_teimosinha == 3:
    valor_teimosinha = 9
elif total_concurso_teimosinha == 6:
    valor_teimosinha = 18
elif total_concurso_teimosinha == 9:
    valor_teimosinha = 27
elif total_concurso_teimosinha == 12:
    valor_teimosinha = 36
elif total_concurso_teimosinha == 18:
    valor_teimosinha = 54
elif total_concurso_teimosinha == 24:
    valor_teimosinha = 72

# CONDICIONAL PRINTANDO TEXTOS TEIMOSINHA:
if total_concurso_teimosinha == 1:
    mostrar_texto = 'Aposta Simples'
else:
    mostrar_texto = 'Teimosinha'

# CONDICIONAL PARA PROBABILIDADE:
if total_numeros_aposta == 15:
    probabilidade = 3268760
elif total_numeros_aposta == 16:
    probabilidade = 204298
elif total_numeros_aposta == 17:
    probabilidade = 24035
elif total_numeros_aposta == 18:
    probabilidade = 4006
elif total_numeros_aposta == 19:
    probabilidade = 843
elif total_numeros_aposta == 20:
    probabilidade = 211

# VARIÁVEIS DE CONTROLE:
custo_aposta_lotofacil = valor_aposta * total_concurso_teimosinha
custo_teimosinha = custo_aposta_lotofacil * total_numeros_aposta

premio_por_jogador = valor_premio / quantidade_jogador
valor_arrecadado = custo_aposta_lotofacil * quantidade_jogos_realizar
valor_jogador = float(valor_arrecadado / quantidade_jogador)
payoff = premio_por_jogador / valor_jogador

# CONTAINER DE DADOS DAS APOSTAS:
with st.container():
    st.header('Dados das Apostas')
    st.write(
        f'Valor da Aposta Simples {nome_jogo}:  :blue[R$ {valor_aposta:.2f}]')
    st.write(f'Custo da {mostrar_texto}: :blue[R$ {
             custo_aposta_lotofacil:.2f}]')
    st.write(f'Valor a Pagar por cada Jogador:  :red[R$ {valor_jogador:.2f}]')
    st.write(f'Valor Arrecadado:  :green[R$ {valor_arrecadado:.2f}]')
    st.write(f'Valor do Prêmio:  :green[R$ {valor_premio:.2f}]')
    st.write(f'Valor do Prêmio por Jogador:  :green[R$ {
             premio_por_jogador:.2f}]')

# VARIÁVEIS DE PROBABILIDADES:
probabilidade_jogos_simples = probabilidade
tentativas = total_concurso_teimosinha * quantidade_jogos_realizar
probabilidade_deste_jogo = probabilidade_jogos_simples / tentativas
probabilidade_meses = probabilidade_deste_jogo / selecao_meses

# CONTAINER DE PROBABILIDADES:
with st.container():
    st.header('Probabilidade de Ganhar')
    st.write(
        f'A Probabilidade de Ganhar o Prêmio com {total_numeros_aposta} Dezenas é de 1 em :blue[{probabilidade_jogos_simples:,}]')
    st.write(
        f'Com :blue[{tentativas}] tentativas ao longo de {selecao_meses} meses, a probabilidade de ganhar é de 1 em :blue[{int(probabilidade_deste_jogo):,}]')
    st.write(
        f'Ou seja, a probabilidade ajustada ao longo dos meses é de 1 em :blue[{int(probabilidade_meses):,}]')

# CONTAINER DE PAYOFF:
with st.container():
    st.header('Payoff')
    st.write(
        f'Payoff: :blue[{payoff:.2f}]')

    if payoff > 1:
        st.success(
            f'O payoff é maior que 1, indicando que o prêmio esperado é superior ao custo da aposta.')
    else:
        st.warning(
            f'O payoff é menor ou igual a 1, indicando que o prêmio esperado não cobre o custo da aposta.')

# CONTAINER DE GRÁFICOS:
with st.container():
    st.header('Análise de Dados')

    # Gráfico de valores por dezenas
    fig_dezenas = px.bar(df_dezenas, x=df_dezenas.index, y='Valor em R$',
                         title='Valor por Dezenas', text='Valor em R$')
    fig_dezenas.update_layout(xaxis_title='Dezenas', yaxis_title='Valor em R$')
    st.plotly_chart(fig_dezenas)

    # Gráfico de valores por teimosinha
    fig_teimosinha = px.line(df_teimosinha, x=df_teimosinha.index, y='Valor em R$',
                             title='Valor por Teimosinha', markers=True, text='Valor em R$')
    fig_teimosinha.update_layout(
        xaxis_title='Concursos', yaxis_title='Valor em R$')
    st.plotly_chart(fig_teimosinha)

    # Gráfico de probabilidade por dezenas
    fig_probabilidade = px.bar(df_probabilidade, x=df_probabilidade.index,
                               y='Probabilidade', title='Probabilidade por Dezenas', text='Probabilidade')
    fig_probabilidade.update_layout(
        xaxis_title='Dezenas', yaxis_title='Probabilidade')
    st.plotly_chart(fig_probabilidade)

# EXIBINDO DADOS DOS JOGOS REALIZADOS:
with st.container():
    st.header('Histórico de Jogos Realizados')
    st.write(df_lotofacil)

# EXIBINDO DADOS DOS PAGAMENTOS:
with st.container():
    st.header('Controle de Pagamentos')
    st.write(df_pagamento)

# EXIBINDO DADOS DOS SALDOS:
with st.container():
    st.header('Saldos')
    st.write(df_saldos)
