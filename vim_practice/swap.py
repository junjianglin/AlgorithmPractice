def swap(a):
	temp = a[1]
	del a[1]
	a.insert(0,temp)

a=[1,2]
swap(a)
print a
