
def weighted_interval_scheduling(input):
	input.sort(cmp=lambda x,y:cmp(x[1],y[1]))
	#compute the largest index i<j such that job i is compatible with j for each job
	compatible = [0] * (len(input)+1)
	for idx, job in enumerate(input):
		j = idx-1
		while j >= 0:
			if input[idx][0] >= input[j][1]:
				compatible[idx+1] = j+1
				break
			j -= 1
	#start DP
	dp = [0]*(len(input)+1)
	pre = [-1]*(len(input)+1)
	dp[0] = 0
	i = 1
	while i < len(dp):
		#opt(j) = max(w_j+opt(compatible[j]),opt(j-1))
		opt1 = (input[i-1][2]+dp[compatible[i]],compatible[i])
		opt2 = (dp[i-1],-1)
		max_opt = max(opt1,opt2)
		#print opt1,opt2,max_opt,dp[i-1]
		dp[i] = max_opt[0]
		pre[i] = max_opt[1]
		i += 1
	print "optimal value is, ",dp[-1]
	path = []
	reconstruct_pre(pre,path,len(input))
	print "schduling path is, ", path
	print dp
	print pre
def reconstruct_pre(pre,path,idx):
	if idx == 0:
		return
	elif pre[idx] == -1:
		reconstruct_pre(pre,path,idx-1)
	else:
		path.insert(0,idx)
		reconstruct_pre(pre,path,pre[idx])

input = [[1,4,1],[3,5,2],[0,6,10],[4,7,4],[3,8,5],[5,9,6],[6,10,7],[8,11,8]]  #[start,end,weight]
weighted_interval_scheduling(input)
