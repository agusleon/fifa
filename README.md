# fifa

Holis! Este es el codigo para levantar reportes de la API publica de FIFA. Por ahora vas a poder levantar unicamente informacion sobre la FIFA Worldcup 2014. 

Las librerias que se usan son las siguientes:
- requests: libreria para hacer la request GET a la API
- pandas: libreria que ayuda a pasar de json a dataframe y hacer la transformacion que quieras
- gc: garbage colector si no se pudo hacer la request
- sys: usada para hacer un exit y no siga corriendo el programa

Para correr el programa tenes que:
1. Descargarte python
2. Agregar python a las variables de entorno de tu PC:
 - Busca la ruta donde descargaste python, copiala.
 - Anda a tus variables de entorno y en la variable PATH, pone add path y pega la ruta
 - Guarda
4. Descargarte las librerias de la siguiente forma en la terminal:
 - pip install libreria
5. Si no tenes descargado pip (muy probablemente):
 - Descargate el archivo get-pip.py de internet
 - Guardalo en la misma ruta donde te descargaste Python
 - En la terminal anda a esa ruta
 - Ejecuta el comando python get-pip.py
 - Fijate que se haya instalado bien haciendo en la terminal pip -v o --version
 - Volve al paso 2.

Si llegaste hasta acá, esto no lo tenes que volver a hacer jaja, es para setear el entorno de python. Para finalmente ejecutar el programa:

6. Desde la terminal parandote en la carpeta que tiene el archivo etl.py, ejecuta: python etl.py

Voilá!
