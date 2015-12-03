from sys import argv

script, inputFile = argv

def printAll(f):
    print f.read()

def rewind(f):
    f.seek(0)
    
def printALine(lineCount, f):
    print lineCount, f.readline()

currentFile = open(inputFile)

print "First lets pring the whole file:\n"

printAll(currentFile)

print "Now let's rewind, kind of like a tape:\n"

rewind(currentFile)

print "Let's print three lines"

currentLine=1
printALine(currentLine, currentFile)

currentLine+=1
printALine(currentLine, currentFile)

currentLine=1
printALine(currentLine, currentFile)
