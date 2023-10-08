from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from utils.parser import parse_string 
from utils.methods import (
    calculate_two_points,
    calculate_three_points,
    calculate_five_points
)

class PuntosView(Screen):
    function_string = StringProperty()
    h_string = StringProperty()
    x_string = StringProperty()
    two_points_res = StringProperty()
    three_points_res = StringProperty()
    five_points_res = StringProperty()

    def on_calculate_pressed(self):
        try:
            func = parse_string(self.function_string)
        except:
            self.two_points_res = 'El formato de la ecuación no es el debido\n' + \
                'revisar la documentación de la función parse_expr de sympy\n' + \
                'El link a esta está en el README.md.'
            self.three_poits_res = 'Error'
            self.five_poits_res = 'Error'
            return

        try: 
            x_val = float(self.x_string)
            h_val = float(self.h_string)
            two_res = calculate_two_points(func, x_val=x_val, h_val=h_val)
            three_res = calculate_three_points(func, x_val=x_val, h_val=h_val)
            five_res = calculate_five_points(func, x_val=x_val, h_val=h_val)
        except:
            self.two_points_res = 'Alguno de los datos ingresados genera un error'
            self.three_poits_res = 'Error'
            self.five_poits_res = 'Error'
            return

        self.two_points_res = f'El valor estimado de f\'({x_val}) es {two_res[0]}\nEl error estimado es de {two_res[1]}'
        self.three_points_res = f'El valor estimado de f\'({x_val}) es {three_res[0]}\nEl error estimado es de {three_res[1]}'
        self.five_points_res = f'El valor estimado de f\'({x_val}) es {five_res[0]}\nEl error estimado es de {five_res[1]}'

