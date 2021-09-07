from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pymongo import MongoClient

client = MongoClient('localhost')
db = client['prueba']
col = db['olx']
driver = webdriver.Firefox()

driver.get('https://www.olx.com.ec/computadoras-laptops_c803')

for i in range(4):

    link_productos = driver.find_elements(By.XPATH, '//a[@class="fhlkh"]')
    links_paginas = []

    for a_link in link_productos:
        links_paginas.append(a_link.get_attribute("href"))

    for link in links_paginas:
        try:
            driver.get(link)
            titulo = driver.find_element(By.XPATH, '//h1').text
            print(titulo)
            driver.back()
        except Exception as e:
            print(e)
            driver.back()
    try:
        boton = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        )

        boton.click()


        WebDriverWait(driver, 10).until(
          EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))
        )

    except Exception as e:
        print (e)
        break

driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
sleep(5)
driver.execute_script("window.scrollTo({top: 20000, behavior: 'smooth'});")
sleep(5)

autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')


for auto in autos:
    try:
      precio = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    except:
      precio = 'NO DISPONIBLE'
    descripcion = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text

    col.insert_one({
        'precio': precio,
        'descripcion': descripcion
    })