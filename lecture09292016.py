prices = [10, -20, 5, 15, 0, -10, 15, -20, 7, 15]

#find the interval that gives the maximum sum


def brute_force(L):
	# compute all possible sums, keep  track of maximum 
	# return max sum and the interval

	ms, interval = L[0], [0,0]

	for i in range(len(L)):
		for j in range(i, len(L)):
			cur_sum = 0
			for k in range(i, j+1):
				cur_sum = cur_sum + L[k]

			if cur_sum > ms:
				ms = cur_sum
				interval = [i,j]

	
	return ms, interval

def brute_force2(L):
	# compute all possible sums, keep  track of maximum 
	# return max sum and the interval

	ms, interval = L[0], [0,0]

	for i in range(len(L)):
		sum_i2j = 0
		for j in range(i, len(L)):
			sum_i2j += L[j]

			if ms < sum_i2j:
				ms, interval = sum_i2j, [i, j]

			print(i, j, L[i:j+1], sum_i2j)
	
	return ms, interval

def left_sum(L, left, right):
	ms, cur_sum = L[right], 0
	for i in range(right, left-1, -1):
		cur_sum += L[i]
		if cur_sum > ms:
			ms = cur_sum

	return ms

def right_sum(L, left, right):
	ms, cur_sum = L[left], 0

	for i in range(left, right + 1):
		cur_sum += L[i]

		if(cur_sum) > ms:
			ms = cur_sum

	return ms

def max_sum(L, left, right):
	if len(L) == 1:
		return L[0]


	mid = (left - right + 1)//2

	#compute max sum of two halves.

	maxLeft = left_sum(L, left, mid-1)
	maxRight = right_sum(L, mid+1, right)

	#compute max sum of overlapping interval
	overlappingSum = max_sum(prices, left, right)

	return max(maxLeft, overlappingSum, maxRight)


#print(list(range(10,5, -1)))
#print(brute_force2(prices))

#print(len(prices)//2)
#print(left_sum(prices, 0, len(prices)//2))

#print(right_sum(prices, len(prices)//2, len(prices) - 1))

#print(max_sum(prices, 0, len(L)-1)

print(max_sum(prices, 0, len(prices) - 1))