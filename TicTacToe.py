## Include condition of draw in this game
import random
blankGrid = "   |   |   \n___|___|___\n   |   |   \n___|___|___\n   |   |   \n   |   |   "
numberGrid = "1  | 2 |  3\n___|___|___\n4  | 5 |  6\n___|___|___\n7  | 8 |  9\n   |   |   "
#print(grid)

#gridList = list(grid)
def instructions():
    print("""Tic-tac-toe is played on a three-by-three grid by two players,
who alternately place the marks X and O in one of the nine spaces in the grid.
Here is a blank grid.""")
    print(blankGrid)
    print("You can choose numbers 1 to 9 to mark cross or nought on a cell.")
    print(numberGrid)

def startMsg():
    choice = int(input("Welcome to Tic-tac-toe. Type 1 to see instructions. Type 2 to continue:"))
    if(choice==1):
        instructions()
    print("\nPlay against the computer. You can start.")
    return

def putPosition():
    position = int(input("Enter position of mark(1-9): "))
    if(type(position) is not int) or (position>9) or (position<1):
        raise Exception("Wrong input. Type an integer between 1 and 9 (included).")
    return position

def chooseXorO():
    XorO_numeric = int(input("What do you want to choose? Enter 1 for X and 2 for O:"))
    if(XorO_numeric==1):
        XorO = "X"
    elif(XorO_numeric==2):
        XorO = "O"
    else:
        raise Exception("Wrong input. Type 1 or 2.")
    return XorO
    
    

def addMark(givenGrid, pos, XorO, emptySpaces, playerTurn):
    givenGridList = list(givenGrid)
    if (pos in emptySpaces):
        emptySpaces.remove(pos)
        playerTurn = not playerTurn
        
        if (pos==1):
            givenGridList[0] = XorO
        if (pos==2):
            givenGridList[5] = XorO
        if (pos==3):
            givenGridList[10] = XorO
        if (pos==4):
            givenGridList[24] = XorO
        if (pos==5):
            givenGridList[29] = XorO
        if (pos==6):
            givenGridList[34] = XorO
        if (pos==7):
            givenGridList[48] = XorO
        if (pos==8):
            givenGridList[53] = XorO
        if (pos==9):
            givenGridList[58] = XorO
    else:
        playerTurn = True
        print("You can't place mark there. Redo turn.")
    
    
    newGrid = "".join(givenGridList)
    return newGrid, emptySpaces, playerTurn

def getPlayerWinCondition(givenGrid, pXO):  #pXO = playerXorO
    gL = list(givenGrid)      #gL = givenGridList
    if (gL[0]==gL[5]==gL[10]==pXO) or (gL[24]==gL[29]==gL[34]==pXO) or (gL[48]==gL[53]==gL[58]==pXO) or (gL[0]==gL[24]==gL[48]==pXO) or (gL[5]==gL[29]==gL[53]==pXO) or (gL[10]==gL[34]==gL[58]==pXO) or (gL[0]==gL[29]==gL[58]==pXO) or (gL[10]==gL[29]==gL[48]==pXO):
        return True
    else:
        return False

def getComputerWinCondition(givenGrid, cXO):  #cXO = computerXorO
    gL = list(givenGrid)      #gL = givenGridList
    return ((gL[0]==gL[5]==gL[10]==cXO) or (gL[24]==gL[29]==gL[34]==cXO) or (gL[48]==gL[53]==gL[58]==cXO) or (gL[0]==gL[24]==gL[48]==cXO) or (gL[5]==gL[29]==gL[53]==cXO) or (gL[10]==gL[34]==gL[58]==cXO) or (gL[0]==gL[29]==gL[58]==cXO) or (gL[10]==gL[29]==gL[48]==cXO))
        
def getDrawCondition(givenGrid):
    gL = list(givenGrid)  #gL = givenGridList
    return not(gL[0]==" " or gL[5]==" " or gL[10]==" " or gL[24]==" " or gL[29]==" " or gL[34]==" " or gL[48]==" " or gL[53]==" " or gL[58]==" ")
            

def gameloop():
    startMsg()
    playerXorO = chooseXorO()
    if(playerXorO == "X"):
        computerXorO = "O"
    else:
        computerXorO = "X"
    print(blankGrid)
    playerTurn = True 
    emptySpaces = [1,2,3,4,5,6,7,8,9]
    currentGrid = blankGrid
    gameOver = False
    while(gameOver == False):
        if playerTurn == True:
            print("Your turn.")
            playerPosition = putPosition()
            currentGrid, emptySpaces, playerTurn = addMark(currentGrid, playerPosition, playerXorO, emptySpaces, playerTurn)
            print("\n")
            print(currentGrid)
        playerWinCondition = getPlayerWinCondition(currentGrid, playerXorO)
        
        if (playerWinCondition is True):
            print("You win.")
            gameOver==True
            break

        if playerTurn == False:
            if emptySpaces:
                computerPosition = random.choices(emptySpaces)
            currentGrid, emptySpaces, playerTurn = addMark(currentGrid, computerPosition[0], computerXorO, emptySpaces, playerTurn)
            print("\nComputer's turn")
            print(currentGrid)
            #print(emptySpaces)

        computerWinCondition = getComputerWinCondition(currentGrid, computerXorO)
        if(computerWinCondition is True):
            print("You lose.")
            gameOver==True
            break
        
        drawCondition = getDrawCondition(currentGrid)
        if(drawCondition is True):
            print("Draw.")
            gameOver = True
            break

choice = 'y'
while (choice=='y') or (choice=='Y'):
    gameloop()
    choice = str(input("Want to play again?(y/n): "))
##position = int(input("Enter position of mark(1-9): "))
##if(type(position) is not int) or (position>9) or (position<1):
##        raise Exception("Wrong input. Type an integer between 1 and 9 (included).")
##XorO_numeric = int(input("What do you want to choose? Enter 1 for X and 2 for O:"))
##if(XorO_numeric==1):
##    XorO = "X"
##elif(XorO_numeric==2):
##    XorO = "O"
##else:
##    raise Exception("Wrong input. Type 1 or 2.")
##
##newGrid = addMark(grid, position, XorO)
##print(newGrid)
##    
