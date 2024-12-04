import re

f = open("Dag3\\input.txt", "r")
input = f.read()
pattern = re.compile(r'mul\([0-9]*,[0-9]*\)')
lstinput = re.findall(pattern, input)

total = 0

for mul in lstinput:
    print(mul)
    a = mul[4:mul.find(",")]
    b = mul[mul.find(",")+1:-1]

    total += int(a) * int(b)

print(f"multiplication result: {total}")
