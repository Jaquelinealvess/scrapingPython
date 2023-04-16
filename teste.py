from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicialize o driver do Selenium
driver = webdriver.Chrome()

# Navegue até a página do iPhone 14 Pro
driver.get("https://www.apple.com/br/iphone-14-pro/")

# Aguarde até que o preço seja carregado na página
preco_elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='current_price-value']"))
)

# Obtenha o valor do preço
preco = preco_elemento.text

# Imprima o valor do preço
print(preco)

# Feche o navegador
driver.quit()