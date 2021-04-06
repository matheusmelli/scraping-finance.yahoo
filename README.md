# Scraping-finance.yahoo

## O que é o Scraping-finance.yahoo?
  O scraping-finance.yahoo é uma ferramenta que permite a busca de dados do mercado financeiro do Estados Unidos, listando todas as ações do mercado.  

## Ferramentas utilizadas
- Python=3.9.4
- beautifulsoup4 =4.9.3
- bs4=0.0.1
- Flask=1.1.2
- html5lib=1.1
- selenium=3.141.0
- requests=2 2.16.0
- pandas=1.2.3
- Flask-Caching=1.10.1
- lxml=4.6.3
- Docker=20.10.5,

## Como utilizar
- Clonar o projeto para sua maquina
- Instalar o Docker em seu sistema operacional(Linux,Windows,Mac)
- Acessar a pasta onde esta o Dockerfile

## Comandos para executar a aplicação dentro do container
- docker build -t <**nome da imagem**> -f Dockerfile .
 (Exemplo: docker build -t scraping -f Dockerfile .)
- docker run -it -p 5000:5000 <**nome da imagem**> bash
- python routes.py
- abrir o link [http://localhost:5000/stocks](http://localhost:5000/stocks)

## Comandos para executar a aplicação fora do container
- docker build -t <**nome da imagem**> -f Dockerfile .
  (Exemplo: docker build -t scraping -f Dockerfile .)
- docker run -d -p 5000:5000 <**nome da imagem**>
- abrir o link [http://localhost:5000/stocks](http://localhost:5000/stocks)
