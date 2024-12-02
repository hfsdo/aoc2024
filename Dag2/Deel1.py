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
    print(f"increase: {increase}")
    for i in range(1, len(levels)):
        if bsafe:
            if levels[i] == levels[i-1]:
                bsafe = False
                print("same")
            if int(levels[i]) <= int(levels[i-1]) and increase>0:
                bsafe = False #decreasing
                print("decrease")
            if int(levels[i]) >= int(levels[i-1]) and increase<0:
                bsafe = False #increasing
                print("increase")
            if int(levels[i]) > int(levels[i-1])+3 and increase>0:
                bsafe = False #increase too much
                print("fast increase")
            if int(levels[i]) < int(levels[i-1])-3 and increase<0:
                bsafe = False #decrease too much
                print("fast decrease")
    if bsafe:
        safe+=1

print(f"safe reports: {safe}")
            
    