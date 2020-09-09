import os
import shutil
import hashlib
import glob

class File:

    def __init__(self, filePath):
        self.exist = os.path.isfile(filePath)
        if not self.exist: return 

        info = os.stat(filePath)
        self.path = filePath        
        self.size = info.st_size
        self.modifyTime = info.st_mtime

        sha512 = hashlib.sha512()
        with open(filePath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha512.update(chunk)

        self.sha512 = sha512.hexdigest()

def SyncFile(srcFile,dstFile): 

    if not isinstance(srcFile,File): return False
    if not isinstance(dstFile,File): return False

    if not srcFile.exist: return False
    if not dstFile.exist: return False

    os.remove(dstFile.path) #usuwa stary plik
    shutil.copyfile(srcFile.path,dstFile.path) #kopiuje w jego miejsce nowy

    return True

def GetFilePathList(dirPath): #wraz z podfolderami
 
    listOfFile = os.listdir(dirPath)
    allFiles = []
    for x in listOfFile:
        fullPath = os.path.join(dirPath, x) 
        if os.path.isdir(fullPath):
            allFiles = allFiles + GetFilePathList(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles
