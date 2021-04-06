#Imagem do Python
FROM python

#Cria a pasta app na raiz do projeto
WORKDIR /app

#Copia o requirements.txt para dentro do container
COPY requirements.txt requirements.txt 
#Instala todas as bibliotecas do requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt \
#Baixa a chave de instalação do google
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#Executa script de shell acima 
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
#Atualiza o apt-get
&& apt-get -y update \
#Instala o Chrome
&& apt-get install -y google-chrome-stable \
#Instala o programa para extrair um zip
&& apt-get install -yqq unzip \
#Baixa o driver do chrome(chromedriver)
&& wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
#Descompacta o arquivo chromedriver
&& unzip /tmp/chromedriver.zip chromedriver -d /app 

#Copia tudo dentro da pasta para a pasta app
COPY . .

#Executa o python3,flask e seta o HOST
CMD ["python3","routes.py", "-m" , "flask", "run", "--host=0.0.0.0"]
