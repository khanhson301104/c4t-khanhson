playerX = 3
playerY = 3





def printMap (side):
    for i in range(side):
        for j in range(side):
            if i == playerY and j == playerX:
                print("P", end="")
            
            else:

                print("*", end="")
        print()





while(True):
    direct = input("Your move: ")
    if direct.lower()== "up":
        playerY = playerY - 1
    if direct.lower()== "down":
        playerY = playerY + 1
    if direct.lower()== "right":
        playerX = playerX +1
    if direct.lower()== "left":
        playerX = playerX -1
    
    printMap(7)

while(True):
    if playerY > 0:
        print("P")
    else:
        print()
    
