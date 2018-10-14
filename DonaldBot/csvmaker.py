# CSV maker module
import os

def csvmaker(csvname, headers):
    global csvfilepath

    cwd = os.getcwd()
    csvfilepath= cwd+ '\\' + csvname
    print(csvname)
    if not os.path.isfile(csvname):#creates a csv with headers if doesn't exist in current directory
        f = open(csvname,"w")
        f.write(headers)
        print('File Created')
    else:
        print("file already made")




def archive(archivename):
    global archivefilepath
    cwd = os.getcwd()
    archivefilepath = cwd+ '\\' + archivename

    if not os.path.isfile(archivename):
        posts_collected = []
        p = open(archivename, 'w')
        p.write("archive for "+ str(archivename) + "\n")
        print('archive made')

    else:
        with open (archivename, "r") as p:
            posts_collected = p.read()
            posts_collected = posts_collected.split("\n")
            posts_collected = list(filter(None, posts_collected))
        print('archive already made')
