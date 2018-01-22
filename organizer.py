import shutil,os,glob

#intro
print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|\n___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
print("                         FILE ORGANIZER                              ")
print("                                                         ~By Ashish  ")
print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|\n___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
os.system("pause")

# Copying Files
def copy(newpath,file):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    shutil.copy(file, newpath)
    os.remove(file)
# Creating Folders
def folder(extension,fname):
    lists=glob.glob(extension)
    # print(lists)
    for name in lists:
        if name=="organizer.py":
            print(name)
            continue
        copy(fname,name)

#Sorting Files

folder("*.py","Python Scripts")
folder("*.java","Java Codes")
folder("*.c","C Codes")
folder("*.html","HTML")
folder("*.cpp","C++ Files")
folder("*.mp3","Music")
folder("*.mp4","Videos")
folder("*.txt","Documents/Text Files")
folder("*.docx","Documents/Word Files")
folder("*.xlsx","Documents/Excel Sheets")
folder("*.pptx","Documents/PowerPoint Presentations")
folder("*.pdf","Documents/PDF Files")
images=["*.jp*","*.png","*.psd","*.bmp"]
for img in images:
    folder(img,"Images")



# for filename in glob.glob("*.*"):
#     os.rename(filename, filename.replace(" ", ""))
#     os.rename(filename, filename.replace("_", ""))
#     os.rename(filename, filename.replace("-", ""))
