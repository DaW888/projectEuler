def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    else:
        return True


def primeFactor(number):
    factors = []
    if isPrime(number):
        factors.append(number)
        return False

    for i in range(2, int(number ** 0.5 + 1)):
        if isPrime(i) and number % i == 0:
            factors.append(i)
    print(factors)


primeFactor(600851475143)