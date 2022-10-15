# ---------- IMPORTS ---------- #

from antlr4 import *
from jsbachLexer import jsbachLexer
from jsbachParser import jsbachParser
from TreeVisitor import TreeVisitor

import sys
import os
import subprocess

# ---------- .LILY PROGRAM FUNCTIONS ---------- #

def lilyProgram(tempo, notes):
    return """\\version "2.22.1"
\\score {
    \\absolute {
        \\tempo 4 = %i
        %s
    }
    \\layout { }
    \\midi { }
}""" % (tempo, notesToString(notes))


def notesToString(notes):
    r = ""
    for note in notes:
        r += LilyNote(note)
    return r


def LilyNote(note):
    baseValue2Note = {
        -9: 'c',
        -7: 'd',
        -5: 'e',
        -4: 'f',
        -2: 'g',
        0:  'a',
        2:  'b'
    }

    alter = ""

    noteNumber = ((note+9) % 12)-9

    if not noteNumber in baseValue2Note:
        noteNumber -= 1
        alter = "is"
    realNote = baseValue2Note[noteNumber]
    octave = int((note-noteNumber)/12)

    result = realNote + alter

    for i in range(octave, 4-1, +1):
        result += ","

    for i in range(octave, 4-1, -1):
        result += "'"

    return result + " "

# ---------- VARIABLES/CONSTANTS ---------- #

tempo = 100
notes = []

fileName = "default"
outputDirecotry = "JSB"

# ---------- INPUT ---------- #

print("===== PROCESSING INPUT =====")
inputFile = sys.argv[1]

fileName = inputFile.rpartition('.')[0].rpartition('/')[-1]
outputDirecotry = "JSB" + fileName

input_stream = FileStream(inputFile, encoding="utf-8")  # .jsb input file
main = sys.argv[2] if len(sys.argv) == 3 else "Main"  # main program to execute

# ---------- CREATE OUTPUT DIRECTORY ---------- #

print("===== GENERATING OUTPUT DIRECTORY =====")
if not os.path.isdir(outputDirecotry):
    os.system("mkdir " + outputDirecotry)
else:
    i = 2
    while os.path.isdir(outputDirecotry + str(i)):
        i += 1
    outputDirecotry += str(i)
    os.system("mkdir " + outputDirecotry)

# ---------- GRAMMAR PROCESSING ---------- #

print("===== PARSING .jsb CODE =====")
lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = jsbachParser(token_stream)
tree = parser.root()

# ---------- VISITOR ---------- #

print("===== VISITING TREE =====")
temp = sys.stdout
sys.stdout = open(outputDirecotry+"/output.out", 'w')

visitor = TreeVisitor(main)
try:
    tempo, notes = visitor.visit(tree)
except Exception as e:
    print("ERROR -", str(e))

sys.stdout = temp

# ---------- PARSED TREE ---------- #

# print("===== PARSED TREE =====")
# print(tree.toStringTree(recog=parser))

# ---------- CREATE .LILY PROGRAM ---------- #

if len(notes) == 0:
    print("Warning: No output notes generated.")
    print("   No files generated.")
    print("   Progam exited.")
    sys.exit()

print("===== GENERATING OUTPUT FILES =====")
with open(outputDirecotry + "/" + fileName + ".lily", 'w') as f:
    f.write(lilyProgram(tempo, notes))

# ---------- OUTPUT FILES ---------- #

subprocess.call(["lilypond", "-o",
                 outputDirecotry, outputDirecotry + "/" + fileName + ".lily"])
subprocess.call(["timidity", "-Ow", "-o", outputDirecotry + "/" + fileName + ".wav",
                 outputDirecotry + "/" + fileName + ".midi"])
subprocess.call(["ffmpeg", "-i", outputDirecotry + "/" + fileName + ".wav",
                 "-codec:a", "libmp3lame", "-qscale:a", "2", outputDirecotry + "/" + fileName + ".mp3"])
