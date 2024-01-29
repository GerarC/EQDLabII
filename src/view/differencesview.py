from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from utils.parser import string_to_float_list
from utils.methods import divided_differences, calculate_polynomial_coefficients

class DifferencesView(Screen):
    x_values_string = StringProperty()
    fx_values_string = StringProperty()
    polynome_string = StringProperty()

    def on_calculate_pressed(self):
        try:
            x_vals = string_to_float_list(self.x_values_string)
            fx_vals = string_to_float_list(self.fx_values_string)
        except:
            self.polynome_string = "Error en la digitación de los valores"
            return
        if len(x_vals) != len(fx_vals):
            self.polynome_string = "Error, ambos deben tener el mismo número de valores"
            return

        dd_table = divided_differences(x_vals, fx_vals)
        polynome = calculate_polynomial_coefficients(x_vals, dd_table)
        result = ""
        sep = ""
        for coef in polynome:
            result += sep
            result += f'{coef}'
            if sep == "": sep = ' + '
            
        self.polynome_string = result
