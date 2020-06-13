# Written by Md. Kauser Ahmmed

'''
L = [1,2,3,4,5,6]

def mystery(L):
	if len(L) == 0:
		return 0;
	return 1 + mystery(L[1: len(L)])


print(mystery([1,2,3,4,5,6]))
'''

'''

mystery(L) return length of L
(1) mystery is correct when L has 0 items.
(2) say L has k+1 items.
Assume mystery is correct for input sizes 0,1,2,.....,k.
line 4 return 1 + k. so, mystery does what it is supposed to do. 

what this means is: 
mystery is correct for input size 0.
mystery is correct for input size 1.
mystery is correct for input size 2.



#reversing a list

def mystery(L):
	if len(L) == 0:
		return []
	else:
		return mystery(L[1:len(L)]) + [L[0]]

print(mystery([1,2,3,4,5]))		

claim: mystery reverses L.
(1) input size is 0.
(2) input size is greater than 0.
line 35 returns the concatanition of reverse of L[1:end] and L[0]
this means mystery is correct.

line 5 



def mystery(L):
	if len(L) == 0:
		return []
	else:
		return mystery(L[1:len(L)]) + [L[0]]

print(mystery([1,2,3,4,5]))

#mystery([1,2,3,4,5,6]) -> mystery([2,3,4,5,6])	+ [1] -> mystery([3,4,5,6]) + [2] + [1]

def mystery(L):
	if len(L) == 0:
		return []
	else:
		return [L[0] * L[0]] + mystery(L[1:len(L)]) 

print(mystery([1,2,3,4,5,6]))
# mystery([1,2,3,4,5,6]) -> [1] + mystery([2,3,4,5,6]) -> [1] + [4,9,16,25,36]



def mystery(L):
	return [ x * x for x in L if x % 2 == 0]

print(mystery([1,2,3,4,5,6]))
'''

def le(L, p):
	return [ x for x in L if x < p]

def gt(L,p):
	return [ x for x in L if x > p]

def sort(L):
	if len(L) == 0:
		return []
	else:
		a = le(L[1: len(L)], L[0])
		b = gt(L[1: len(L)], L[0])

	return sort(a) + [L[0]] + sort(b)
	
#print(le([20,58,25, 9, 10, 16, 39, 77, 65], 30))
#print(gt([20,58,25, 9, 10, 16, 39, 77, 65], 30))
print(sort([20,58,25, 9, 10, 16, 39, 77, 65]))

