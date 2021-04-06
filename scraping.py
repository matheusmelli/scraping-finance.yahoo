from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import pandas as pd
import requests
import json
from selenium.webdriver.chrome.options import Options
from time import sleep

def scraping(region):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # activates widnow with below link  
    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    driver.get('https://ca.finance.yahoo.com/screener/new')
    sleep(10)

    # remove a opção dos Estados Unidos
    us_slection_xpath = '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]'
    driver.find_element_by_xpath(us_slection_xpath).click()
    sleep(5)

    # clica na opção de adicionar região
    add_region_xpath = '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li'
    driver.find_element_by_xpath(add_region_xpath).click()
    sleep(5)
    
    #Lista todos paises
    countries = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul')
    options = countries.find_elements_by_tag_name("li")
    sleep(5)

    i = 0
    for option in options:
        i += 1
        if option.text == region:
            break
  
    canada_box_xpath = '//*[@id="dropdown-menu"]/div/div[2]/ul/li['+str(i)+']/label/span'
    driver.find_element_by_xpath(canada_box_xpath).click()
    sleep(5)

    #click on search
    find_button_xpath = '//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]'
    driver.find_element_by_xpath(find_button_xpath).click()
    sleep(5)

    element = driver.find_element_by_xpath('//*[@id="scr-res-table"]')
    html_content = element.get_attribute('innerHTML')
    soup = BeautifulSoup(html_content,'html.parser')
    table = soup.find_all('div',class_='Ovx(a) Ovx(h)--print Ovy(h) W(100%)')

    df_full = pd.read_html(str(table))[0]
    df = df_full[['Symbol', 'Name', 'Price (Intraday)']]
    df.columns = ['symbol', 'name', 'price']

    dados = (df.to_dict('records'))
    symbol =[]

    for moedas in dados:
        arraySymbol= {}
        arraySymbol[moedas.get("symbol")] = moedas
        symbol.append(arraySymbol)

    with open('dados.json', 'w',encoding='utf-8') as json_file:
        js = json.dumps(symbol, indent=2)
        json_file.write(js)

    driver.quit()

    return symbol