"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking
any two primes and concatenating them in any order the result
will always be prime. For example, taking 7 and 109, both 7109
and 1097 are prime. The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two
primes concatenate to produce another prime.
"""


def prime_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, n):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    primes = []
    for j in range(n + 1):
        if sieve[j]:
            primes.append(j)
    return sieve, primes


def is_prime(n):
    if (n <= 3):
        return n > 1
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True


def make_pairs(a, upper_bound):
    pairs = set()
    for b in range(a + 1, upper_bound):
        if (is_prime(int(f"{primes[a]}{primes[b]}")) and
                is_prime(int(f"{primes[b]}{primes[a]}"))):
            pairs.add(primes[b])
    return pairs


limit = 30000

sieve, primes = prime_sieve(limit)

upper_bound = len(primes)

result = 2147483647

pairs = [0] * (upper_bound + 1)

for a in range(1, upper_bound):
    if (primes[a] * 5 >= result):
        break
    if (pairs[a] == 0):
        pairs[a] = make_pairs(a, upper_bound)
    testSet = pairs[a]

    for b in range(a + 1, upper_bound):
        if (primes[a] + primes[b] * 4 >= result):
            break
        if (primes[b] not in testSet):
            continue
        if (pairs[b] == 0):
            pairs[b] = make_pairs(b, upper_bound)
        tempA = testSet.copy()
        testSet = testSet.intersection(pairs[b])
        if (len(testSet) == 0):
            testSet = tempA
            continue

        for c in range(b + 1, upper_bound):
            if (primes[a] + primes[b] + primes[c] * 3 >= result):
                break
            if (primes[c] not in testSet):
                continue
            if (pairs[c] == 0):
                pairs[c] = make_pairs(c, upper_bound)
            tempB = testSet.copy()
            testSet = testSet.intersection(pairs[c])
            if (len(testSet) == 0):
                testSet = tempB
                continue

            for d in range(c + 1, upper_bound):
                if (primes[a] + primes[b] + primes[c] +
                        primes[d] * 2 >= result):
                    break
                if (primes[d] not in testSet):
                    continue
                if (pairs[d] == 0):
                    pairs[d] = make_pairs(d, upper_bound)
                tempC = testSet.copy()
                testSet = testSet.intersection(pairs[d])
                if (len(testSet) == 0):
                    testSet = tempC
                    continue

                e = min(testSet)

                if (primes[a] + primes[b] + primes[c] +
                        primes[d] + e < result):
                    result = primes[a] + primes[b] + primes[c] + primes[d] + e

                print(result)

                print([primes[a], primes[b], primes[c], primes[d], e])

                testSet = tempC

            testSet = tempB

        testSet = tempA
