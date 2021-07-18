import numpy as np
import random 
import math

def game2048(size):
	board = np.zeros((size,size))
	return board

def play(self, direction):
	if direction in 'Ww':
		self.up()
	elif direction in 'Ss':
		self.down()
	elif direction in 'Aa':
		self.left()
	elif direction in 'Dd':
		self.right()
				
def add2(board,size):
	i = 0
	zeros,n = [],0
	while i < size:
		j = 0
		while j < size:
			if board[i][j] == 0.0:
				zeros.append((i,j))
				n += 1
			j += 1
		i += 1
	if n == 0.0:
		return 
	index = zeros[np.random.randint(n)]
	board[index[0]][index[1]] = 2.0
	return board

def getState(board,size):
    if board[size-1][size-1] == 0:
        return True
    i = 0
    while i < size-1:
        j = 0
        while j < size-1:
            if board[i][j] == board[i][j+1]:
                return True
            if board[i][j] == board[i+1][j]:
                return True
            if board[i][j] == 0:
                return True
            j += 1
        i += 1
    
    i,j = 0,size-1
    while i < size-1:
        if board[i][j] == board[i+1][j]:
            return True
        if board[i][j] == 0:
            return True
        i += 1
    
    i,j = size-1,0
    while j < size-1:
        if board[i][j] == board[i][j+1]:
            return True
        if board[i][j] == 0:
            return True
        j += 1
    return False

def swap(board,i,j,k,l):
    board[i][j],board[k][l] = board[k][l],board[i][j]
    return board

def remove0(board,size):
    for i in range(size):
        zer = 0
        for j in range(size):
            if board[i][j] != 0:
                board = swap(board,i,j,i,zer)
                zer += 1
    return board
			
def merge(mat,size):
    score = 0
    for i in range(size):
        for j in range(size-1):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]*=2
                score += mat[i][j]   
                mat[i][j+1]=0
                # done=True
    return mat,score

def reverse(board,size):
    for i in range(size):
        board[i] = board[i][::-1]
    return board

def transpose(board,size):
    board = [list(i) for i in zip(*board)]
    return board

def left(board,size):
    board = remove0(board,size)
    # print('left')
    board,score = merge(board,size)
    # print('left')
    board = remove0(board,size)
    return board,score

def right(board,size):
	board = reverse(board,size)
	board,score = left(board,size)
	board = reverse(board,size)
	return board,score

def up(board,size):
    # print(board)
    board = transpose(board,size)
    # print(board)
    board,score = left(board,size)
    # print(board)
    board = transpose(board,size)
    # print(board)
    return board,score

def down(board,size):
	board = transpose(board,size)
	board,score = right(board,size)
	board = transpose(board,size)
	return board,score

def RUN(board,size,i):
    if i == 0:
        return up(board,size)
    elif i == 1:
        return down(board,size)
    elif i == 2:
        return left(board,size)
    else:
        return right(board,size)

#convert the input game matrix into corresponding power of 2 matrix.
def getInput(X,board_size):
    power_mat = np.zeros((1,4,4,14),dtype=np.float32)
    for i in range(board_size):
        for j in range(board_size):
            if(X[i][j]==0):
                power_mat[0][i][j][0] = 1.0
            else:
                power = int(math.log(X[i][j],2))
                power_mat[0][i][j][power] = 1.0
    return power_mat        

#find the number of empty cells in the game matrix.
def findemptyCell(mat,board_size):
    count = 0
    for i in range(board_size):
        for j in range(board_size):
            if(mat[i][j]==0):
                count+=1
    return count

def softmax(mat):
    e = np.exp(mat)
    return e/np.sum(e)
