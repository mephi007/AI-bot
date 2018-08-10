import random #for toss
board=['','','','','','','','','','']
def drawboard(board):
	print(' |   |')

	print(' '+board[7]+ '|' +'   '+ board[8]+ '|' + board[9])
	print('------------')
	print(' |   |')

	print(' '+board[6]+ '|' +'   '+ board[5]+ '|' + board[6])
	print('-------------')
	print(' '+board[3]+ '|' +'   '+ board[2]+ '|' + board[1])
	print(' |   |')

drawboard(board)

#taking input from user

def input_player():
	letter = ''
	#while loop - if user mistakenly gives input other than X or O
	while not(letter == 'X' or letter =='O'):
		print('Do you want to be X or O?')
		letter = raw_input().upper()

	if letter == 'X':
		return ['X' , 'O']
	else:
		return['O', 'X']

print(input_player())

def first_move():
	
	
	print('choose number for toss, 0 or 1?')
	toss = raw_input()

	if random.randint(0,1) == toss:
		return ' player'
	else:
		return 'computer'

def playAgain():
	print('do you want to play again? yes or no?')
	return raw_input().lower().startswith('y')

def makeMove(board , letter , move):
	board[move] = letter

def winner(board, letter):
	return ((board[7]==letter and board[8]==letter and board[9]==letter )
		or (board[4]==letter and board[5]==letter and board[6]==letter)or
				(board[1]==letter and board[2]==letter and board[3]==letter)or
				(board[7]==letter and board[4]==letter and board[1]==letter)or
				(board[8]==letter and board[5]==letter and board[2]==letter)or
				(board[9]==letter and board[6]==letter and board[3]==letter)or
				(board[7]==letter and board[5]==letter and board[3]==letter) or 
				(board[9]==letter and board[5]==letter and board[1]==letter)
				)

def board_copy(board):

	dupeboard = []

	for i in board:
		dupeboard.append(i)

def free_space(board , move):
	return board[move]==' '

def player_move(board):
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(board, int(move)):
		move = raw_input(' what is your next move?')
		return int(move)
def random_moves(board , moves):
	possibleMoves = []
	for i in moves:
		if free_space(board , i):
			possibleMoves.append(i)

	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)

	else:
		return None

def getComputerMove(board , computerLetter):
	if computerLetter == 'X'
		playerLetter = 'O'
	else:
		playerLetter = 'X'
# computer checking if it can win in one move
	for i in range(1,10):
		copy = board_copy(board)
		if free_space(copy, i):
			makeMove(copy , computerLetter, i)
			if winner(copy , computerLetter):
				return i 
# #computer checking if player can win in one move
# 	for i in range(1,10):
# 		copy = board_copy(board)
# 		if free_space(copy , i):
# 			makeMove(copy, playerLetter , i)
# 			if winner(copy,playerLetter):
# 				return i
# #check available space in corner
# 	move = random_moves(board , [ 1,3,7,9])
# 	if move != None:
# 		return i

print(first_move())


print(winner(['','O','O','O','','','','','',''] ,'O'))

print(playAgain())