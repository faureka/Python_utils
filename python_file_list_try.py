import os
import shutil
dstdir = 'C:/Users/stifler/Documents/NOKIA_FINAL_BACKUP/IMAGES'
list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk('.'):
    for filename in filenames:
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"): 
            shutil.copy(os.sep.join([dirpath, filename]),dstdir)
