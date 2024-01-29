import requests
from bs4 import BeautifulSoup

def web_scraping():
    url = "https://g1.globo.com/economia/noticia/2024/01/29/salario-minimo-com-valor-reajustado-passa-a-ser-pago-a-partir-desta-semana.ghtml"  # Insira o URL desejado

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Exemplo de extração de informações
    titulo = soup.find("h1").text
    paragrafos = soup.find_all("p")

    print("Título:", titulo)
    print("Parágrafos:")
    for paragrafo in paragrafos:
        print("-", paragrafo.text)

web_scraping()