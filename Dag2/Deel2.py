def compareLevels(sLevel, i, j):
    btmp = True
    if sLevel[i] == sLevel[j]:
        btmp = False
        print(f"same")
    elif int(sLevel[i]) <= int(sLevel[j]) and increase>0:
        btmp = False #decreasing
        print("decrease")
    elif int(sLevel[i]) >= int(sLevel[j]) and increase<0:
        btmp = False #increasing
        print("increase")
    elif int(sLevel[i]) > int(sLevel[j])+3 and increase>0:
        btmp = False #increase too much
        print("fast increase")
    elif int(sLevel[i]) < int(sLevel[j])-3 and increase<0:
        btmp = False #decrease too much
        print("fast decrease")
    return btmp

def compareReport(sLevel):
    for lvl in range(1, len(sLevel)):        
        if not compareLevels(sLevel, lvl, lvl-1):
            return False
    return True

reportlist = []

with open('Dag2\\input.txt', 'r') as file:
    for line in file:
        reportlist.append(line.replace("\n", ""))

safe = 0
for report in reportlist:
    bsafe = True
    print("---------")
    print(f"report: {report}")
    levels = report.split(" ")
    
    increase = int(levels[1]) - int(levels[0])
    if increase == 0:
        increase = int(levels[2]) - int(levels[0])
        if increase == 0: 
            bsafe = False
    print(f"increase: {increase}")
    
    if compareReport(levels):
        bsafe = True
    else:
        bsafe = False
        for i in range(0, len(levels)):
            tmplvl = report.split(" ")
            del tmplvl[i]
            increase = int(tmplvl[1]) - int(tmplvl[0])
            if increase == 0:
                increase = int(tmplvl[2]) - int(tmplvl[0])
                if increase == 0: 
                    bsafe = False
            print(f"tmp: {tmplvl}")
            if not bsafe:
                print("comp")
                bsafe = compareReport(tmplvl)
            
            
    if bsafe:
        safe+=1
    else:
        print("unsafe")

#300<x<388
#!328
print(f"safe reports: {safe}")
            
    