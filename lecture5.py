'''
assignment 2 today. next tuesday.
'''

# assignment 1 solution.

'''

def depth(T):
	if T is None:
		return -1
	if T.right is None and T.left is None:
		return 0
	return 1 + max(depth(T.right), depth(T.left))

(1) In case T is empty or nil, depth works correctly.
(2) Input size or number of nodes of T is k + 1. And assume Depth works correctly for input size 0, 1, 2, ..., k. 
T.left and T.right, each has fewer than k + 1 nodes. 
Then, Depth(T.left) and Depth(T.right) return the correct depths for the left and right subtrees.
So, 1 + max( depth of left subtree , depth of right subtree ) is the correct answer. 
Therefore, Depth is correct for T with input size k + 1.

-------
Claim: Depth works correctly for trees of any depth.
Induction on depth of trees.
(1) Smallest depths -1 and 0. Depth works correctly.
(2) Assume Depth works correctly for trees of depth 0, 1, ..., k.
Assume that depth of T is k + 1. 
Then, depths of left subtree and right subtree are less than k + 1.
So, depths of T is exactly 1 + max {depth of left tree, depth of right tree}
And Depth(T.left) and Depth(T.right) correctly return the values (by assumption).


#-----------------


def palindrome(s):
	if len(s) <= 1:
		return True

	return s[0] == s[len(s) - 1] and palindrome(s[1: len(s) - 1])



'''



def f(L):
	n = len(L)
	i = 1
	sum = 0
	while i <= n:
		for j in range(n):
			sum += (i * j)
		i = i * 2


'''
step 0, i=1
step 1, i=2
step 2, i=2^2
...
step k, i=2^k
If loop exists after k steps, then 2^k = n. Therefore, k = log_2 n

each step is of n  for j. 

'''


def f(L):
	if len(L) <= 1:
		return 1
	x = f(L[1: len(L)])
	return x + 1

# Theta(n)


'''
# Define T(n) to be the running time of f for input size n.
T(n) = c + T(n-1) = c + c + T(n-2) = 3c + T(n - 3) [after 3 steps]
T(n-1) = c + T(n-1-1) = c + T(n-2)
T(n-2) = c + T(n-2-1) = c + T(n-3)

after k steps, T(n) = kc + T(n-k)
f stops when L has 0 items. In other words n-k=0, n=k.

T(0) = 1
T(n) = nc + T(n-n) = nc + T(0) = n*c + 1 [for k = n]
     = n*c + 1, is in Theta(n)
'''

def f(L):
	if len(L) <= 1:
		return 1
	x = f(L[0: len(L)//2])
	return x + 1

# Theta(log(n))

'''
Define T(n) to be the running ...
T(n) = c + T(n/2) = c + c + T(n/2*2) = 2c + T(n/2*2)
     = 3c + T(n/2^3)

for k steps, T(n) = kc + T(n/2^k)

T(1) = 1

n/2^k = 1
=> n = 2^k
=> k = log_2 n

for k = log_2 n
T(n) = log_2 n * c + T(n / n) = log_2 n * c + 1
     = log_2 n * c + 1 is in Theta(log n)


T(n/2) = c + T(n/2*2)

'''

def h(L):
	if len(L) <= 1:
		return 1
	a = f(L[0: len(L)//2])
	b = 1 + f(L[1: len(L)])
	return a + b


'''
Define T(n) to be the running ...
T(n) = c + T(n/2) + T(n-1)
'''
