# unif
Unificador de Archivos de Video y Audio m3u8

Al descargar videos con algunas extensiones de google se llega a descargar en audio y video entonces
Este proyecto es un script de Python que automatiza
la tarea de unificar archivos de video y audio separados en un solo archivo,
Aunque los nombres de los archivos de ejemplo contienen [audio_0_1.m3u8] y [video_1.m3u8]
el script está diseñado para trabajar con cualquier formato de archivo que sea compatible con la biblioteca moviepy,
incluyendo .mp4, .mkv, .avi, .mov, .flv, y muchos más.

El script busca archivos de video y audio que tengan el mismo nombre 

Instalación
Para instalar las dependencias necesarias para ejecutar este script, puedes usar el siguiente comando:

pip install -r requirements.txt

Uso
Para usar este script, simplemente ejecútalo con Python:
*

python unif.py C:\ruta\a\tus\archivos C:\ruta\a\tus\archivos\unq		#1 la ruta donde estan los videos a unifica
															#2 la ruta donde lo guardaras


*

Asegúrate de modificar la variable directorio en el script para que apunte al directorio donde se encuentran tus archivos de video y audio.
