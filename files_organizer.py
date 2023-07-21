import os
import shutil


current_directory = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_directory):

    print("Start Orgnizing Files in Your Download Folder!")

    if filename.endswith(".png","jpg","jpeg","gif"):

        if not os.path.exists("Images"):

            os.mkdir("Images")
        
        shutil.copy(filename, "Images")

        os.remove(filename)

    
    if filename.endswith(".doc","docx","xlsx","pdf","pptx"):

        if not os.path.exists("Docs"):

            os.mkdir("Docs")
        
        shutil.copy(filename, "Docs")

        os.remove(filename)

    
    if filename.endswith(".zip","rar"):

        if not os.path.exists("Archive"):

            os.mkdir("Archive")
        
        shutil.copy(filename, "Archive")

        os.remove(filename)


    if filename.endswith(".mp4","mkv","mov","avi"):

        if not os.path.exists("Videos"):

            os.mkdir("Videos")
        
        shutil.copy(filename, "Videos")

        os.remove(filename)


    if filename.endswith(".mp3","wav"):

        if not os.path.exists("Sounds"):

            os.mkdir("Sounds")
        
        shutil.copy(filename, "Sounds")

        os.remove(filename)

    
    if filename.endswith(".iso","img"):

        if not os.path.exists("ISO"):

            os.mkdir("ISO")
        
        shutil.copy(filename, "ISO")

        os.remove(filename)


print("Orgnizing files have been Done!")





