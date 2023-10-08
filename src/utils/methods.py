from sympy.core.expr import UnevaluatedExpr
from sympy.functions import Abs
from sympy.core import diff
from sympy.abc import x

def calculate_two_points(func, x_val, h_val):
    point_one = func.subs({x: x_val})
    point_two = func.subs({x: x_val + h_val})
    result = (point_two - point_one)/h_val
    error = Abs((h_val/2)*diff(diff(func, x), x).subs({x: x_val}))
    # error = (h_val/2)*(diff(Derivative(func)), x_val)
    return round(result, 5), round(error, 5)
        

def calculate_three_points(func, x_val, h_val):
    point_one = func.subs({x: x_val - h_val})
    point_two = func.subs({x: x_val + h_val})
    result = float((point_two - point_one)/(2*h_val))
    error = float(Abs(((h_val**2)/6)*diff(diff(diff(func, x), x),x).subs({x: x_val})))
    return round(result, 7), round(error, 7)

def calculate_five_points(func, x_val, h_val):
    val_1= func.subs({x: x_val - 2*h_val})
    val_2 = 8*func.subs({x: x_val - h_val})
    val_3 = 8*func.subs({x: x_val + h_val})
    val_4 = func.subs({x: x_val + 2*h_val})
    result = float((val_1-val_2+val_3-val_4)/(12*h_val))
    fifth_derivative = diff(diff(diff(diff(diff(func, x), x), x), x),x)
    error = float(Abs(((h_val**2)/6)*fifth_derivative.subs({x: x_val})))
    return round(result, 10), round(error, 10)


def newton_raphson(func, x_0, tol=1e-4, max_iteration=100):
    derivative = diff(func, x)
    prev = None
    for i in range(max_iteration):
        f_val = func.subs({x: x_0})
        diff_val = derivative.subs({x: x_0})

        prev = x_0
        x_0 = x_0 - (f_val/diff_val)

        if abs(f_val) < tol or round(prev, 6) == round(x_0, 6):
            return round(float(x_0), 6), i + 1
        
    return round(float(x_0), 6), max_iteration

def divided_differences(x_data, fx_data):
    n = len(x_data)
    dd_table = []
    for _ in range(n): dd_table.append([None for _ in range(n)])

    for i in range(n): dd_table[i][0] = fx_data[i]

    for j in range(1, n):
        for i in range(n - j):
            dd_table[i][j] = (dd_table[i + 1][j - 1] - dd_table[i][j - 1]) / (x_data[i + j] - x_data[i])

    return dd_table

def calculate_polynomial_coefficients(x_data, dd_table):
    n = len(x_data)
    coefficients = [dd_table[0][0]]

    for i in range(1, n):
        term = round(float(dd_table[0][i]),4)
        for j in range(i):
            prev_term = UnevaluatedExpr(term) if not isinstance(term, UnevaluatedExpr) else term
            term = prev_term*UnevaluatedExpr(x - x_data[j])
        coefficients.append(term)

    return coefficients

def trapezoid_rule(func, a, b, epsilon, is_cotes: bool = False):
    integral_approximation = ((b-a)*(func.subs(x, a) + func.subs(x, b)))/2
    error = (((b-a)**3)/12)*diff(diff(func, x), x).subs(x, epsilon)
    return integral_approximation - error if is_cotes else (integral_approximation, error)

def composed_trapezoid_rule(func, a, b, interval, epsilon):
    h = (b - a) / interval
    x_values = [a + i * h for i in range(interval + 1)]
    integral_approximation = 0
    second_diff = diff(diff(func, x), x)

    for val in x_values:
        if(val == a or val == b): integral_approximation += func.subs(x, val)
        else: integral_approximation += 2*func.subs(x, val)
    integral_approximation *= (h/2)
    integral_approximation -= ((b-a)/(12*interval**2))*second_diff.subs(x, epsilon)
    return integral_approximation

def simpson_rule(func, a, b, epsilon):
    h = (b - a) / 2
    fx0 = func.subs(x, a)
    fx1 = func.subs(x, a + h)
    fx2 = func.subs(x, b)
    diff_4 = diff(diff(diff(diff(func, x), x), x), x)
    error = ((h**5)/90)*diff_4.subs(x, epsilon)
    integral_estimation = (h/3)*(fx0 + 4*fx1 + fx2) - error
    return integral_estimation

def three_eight_simpson_rule(func, a, b, epsilon):
    h = (b - a) / 3
    fx0 = func.subs(x, a)
    fx1 = func.subs(x, a + h)
    fx2 = func.subs(x, a + 2*h)
    fx3 = func.subs(x, b)
    diff_4 = diff(diff(diff(diff(func, x), x), x), x)
    error = (3*(h**5)/80)*diff_4.subs(x, epsilon)
    integral_estimation = (3*h/8)*(fx0 + 3*fx1 + 3*fx2 + fx3) - error
    return integral_estimation
