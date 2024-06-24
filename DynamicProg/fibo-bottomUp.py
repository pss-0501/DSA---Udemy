
counter = 0

def fib(n):
    global counter

    my_list = [0,1]

    for i in range(2,n + 1):
        counter += 1
        next_fib = my_list[i - 1] + my_list[i - 2]
        my_list.append(next_fib)
    return my_list[n]


n = 20 

print("\nFib of", n, "=", fib(n))
print('\nCounter:', counter)