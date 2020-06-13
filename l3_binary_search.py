# Created by MD KAUSER AHMMED
# Dated: 08/30/2016

'''

Mathematical induction is a technique to reason about correctness of a program.

goal: prove P is correct for all input sizes. 

To accomplice this goal we have to carry out 2 steps:

1) Prove p is correct for smallest steps.
2) Prove that, if P is correct for 0,1,2,3, ..., k input sizes, 
				then P is also true for size k + 1

'''
'''
def R(L): 
	if len(L) == 0:
		return []
	else:
		return R(L[1: len(L)]) + [L[0]]


print(R([1,2,3,4]))
'''


'''
Mathmatical induction:
1) R is correct for input size 0. (line #19, 20)
2) Assume R is correct for input sizes 0,1,2,...,k.
let say L has k + 1 items.
So, R[L] returns (line 22) R(L[1: len(L)]) + L[0] 
this return value is: reverse of L[1: len(L)] + [L[0]],
which is the reverse of L. 

Therefore, R is correct for all input sizes.

Mathematical induction on input [1,2,3,4,5,6]
R([1,2,3,4,5,6]) returns R([1,2,3,4,5,6]) + [1]

assumes that R returns correct values for input sizes less than 6 => [6,5,4,3,2].
So function will also return correct result for [6,5,4,3,2,1].

Without the (base case reasoning) i.e. prove 1 is incomplete.

'''

#binary search: recursive
'''
def search(x,L, left, right):
	if left > right: 
		return False
	mid = (left + right) // 2

	if x == L[mid]:
		return True
	if x > L[mid]:
		return search(x, L, mid + 1, right)
	else:
		return search(x, L, left, mid - 1)

L = [1,2,3,4,5,6]
print(search(2, L, 0, len(L) - 1))
'''


#binary search: iterative

def search(x, L):
	left, right = 0, len(L) - 1

	while(left <= right):
		mid = (left + right)//2
		if x == L[mid]:
			return True

		if x > L[mid]:
			left = mid + 1
		else:
			right = mid - 1

	return False

print(search(1, [1,2,3,4]))

