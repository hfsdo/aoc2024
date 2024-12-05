xmasgrid = []

def isXMAS(MCoord, ACoord, SCoord):
    try:
        if xmasgrid[MCoord[0]][MCoord[1]] != "M": return False
        if xmasgrid[ACoord[0]][ACoord[1]] != "A": return False
        if xmasgrid[SCoord[0]][SCoord[1]] != "S": return False
        #print(f"{MCoord}, {ACoord}, {SCoord}")
        return True
    except:
        return False


with open('Dag4\\input.txt', 'r') as file:
    for line in file:
        print(f"{len(line)}: {line}")
        xmasgrid.append(line)

total = 0
for i in range(0, len(xmasgrid)):
    for j in range(0, len(xmasgrid[i])):
        if xmasgrid[i][j] == "X":
            #check
            #print(f"coord: {i},{j}")
            #left/right
            if isXMAS((i,j+1),(i,j+2),(i,j+3)):
                total+=1
                #print(f"right:{xmasgrid[i][j]}{xmasgrid[i][j+1]}{xmasgrid[i][j+2]}{xmasgrid[i][j+3]}: coord:{i},{j}")
            if isXMAS((i,j-1),(i,j-2),(i,j-3)):
                total+=1
                #print(f"left:{xmasgrid[i][j]}{xmasgrid[i][j-1]}{xmasgrid[i][j-2]}{xmasgrid[i][j-3]}: coord:{i},{j}")

            #up/down
            if isXMAS((i+1,j),(i+2,j),(i+3,j)):
                total+=1
                #print(f"down:{xmasgrid[i][j]}{xmasgrid[i+1][j]}{xmasgrid[i+2][j]}{xmasgrid[i+3][j]}: coord:{i},{j}")
            if isXMAS((i-1,j),(i-2,j),(i-3,j)):
                total+=1
                #print(f"up:{xmasgrid[i][j]}{xmasgrid[i-1][j]}{xmasgrid[i-2][j]}{xmasgrid[i-3][j]}: coord:{i},{j}")

            #diagonal
            if isXMAS((i+1,j+1),(i+2,j+2),(i+3,j+3)):
                total+=1
                #print(f"down/right:{xmasgrid[i][j]}{xmasgrid[i+1][j+1]}{xmasgrid[i+2][j+2]}{xmasgrid[i+3][j+3]}: coord:{i},{j}")
            if isXMAS((i-1,j+1),(i-2,j+2),(i-3,j+3)):
                total+=1
                #print(f"up/right:{xmasgrid[i][j]}{xmasgrid[i-1][j+1]}{xmasgrid[i-2][j+2]}{xmasgrid[i-3][j+3]}: coord:{i},{j}")
            if isXMAS((i-1,j-1),(i-2,j-2),(i-3,j-3)):
                total+=1
                #print(f"up/left:{xmasgrid[i][j]}{xmasgrid[i-1][j-1]}{xmasgrid[i-2][j-2]}{xmasgrid[i-3][j-3]}: coord:{i},{j}")
            if isXMAS((i+1,j-1),(i+2,j-2),(i+3,j-3)):
                total+=1
                #print(f"down/left:{xmasgrid[i][j]}{xmasgrid[i+1][j-1]}{xmasgrid[i+2][j-2]}{xmasgrid[i+3][j-3]}: coord:{i},{j}")

#x<2590
print(f"XMAS occurences: {total}")
            
