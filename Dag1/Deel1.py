lstLeft = []
lstRight = []

with open('Dag1\\input.txt', 'r') as file:
    for line in file:
        items = line.replace("\n","").split(" ")
        lstLeft.append(items[0])
        lstRight.append(items[3])

lstLeft.sort()
lstRight.sort()
total = 0

for i in range(0, len(lstLeft)):
    total += abs(int(lstLeft[i]) - int(lstRight[i]))

print(f"total distance: {total}")