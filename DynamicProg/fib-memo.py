
counter = 0
memo = 100 * [None]

def fib(n):
    global counter
    counter += 1

    if memo[n]:
        return memo[n]

    if n == 0 or n == 1:
        return n
    
    memo[n] =  fib(n-1) + fib(n-2)
    return memo[n]


n = 20 

print("\nFib of", n, "=", fib(n))
print('\nCounter:', counter)