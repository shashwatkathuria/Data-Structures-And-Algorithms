# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:43:43 2018

@author: shash
"""

def input(filename):
	with open(filename, 'r') as f:
		w, n = map(int, f.readline().rstrip().split(' '))
		values, weights = zip(*[map(int, line.rstrip().split(' ')) for line in f])
	return w, n, values, weights

def solve_1(filename):
	w, n, values, weights = input(filename)

	dp = [[0] * (w+1) for _ in range(n+1)]

	for i in range(1, n+1): # current item is weights[i-1] & values[i-1]
		for k in range(0, w+1):		# current size is k
			if k < weights[i-1]:
				dp[i][k] = dp[i-1][k]
			else:
				dp[i][k] = max(dp[i-1][k], dp[i-1][k-weights[i-1]] + values[i-1])

	return dp[n][w]



def solve_2(filename):
	w, n, values, weights = input(filename)
	def helper(memo, size, i):
		if size == 0 or i == 0:
			return 0


		if (size, i) in memo:
			return memo[(size, i)]

		if size < weights[i-1]:
			t = helper(memo, size, i-1)
		else:
			t = max( helper(memo, size, i-1), 
				     helper(memo, size-weights[i-1], i-1) + values[i-1] )
		memo[(size, i)] = t
		return t

	memo = {}
   
	return helper(memo, w, n)

if __name__ == '__main__':
	max_value = solve_2('BigKnapsack.txt')
	print (max_value)

	# import sys	
	# sys.setrecursionlimit(10000)
	# max_value = solve_2('knapsack_big.txt')
	# print max_value