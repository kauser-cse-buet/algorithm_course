# written by MD KAUSER AHMMED

'''

running time:


Definition: if f(n) is in O(g(n)), then f(n) <= c * g(n), when n is large. [upper bound]
Definition: if f(n) is in Omega(g(n)), then f(n) >= c * g(n), when n is large. [lower bound]


'''
'''
def f(L):
	sum, n = 0, len(L)
	for i in range(n):
		sum += L[i]

	return sum
'''
#running time in O(n) or O(n^2).

'''
True or false, running time of f is in O(n^2). [True].
O(n)  [True]
O(n ^ 10) [True]
O(1). false

f(n) = 2 + 1 + n <= 2 * n in O(n) when n is large.



'''


'''
10n^2 + 5n in Omega(n^2) 
10n^2 + 5n >= 1 * n^2 for n>1 [here c = 1]. therefore, f(n) is in Omega(n^2)
10n^2 + 5n is in Omeage(n ^ 3) ???

Is it true> 10n^2 + 5n >= c * n^3, when n is large. [Not possible. 10n^2 + 5n is NOT in Omega(n^3)]
proof: n = 1, f(n) = 15. And 15 > c * 1. 

[Answer is false]


10n^2 + 5n is in Omeage(n ^ 2) ??? true, c = 1
10n^2 + 5n is in Omeage(n) ??? true, c = 1
10n^2 + 5n >= n, for n>1

5n is in Omega(1) ? True, c = 1
5n > 1 * 1 for n > 1.


'''


'''
def f(L):
	sum, n = 0, len(L)
	for i in range(n): # i from 0 to n-1
		for j in range (i, n): # j from i to n-1 
			sum += L[i] * L[j]

	return sum

'''

'''
Omega(1)
O(n^2) because f takes at most n^2 steps.
O(n) [false]
Omega(n) [true] line 4 gives n iterations, each of which takes at least 1 step.


let's unroll the loops.
i = 0, inner loop takes n steps.
i = 1, inner loop takes n-1 steps.
i = 2, inner loop takes n - 2 steps.

i = n -1 , inner loop takes 1 step. 

adding all steps: 1 + 2 + 3+ ... + n = n*(n + 1)/2 = .5n^2 + .5n in O(n^2) ??? [true]

.5n^2 + .5n >= 0.5n^2 for n > 1. Therefore, running time is in Omega(n^2).
'''	



'''
Theta(n ^ 2)
Derfinition: f(n) is in Theta(g(n)) is in Theta(g(n)) if f(n) is in both in O(g(n)) and Omega(g(n)).
'''


'''
claim: 1 + 2 + 3 + ... + n = n * (n + 1)/2

n = 1,  
'''

'''
def f(L):
	sum, n = 0, len(L)
	i, j = 1, 0
	while i < n:
		sum += i
		i = i * 2
		print("i", i)

	return sum

print(f([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
'''


'''
iteration 
1 i = 2
2, i = 2 * 2
3, i = 2 * 3
4


k, i = 2^k


2 ^ k = n
therefore, k = log(n) [base 2]
'''

'''


def f(L):
	sum, n = 0, len(L)
	i, j = 1, 0
	while i < n:
		sum += i
		i = i * 2
		for j in range(n):
			sum += i *j

	return sum

print(f([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))

'''
'''
O(nlog(n))
Omega(nlog(n))
Theta(nlog(n))
'''




def f(L):
	if len(L) == 0:
		return 0
	return 1 + f(L[1: len(L)])

print(f([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))



'''
how to calculate number of steps???? recursive function.
'''