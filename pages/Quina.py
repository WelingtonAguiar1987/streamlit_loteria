import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import random
import locale

# CONVERSÃO MOEDA
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

# NOME DO JOGO:
nome_jogo = 'QUINA'

# LISTA DE DADOS DOS JOGOS POR DEZENAS:
lista_dezenas = {
    'Dezenas': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'Valor em R$': [2.50, 15, 52.50, 140, 315, 630, 1155, 1980, 3217.50, 5005, 7507.50]
}

# LISTA DE DADOS DOS JOGOS POR TEIMOSINHA:
lista_teimosinha = {
    'Concursos': [1, 3, 6, 12, 18, 24],
    'Valor em R$': [2.50, 7.50, 15, 30, 45, 60]
}


# LISTA DE DADOS DOS JOGOS POR DEZENAS:
lista_probabilidade = {
    'Dezenas': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'Probabilidade': [24040016, 4006669, 1144763, 429286, 190794, 95396, 52035, 30354, 18679, 12008, 8005]
}


# LISTA DE DADOS DOS JOGOS POR DEZENAS:
lista_meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# GERANDO OS DATAFRAMES COM DADOS DOS JOGOS E VALORES:
df_dezenas = pd.DataFrame(lista_dezenas)
df_teimosinha = pd.DataFrame(lista_teimosinha)
df_probabilidade = pd.DataFrame(lista_probabilidade)
df_quina = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\Quina.xlsx", sheet_name='QUINA', header=0)
df_pagamento = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\CONTROLE PAGAMENTO JOGOS.xlsx", header=0, sheet_name='QUINA')

df_bolas_jogadas = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\CONTROLE PAGAMENTO JOGOS.xlsx", header=0, sheet_name='DEZENAS APOSTADAS-QUINA')

df_saldos = pd.read_excel(
    r"C:\Users\welin\OneDrive\Anexos de email\Documentos\Meus Projetos em Python\Loterias\CONTROLE PAGAMENTO JOGOS.xlsx", header=0, sheet_name='QUINA-SALDOS')

# TRATANDO OS DADOS NOS DATAFRAMES:
# Transformando a coluna Concurso de Float para String:
df_quina['Concurso'] = df_quina['Concurso'].astype(str)

# Convertendo a coluna 'DATA DO PAGAMENTO' para datetime
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
df4 = df_quina.set_index(['Concurso'])

# CONFIGURAÇÃO DE PÁGINA:
st.set_page_config(page_title='JOGOS DO PEZÃO',
                   page_icon='🎱 ', layout='wide')

st.title(f'JOGOS DO PEZÃO - {nome_jogo} 🎲')
st.sidebar.header('Controle dos Jogos: ', divider='rainbow')
st.sidebar.image('imagem_quina.JPG')
total_numeros_aposta = st.sidebar.selectbox(
    'Selecione a Quantidade de Dezenas Desejada para este Jogo: ', list(lista_dezenas['Dezenas']))


total_concurso_teimosinha = st.sidebar.selectbox(
    'Selecione a Quantidade de Concursos que Deseja Participar Neste Jogo: ', list(lista_teimosinha['Concursos']))

quantidade_jogos_realizar = st.sidebar.number_input(
    'Digite a Quantidade de Jogos que Deseja Realizar: ', value=1)

quantidade_jogador = st.sidebar.number_input(
    'Digite a Quantidade de Jogadores: ', value=1)

valor_premio = st.sidebar.number_input(
    'Digite o Valor Total "Simulado" do Prêmio: ', value=0)
valor_premio_em_Real_formatado = locale.currency(valor_premio)

selecao_meses = st.sidebar.selectbox(
    'Selecione a Quantidade de Meses a Realizar os Jogos: ', list(lista_meses))

# CONDICIONAL PARA O PREÇO DAS APOSTAS SIMPLES:
if total_numeros_aposta == 5:
    valor_aposta = 2.50

elif total_numeros_aposta == 6:
    valor_aposta = 15

elif total_numeros_aposta == 7:
    valor_aposta = 52.50

elif total_numeros_aposta == 8:
    valor_aposta = 140

elif total_numeros_aposta == 9:
    valor_aposta = 315

elif total_numeros_aposta == 10:
    valor_aposta = 630

elif total_numeros_aposta == 11:
    valor_aposta = 1155

elif total_numeros_aposta == 12:
    valor_aposta = 1980

elif total_numeros_aposta == 13:
    valor_aposta = 3217.50

elif total_numeros_aposta == 14:
    valor_aposta = 5005

elif total_numeros_aposta == 15:
    valor_aposta = 7507.50


# CONDICIONAL PARA O PREÇO DAS APOSTAS POR TEIMOSINHAS:
if total_concurso_teimosinha == 1:
    valor_teimosinha = 2.50

elif total_concurso_teimosinha == 3:
    valor_teimosinha = 7.50

elif total_concurso_teimosinha == 6:
    valor_teimosinha = 15

elif total_concurso_teimosinha == 12:
    valor_teimosinha = 30


elif total_concurso_teimosinha == 18:
    valor_teimosinha = 45

elif total_concurso_teimosinha == 24:
    valor_teimosinha = 60


# CONDICIONAL PRINTANDO TEXTOS TEIMOSINHA:
if total_concurso_teimosinha == 1:
    mostrar_texto = 'Aposta Simples'

else:
    mostrar_texto = 'Teimosinha'


# CONDICIONAL PARA PROBABILIDADE:
if total_numeros_aposta == 5:
    probabilidade = 24040016

elif total_numeros_aposta == 6:
    probabilidade = 4006669

elif total_numeros_aposta == 7:
    probabilidade = 1144763

elif total_numeros_aposta == 8:
    probabilidade = 429286

elif total_numeros_aposta == 9:
    probabilidade = 190794

elif total_numeros_aposta == 10:
    probabilidade = 95396

elif total_numeros_aposta == 11:
    probabilidade = 52035

elif total_numeros_aposta == 12:
    probabilidade = 30354

elif total_numeros_aposta == 13:
    probabilidade = 18679

elif total_numeros_aposta == 14:
    probabilidade = 12008

elif total_numeros_aposta == 15:
    probabilidade = 8005


# CONDICIONAL PARA DEFINIÇÃO DE MÊS OU MESES:
if selecao_meses == 1:
    resultado_selecao_meses = 'Mês'

else:
    resultado_selecao_meses = 'Meses'


# VARIÁVEIS DE CONTROLE:
custo_aposta_quina = valor_aposta * total_concurso_teimosinha
custo_teimosinha = custo_aposta_quina * total_numeros_aposta

premio_por_jogador = valor_premio / quantidade_jogador
premio_por_jogador_em_Real_formatado = locale.currency(premio_por_jogador)
valor_arrecadado = custo_aposta_quina * quantidade_jogos_realizar
valor_arrecadado_em_Real_formatado = locale.currency(valor_arrecadado)
valor_jogador = (valor_arrecadado / quantidade_jogador)
valor_jogador_em_Real_formatado = locale.currency(valor_jogador)
aliquota_ir = 0.5
ir_pagar = (premio_por_jogador * aliquota_ir) / 10
ir_pagar_em_Real_formatado = locale.currency(ir_pagar)
ganho_liquido = (premio_por_jogador - ir_pagar)
ganho_liquido_em_Real_formatado = locale.currency(ganho_liquido)
ir_total = ((ir_pagar * (quantidade_jogador - 1)))
ir_total_em_Real_formatado = locale.currency(ir_total)

# PAYOFF:
payoff = ganho_liquido / valor_jogador

# CONTAINER DE DADOS DAS APOSTAS:
with st.container():
    st.header('Dados das Apostas', divider='rainbow')
    st.write(
        f'Valor da Aposta Simples {nome_jogo}:  :blue[ R$ {valor_aposta:.2f}].')
    st.write(f'Custo da {mostrar_texto}: :blue[ R$ {
             custo_aposta_quina:.2f}].')
    st.write(
        f'Valor a Pagar por cada Jogador:  :red[ {valor_jogador_em_Real_formatado}].')
    st.write(f'Valor Arrecadado:  :green[ {
             valor_arrecadado_em_Real_formatado}].')
    st.write(f'Quantidade de Apostas Realizadas: :blue[ {
             quantidade_jogos_realizar}].')
    st.write(f'Quantidade de Jogadores Participantes: :blue[ {
             quantidade_jogador}].')
    st.write(f'Valor do Prêmio Simulado:  :green[ {
             valor_premio_em_Real_formatado}].')
    st.write(f'Valor do Prêmio Bruto Por Jogador:  :green[ {
             premio_por_jogador_em_Real_formatado}].')
    st.write(f'Estimativa de Imposto de Renda a deduzir Por Cota (5%): :red[ {
             ir_pagar_em_Real_formatado}].')
    st.write(f'Estimativa de Prêmio Líquido a Receber Por Cota: :green[ {
             ganho_liquido_em_Real_formatado}].')


st.header('', divider='rainbow')
st.subheader(f':orange[ATENÇÃO - IMPOSTO DE RENDA]')
st.write(f'Imposto de Renda Total a Pagar (somatória todas as Cotas): :red[ {
    ir_total_em_Real_formatado}].')
st.header('', divider='rainbow')

# VARIÁVEIS DE PROBABILIDADES:
probabilidade_jogos_simples = probabilidade
tentativas = total_concurso_teimosinha * quantidade_jogos_realizar
probabilidade_deste_jogo = probabilidade_jogos_simples / tentativas
probabilidade_meses = probabilidade_deste_jogo / selecao_meses

# CONDICIONAL PARA DEFINIÇÃO DE MÊS OU MESES:
resultado_selecao_mes = 'Mês'
resultado_selecao_meses = 'Meses'
total_por_cada_jogador = (valor_jogador * selecao_meses)
total_por_cada_jogador_em_Real_formatado = locale.currency(
    total_por_cada_jogador)
payoff_meses = (ganho_liquido / total_por_cada_jogador)
total_arrecadado_meses = valor_arrecadado * selecao_meses
total_arrecadado_meses_em_Real_formatado = locale.currency(
    total_arrecadado_meses)
total_tentativas_meses = tentativas * selecao_meses

# CONDICIONAL MÊS OU MESES:
if selecao_meses == 1:
    escrever_meses = resultado_selecao_mes
elif selecao_meses >= 2:
    escrever_meses = resultado_selecao_meses

# CONTAINER DE PROBABILIDADES:
with st.container():
    st.header('Probabilidades', divider='rainbow')
    st.write(f'Probabilidade de Jogos Simples {nome_jogo}: :orange[{
        probabilidade_jogos_simples}].')
    st.write(f'Concorrerá por: :violet[{tentativas}] Tentativas Neste Mês.')
    st.write(f'Probabilidade com essa Estratégia: :orange[ {
        probabilidade_deste_jogo:.0f}].')
    st.write(f'Payoff do Prêmio em 1 Mês: Com Esses Jogos Você Ganhará :orange[ {
        payoff:.0f}] Vezes o Valor Investido: :red[ {valor_jogador_em_Real_formatado}].')
    if selecao_meses >= 2:
        st.write(f'Payoff do Prêmio ao longo de :blue[{selecao_meses} meses]: Com Esses Jogos Você Ganhará :orange[ {
            payoff_meses:.0f}] Vezes o Valor Investido: :red[{total_por_cada_jogador_em_Real_formatado}].')

# CONTAINER DE PAYOFF:
with st.container():
    if ganho_liquido >= total_por_cada_jogador:
        st.success(
            f'O Prêmio Líquido de {ganho_liquido_em_Real_formatado} é {payoff_meses:.0f} Vezes maior que o Custo das Apostas em {selecao_meses} {escrever_meses}.')

    elif ganho_liquido == 0:
        st.warning(f'Adicione um Valor de Prêmio.')

    else:
        st.warning(
            f'O Prêmio Líquido de {ganho_liquido_em_Real_formatado} Reais é menor que o Valor Investido em {selecao_meses} {escrever_meses}, indicando que o Prêmio esperado não cobre os custos das apostas.')
        st.warning(f' {total_por_cada_jogador_em_Real_formatado}.')


with st.container():
    if selecao_meses == 1:
        total_por_cada_jogador = valor_jogador * selecao_meses
    else:
        with st.container():
            st.header('', divider='rainbow')
            st.header('Probabilidade de Ganhar')
            st.write(f'Valor Arrecadado ao longo de :blue[{selecao_meses} meses] é: :green[ {
                total_arrecadado_meses_em_Real_formatado}].')
            st.write(f'Valor Gasto Por Cada Jogador ao longo de :blue[{selecao_meses} meses] é: :red[ {
                total_por_cada_jogador_em_Real_formatado}].')
            st.write(
                f'A Probabilidade de Ganhar o Prêmio com :blue[{total_numeros_aposta} Dezenas] é de :blue[1] em :blue[{probabilidade_jogos_simples:,}].')
            st.write(f'Ao longo de :blue[{selecao_meses} meses] Você Concorrerá por: :violet[{
                     total_tentativas_meses}] Tentativas.')
            st.write(
                f'Com :violet[{total_tentativas_meses}] tentativas ao longo de :blue[{selecao_meses} meses], a probabilidade de ganhar é de :blue[1] em :blue[{int(probabilidade_meses):,}].')
            st.write(
                f'Ou seja, a probabilidade ajustada ao longo dos meses é de :blue[1] em :blue[{int(probabilidade_meses):,}].')
st.header('', divider='rainbow')

# DATAFRAMES EM COLUNAS:
col1, col2, col3 = st.columns(3)
with st.container():
    col1.subheader('Preço Por Apostas: ')
    col1.dataframe(df1)
    col2.subheader('Preço Por Teimosinha: ')
    col2.dataframe(df2)
    col3.subheader('Probabilidades: ')
    col3.dataframe(df3)

    # DATAFRAMES
    st.subheader(f'Dados Históricos dos Concursos da {nome_jogo}: ')
    st.dataframe(df4)

# ANÁLISE DAS DEZENAS MAIS SORTEADAS
# Contar a frequência das dezenas sorteadas
dezenas = df_quina.filter(regex='Bola').values.flatten()
frequencia_dezenas = pd.Series(dezenas).value_counts().reset_index()
frequencia_dezenas.columns = ['Dezenas', 'Frequência']
frequencia_dezenas = frequencia_dezenas.sort_values(
    by='Frequência', ascending=False)

# Exibir o dataframe com o ranking das dezenas mais sorteadas
st.subheader(f'Ranking das Dezenas Mais Sorteadas na {nome_jogo}')
st.dataframe(frequencia_dezenas)

# Criar gráfico interativo das dezenas mais sorteadas
fig = px.bar(frequencia_dezenas, x='Dezenas', y='Frequência',
             title=f'Dezenas Mais Sorteadas na {nome_jogo}')
st.plotly_chart(fig)

# Exibir as informações adicionais
st.header('', divider='rainbow')

with st.container():
    st.header('Tabela Controle de Pagamentos')
    st.dataframe(df_pagamento)

    total_pago_neste_jogo = np.sum(
        df_pagamento['VALOR PAGAMENTO'])
    total_pagamentos = df_pagamento['VALOR PAGAMENTO'].count()
    total_participantes = df_pagamento['NOME DO JOGADOR'].count()
    faltam_pagar = total_participantes - total_pagamentos

st.subheader(f'Cálculos de Pagamentos')

col4, col5 = st.columns(2)
with st.container():
    descontos = col4.number_input(
        'Descontar Valores Pagos para Completar os Jogos: ')
    saldos_anteriores = col4.number_input(
        'Digite o Valor que tem de Saldos Anteriores: ')
    saldos_anteriores_liquidos = (saldos_anteriores - descontos)

    total_pago = float(total_pago_neste_jogo + saldos_anteriores_liquidos)

    if total_pago_neste_jogo >= 1:
        st.write(f'Valor Total Já Pago Por PIX: :red[R$ {
                 total_pago_neste_jogo:.2f}.]')
        st.write(f'Descontos: Valores Pagos para Completar Jogos Anteriores: :red[R$ {
                 descontos:.2f}.]')
        st.write(f'Saldos Anteriores Bruto: :green[R$ {
                 saldos_anteriores:.2f}.]')
        st.write(f'Saldos Anteriores Líquido: :green[R$ {
                 saldos_anteriores_liquidos:.2f}.]')
        st.write(
            f'Valor Já Disponível Para Jogar: :green[R$ {total_pago:.2f}.]')
        st.write(f'Total Jogadores: :blue[{total_participantes}.]')
        st.write(f'Já pagaram: :green[{total_pagamentos}.]')
        st.write(f'Faltam Pagar: :red[{faltam_pagar}.]')

    st.header('', divider='rainbow')


with st.container():
    st.header(
        f'Relatório de Concursos Participados e Bolas Jogadas na {nome_jogo}')
    st.dataframe(df_bolas_jogadas)

    df_bolas_jogadas['VALOR GASTO NESTE JOGO'] = pd.to_numeric(
        df_bolas_jogadas['VALOR GASTO NESTE JOGO'], errors='coerce')

    total_valor_gasto_neste_jogo = np.sum(
        df_bolas_jogadas['VALOR GASTO NESTE JOGO'])

    df_bolas_jogadas['VALOR GANHO NESTE JOGO'] = pd.to_numeric(
        df_bolas_jogadas['VALOR GANHO NESTE JOGO'], errors='coerce')

    total_valor_ganho_neste_jogo = np.sum(
        df_bolas_jogadas['VALOR GANHO NESTE JOGO'])

    # Condicional para verificar se qualquer variável é maior ou igual a 1
    if total_valor_gasto_neste_jogo >= 1 or total_valor_ganho_neste_jogo >= 1:
        st.write(f'Valor Total Gastos Nesses Jogos: :red[R$ {
                 total_valor_gasto_neste_jogo:.2f}]')
        st.write(f'Valor Total Ganho Nesses Jogos: :green[R$ {
                 total_valor_ganho_neste_jogo:.2f}]')
    st.header('', divider='rainbow')


# INPUT PARA QUANTIDADE DE JOGOS A GERAR
quantidade_jogos_gerar = st.sidebar.number_input(
    'Digite a Quantidade de Jogos a Gerar (Máximo 300): ', min_value=1, max_value=300, value=1)

# INPUT PARA QUANTIDADE DE JOGOS A GERAR
if total_numeros_aposta == 5:
    lista_top_dezenas = range(6, 81)

elif total_numeros_aposta == 6:
    lista_top_dezenas = range(7, 81)

elif total_numeros_aposta == 7:
    lista_top_dezenas = range(8, 81)

elif total_numeros_aposta == 8:
    lista_top_dezenas = range(9, 81)

elif total_numeros_aposta == 9:
    lista_top_dezenas = range(10, 81)

elif total_numeros_aposta == 10:
    lista_top_dezenas = range(11, 81)

elif total_numeros_aposta == 11:
    lista_top_dezenas = range(12, 81)

elif total_numeros_aposta == 12:
    lista_top_dezenas = range(13, 81)

elif total_numeros_aposta == 13:
    lista_top_dezenas = range(14, 81)

elif total_numeros_aposta == 14:
    lista_top_dezenas = range(15, 81)

elif total_numeros_aposta == 15:
    lista_top_dezenas = range(16, 81)


selecao_top_dezenas = st.sidebar.selectbox(
    'Selecione a Quantidade de Dezenas Mais Sorteadas Deseja Filtrar: ', list(lista_top_dezenas))

# SELECIONANDO AS 20 DEZENAS MAIS SORTEADAS
top_dezenas = frequencia_dezenas.head(selecao_top_dezenas)['Dezenas'].tolist()

# GERANDO COMBINAÇÕES DE 15 DEZENAS
combinacoes_jogos = [random.sample(top_dezenas, total_numeros_aposta)
                     for _ in range(quantidade_jogos_gerar)]

# CRIANDO DATAFRAME COM AS COMBINAÇÕES GERADAS
df_combinacoes_jogos = pd.DataFrame(combinacoes_jogos, columns=[
                                    f'Dezena {i+1}' for i in range(total_numeros_aposta)])

if quantidade_jogos_gerar == 1:
    resultado_quantidade_jogos_gerar = 'Jogo Gerado'
else:
    resultado_quantidade_jogos_gerar = 'Jogos Gerados'

# EXIBINDO AS COMBINAÇÕES GERADAS
st.subheader(
    f'{quantidade_jogos_gerar} {resultado_quantidade_jogos_gerar} com {total_numeros_aposta} Dezenas das {selecao_top_dezenas} Mais Sorteadas')
st.dataframe(df_combinacoes_jogos)
