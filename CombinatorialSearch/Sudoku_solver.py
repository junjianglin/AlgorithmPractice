DIM = 9
NCELLS = DIM*DIM
from collections import Counter

class Point():
	def __init__(self,x=-1,y=-1):
		self.x = x
		self.y = y

class Board():
	def __init__(self,matrix):
		self.matrix = matrix
		self.freeCount = self.__updateFreeCount(matrix)
		self.move = [Point() for _ in range(NCELLS)]

	def __updateFreeCount(self,matrix):
		count = 0
		for row in matrix:
			for col in row:
				if col == -1:
					count += 1
		return count
	
	def nextSquare(self):
		matrix = self.matrix
		openSquares = []
		x = 0
		while x < len(matrix):
			y = 0
			while y < len(matrix[x]):
				if matrix[x][y] == -1:
					counter = self.__init_counter()
					square = self.getSqureInfo(x,y,matrix,counter)
					openSquares.append(square)
				y += 1
			x += 1
		target = min(openSquares)
		return target

	def getSqureInfo(self,x,y,matrix,counter):
		#check row
		for item in matrix[x]:
			if item != -1:
				counter[item] -=1
		#check column
		i = 0
		while i < len(matrix):
			item = matrix[i][y]
			if item != -1:
				counter[item] -=1
			i += 1
		#check sector
		sector = [(1,1),(1,4),(1,7),\
				  (4,1),(4,4),(4,7),\
				  (7,1),(7,4),(7,7)]
		for (p,q) in sector:
			if (x,y) in [(p+i,q+j) for i in range(-1,2) for j in range(-1,2)]:
				sec_find = (p,q)
				break
		p,q = sec_find
		for m,n in [(p+i,q+j) for i in range(-1,2) for j in range(-1,2)]:
			item = matrix[m][n]
			if item != -1:
				counter[item] -=1
		#summarize and return
		counter += Counter({0:0})
		keys = counter.keys()
		num_keys = len(keys)
		return (num_keys,x,y,keys)


	def __init_counter(self):
		counter = Counter([1,2,3,4,5,6,7,8,9])
		return counter
	
	def printBoard(self):
		for row in self.matrix:
			print ", ".join(map(str,row))

def construct_candidates(a,k,board):
	square = board.nextSquare()
	x = square[1]
	y = square[2]
	possibles = square[-1]
	#print x,y,possibles
	ncandidates = square[0]
	if ncandidates == 0:
		return possibles,ncandidates
	else:
		board.move[k].x = x
		board.move[k].y = y
		#print "Assignment: board,k,x,y: ", k,board.move[k].x,board.move[k].y
		return possibles,ncandidates

def make_move(a,k,board):
	x = board.move[k].x
	y = board.move[k].y
	board.matrix[x][y] = a[k]
	board.freeCount -= 1
	#print "make_move",x,y,a[k]

def unmake_move(a,k,board):
	#print "current unmake k: ",k
	x = board.move[k].x
	y = board.move[k].y
	board.matrix[x][y] = -1
	board.freeCount +=1
	#print "unmake_move",x,y
	#board.printBoard()

def is_a_solution(a,k,board):
	if board.freeCount == 0:
		return True
	else:
		return False

def process_solution(a,k,board):
	board.printBoard()
	return True

def sudoku(a,k,board):
	global finished
	if is_a_solution(a,k,board):
		finished = process_solution(a,k,board)
	else:
		k += 1
		c,ncandidates = construct_candidates(a,k,board)
		#if ncandidates == 0:
		#	print "stuck"
		for i in range(ncandidates):
			a[k] = c[i]
			#print "k before make move ", k
			#print "a[k] is ", a[k]
			#print "board12 before make_move,k,x,y: ",k,board.move[12].x,board.move[12].y
			make_move(a,k,board)
			#print "before sudoku, k,x,y:",k,board.move[k].x,board.move[k].y
			#print "board12 before sudoku,k,x,y: ",k,board.move[12].x,board.move[12].y
			sudoku(a,k,board)
			#print "k before unmake ", k
			#print "before unmake, k,x,y:",k,board.move[k].x,board.move[k].y
			#print "board12 before unmake,k,x,y: ",k,board.move[12].x,board.move[12].y
			unmake_move(a,k,board)
			if finished:
				return

finished = False
def main():
	global finished
	testcase = input()
	print testcase
	for _ in range(testcase):
		finished = False
		space = raw_input()
		matrix = []
		for _ in range(DIM):
			temp = map(int,raw_input().split(','))
			matrix.append(temp)
		board = Board(matrix)
		a = [0] * (DIM*DIM)
		k = -1
		sudoku(a,k,board)
	
if __name__ == '__main__':
	main()

