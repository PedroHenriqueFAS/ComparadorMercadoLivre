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

produtos_input = ['casaco masculino', 'iphone 16', 'camisa feminina', 'tenis masculino']

for produto_input in produtos_input:

    driver.get(LINK)
    time.sleep(1)
    barra_pesquisa = driver.find_element(By.ID, "cb1-edit")

    #produto_input = 'iphone 16' 
    #produto_input = input('Digite o produto que deseja pesquisar: ')

    barra_pesquisa.send_keys(produto_input)
    produto_input = produto_input.split() #split serve para separar as palavras 
    time.sleep(1)
    barra_pesquisa.send_keys(Keys.ENTER)
    time.sleep(2)

    produto_lista = driver.find_elements(
        By.CSS_SELECTOR, 'li[class="ui-search-layout__item"]')

    errado = False

    for produto in produto_lista:
        produto_pesquisado = produto
        produto_texto = produto.find_element(By.CSS_SELECTOR, 
                                            "div[class='poly-card__content']")

        produto_texto = produto_texto.find_element(By.CSS_SELECTOR, 
                                                'a[class="poly-component__title"]')
        titulo_produto = produto_texto.text
        
        for palavra in produto_input:
            if not palavra.lower() in titulo_produto.lower():
                errado = True
        
        if errado == True:
            errado = False
            continue
        break

    preco = produto_pesquisado.find_element(By.CSS_SELECTOR, 
                                            'span[class="andes-money-amount__fraction"]').text

    with open('produtos.txt', 'a+') as file:
        file.write(f'Produto: {titulo_produto}-Preco:{preco}\n')
    #print(produto_pesquisado.text)
    print(titulo_produto, preco)
        

input('Pressione Enter para finalizar')