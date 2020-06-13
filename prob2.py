'''

md kauser ahmmed

T(n) = n + 2 * T(n/2) = n + 2 ( n/2 + 2 * T(n/2^2)) = 
= 2 * n + 2^2 * T(n/2^2)
= 3 * n + 2 ^ 3 T

 = n (1 + 1/2 + 1/2^2 + ... + 1/2^(k-1)) + 2 * T(n/2^k)
= n (1 + 1/2 + ... + 1/2^(log_2 n - 1)) + 2 * 1 < 2n + 1

2n + 1 < 2n + n < 3n, is in O(n)
2n + 1 > n , is in Omega(n)
 is in Theta(n)


1 + 1/2 + ... + 1/2^(log_2 n - 1) < 2 


T(n/2) = n/2 + 2 * T(n/2^2)
T(n/4) = n/4 + 2 * 
n = 2^k
k = log_2(n)
'''