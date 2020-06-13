'''
T(n) = n^d + aT(n/b)
(1) if d=log_b(a), T(n) is in Theta(n^d log n)
(2) if d != log_b(a), T(n) is in Theta(n^max{d, log_b(a)})

'''
# T(n)  = c + T(n-1)
#S(n) = c + S(n-1) is also in Theta(n)
def M(A,B): 
	if A == []:
		return B
	if B == []:
		return A
	if A[0] < B[0]:
		return [A[0]] + M(A[1:], B)
	else:
		return [B[0]] + M(A, B[1:])



#input: unsorted list of numbers
# output: a sorted list of numbers in L 
# T(n) = 1 + 2 * T(n/2), in Theta(n)
#S(n) = 
def Sort(L): # S(n) = 2*S(n/2), in Theta(n log n)
	if len(L) <= 1:
		return L

	mid = len(L)//2

	A = Sort(L[:mid])
	# L[:mid] -> n/2
	#S(n/2)

	B = Sort(L[mid:]) #S(n/2)

	return M(A, B)

a =[1,2,3]
b=[-2,-1,10] 
print(M(a,b))

print(Sort([-1,-2,1,10,2,9]))

def random_list(n):
	import random
	return [random.randint(0,20) for x in range(n)]

rndList = random_list(10)
print(rndList)
print(Sort(rndList))
