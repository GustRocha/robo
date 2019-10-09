from selenium import webdriver #para abrir o navegador e controlar 
from selenium.webdriver.common.keys import Keys # para controlar as teclas
import time
import xlrd #biblioteca para ler o excel

print("Iniciado o processo ...\n")
workbook = xlrd.open_workbook('dominio.xlsx')



driver = webdriver.Chrome('/home/gustavo/Desktop/Robos/chromedriver')# a onde esta salvo o drive do chrome
driver.get("https://registro.br/") 


dominio = ["facebook.com.br","dafiti.com.br","lol.com.br"] # lista de paginas para entrar
for dominio in dominio: 

    pesquisa =driver.find_element_by_id("is-avail-field") # Seleciona o campo de busca baseado no id
    pesquisa.clear() #limpa o campo de busca
    pesquisa.send_keys(dominio)#inser no campo
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(3)
    resultados = driver.find_elements_by_tag_name("strong")# localiza os elementos em "strong" negrito
    print("dominio %s %s" % (dominio, resultados[4].text))# imprime o resultado do negrito na lista 4  

driver.close()