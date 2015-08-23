from stack import Stack

def size(stk):
	stk_tmp = Stack()
	counter = 0
	while not stk.is_empty():
		stk_tmp.push(stz.pop)
		counter = counter + 1
	while not stk_tmp.is_empty():
		stk.push(stz.pop())
	return counter

def main():
	stk = Stack([1,2,3,4])
	print size(stk)

if __name__ == '__main__':
	main()