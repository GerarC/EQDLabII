from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from utils.methods import newton_raphson
from utils.parser import parse_string

class NewtonView(Screen):
    function_string = StringProperty()
    x0_string = StringProperty()
    tol_string = StringProperty()
    max_string = StringProperty()
    result_newton_raphson = StringProperty()

    def on_calculate_pressed(self):
        try:
            func = parse_string(self.function_string)
        except:
            self.result_newton_raphson = 'El formato de la ecuación no es el debido\n' + \
                'revisar la documentación de la función parse_expr de sympy\n' + \
                'El link a esta está en el README.md.'
            return

        try: 
            x0_val = float(self.x0_string)
            tol_val = float(self.tol_string)
            max_val = int(self.max_string)
            result = newton_raphson(func, x0_val, tol_val, max_val)
        except:
            self.result_newton_raphson = 'Alguno de los datos ingresados genera un error'
            return
        
        if(result[1] == max_val):
            self.result_newton_raphson = f'El resultado no fue encontrado en {max_val} iteraciones\nel último resultado estimado fue {result[0]}.'
        else:
            self.result_newton_raphson = f'El resultado estimado hallado en {result[1]} iteraciones\nfue {result[0]}.'
