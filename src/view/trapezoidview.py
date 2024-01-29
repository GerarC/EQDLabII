from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from utils.methods import composed_trapezoid_rule, trapezoid_rule
from utils.parser import parse_string

class TrapezoidView(Screen):
    function_string = StringProperty()
    low_limit_string = StringProperty()
    upp_limit_string = StringProperty()
    splits_string = StringProperty()
    epsilon_string = StringProperty()
    composed_integral_estimation_string = StringProperty()
    integral_estimation_string = StringProperty()

    def on_calculate_pressed(self):
        try: func = parse_string(self.function_string)
        except:
            self.integral_estimation = 'El formato de la ecuación no es el debido\n' + \
                'revisar la documentación de la función parse_expr de sympy\n' + \
                'El link a esta está en el README.md.'
            return
        try:
            low_limit = float(self.low_limit_string)
            upp_limit = float(self.upp_limit_string)
            epsilon = float(self.epsilon_string)
            splits = int(self.splits_string)
        except:
            self.composed_integral_estimation_string = "some of the values cannot be converted to a number."
            return
        try:
            composed_integral_est = composed_trapezoid_rule(func, low_limit, upp_limit, splits, epsilon)
            trapezoid_res = trapezoid_rule(func, low_limit, upp_limit, epsilon)
            self.composed_integral_estimation_string = f'Dados estos parámetros, el valor estimado de la integral es: {round(float(composed_integral_est), 4)}'
            self.integral_estimation_string = f'El valor estimado de la integral, usando la regla del trapecio, es: {round(float(trapezoid_res[0]), 4)}, con un error de {round(float(trapezoid_res[1]), 4)}'
        except:
            self.composed_integral_estimation_string = "something is going wrong operating the function with this parameters."
            return
