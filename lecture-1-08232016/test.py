
def MAX(L):
	if len(L) == 1:
		return L[0]
	m= MAX(L[1 : len(L)])
	if m < L[0]:
		return L[0]
	return m

print(MAX([1,5,9,4]))
#print(MAX([]))  # generate error for this output.
print(MAX([1,5,9,4]))

'''
MAX is correct when input size is 1. (lines 3-4)
Assume that MAX is correct for input size 1,2,...., k, and L has k+1 elements.
Say, L = [x_1, x_2, ...., x_k+1]
then, line 5,
m = MAX([x_2, x_3], ..., x_k+1])
m is largest element among x_2, x_3, . , x_k+1
lines 6-8: m is the largest among x_1, x_2, ..., x_k+1. Therefore, MAX is correct for input size k+1.

Therefore, MAX is correct for all input sizes (except input size 0).

GOAL: prove P is correct fot all input sizes:
Induction has 2 steps:
(1) Prove P is correct for all smallest irreducible inputs.
(2) Prove: "If P is correct for input sizes 0,1,2, ...., k, "
			then P is also correct for input size k+1." (for any k)"

After  carrying out these 2 steps, Why is P correct for all inputs?
Is P correct for input size 0? Yes, because (1)
Is P correct for input size 1? Yes, 
	because in (2), "If P is correct for input size 0, then it is correct for input size 1."
Is P correct for input size  2? Yes
because in (2), "If P is correct for input size 0,1, then P is correct for input size 2."



def MAX(L):
	if len(L) == 1:
		return L[0]
		m= MAX(L[1 : len(L)])
		return m


def MAX(L):
	if len(L) == 1:
		return L[0]
		m= MAX(L)
		if m < L(0):
			return L[0]
		return m

'''		


'''
my note: 

define getMax(L):
	if len(L) == 1:
		return L[0]
	m = getMax(L[1: len(L)])
	if L[0] > m:
		return L[0]
	return m

Here, 
step 1-> getMax is correct for input size n = 1, 
step 2-> prove : if getMax is correct for input size n = m, 
		      then it will be also correct for input size n = m + 1

here, 
size of L = k,
m = getMax(L[1: len(L)]), let we assume getMax is correct for input size = k - 1; i.e. getMax(1: len(L)) is correct. 

now,
define getMax(L):
	if L[0] > m:
		return L[0]
	return m

getMax is correct for k.

so, step 2 is also proved. 

so, this recursive function is correct [proved by mathmatical induction].

''' 
