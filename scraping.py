from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import json
from selenium.webdriver.chrome.options import Options

def scraping(region):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome("./chromedriver",chrome_options=chrome_options)
    driver.get("https://finance.yahoo.com/screener/unsaved/31ee4cb9-6feb-4c4f-959f-b0c2f9082e85")
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