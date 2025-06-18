# 🎯 Problem: Count how many prime numbers are less than n
# 📘 Concept: Sieve of Eratosthenes
# 💡 Example: n = 10 → Primes are [2,3,5,7] → Count = 4

def count_primes(n):
    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(is_prime)

# ✅ Test
print(count_primes(10))  # Output: 4
