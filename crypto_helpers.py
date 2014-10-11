from functools import reduce
import re, math
from math_helpers import gcd, multiply_matrix
from math_helpers import split_number, to_histogram, lcm


def get_m_n_elements(element, z_value):
    gcd_value, matrixes = gcd(element, z_value)

    if gcd_value is not 1:
        return None

    inverted_matrixes = [((0, 1), (1, -matrix[0][0])) for matrix in matrixes]
    inv_matrix = reduce(multiply_matrix, inverted_matrixes[::-1])

    return inv_matrix


def find_multiplicative_inverse_element(element, z_value):
    matrix = get_m_n_elements(element, z_value)
    if matrix is None:
        return None

    n_val = matrix[0][1]

    return (z_value + n_val) % z_value



def solve_congruence_equation(equation):
    EQUATION_RGX = r'(\d+)\s*\*\s*\w\s*=\s*(\d+)\s*mod\s*(\d+)\s*'

    def is_solution(a_val, b_val, m_val, x_val):
        return a_val * x_val % m_val == b_val

    equation = re.match(EQUATION_RGX, equation)
    if equation is None:
        raise ValueError("Equation must be 'a*x = b mod n' type!")

    a_val, b_val, m_val = [int(val) for val in equation.groups()]
    gcd_val = gcd(a_val, m_val)[0]

    if gcd_val == 1:
        # Exactly one solution
        a_inverse = find_multiplicative_inverse_element(a_val, m_val)
        return [(b_val * a_inverse) % m_val]
    elif b_val % gcd(a_val, b_val)[0] == 0:
        # Exactly multiple solutions
        return [x for x in range(m_val) if is_solution(a_val, b_val, m_val, x)]
    else:
        # No solution
        return []



def euler_function(value):
    count = 0
    for i in range(value):
        if gcd(value, i)[0] == 1:
            count += 1
    return count

def carmichael_function(m_val):    
    if m_val is 1:
        # 1th Case -> if m = 1
        return 1

    value = 2**3
    alfa = 3
    while value < m_val:
        value *= 2
        alfa += 1

    if value == m_val:
        # 2nd Case -> if m = 2**a, a > 2
        return 2**(alfa - 2)

    arr = []
    split_number(m_val, arr)
    hist = to_histogram(arr)

    if m_val in [2, 4] or (len(hist) == 1 and list(hist.keys())[0] > 2):
        # 3rd Case -> if m = 2, 4, p**a where p is prime > 2
        return euler_function(m_val)

    # 4th Case -> NSN(Carm(p_1**a_1), Carm(p_2**a_2), ..., Carm(p_n ** a_n))
    values = [carmichael_function(p**a) for p, a in hist.items()]
    val1 = values.pop(0)
    while values:
        val1 = lcm(val1, values.pop(0))

    return val1



def solve_quadratic_equation(equation):
    def is_solution(a_val, b_val, m_val, x_val):
        return x_val**a_val % m_val == b_val
    
    EQUATION_RGX = r'x\*{2}(\d+)\s*=\s*(\d+)\s*mod\s*(\d+)'
    equation = re.match(EQUATION_RGX, equation)
    if equation is None:
        raise ValueError("Equation must be 'x**a = b mod n' type!")
    
    a_val, b_val, m_val = [int(val) for val in equation.groups()]
    return [x for x in range(1, m_val) if is_solution(a_val, b_val, m_val, x)]



def solve_chinese_remainder_theorem(equations):
    EQUATION_RGX = r'x\s*=\s*(\d+)\s*mod\s*(\d+)'
    values = []
    for equation in equations:
        result = re.match(EQUATION_RGX, equation)
        if result is None:
            raise ValueError("Equation must be 'x = a mod m' type!")
        values.append([int(val) for val in result.groups()])

    x_val = None
    z_val = 1
    for row in values:
        a_val, m_val = row
        if x_val is None:
            x_val = a_val
            z_val *= m_val
            continue

        matrix = get_m_n_elements(m_val, z_val)
        if matrix is None:
            return None

        u_val = matrix[0][0] if int(math.fabs(matrix[1][0])) == m_val else matrix[0][1]
        x_val = x_val + u_val * (a_val - x_val) * z_val
        z_val *= m_val

    return x_val % z_val
