# Extraer Enlaces Salientes de un Sitio

Este repositorio contiene scripts en Python para extraer enlaces salientes de un sitio web utilizando el sitemap de las páginas estáticas. También se incluye una guía para procesar y limpiar los datos en LibreOffice Calc.

## Requisitos

1. **Python 3.x**
2. Instalar dependencias con el siguiente comando:

   ```bash
   pip install -r requirements.txt
   ```

## Instrucciones

### 1. Extraer URLs de las Páginas Estáticas

El archivo `scripts/extraer_urls_paginas.py` extrae todas las URLs de las páginas estáticas desde un sitemap XML.

#### Uso:

```bash
python3 scripts/extraer_urls_paginas.py
```

Las URLs se guardarán en el archivo `urls_from_pages_sitemap.txt`.

### 2. Extraer Enlaces Externos de las Páginas

El archivo `scripts/extraer_enlaces_sitio.py` toma el archivo de URLs de páginas estáticas y extrae los enlaces salientes de cada una.

#### Uso:

```bash
python3 scripts/extraer_enlaces_sitio.py



```

Los enlaces extraídos se guardarán en el archivo `external_links_pages.txt`.

### 3. Limpieza de Enlaces en LibreOffice Calc

Consulta la documentación en `docs/libreoffice_instructions.md` para instrucciones detalladas sobre cómo limpiar y procesar las URLs en LibreOffice Calc.






¡Perfecto! Ahora crearé el resumen y los scripts organizados en carpetas para que puedas subirlo a **GitHub**. A continuación te doy un esquema del repositorio con las instrucciones incluidas.

### 1. Nombre del repositorio:

**"extraer-enlaces-salientes-sitio"**

### 2. Estructura del repositorio:

```bash
extraer-enlaces-salientes-sitio/
│
├── LICENSE
├── README.md
├── scripts/
│   ├── extraer_urls_paginas.py        # Script para extraer URLs de páginas estáticas del sitemap
│   ├── extraer_enlaces_sitio.py       # Script para extraer los enlaces externos de cada página
├── docs/
│   └── libreoffice_instructions.md    # Instrucciones para limpiar URLs en LibreOffice Calc
└── requirements.txt                   # Archivo de dependencias de Python
```

### 3. Contenido del README:

```markdown
# Extraer Enlaces Salientes de un Sitio

Este repositorio contiene scripts en Python para extraer enlaces salientes de un sitio web utilizando el sitemap de las páginas estáticas. También se incluye una guía para procesar y limpiar los datos en LibreOffice Calc.

## Requisitos

1. **Python 3.x**
2. Instalar dependencias con el siguiente comando:

   ```bash
   pip install -r requirements.txt
   ```

## Instrucciones

### 1. Extraer URLs de las Páginas Estáticas

El archivo `scripts/extraer_urls_paginas.py` extrae todas las URLs de las páginas estáticas desde un sitemap XML.

#### Uso:

```bash
python3 scripts/extraer_urls_paginas.py
```

Las URLs se guardarán en el archivo `urls_from_pages_sitemap.txt`.

### 2. Extraer Enlaces Externos de las Páginas

El archivo `scripts/extraer_enlaces_sitio.py` toma el archivo de URLs de páginas estáticas y extrae los enlaces salientes de cada una.

#### Uso:

```bash
python3 scripts/extraer_enlaces_sitio.py
```

Los enlaces extraídos se guardarán en el archivo `external_links_pages.txt`.

### 3. Limpieza de Enlaces en LibreOffice Calc

Consulta la documentación en `docs/libreoffice_instructions.md` para instrucciones detalladas sobre cómo limpiar y procesar las URLs en LibreOffice Calc.
```

### 4. Contenido del `requirements.txt`:

```txt
requests
beautifulsoup4
```

### 5. Contenido de los scripts:

#### `extraer_urls_paginas.py` (extraer URLs de páginas estáticas del sitemap):

```python
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
```

#### `extraer_enlaces_sitio.py` (extraer enlaces externos de cada página):

```python
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
```

### 6. Instrucciones para **LibreOffice Calc** (`docs/libreoffice_instructions.md`):

```markdown
# Instrucciones para limpiar y procesar URLs en LibreOffice Calc

Si tienes un archivo con una estructura donde cada fila tiene dos enlaces separados por `->`, puedes seguir los pasos a continuación para extraer solo el segundo enlace usando **LibreOffice Calc**.

## Paso 1: Abrir tu archivo en LibreOffice Calc

Abre el archivo que contiene las URLs en LibreOffice Calc.

## Paso 2: Insertar la fórmula

1. **Selecciona la columna donde tienes las URLs**.
2. **Crea una nueva columna** junto a la original.
3. En la nueva columna, usa la siguiente fórmula en la celda correspondiente (suponiendo que el texto esté en la celda A1):

   ```excel
   =EXTRAE(A1;HALLAR("-> ";A1)+3;LARGO(A1))
   ```

Esta fórmula extraerá el texto que viene después de `"-> "` y eliminará el primer enlace.

## Paso 3: Arrastrar la fórmula

Arrastra la fórmula hacia abajo para aplicarla a todas las filas que contienen URLs.

¡Listo! Ahora tendrás solo los enlaces que vienen después de `"-> "`.
```

---

### Próximos pasos:

1. **Crea un repositorio en GitHub** con el nombre **"extraer-enlaces-salientes-sitio"**.
2. **Sube todos los archivos** proporcionados en la estructura.
3. **Agrega la licencia Creative Commons**.

Si tienes alguna duda sobre cómo proceder o necesitas ajustes adicionales, no dudes en decírmelo. ¡Estoy aquí para ayudarte!
