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
