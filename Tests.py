import threading

from SimpleFileSyncCore.Files import *
from SimpleFileSyncCore.alive_progress import alive_bar


SRC_fileList = []
DST_fileList = []



SRCInput = input("Folder źródłowy:")
DSTInput = input("Folder docelowy:")

if not os.path.exists(SRCInput) or not os.path.exists(DSTInput):
    print("Błąd: Nieprawidłowa ścieżka")
    quit()

SRCfilePaths = GetFilePathList(SRCInput)
DSTfilePaths = GetFilePathList(DSTInput)

print("Obliczam hashe")

with alive_bar(len(SRCfilePaths)+len(DSTfilePaths)) as bar:

    for x in SRCfilePaths:
        SRC_fileList.append(File(x))
        bar()

    for x in DSTfilePaths:
        DST_fileList.append(File(x))
        bar()










