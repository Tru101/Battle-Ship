import random as computer_call
import time as thinking_call

def game_board(x,y):
   z = x + y
   return(z)

row_List = ['A','B','C','D','E','F','G','H','I','J']
column_List = ['1','2','3','4','5','6','7','8','9','10','11']
game_boardplayer = []
game_boardcomputer = []
game_board_available = []
moves_called = []
listcounter1 = 0
listcounter2 = 0
listcounter3 = 0
listcounter4 = 0
u = 0
p = 0
computers_ship_decision = computer_call.randint(1,4)
preset_player1 = ['A1','A2','A3','A4','A5','C10','D10','E10','F10','H5','H6','H7','J3','J4','E7','F7','G8','H1' ]
preset_computer1 = ['A5','B5','C5','D5','E5','G6','G7','G8','G9','E2','F2','G2','I4','I5','C9','C10','I9','J1']
preset_computer2 = ['B3','B4','B5','B6','B7','D1','E1','F1','G1','H6','H7','H8','E9','F9','F4','F5','J3','J5']
preset_computer3 = ['D3','D4','D5','D6','D7','G3','G4','G5','G6','B9','C9','D9','I2','I3','I7','I8','C1','G10']
preset_computer4 = ['A5','A2','A3','A4','A5','A10','B10','C10','D10','J1','J2','J3','J6','J7','G1','H1','E4','E7']


if computers_ship_decision == 1:
    computers_ships = preset_computer1
if computers_ship_decision == 2:
    computers_ships = preset_computer2
if computers_ship_decision == 3:
    computers_ships = preset_computer3    
if computers_ship_decision == 4:
    computers_ships = preset_computer4    
    
for i in range (1,101):
    column_number = column_List[listcounter1]
    if column_number == '11':
        listcounter2 = listcounter2 + 1 
        column_number = '1'
        listcounter1 = 0
    row_letter = row_List[listcounter2]
    game_boardplayer.append(game_board(row_letter,column_number))
    game_boardcomputer.append(game_board(row_letter,column_number))
    game_board_available.append(game_board(row_letter,column_number))
    listcounter1 = listcounter1 + 1
    
    
for i in range(1,19):
   i = listcounter3
   listcounter3 = listcounter3 + 1
   if preset_player1[i] in game_boardplayer:
      # print(preset_player1[i])
       game_boardplayer.remove(preset_player1[i])

for i in range(1,19):
   i = listcounter4
   listcounter4 = listcounter4 + 1
   if computers_ships[i] in game_boardcomputer:
     #  print(preset_computer1[i])
       game_boardcomputer.remove(computers_ships[i])      

#print(game_boardplayer)#Board with values that determine a miss for the computer
#print(game_boardcomputer)#Board with values that determine a miss for the player
#print(game_board_available)#Board with avilable spaces to make a move 

while True:
    preset_player2 = ['A2', 'B2', 'C2', 'D2', 'E2', 'C8', 'C9', 'E4', 'E5', 'E6', 'E7', 'G4', 'J4', 'J5', 'G7', 'H7', 'I7', 'G9']
    preset_player3 = ['A1', 'B1', 'F1', 'G1', 'H1', 'A10', 'B10', 'D4', 'D5', 'D6', 'D7', 'D8', 'F4', 'I5', 'H7', 'H8', 'H9', 'H10']
    question1 = input("To see game board presets, input 1, 2, or 3. Press Enter when ready. ")
    if question1 == "":
        break
    elif question1 == "1":
        print(preset_player1)
    elif question1 == "2":
        print(preset_player2)
    elif question1 == "3":
        print(preset_player3)
#to select presets:
question2 = input("Please input preset. ")
while question2 == "2":
    preset_player1 = preset_player2
    break
while question2 == "3":
    preset_player1 = preset_player3
    break
while question2 == "1":
    break


for i in range(1,1000):
    player_move = input("Players turn! Please select a Letter (Capital letter Please) from A-J and a number 1-10 to make your attack. If you want to see the moves you have already called input Z11 ")
    if player_move == 'Z11':
        print(moves_called)
        continue
    else:
        moves_called.append(player_move)
    
    if player_move in computers_ships:
        print("You HIT! a ship")
        u = u + 1
        #print(u)
        computers_ships.remove(player_move)
    #print(computers_ships)    
    else:
        print("You missed")
    if u == 5:
        print("You've sank the computer's Carrier")
    if u == 9:
        print("You've sank the computer's battleship")
    if u == 12:
        print("You've sank the computer's cruiser")
    if u == 14 or u == 16:
        print("You've sank the computer's destroyer")
    if u == 17 or u == 18:
        print("You've sank the computer's submarine")    
    
    print("Computer is making it's move....")
    thinking_call.sleep(3.5)
    x = computer_call.randint(0,100)
    computer_move = game_board_available[x]
    print(computer_move)
    if computer_move in preset_player1:
        print("The computer HIT one of your ships!")
        preset_player1.remove(computer_move)
        
    else:
        print("The computer missed")
    if p == 5:
        print("The computer sank your Carrier")
    if p == 9:
        print("The computer sank your battleship")
    if p == 12:
        print("The computer sank your cruiser")
    if p == 14 or u == 16:
        print("The computer sank your destroyer")
    if p == 17 or p == 18:
        print("The computer sank your submarine")    
          
    if preset_player1 == []:
        print("Game is over! The computer won")
        break
    elif computers_ships == []:
        print("Game is over! You won!")
        break