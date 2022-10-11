'''
En la clase contenedor (lista de números enteros) implementar:
*La función que agrega elementos nuevos al contenedor y los ordena, por lo tanto regresa una lista ordenada 
*La función que borra cualquier elemento especificado del contenedor, devuelve verdadero si lo encontró y borró o falso si ocurre cualquier otro caso
*La función que devuelve el valor medio del contenedor o levanta una excepción cuando el contenedor está vacío.

El valor medio del contenedor (ordenado) es aquel que  se encuentra en la posición n/2, 
donde n es el número de elementos del contenedor, si n es par, entonces el valor medio es (n/2)+1.

Para realizar la prueba de código, se puede agregar "if __name__ == '__main__':" o creando un objeto de la clase.

Ejemplo 1:
contenedor = [1,5,4,6]
*Agregar 8: contenedor = [1,4,5,6,8]
*Borrar 5: contenedor = [1,4,6,8]
*Valor medio: 6

Ejemplo 2:
contenedor = [2,7,8]
*Agregar 9: contenedor = [2,7,8,9]
*Borrar 8: contenedor = [2,7,9]
*Valor medio: 7
'''

class Container:
    container = []
    
    def __init__(self):
        pass

    def add(self, value: int) -> None:
        pass

    def delete(self, value: int) -> bool:
        pass

    def get_median(self) -> int:
        pass