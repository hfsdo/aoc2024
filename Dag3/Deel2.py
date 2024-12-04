import re

f = open("Dag3\\input.txt", "r")
input = f.read()
pattern = re.compile(r'don\'t|do|mul\([0-9]*,[0-9]*\)')
lstinput = re.findall(pattern, input)

total = 0
mulenabled = True

for mul in lstinput:
    print(mul)
    if mul == "do":
        mulenabled = True
    elif mul == "don\'t":
        mulenabled = False
    elif mulenabled:
        a = mul[4:mul.find(",")]
        b = mul[mul.find(",")+1:-1]

        total += int(a) * int(b)

print(f"multiplication result: {total}")
