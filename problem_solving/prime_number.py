# prime_checker.py
# This script checks if a number is prime
# and prints all prime numbers up to a given number.

def is_prime(n):
    # A number less than 2 is not prime
    if n < 2:
        return False
    # Check for factors from 2 to square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_up_to(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]

# Example usage
if __name__ == "__main__":
    number = 30
    print(f"Prime numbers up to {number}: {list_primes_up_to(number)}")
    