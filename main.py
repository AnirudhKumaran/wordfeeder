import eel
import sys
sys.path.append('./app')
from LoadFileDialog import LoadFileDialog
from WordMailMerge import WordMailMerge

def main():
    eel.init('web')
    eel.start('templates/index.html', jinja_templates='templates',size=(400,800),geometry={'size':(400,800)})

@eel.expose
def generateWordFile(fileName,d,outputFile):
    wmm = WordMailMerge(fileName)
    return wmm.createFile(d,outputFile)

@eel.expose
def processWordFile(fileName):
    wmm = WordMailMerge(fileName)
    return wmm.getFields()

@eel.expose
def getWordFile():
    lfd = LoadFileDialog()
    v = lfd.selectedFile
    del lfd
    return v

if __name__=="__main__":
    main()
