import urllib.request
import os
from bs4 import BeautifulSoup

# URL do diretório que contém os arquivos a serem baixados
url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'

# Diretório de destino para salvar os arquivos baixados
dest_dir = 'C:\\Users\\conta\\OneDrive\\Área de Trabalho\\teste'

# Verificar se o diretório de destino existe. Se não, criar.
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Obter a página HTML do diretório
html = urllib.request.urlopen(url).read()

# Analisar a página HTML com o BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar todos os links de download na página HTML
links = soup.find_all('a')

# Loop pelos links de download
for link in links:
    href = link.get('href')
    # Verificar se o link é um arquivo zip e baixá-lo se for
    if href.endswith('.zip'):
        file_url = url + href
        filename = os.path.join(dest_dir, href)
        urllib.request.urlretrieve(file_url, filename)