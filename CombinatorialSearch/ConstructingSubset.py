import sys

def is_a_solution(a,k,n):
	if k == n-1:
		return True
	else:
		return False

def process_solution(a,k):
	for i in range(k+1):
		if a[i] == True:
			sys.stdout.write(str(i+1))
	sys.stdout.write("\n")

def construct_candidates(a,k,n):
	c = []
	c.append(True)
	c.append(False)
	ncandidates = 2
	return c,ncandidates

def backtrack_subset(a,k,n):

	if is_a_solution(a,k,n):
		process_solution(a,k)
	else:
		k += 1
		c,ncandidates = construct_candidates(a,k,n)
		for i in range(ncandidates):
			#print k,i
			a[k] = c[i]
			backtrack_subset(a,k,n)


def generate_subsets(n):
	k = -1
	a = [0] * n
	backtrack_subset(a,k,n) 

generate_subsets(3)
