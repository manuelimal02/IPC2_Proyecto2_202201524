class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def comparar(self, otra_lista):
        nodo1 = self.cabeza
        nodo2 = otra_lista.cabeza

        while nodo1 is not None and nodo2 is not None:
            if nodo1.dato != nodo2.dato:
                return False
            nodo1 = nodo1.siguiente
            nodo2 = nodo2.siguiente

        if nodo1 is not None or nodo2 is not None:
            return False

        return True

# Crear dos listas doblemente enlazadas para comparar
lista1 = ListaDoblementeEnlazada()
lista1.agregar(1)
lista1.agregar(2)
lista1.agregar(3)

lista2 = ListaDoblementeEnlazada()
lista2.agregar(1)
lista2.agregar(2)
lista2.agregar(3)

# Llamar a la función para comparar las listas
if lista1.comparar(lista2):
    print("Las listas son iguales")
else:
    print("Las listas no son iguales")
