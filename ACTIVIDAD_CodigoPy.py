print ("Hola pibes")

print ("puto el que lee")


import os
import shutil
from datetime import datetime

# source_file --> ruta al archivo que queres backupear
# backup_dir --> ruta a la carpeta donde se van a guardar los backups

source_file =  'C:/Users/Iruiv/OneDrive/Escritorio/UADE/tercer año/segundo cuatri/ing de software/prueba.py'  # Cambia esta ruta por la de tu archivo
backup_dir = 'C:/Users/Iruiv/OneDrive/Escritorio/UADE/tercer año/segundo cuatri/ing de software/backups/'

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = os.path.join(backup_dir, f"backup_{timestamp}.txt")

shutil.copy2(source_file, backup_file)

print(f"Backup realizado: {backup_file}")