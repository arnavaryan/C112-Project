import os
import shutil

source= "C:/Users/malho_9yypg6y/Downloads"
dest="C:/Users/malho_9yypg6y/Desktop/Document_Files"

list_of_files=os.listdir(source)
#print(list_of_files)

for file_name in list_of_files:
    name,ext=os.path.splitext(file_name)
    
    if ext=="":
        continue
    
    if ext in [".txt", ".pdf", ".doc", ".docx"]:
        path1= source + "/" + file_name
        path2= dest
        path3= dest + "/" + file_name

        if os.path.exists(path2):
            print("Moving")

            shutil.move(path1,path3)

        