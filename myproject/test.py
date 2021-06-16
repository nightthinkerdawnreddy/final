#taking the input in the python
from typing import Pattern


sone=[]
for i in range(5):
    s=list(input())
    sone.append(s)
pattern=[]
for i in range(len(sone)):
    so=[]
    for j in range(len(sone[i])):
        if sone[i][j] != " ":
            so.append(sone[i][j])
    pattern.append(so)    
searchword='EAST'
for i in range(len(pattern)):
    for j in range(len(pattern[0])):
        rowword=''
        colword=''
        diaword=''
        for k in range(len(searchword)):
            if j+k < len(pattern[0]):
                rowword += pattern[i][j+k]
            if j+k < len(pattern):
                colword += pattern[j+k][i]
            if i+k < len(pattern) and j+k < len(pattern[0]):
                diaword += pattern[i+k][j+k]
        if rowword == searchword or searchword == colword or diaword == searchword:
            print("yes the word found",rowword,colword,diaword)
            
