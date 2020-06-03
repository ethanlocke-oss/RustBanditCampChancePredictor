class Color:
    def __init__(self, color, chance):
        self.color = color
        self.chance = chance
        self.currChance = self.chance
        self.wonRecently = False
    

colors = []

# 5 indices 0 being yellow index  4 being red

colors.append(Color("y", 0.48))
colors.append(Color("g", 0.24))
colors.append(Color("b", 0.16))
colors.append(Color("p", 0.08))
colors.append(Color("r", 0.04))

while True:
    winningColor = input("\n\nEnter Color: ")
    for i in colors :
        if winningColor == i.color and i.wonRecently:
            i.currChance *= i.chance
        elif winningColor == i.color and not i.wonRecently:
            i.currChance = i.chance
            i.currChance *= i.chance
            i.wonRecently = True
        elif i.wonRecently :
            i.currChance = i.chance
            i.wonRecently = False
        else :
            i.currChance += i.chance
    

    highestOddColor = Color("None", -1)
    print("\n")
    for i in colors :
        print(str(i.currChance * 100))
        if i.currChance > highestOddColor.currChance :
            highestOddColor = i

    print("\n\n" + highestOddColor.color + " with a " + str(highestOddColor.currChance * 100) + "%")