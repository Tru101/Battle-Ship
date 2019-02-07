import random as computer_call

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


for i in range(1,1000):
    player_move = input("Players turn! Please select a Letter(Capital letter Please) from A-J and a number 1-10 to make your attack. If you want to see the moves you have already called input Z11")
    if player_move == 'Z11':
        print(moves_called)
    else:
        moves_called.append(player_move)
    if player_move in computers_ships:
        print("HIT!!")
        computers_ships.remove(player_move)
    print(computers_ships)    
    
    if player_move in game_boardcomputer:
        print("Miss")
        game_boardcomputer.remove(player_move)
    continue    
    x = computer_call.randint(0,100)
    computer_move = game_board_available[x]
    print(computer_move)
    if computer_move in preset_player1:
        print("HIT!!")
        preset_player1.remove(computer_move)
    if computer_move in game_boardplayer:
        print("Miss")
          
    if preset_player1 == [] or computers_ships == []:
        print("Game is over")
        break