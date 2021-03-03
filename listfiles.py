# importing libraries 
import subprocess 
import os

#returns file names in an array
#IE ['Downloads', 'Documents']
def listfiles(location):
    cmd = ['ls', str(location)]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    o, e = proc.communicate()

    listdirectory=list(o.decode('utf-8'))

    output = []
    wordassembly = ""

    for x in range(len(listdirectory)):
        if(listdirectory[x] != "\n"):
            wordassembly = wordassembly + listdirectory[x]
        else:
            output.append(wordassembly)
            wordassembly = ""
    return output

