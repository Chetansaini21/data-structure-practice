def fibonacci(num):
    # fibonacci is only for positive integers
    assert num>=0 and int(num)==num, 'Fibonacci number cannot be negative number or non integer.'
    if num in [0,1]:
        return num
    else:
        fn = fibonacci(num-1) + fibonacci(num-2)
        return fn

print(fibonacci(6))