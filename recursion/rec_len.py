def rec_len(L):
	"""(nested list) -> int
	Return the total number of non-list elements within nested list L.
	For example, rec_len([1,'two',[[],[[3]]]]) == 3
	"""

	if not L:
		return 0
	elif isinstance(L[0],list):
		return rec_len(L[0]) + rec_len(L[1:])
	else:
		return 1 + rec_len(L[1:]) 


print rec_len([1,'two',[[],[[3]]]])