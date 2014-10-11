from random import randint

def compute_modulo(number, exponent, modulo):
    """ Fastest way how to compute modulo numbers. """
    if number > modulo:
        number = number % modulo

    res = 1
    while exponent > 0:
        if exponent % 2 != 0:
            res = (res * number) % modulo
        exponent = int(exponent / 2)
        number = (number**2) % modulo

    return res

def rabin_miller(num, num_k=10):
    """
    Rabin-Miller test for evaluating if number is prime.

    If number is not prime, then it returns False. If number is probably prime,
    then it returns True. K param is number of performed tests.
    """
    num = int(num)
    
    if num is 2:
        return True
    
    num_d = num - 1
    num_r = 0
    while num_d % 2 == 0:
        num_r += 1
        num_d = int(num_d / 2)

    for _ in range(num_k):
        num_a = randint(2, num - 1)
        for i in range(num_r):
            res = compute_modulo(num_a, 2**i * num_d, num)
            if res == num - 1 or (res == 1 and i == 0):
                break
        else:
            return False

    return True

def rabin_generator(max_num, num_k=10):
    """ Fast method to generate prime numbers. """
    prime = 2
    while prime < max_num:
        if rabin_miller(prime, num_k) is True:
            yield prime
        prime += 1

def multiples_generator(value, max_num, multiplicator):
    """ Generator for product numbers. """
    while value <= max_num:
        yield value
        value *= multiplicator



def divide(num):
    """ Find first divisor. """
    cnt = 2
    while cnt < num:
        if num % cnt == 0:
            return cnt
        cnt += 1

    return num

def split_number(cnt, arr):
    """ Splits number into its divisions. """
    div = divide(cnt)
    if div != cnt:
        arr.append(div)
        split_number(int(cnt / div), arr)
    else:
        arr.append(cnt)

def to_histogram(arr):
    """ Returns histogram for values in array. """
    hist = {}
    for value in arr:
        if value in hist:
            hist[value] += 1
        else:
            hist[value] = 1

    return hist



def gcd(val1, val2):
    """ 
    Finds greater common delimiter for two values. Additionally it returns
    matrixes used to search multiplicative inverse element.
    """
    matrix = []
    val1, val2 = sorted([val1, val2])[::-1]

    while val2 != 0:
        matrix.append(((int(val1 / val2), 1), (1, 0)))
        val1, val2 = (val2, val1 % val2)

    return val1, tuple(matrix)

def lcm(val1, val2):
    """ Finds least common multiple for two values. """
    val1, val2 = sorted([val1, val2])[::-1]
    lcm_val = val1

    while lcm_val % val2 != 0:
        lcm_val *= val1

    return lcm_val



def multiply_matrix(mtx1, mtx2):
    """
    Performs multiplication for two matrixes.
    """
    res = [[sum(ea * eb for ea, eb in zip(a, b)) for b in mtx2] for a in mtx1]
    return tuple([tuple(row) for row in res])
