
def input_fun():
    symbol_input = input("What will you select, X or O? ")
    if symbol_input in ["X","x","O","o"]:
        pass
    else:
        print("Please select either X or O\n")
        input_fun()

    return symbol_input
  
def dashboard(player_input):
    print("\n {} | {} | {}".format(player_input[0],player_input[1],player_input[2]))
    print("----------")
    print(" {} | {} | {}".format(player_input[3],player_input[4],player_input[5]))
    print("----------")
    print(" {} | {} | {}".format(player_input[6],player_input[7],player_input[8]))

# Logic of game
def checkIfGameEnds(player_input):
    game_check = [[0, 1, 2], [3, 4, 5], 
               [6, 7, 8], [0, 3, 6], 
               [1, 4, 7], [2, 5, 8], 
               [0, 4, 8], [2, 4, 6]]

    for check_indices in game_check:
        try:
            player_check = [player_input[i] for i in check_indices]
            player_set = [x for x in player_check if x]
            if len(player_set)==3 and len(set(player_set))==1:
                if (player_set)[0] == player1:
                    print(f"\nGame is won by Player 1 (Symbol : {player1})")
                else:
                    print(f"\nGame is won by Player 2 (Symbol : {player2})")
                return True
        except:
            pass
    else:
        return False

#####################################################################################################
print("Welcome to Tic Tac Toe")
symbol_input = input_fun() 
if symbol_input in ["X","x"]:
    player1 = "X"
    player2 = "O"
else:
    player1 = "O"
    player2 = "X"  
print(f"\nSymbol for Player 1 is {player1} and for Player 2 is {player2}\n")

print(" 1 | 2 | 3")
print("----------")
print(" 4 | 5 | 6")
print("----------")
print(" 7 | 8 | 9\n")

endGame = False
counter = 0
player_input = [''  for x in range(9)]

for _ in range(9):    
    counter += 1
    if not(endGame):
        input_value = int(input("\nPlease enter the position for your move (1 to 9): "))
        if (counter%2 != 0):
            replacement = player1
        else:
            replacement = player2
    
        player_input[input_value-1] = replacement
        dashboard(player_input)
        endGame = checkIfGameEnds(player_input)
    else:
        print("Game Over\n")
        player_input.clear()
        break