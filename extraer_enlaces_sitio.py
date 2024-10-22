import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Función para obtener enlaces externos de una página
def get_external_links(url, base_domain):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        external_links = []

        for link in links:
            href = link['href']
            href = urljoin(url, href)  # Convertir enlaces relativos a absolutos
            parsed_url = urlparse(href)
            # Comprobar si es un enlace externo
            if parsed_url.netloc and parsed_url.netloc != base_domain:
                external_links.append(href)

        return external_links
    except Exception as e:
        print(f"Error procesando {url}: {e}")
        return []

# Leer URLs desde el archivo
def read_urls_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Guardar los enlaces externos en un archivo
def save_external_links(output_file, url, external_links):
    with open(output_file, 'a') as f:
        for link in external_links:
            f.write(f"{url} -> {link}\n")

# Archivo que contiene las URLs del sitemap de páginas estáticas
input_file = "urls_from_pages_sitemap.txt"
# Archivo donde se guardarán los enlaces externos de las páginas estáticas
output_file = "external_links_pages.txt"

# Leer todas las URLs del archivo de páginas estáticas
urls = read_urls_from_file(input_file)

# Procesar todas las URLs sin límite
for url in urls:
    print(f"Visitando: {url}")
    base_domain = urlparse(url).netloc  # Dominio base de la URL
    external_links = get_external_links(url, base_domain)  # Extraer los enlaces externos
    save_external_links(output_file, url, external_links)  # Guardar en el archivo

print(f"Extracción completa. Se han procesado {len(urls)} URLs.")
