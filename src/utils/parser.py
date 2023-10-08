from sympy.parsing import parse_expr


def parse_string(str_func: str):
    func = parse_expr(str_func)
    return func

def string_to_float_list(str_list: str):
    splitted_str = str_list.split(',')
    float_list = [float(num) for num in splitted_str]
    return float_list

