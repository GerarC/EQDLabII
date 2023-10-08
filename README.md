# EQDLabII
Segundo Laboratorio para la materia de Ecuaciones Diferenciales

## Descripción
Para este laboratorio se tuvieron que implementar varios
Métodos númericos enseñados en la clase de *Ecuaciones Diferenciales y Métodos Númericos*.  
    
Los implementados en este código fueron:
- Fórmulas de 2, 3 y 5 puntos.
- Método de Newton-Raphson.
- Diferencias Divididas.
- Regla del Trapecio Compuesto.
- Fórmulas de Newton-Cotes.

## Formato de de las funciones

El formato es muy simple, solo usar parentesis,
todas las multiplicaciones deben de ser explicitas usando '*',
y los exponenciales deben ponerse como doble asterisco '**'.
    
Ejemplos:
 - cos(x) - x
 - 2**ln(x)
 - 1 - 2*x + 3*x**2 - 5*x**3


## Instalación
Para ejecutar este proyecto se necesita activar un entorno virtual,
instalar los paquetes necesarios y finalmete ejecutar el *src/main.py*
    
Para crear el entorno virtual unicamente es necesario ejecutar el siguiente comando:
~~~ bash
python -m venv venv
~~~
    
Activarlo con:
~~~ bash
source ./venv/bin/activate
~~~
    
Luego de creado y activado el entorno virtual por primera vez,
se tienen que instalar las dependencias:
~~~ bash
pytohn -m pip -r requirements.txt
~~~
    
Hecho todo lo anterior ya se puede abrir la aplicación:
~~~ bash
python ./src/main.py
~~~

