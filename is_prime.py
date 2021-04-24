
"""
This is a simple and fast algorithm to determine if a given number is prime.
>>> is_prime(7)
>>> True
>>> is_prime(123456)
>>> False
"""


def is_prime(num):
    # Keeps track of the number of even divisors. If this number gets higher than 2, then the number is not prime
    divisor_count = 0
    max_tries = 100  # Max number of times the algorithm will test a number. 100 is sufficient.
    common_nums = "0, 2, 4, 6, 8"  # If last digit of num is in this string, num is not prime.
    string_num = str(num)

    if len(string_num) > 1:
        if string_num[-1] in common_nums:
            # If the last digit of num is in common_nums, return False (num is not prime)
            return False

    for i in range(1, max_tries):
        remainder = num % i

        if remainder == 0 and divisor_count < 3:
            # if remainder == 0, then we've found an even divisor.
            divisor_count += 1

        if divisor_count >= 3:
            return False

    return True  # If this line of code is reached, then num is prime. Return True
