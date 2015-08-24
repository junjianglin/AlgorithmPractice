
DIM = 8
finished = False

def construct_candidates(a,k,board):
	potential = set(range(DIM))
	#filling by row
	i = 0
	while i < len(board[k]):
		#check col
		for j in range(k):
			if 1 == board[j][i]:
				if i in potential:
					potential.remove(i)
				break
		#check diagonal
		try:
			for j in range(1,k+1):
				if board[k-j][i-j] == 1:
					if i in potential:
						potential.remove(i)
					break
				if board[k-j][i+j] == 1:
					if i in potential:
						potential.remove(i)
					break
		except IndexError:
			pass
		i += 1
	c = list(potential)
	#print "potentials: ", c
	ncandidates = len(c)
	return c, ncandidates

def is_a_solution(a,k,board):
	if k == len(board)-1:
		return True
	else:
		return False
		
def process_solution(a,k,board):
	global finished
	finished = True
	for row in board:
		print row
	return finished

def make_move(a,k,board):
	board[k][a[k]] = 1
	#print "make move, k, a[k]", k, a[k]

def un_make_move(a,k,board):
	board[k][a[k]] = 0
	#print "un_make_move, k, a[k]", k, a[k]

def eightQueens(a,k,board):
	global finished
	if is_a_solution(a,k,board):
		finished = process_solution(a,k,board)
	else:
		k += 1
		#print "k is ", k
		c, ncandidates = construct_candidates(a,k,board)
		for i in range(ncandidates):
			a[k] = c[i]
			make_move(a,k,board)
			eightQueens(a,k,board)
			un_make_move(a,k,board)
			if finished:
				return 

def generate_queens():
	global finished
	board = [[0] * DIM for _ in range(DIM)]
	a = [0] * DIM
	k = -1
	eightQueens(a,k,board)

generate_queens()
