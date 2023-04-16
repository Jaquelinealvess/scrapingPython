from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoespera
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
import os

#pegamos o caminho do aquivo no computadorr 
nome_arquivo_tabela = "C:\\Users\C2543679\Downloads\Projetos python\scraping\DadosTabela.xlsx"
planilhaDadosTabela = load_workbook(nome_arquivo_tabela)
#selecionaando a sheet de dados
sheet_selecionada = planilhaDadosTabela['Dados']

#abre o navegador da web do google Chrome
driver = opcoesSelenium.Chrome()
#options.add_argument('--disable-gpu')
driver.get("https://www.apple.com/br/iphone-14-pro/")
tempoespera.sleep(3)
# Aguarde até que o preço seja carregado na página
preco_elemento = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/section[2]/div/p[1]/span[1]")
# Obtenha o valor do preço
preco = preco_elemento.text

# Imprima o valor do preço
print(preco)

driver.quit()