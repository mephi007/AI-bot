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

print(first_move())
print(playAgain())