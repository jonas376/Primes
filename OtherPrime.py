import datetime
def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    startTime = datetime.datetime.now()
    factors = []
    d = 2
    counter = 0
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
        counter = counter + 1
    endTime = datetime.datetime.now()
    timePassed = endTime - startTime
    # print("counter = ", counter)
    # print(str(timePassed))
    return str(timePassed), factors





# pfs = prime_factors(1000)
# largest_prime_factor = max(pfs) # The largest element in the prime factor list