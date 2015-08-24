DIM = 9
from collections import Counter

class error(Exception):
	pass

def init_counter():
	return Counter(range(1,DIM+1))

def checkRow(matrix,x,y):
	#check row
	counter = init_counter()
	for item in matrix[x]:
		counter[item] -=1
	counter += Counter({0:0})
	if sum(counter.values()) != 0:
		return False
	else:
		return True

def checkCol(matrix,x,y):
	#check column
	counter = init_counter()
	i = 0
	while i < len(matrix):
		item = matrix[i][y]
		counter[item] -=1
		i += 1
	counter += Counter({0:0})
	if sum(counter.values()) != 0:
		return False
	else:
		return True

def checkSector(matrix,x,y):
	#check sector
	counter = init_counter()
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
		counter[item] -=1
	counter += Counter({0:0})
	if sum(counter.values()) != 0:
		return False
	else:
		return True

def sudoku_checker(matrix):
	try:
		x = 0
		while x < len(matrix):
			y = 0
			while y < len(matrix[x]):
				if checkRow(matrix,x,y) and checkCol(matrix,x,y) and checkSector(matrix,x,y):
					y += 1
				else:
					raise error
			x += 1
		return True
	except error:
		return False


def main():
	testcase = input()
	for _ in range(testcase):
		matrix = []
		for _ in range(DIM):
			temp = map(int,raw_input().split(','))
			matrix.append(temp)
		print sudoku_checker(matrix)	
		
		
		
	
if __name__ == '__main__':
	main()
