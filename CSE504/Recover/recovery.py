from pathlib import Path


with open(Path(__file__).parent/'input.txt') as file:
                    log=file.read()

                    
ignore =[]
undo = []
undo2 = []
redo = []
redo2 = []
ckpt = False
log=log.splitlines()  #string --> list of strings

for itr in reversed(log):
        c = itr[1:-1].split(' ')
        if 'CKPT' in c[0]:
                ckpt = True
        elif 'COMMIT' in c[0] and ckpt == True:
                ignore.append(c[1])
        elif 'COMMIT' in c[0] and ckpt == False:
                redo.append(c[1])
        elif 'START' in c[0] and c[1] not in redo and c[1] not in ignore:
                undo.append(c[1])
        
for i in(undo):
        for j in reversed(log): 
            d = j[1:-1].split(' ')
            if i == d[0]:
                    undo2.append({d[1],d[2]})
                    


for i in(redo):
        for j in reversed(log): 
            d = j[1:-1].split(' ')
            if i == d[0]:
                    redo2.append({d[1],d[3]})

print("Undo :",*undo)
print("Redo :",*redo)
print("Ignore :",*ignore)
print("Undo transaction of ",*undo2)
print("Redo transaction of ",*redo2)

        


