# Author: Luis Chavez
# Assignment: Tic-Tac-Toe game
#Course: CSE210 - 20

def main():
    
    #The spots that the board will display
    number_spot = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9"
        }
    
    playing = True
    user_turn = 0

    #Star a while loop until the game ends
    while playing:
        #Display the board
        display_board(number_spot)

        #1. This if statement avoid to show the input text when the game ends
        #2. Check if the turn if for Player X or Player O
        #3. Ask the player to pick one square
        if user_turn < 9:
            if (user_turn + 1) % 2 == 0:
                user_number = input("\no's turn to choose a square (1-9): ")
            else:
                user_number = input("\nx's turn to choose a square (1-9): ")
            
            #Verify if the user typets and integer
            if user_number.isdigit() and int(user_number) in number_spot:
                
                #Check if the spot is not selected so the player can use it. If it is already selected,
                #avoid to overwriting
                if not number_spot[int(user_number)] in {"x", "o"}:
                    user_turn += 1
                    number_spot[int(user_number)] = check_user_turn(user_turn)

                #Check if the spot if already selected to avoit overwriting
                elif number_spot[int(user_number)] in {"x", "o"}:
                    print("Invalid square selected, please try another")
        
            #Check if the game ends because one player won
            if three_row(number_spot) == True:
                display_board(number_spot)
                print("\nGoog game. Thanks for playing!")
                playing = False
        
        #Ends the game if there is no winner, a tie
        else:
            print("\nIt's a tie, there is no winner")
            print("Good game. Thanks for playing!")
            playing = False



#This function takes the values of the dictionary "number_spot"
# and display the board with the numbers 1-9
def display_board(number_spot):

    board = (f"\n{number_spot[1]}|{number_spot[2]}|{number_spot[3]}\n"
                f"-+-+-\n"
                f"{number_spot[4]}|{number_spot[5]}|{number_spot[6]}\n"
                f"-+-+-\n"
                f"{number_spot[7]}|{number_spot[8]}|{number_spot[9]}")
        
    print(board)

#This function is to check when is the player's 1 or 2 turn
def check_user_turn(turn):

    #If the remainder of the turn (numeber of the turn) is 0
    #is player's 2 turn. If the remainder if not 0, then is
    #player's 1 turn
    if turn % 2 == 0:
        return "o"
    else:
        return "x"

# This function will check if the game ends by a horizontal row, vertical rod, diagonal row or a tie.
def three_row(number_spot):
    
    if (number_spot[1] == number_spot[2] == number_spot[3]) or (number_spot[4] == number_spot[5] == number_spot[6]) or (number_spot[7] == number_spot[8] == number_spot[9]):
        return True
    
    elif (number_spot[1] == number_spot[4] == number_spot[7]) or (number_spot[2] == number_spot[5] == number_spot[8]) or (number_spot[3] == number_spot[6] == number_spot[9]):
        return True
    
    elif (number_spot[1] == number_spot[5] == number_spot[9]) or (number_spot[3] == number_spot[5] == number_spot[7]):
        return True

if __name__ == '__main__':
    main()