import os
import sys
from moviepy.editor import VideoFileClip, AudioFileClip

# Comprueba que se han proporcionado los argumentos correctos
if len(sys.argv) != 3:
    print("Uso: python unificar.py directorio_entrada directorio_salida")
    sys.exit(1)

# Directorio donde se encuentran los archivos
directorio = sys.argv[1]

# Directorio donde se guardarán los videos unificados
directorio_salida = sys.argv[2]

# Crea el directorio de salida si no existe
os.makedirs(directorio_salida, exist_ok=True)

# Obtén una lista de todos los archivos en el directorio
archivos = os.listdir(directorio)

# Agrupa los archivos por nombre base (sin extensión)
archivos_agrupados = {}
for archivo in archivos:
    nombre_base = archivo.split('[')[0]  # Obtiene el nombre base antes del corchete
    if nombre_base not in archivos_agrupados:
        archivos_agrupados[nombre_base] = []
    archivos_agrupados[nombre_base].append(archivo)

# Procesa cada grupo de archivos
for nombre_base, grupo in archivos_agrupados.items():
    # Asegúrate de que hay un archivo de video y uno de audio
    if len(grupo) != 2:
        continue

    # Identifica cuál archivo es el video y cuál es el audio
    archivos_video = [archivo for archivo in grupo if 'video' in archivo]
    archivos_audio = [archivo for archivo in grupo if 'audio' in archivo]

    if archivos_video and archivos_audio:
        archivo_video = archivos_video[0]
        archivo_audio = archivos_audio[0]
    else:
        print(f"No se encontró un par de archivos de audio y video para {nombre_base}")
        continue

    # Crea los clips de video y audio
    clip_de_video = VideoFileClip(os.path.join(directorio, archivo_video))
    clip_de_audio = AudioFileClip(os.path.join(directorio, archivo_audio))

    # Combina los clips de video y audio
    video_final = clip_de_video.set_audio(clip_de_audio)

    # Guarda el video final en el directorio de salida
    video_final.write_videofile(os.path.join(directorio_salida, nombre_base + '_final.mp4'))
