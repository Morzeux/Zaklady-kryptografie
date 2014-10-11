from math_helpers import gcd, multiply_matrix
from crypto_helpers import find_multiplicative_inverse_element
from crypto_helpers import solve_congruence_equation
from crypto_helpers import euler_function
from crypto_helpers import carmichael_function
from crypto_helpers import solve_quadratic_equation

def unit_test(func):
    def wrapper(*args, **kwargs):
        print('Testing \'%s\'... ' % func.__name__, end='')
        try:
            res = func(*args, **kwargs)
        except:
            print('Fail')
            raise
        else:
            print('OK')
            return res
    return wrapper

################ TOOLS ###############

@unit_test
def test_gcd():
    assert gcd(13, 6) == (1, (((2, 1), (1, 0)),
                              ((6, 1), (1, 0))))
    assert gcd(316, 128) == (4, (((2, 1), (1, 0)),
                                 ((2, 1), (1, 0)),
                                 ((7, 1), (1, 0)),
                                 ((2, 1), (1, 0))))

@unit_test    
def test_multiply_matrix():
    assert multiply_matrix(((0, 1), (1, -6)), ((0, 1), (1, -2))) == ((1, -2), (-6, 13))

############## Multiplicative Inverse Element ##########

@unit_test
def test_multiplicative_inverse():
    assert find_multiplicative_inverse_element(6, 13) == 11 
    assert find_multiplicative_inverse_element(3, 7) == 5
    assert find_multiplicative_inverse_element(5, 13) == 8
    assert find_multiplicative_inverse_element(3, 5) == 2
    assert find_multiplicative_inverse_element(2, 10) == None
    assert find_multiplicative_inverse_element(9, 14) == 11
    assert find_multiplicative_inverse_element(11, 91) == 58
    assert find_multiplicative_inverse_element(17, 17) == None
    assert find_multiplicative_inverse_element(23, 79) == 55
    assert find_multiplicative_inverse_element(11, 29) == 8

################ Congruence equation ######################

@unit_test
def test_solve_congruence_equations():
    assert solve_congruence_equation("5*x = 1 mod 27") == [11]
    assert solve_congruence_equation("5*x = 3 mod 27") == [6]
    assert solve_congruence_equation("6*x = 5 mod 12") == []
    assert solve_congruence_equation("10*x = 6 mod 12") == [3, 9]
    assert solve_congruence_equation("11*x = 22 mod 77") == [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72]
    assert solve_congruence_equation("12*x = 7 mod 24") == []

############## EULER AND CARMICHAEL FUNCTIONS #################

@unit_test
def test_euler_function():
    assert euler_function(4) == 2
    assert euler_function(11) == 10
    assert euler_function(10) == 4
    assert euler_function(12) == 4
    assert euler_function(20) == 8
    assert euler_function(25) == 20
    assert euler_function(100) == 40
    assert euler_function(1024) == 512
    #assert euler_function(512**24) == 4096

@unit_test
def test_carmichael_function():
    assert carmichael_function(4) == 2
    assert carmichael_function(11) == 10
    assert carmichael_function(10) == 4
    assert carmichael_function(12) == 2
    assert carmichael_function(20) == 4
    assert carmichael_function(25) == 20
    assert carmichael_function(100) == 20
    assert carmichael_function(1024) == 256
    #assert euler_function(512**24) == 1024

############## QUADRATIC EQUATIONS ############

@unit_test
def test_solve_quadratic_equation():
    assert solve_quadratic_equation('x**2 = 1 mod 21') == sorted([1, 8, 13, 20])
    assert solve_quadratic_equation('x**2 = 1 mod 221') == sorted([1, 118, 220, 103])
    assert solve_quadratic_equation('x**2 = 1 mod 385') == sorted([1, 351, 34, 274, 76, 384, 111, 309])
    assert solve_quadratic_equation('x**2 = 1 mod 105') == sorted([1, 29, 41, 34, 64, 71, 76, 104])
    assert solve_quadratic_equation('x**2 = 1 mod 209') == sorted([1, 56, 153, 208])

############## GLOBALS ##############

def run_tests():
    for obj in globals().values():
        if hasattr(obj, '__call__') and obj.__name__ == 'wrapper':
            obj()

run_tests()
