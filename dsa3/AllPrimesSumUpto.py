def all_prime_pairs(A):
    # Step 1: Sieve of Eratosthenes
    is_prime = [True] * (A + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(A ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, A + 1, i):
                is_prime[j] = False

    # Step 2: Find all valid pairs
    pairs = []
    for i in range(2, A // 2 + 1):
        if is_prime[i] and is_prime[A - i]:
            pairs.append([i, A - i])
    return pairs