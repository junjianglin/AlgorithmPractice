def app(n):
	print 'something' 

def function1(aa):
	app(aa)

def function2(b):
	function1(b)

def function3(c):
	function2(c)
        return 'a'

def main():
	function3(100)

if __name__ == '__main__':
		main()
