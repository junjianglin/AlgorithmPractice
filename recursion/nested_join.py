# def nested_join(s,L):
# 	return str.join(s,nested_join_helper(L))

# def nested_join_helper(L):
# 	if not L:
# 		return []
# 	elif isinstance(L[0],list):
# 		return nested_join_helper(L[0]) + nested_join_helper(L[1:])
# 	else:
# 		return [L[0]] + nested_join_helper(L[1:])

def nested_join(s,L):
	return str.join(s,[nested_join(s,x) if isinstance(x,list) else x for x in L])



print nested_join(' ',['one',['two','three'],'four'])