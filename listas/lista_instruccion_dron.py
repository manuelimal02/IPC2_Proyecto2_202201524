from nodos.nodo_instruccion_dron import nodo_instruccion_dron
import os

class lista_doble_instruccion_dron:

    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_instruccion_dron(self, instruccion_dron):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = nodo_instruccion_dron(instruccion_dron=instruccion_dron) 
        # Si la lista está vacía
        if self.cabeza is None:
            # El nuevo nodo se convierte en la cabeza 
            self.cabeza = nuevo_nodo
            # El nuevo nodo también se convierte en la cola  
            self.cola = nuevo_nodo  
        else:
            # El nuevo nodo apunta al nodo anterior
            nuevo_nodo.anterior = self.cola  
            # El nodo anterior apunta al nuevo nodo
            self.cola.siguiente = nuevo_nodo  
            # El nuevo nodo se convierte en la cola de la lista
            self.cola = nuevo_nodo 