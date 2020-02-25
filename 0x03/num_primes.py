import math
import sys
import time

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    max_prime = int(sys.argv[1])
    num_primes = 0
    start = time.time()
    for maybe_prime in range(2, max_prime):
        if is_prime(maybe_prime):
            num_primes += 1
    elapsed = time.time() - start

    print("Number of primes below {} is {}, spend {:f}s".format(max_prime, num_primes, elapsed))
