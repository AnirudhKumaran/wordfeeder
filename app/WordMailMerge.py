from mailmerge import MailMerge
from pathlib import Path

class WordMailMerge:

    mm = None
    dest = str(Path.home() / "Downloads")+"\\"
    fileExtension = ".docx"

    def __init__(self,file):
        self.mm = MailMerge(file)

    def getFields(self):
        l = list(self.mm.get_merge_fields())
        l.sort()
        return l

    def createFile(self,d,fileName):
        outputFile = self.dest + fileName + self.fileExtension
        self.mm.merge(**d)
        self.mm.write(outputFile)