from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from utils.methods import trapezoid_rule, simpson_rule, three_eight_simpson_rule
from utils.parser import parse_string

class NewtonCotesView(Screen):
    function_string = StringProperty()
    low_limit_string = StringProperty()
    upp_limit_string = StringProperty()
    splits_string = StringProperty()
    epsilon_string = StringProperty()
    trapezoid_rule_string = StringProperty()
    simpson_string = StringProperty()
    simpson_three_eight_string = StringProperty()

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
        except:
            self.trapezoid_rule_string = "some of the values cannot be converted to a number."
            return

        simpson_res = simpson_rule(func, low_limit, upp_limit, epsilon)
        try:
            trapezoid_res = trapezoid_rule(func, low_limit, upp_limit, epsilon, True)
            simpson_three_eight_res = three_eight_simpson_rule(func, low_limit, upp_limit, epsilon)

            self.trapezoid_rule_string = f'El resultado es {round(float(trapezoid_res), 4)}' 
            self.simpson_string = f'El resultado es {round(float(simpson_res), 4)}' 
            self.simpson_three_eight_string = f'El resultado es {round(float(simpson_three_eight_res), 4)}' 
        except:
            self.trapezoid_rule_string = "something is going wrong operating the function with this parameters."
            return
