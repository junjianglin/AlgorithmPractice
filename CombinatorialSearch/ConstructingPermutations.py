import sys

def is_a_solution(a,k,S):
	if len(S) == 0:
		return True
	else:
		return False

def process_solution(a,k):
	for i in range(k+1):
		sys.stdout.write(str(a[i]))
	sys.stdout.write("\n")

def construct_candidates(a,k,S):
	c = []
	ncandidates = len(S)
	S_remove = []
	for x in S:
		c.append(x)
		temp = S[:]
		temp.remove(x) 
		S_remove.append(temp)

	return c,ncandidates,S_remove

def backtrack_permutation(a,k,S):

	if is_a_solution(a,k,S):
		process_solution(a,k)
	else:
		k += 1
		c,ncandidates,S_new = construct_candidates(a,k,S)
		for i in range(ncandidates):
			#print k,i
			a[k] = c[i]
			backtrack_permutation(a,k,S_new[i])

def generate_permutation(n):
	k = -1
	a = [0] * n
	S = range(1,n+1)
	backtrack_permutation(a,k,S) 

generate_permutation(3)
