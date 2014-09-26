import shutil
import os
source = os.listdir(".")
destination = "C:/Users/stifler/Documents/NOKIA_FINAL_BACKUP/IMAGES"
for files in source:
    if files.endswith(".jpg") or files.endswith(".png") or files.endswith(".gif"): 
        shutil.copy(files,destination)
