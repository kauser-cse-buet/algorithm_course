'''
T(n) = n + T(n/2), is in Theta(n)
T(n) = n + 2T(n/2), is in Theta(n log n)
T(n) = n + 3T(n/2), is in Theta(n^(log_2 3))
T(n) = n + 4T(n/2), is in Theta(n^2)

T(1) = c
T(n) = n + T(n/2) = n + n/2 + T(n/2^2) = n + n/2 + n/2^2 + T(n/2^3)
T(n) = n + n/2 + n/2^2 + n/2^3 + T(n/2^4)
T(n) = n + n/2 + n/2^2 + n/2^3 + ..... + n/2^(k-1) + T(n/2^k)
Stop when n/2^k = 1 or k = log_2(n)
T(n) = n*(1 + 1/2 + 1/2^2 + 1/2^3 + .... + 1/2^(log_2(n)-1)) + T(1)
T(n) < 2n, so T(n) is in O(n)
T(n) > n, so T(n) is in Omega(n)

----------------------------------

T(1) = 1
T(n) = n + 2T(n/2) = n + 2( n/2 + 2T(n/2^2) ) = 2n + 2^2 T(n/2^2)
T(n) = 2n + 2^2 ( n/2^2 + 2T(n/2^3) ) = 3n + 2^3 T(n/2^3)
T(n) = k*n + 2^k * T(n/2^k)
When k=log_2(n), we stop.
T(n) = log_2(n) * n + 2^(log_2(n)) * T(1) = n*log_2(n) + n*1
So, T(n) is in Theta(n log n)

----------------------------------

T(1) = 1
T(n) = n + 3T(n/2) = n + 3( n/2 + 3T(n/2^2) )
	= n + (3/2)*n + 3^2*T(n/2^2)
T(n) = n + (3/2)*n + 3^2* (n/2^2 + 3*T(n/2^3))
T(n) = n + (3/2)*n + (3/2)^2*n + 3^3*T(n/2^3)
T(n) = n + (3/2)*n + (3/2)^2*n + 3^3*(n/2^3 + 3*T(n/2^4))
T(n) = n + (3/2)*n + (3/2)^2*n + (3/2)^3 + 3^4*T(n/2^4))
T(n) = n*(1 + 3/2 + (3/2)^2 + ..... + (3/2)^(k-1)) + 3^k*T(n/2^k)
T(n) = n*(2*((3^log_2(n) / n) -1)) + 3^log_2(n)
T(n) = 2*3^log_2(n) + 3^log_2(n) - n, is in Theta(n^(log_2 3))

1 + 3/2 + (3/2)^2 + ..... + (3/2)^(k-1) = ((3/2)^log_2(n) - 1)/(3/2-1)


T(n/2^3) = n/2^3 + 3*T(n/2^4)
'''