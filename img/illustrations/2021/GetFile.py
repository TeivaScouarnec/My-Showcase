import os

ActualFolder = os.getcwd()

print (str(ActualFolder).split("img"))

def GetFile():
    FilesInFolder = os.listdir()
    Files = []
    print (FilesInFolder)
    for a in FilesInFolder:
        if a.endswith((".png",".jpg")):
            Files.append(a)
    print (Files)
    return Files

def WriteFile(folder):
    Resultat = "resultat.txt"
    Folder = os.listdir()
    PathFolder = (str(ActualFolder).split("img"))
    print(PathFolder)
    YearPathFolder = (str(ActualFolder).split("illustrations\\"))
    f = open(Resultat,"w")

    for i in folder:
        path = str(str("..\\img\\") + PathFolder[1] + '\\' + str(i)) 
        print (path)

        YearPath = YearPathFolder[1]
        f.write(("<a href=" + "'" + path + "'" + str(" data-lightbox=") + "'" + YearPath + "'" + str(" data-title=") + "'" + str(i) + "'" + str("> <img class= ") + "'" + str("illustrations") + "'" + str(" src=") + "'" + path + "'" + str(" alt=") + "'" + str(i) + "'" + str("></a>" + "\n")))

draws = GetFile()
WriteFile(draws)



