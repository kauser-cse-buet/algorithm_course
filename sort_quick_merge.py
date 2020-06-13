# quick sort , merge sort , space complexity reduce by in place sort by pointer. 

import random

def random_list(n, Min, Max):
	return [ random.randint(Min,Max) for i in range(n) ]
'''

if __name__ == '__main__':
	for i in range(10):
		print(random_list(20,-100,100))
'''
L = [19,2,3,5,59,30,68,8,945,56,77,23,133]

# quick sort start

def lessThan(L, n):
	return [x for x in L if x < 100]

#print(lessThan(L, 100))

def le(L, p):
	return [x for x in L if x <= p]


def gt(L, p):
	return [x for x in L if x > p]


def Sort(L):
	if len(L)  <= 1:
		return L

	p = L[0]

	A = le(L[1:], p)
	B = gt(L[1:], p)

	return Sort(A) + [p] + Sort(B)

def quickSort(L):
	if len(L) <= 1:
		return L

	pivot = L[0]
	A = [x for x in L[1:] if x <= pivot]
	B = [x for x in L[1:] if x > pivot]

	return quickSort(A) + [pivot] + quickSort()

def Split(L, left, right, pivot):
	pivot = L[left]

	l, r = left + 1, right

	while l <= r: 
		if pivot <= L[l]:
			L[l], L[r] = L[r], L[l]
			r = r - 1
		else:
			l = l + 1

	L[left], L[l-1] = L[l-1], L[left]

	return l - 1

def Sort2(L, left, right):
	if left < right:
		pivot = L[left]
		i = Split(L, left, right, pivot)

		Sort2(L, left, i - 1)
		Sort2(L, i + 1, right)

'''
(average casse, assuming a good split) Time complexity: 
T(n) = 2n + 2T(n/2) is in Theta(n log n)
Space complexity 
S(n) = n + 2S(n/2) is in Theta(n log n)
S(n) = c + 2S(n/2) is in Theta(n)
'''


# quick sort end

L = random_list(20, 1, 50)

print('List: ', L)
Sort2(L, 0, len(L)-1)
print(L)



