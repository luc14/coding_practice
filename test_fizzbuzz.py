import sys
import io
import fizzbuzz

def test_fizzbuzz():
    s = io.StringIO()
    fizzbuzz.print_result(10, where=s)
    result = s.getvalue().splitlines()
    assert result == ['1', '1', 'BuzzFizz', 'Buzz', 'Fizz', '8', 'BuzzFizz', 'Buzz', '34', 'Fizz']

    assert fizzbuzz.translate_fibonacci(15) == 'FizzBuzz'
    assert fizzbuzz.translate_fibonacci(333) == 'Buzz'
    assert fizzbuzz.translate_fibonacci(500) == 'Fizz'
    assert fizzbuzz.translate_fibonacci(11) == 'BuzzFizz'
    assert fizzbuzz.translate_fibonacci(104) == 104

    assert fizzbuzz.is_prime(20) == False
    assert fizzbuzz.is_prime(13) == True

    assert list(fizzbuzz.generate_fibonacci(8)) == [1,1,2,3,5,8,13,21]
