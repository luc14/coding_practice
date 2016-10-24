'''generates, translates and prints Fibonacci numbers
'''
def generate_fibonacci(n):
    '''yields n fibonacci numbers.
    '''
    for i in range(n):
        if i < 2:
            yield 1
            continue
        if i == 2:
            f1, f2 = 1, 1
        f1, f2 = f2, f1+f2
        yield f2

def is_prime(n):
    '''returns True if n is a prime; otherwise returns False.
    '''
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def translate_fibonacci(f):
    '''
    Args: f is a positive integer.

    Returns:
    "Buzz" when f is divisible by 3 but not by 15.
    "Fizz" when f is divisible by 5 but not by 15.
    "FizzBuzz" when f is divisible by 15.
    "BuzzFizz" when f is prime.
    the value f otherwise.
    '''
    if f%15 == 0:
        return "FizzBuzz"
    if f%3 == 0:
        return "Buzz"
    if f%5 == 0:
        return "Fizz"
    if is_prime(f):
        return "BuzzFizz"
    return f

def print_result(n, where=None):
    '''prints the first n translated fibonacci numbers according to translate_fibonacci function.
    prints the result to file-object if where is not None.
    '''
    for f in generate_fibonacci(n):
        result = translate_fibonacci(f)
        print(result, file=where)
