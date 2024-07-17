"""
                                           
   Lecture 1 Question 7 : tic tac toe      
                                           
   Extend functions given in class to play tic tac toe                        
                                           
   Pietro Rescigno - Scientific Computing with Python 23/24  
                                           
"""

# String containing the board

board = """
 {s1:^3} | {s2:^3} | {s3:^3}
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}
-----+-----+-----      123
 {s7:^3} | {s8:^3} | {s9:^3}       456
                       789  
"""
# Lists containing each player's moves
Ogame = []
Xgame = []

# Initialize play: use the dictionary to 
# set all squares to empty

def initialize_board(play):
    for n in range(9):
        play["s{}".format(n+1)] = ""

def show_board(play):
    """ display the playing board.  We take a dictionary with the current state of the board
    We rely on the board string to be a global variable"""
    print(board.format(**play))
    
def get_move(n, xo, play):
    """ ask the current player, n, to make a move -- make sure the square was not 
        already played.  xo is a string of the character (x or o) we will place in
        the desired square """
    valid_move = False
    while not valid_move:
        idx = input("player {}, enter your move (1-9)".format(n))
        if play["s{}".format(idx)] == "":
            valid_move = True
        else:
            print("invalid: {}".format(play["s{}".format(idx)]))
            
    play["s{}".format(idx)] = xo
    if player==0:
        Xgame.append(idx)
    else:
        Ogame.append(idx)

def check_win(player):
	if player==0:
		if (all(x in Xgame for x in ['1','2','3']) or\
		all(x in Xgame for x in ['4','5','6']) or\
		all(x in Xgame for x in ['7','8','9']) or\
		all(x in Xgame for x in ['1','4','7']) or\
		all(x in Xgame for x in ['2','5','8']) or\
		all(x in Xgame for x in ['3','6','8']) or\
		all(x in Xgame for x in ['1','5','9']) or\
		all(x in Xgame for x in ['3','5','7'])):
			return 1
		else:
			return 0
	if player==1:
		if (all(x in Ogame for x in ['1','2','3']) or\
		all(x in Ogame for x in ['4','5','6']) or\
		all(x in Ogame for x in ['7','8','9']) or\
		all(x in Ogame for x in ['1','4','7']) or\
		all(x in Ogame for x in ['2','5','8']) or\
		all(x in Ogame for x in ['3','6','8']) or\
		all(x in Ogame for x in ['1','5','9']) or\
		all(x in Ogame for x in ['3','5','7'])):
			return 1
		else:
			return 0



play ={}
initialize_board(play)
show_board(play)
#print(f'Starting game of tic-tac-toe. Enter move \'E\' to end game.' )
nmove=0
xo = ['x','o']
while nmove!=9:
    player = nmove%2
    get_move(player,xo[player],play)
    show_board(play)
    nmove = nmove + 1
    if check_win(player):
        print(f"Player {player} wins!")
        break

# Show board using 
