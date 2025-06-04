import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
path = os.getcwd() + '/chromedriver.exe'

options = webdriver.ChromeOptions()

service = Service(executable_path = path)

driver = webdriver.Chrome(options=options, service=service)

LINK = "https://www.mercadolivre.com.br/" 

driver.get(LINK)
time.sleep(1)
barra_pesquisa = driver.find_element(By.ID, "cb1-edit")

produto_input = input('Digite o produto que deseja pesquisar: ')

barra_pesquisa.send_keys(produto_input)
time.sleep(1)
barra_pesquisa.send_keys(Keys.ENTER)
time.sleep(2)

produto = driver.find_element(
    By.CSS_SELECTOR, 'li[class="ui-search-layout__item"]')
print(produto.text)

input('Pressione Enter para finalizar')