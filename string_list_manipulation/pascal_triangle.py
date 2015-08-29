import sys
def print_pascal(n):
	pascal = []
	pascal.append([1])
	pascal.append([1,1])
	print " "*(n-1)+str(1)+" "*(n-1)
	print " "*(n-2)+str(1)+" "+str(1)+" "*(n-2)
	i = 2
	while i < n:
		sys.stdout.write(" "*(n-i-1)+str(1))
		j = 0
		temp = [1]
		while j < i-1:
			sys.stdout.write(" ")
			num = pascal[i-1][j] + pascal[i-1][j+1]
			temp.append(num)
			sys.stdout.write(str(num))
			j += 1
		temp.append(1)
		sys.stdout.write(" "+str(1)+" "*(n-i-1)+"\n")
		pascal.append(temp)
		i += 1
print_pascal(20)
