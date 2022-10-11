#!/usr/bin/env python3

'''
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
    '''Contenedor (lista de números enteros)'''

    def __init__(self):
        self.container = []

    def add(self, value: int) -> None:
        '''Función que agrega elementos nuevos al contenedor y los ordena'''
        self.container.append(value)
        self.container = sorted(self.container)

    def delete(self, value: int) -> bool:
        '''Función que borra cualquier elemento especificado del contenedor, devuelve verdadero si lo encontró y borró o falso si ocurre cualquier otro caso'''
        try:
            self.container.remove(value)
            return True

        except ValueError:
            return False

    def get_median(self) -> int:
        '''Función que devuelve el valor medio del contenedor o levanta una excepción cuando el contenedor está vacío.'''
        if len(self.container) == 0:
            raise ValueError("Contenedor vacío")

        return self.container[len(self.container) // 2]
        
    def __repr__(self) -> str:
        return ", ".join(str(num) for num in self.container)

if __name__ == '__main__':

    print(">>> Ejemplo 1\n")
    contenedor_ej_1 = Container()
    contenedor_ej_1.add(1)
    contenedor_ej_1.add(5)
    contenedor_ej_1.add(4)
    contenedor_ej_1.add(6)
    print(contenedor_ej_1)
    # Prueba
    contenedor_ej_1.add(8)
    print(contenedor_ej_1)
    contenedor_ej_1.delete(5)
    print(contenedor_ej_1)
    print(f"Valor medio: {contenedor_ej_1.get_median()}")

    print("\n>>> Ejemplo 2\n")
    contenedor_ej_2 = Container()
    contenedor_ej_2.add(2)
    contenedor_ej_2.add(7)
    contenedor_ej_2.add(8)

    print(contenedor_ej_2)
    # Prueba
    contenedor_ej_2.add(9)
    print(contenedor_ej_2)
    contenedor_ej_2.delete(8)
    print(contenedor_ej_2)

    print(f"Valor medio: {contenedor_ej_2.get_median()}")
