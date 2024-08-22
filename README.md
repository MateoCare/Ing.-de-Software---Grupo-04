# Ing.-de-Software---Grupo-04

## Script para hacer backups locales

librerias utilizadas: os, shutil, datetime

source_file: contiene la ruta del archivo al que le queremos hacer backup
backup_dir: contiene la ruta de la carpeta donde se van a guardar las copias

si la carpeta/ruta no existe la crea

timestamp: toma la fecha actual (año,mes,dia hora,minutos,segundos)

backup_file: crea un archivo txt con la fecha actual en la carpeta asignada 

shutil.copy2 copia el contenido del archivo original y lo guarda en una copia en la carpeta de backups