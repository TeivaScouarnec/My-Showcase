import os

ActualFolder = os.path.dirname(__file__)

print ("[Script] The actual folder is: " + str((ActualFolder).split("img")))

#Obtiens les images qui sont dans le fichier où se trouve le script
def GetFile():
    FilesInFolder = os.listdir(ActualFolder)
    Files = []
    print (("[Script] The files in folder is: ") + str(FilesInFolder))
    
    for a in FilesInFolder:
        if a.endswith((".png",".jpg")):
            Files.append(a)
    print (("[Script] The images founds is: ") + str(Files))
    
    return Files

#Ecris dans un fichier, les balises pour intégrer les élements
def WriteFile(folder):
    Resultat = "resultat.txt"
    PathFolder = (str(ActualFolder).split("img"))
    print(("[Script] The path of folder is: ") + str(PathFolder))
    YearPathFolder = (str(ActualFolder).split("illustrations\\"))
    f = open(str(ActualFolder) + "\\" + Resultat,"w")

    for i in folder:
        path = str(str("..\\img\\") + PathFolder[1] + '\\' + str(i)) 

        YearPath = YearPathFolder[1]
        f.write(("<a href=" + "'" + path + "'" + str(" data-lightbox=") + "'" + YearPath + "'" + str(" data-title=") + "'" + str(i) + "'" + str("> <img class= ") + "'" + str("illustrations") + "'" + str(" src=") + "'" + path + "'" + str(" alt=") + "'" + str(i) + "'" + str("></a>" + "\n")))

draws = GetFile()
WriteFile(draws)



