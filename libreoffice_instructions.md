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
