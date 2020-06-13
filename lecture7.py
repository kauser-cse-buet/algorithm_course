'''
abstract framework of mathematical induction

1. Prove your program works correctly on smalledst input sizes. 
2. Prove that "if your program works correctly on input size less than k+1, 
it also works correctly on input size k+1."
'''

def my_length(L):
	if L[]: return 0
	return 1 + my_length( [1:] )

'''
Tracing... is tedious especially for complicated programs. 
Here is inductive reasoning:
1. my_length is correct for smallest lists (empty lists). Why? line 10.
2. let's say L has length k+1. If we presume that my_length works correctly for input size less tha k+1, then 
the recursive call on line 9 returns kbecause the length of L[1:] is k. 

Therefore, the program returns 1+k (line 11), which is correct length of L. 
'''
