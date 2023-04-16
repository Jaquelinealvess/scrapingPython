from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoespera
from openpyxl import load_workbook
import os

#pegamos o caminho do aquivo no computadorr 
nome_arquivo_tabela = "C:\\Users\C2543679\Downloads\Projetos python\scraping\DadosTabela.xlsx"
planilhaDadosTabela = load_workbook(nome_arquivo_tabela)
#selecionaando a sheet de dados
sheet_selecionada = planilhaDadosTabela['Dados']

#abre o navegador da web do google Chrome
navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallengeocr.azurewebsites.net/")

#copia o xpath da tabela
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

#pega linhas e colunas da tabela
linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

linha = 1
i = 1
#enquanto o i for menor do que 4
while i < 4:

    #selecionaando a sheet de dados
    sheet_dados = planilhaDadosTabela['Dados']

    #copia o xpath da tabela
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    #pega linhas e colunas da tabela
    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementoTabela.find_elements(By.TAG_NAME, "td")
# para cada 
    for linhaAtual in linhas:
        #print(linhaAtual.text)
        #pegando a ultima linha + 1
        linha = linha + 1
        #definindo o nome da coluna + o numero da linha
        linha = len(sheet_dados['A'])+ 1
        colunaA = "A" + str(linha) #A1
        colunaB = "B" + str(linha) #B1
        colunaC = "C" + str(linha) #C1

        #pegando o texto da linha
        texto = linhaAtual.text
        #separamos com o split todas as palavras com espaço entre textos
        texto2 = texto.split(" ")
        #imprimimos os dados da tabela no excel
        sheet_dados[colunaA] = texto2[0]
        sheet_dados[colunaB] = texto2[1]
        sheet_dados[colunaC] = texto2[2]

    i +=1
    #aguarda 2 segundos para o computador ou site processar
    tempoespera.sleep(2)
    #encontra o xpath do botao next e clica
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    #aguarda 2 segundos para o computador ou site processar
    tempoespera.sleep(2)
else:
    print("pronto")

#salva o arquivo com alterações
planilhaDadosTabela.save(filename=nome_arquivo_tabela)
#abre o arquivo
os.startfile(nome_arquivo_tabela)
        

