import requests
from bs4 import BeautifulSoup

# Función para obtener URLs de un sitemap
def get_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, 'xml')
    urls = [loc.text for loc in soup.find_all('loc')]
    return urls

# Archivo donde guardaremos las URLs de las páginas
output_file = "urls_from_pages_sitemap.txt"

# Sitemap de las páginas estáticas
sitemap_url = "https://xnet-x.net/page-sitemap.xml"

# Extraer todas las URLs de las páginas y guardarlas en el archivo
with open(output_file, 'w') as f:
    print(f"Extrayendo URLs del sitemap de páginas: {sitemap_url}")
    urls = get_sitemap_urls(sitemap_url)
    for url in urls:
        f.write(url + "\n")

print(f"Todas las URLs de las páginas estáticas se han guardado en {output_file}.")
