# Importa tkinter
import tkinter as tk
from nodos.nodo_mensaje import nodo_mensaje

class lista_doble_mensaje:

    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_mensaje(self, mensaje):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = nodo_mensaje(mensaje=mensaje) 
        # Si la lista está vacía o el nuevo mensaje va antes del primer mensaje en orden alfabético
        if self.cabeza is None or mensaje.nombre_mensaje < self.cabeza.mensaje.nombre_mensaje:
            # El nuevo nodo se convierte en la cabeza 
            nuevo_nodo.siguiente = self.cabeza
            if self.cabeza:
                # Si la cabeza existe (no es None), establecemos su anterior como el nuevo nodo
                self.cabeza.anterior = nuevo_nodo
            # El nuevo nodo se convierte en la nueva cabeza de la lista
            self.cabeza = nuevo_nodo
            if self.cola is None:
                # Si la cola también es None (lista vacía), el nuevo nodo se convierte en la cola
                self.cola = nuevo_nodo
        else:
            # Si la lista no está vacía y el nuevo mensaje no es el primero en orden alfabético
            actual = self.cabeza
            while actual.siguiente and mensaje.nombre_mensaje >= actual.siguiente.mensaje.nombre_mensaje:
                # Avanzamos a través de la lista hasta encontrar el lugar adecuado
                actual = actual.siguiente
            # Insertamos el nuevo nodo después del nodo actual
            nuevo_nodo.siguiente = actual.siguiente
            if actual.siguiente:
                # Si el nodo siguiente existe, establecemos su anterior como el nuevo nodo
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            # Si el nuevo nodo se inserta después del último nodo, se convierte en la nueva cola
            if nuevo_nodo.siguiente is None:
                self.cola = nuevo_nodo


    def mostrar_mensaje(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza  
        print("----------------")
        print("Esta es la lista mensajes")
        while actual:
            # Imprimimos el objeto del nodo actual
            print("Nombre Mensaje:", actual.mensaje.nombre_mensaje, "Sistema Dron:", actual.mensaje.nombre_sistema_dron)
            print(" ")
            actual.mensaje.lista_instruccion.mostrar_instruccion()
            # Avanzamos al siguiente nodo  
            actual = actual.siguiente 
            # Imprimimos "None" al final para indicar el final de la lista
        print("----------------")
    
    def inicializar_lista_mensaje(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza
        while actual:
            # Guarda una referencia al siguiente nodo
            siguiente = actual.siguiente
            # Elimina el nodo actual  
            del actual 
            # Avanza al siguiente nodo 
            actual = siguiente
        # Después de eliminar todos los nodos, la lista está vacía  
        self.cabeza = None
        self.cola = None  
    
    def mostrar_mensajes_pantalla(self,scrolled_text):
        # Comenzamos desde la cabeza de la lista
        actual = self.cabeza  
        while actual:
            # Agrega el nombre del mensaje al scrolledtext
            scrolled_text.insert(tk.END, "---------------------------" + '\n')
            scrolled_text.insert(tk.END, actual.mensaje.nombre_mensaje + '\n')
            scrolled_text.insert(tk.END, "---------------------------" + '\n')
            actual.mensaje.lista_instruccion.mostrar_instruccion_pantalla(scrolled_text)
            # Avanzamos al siguiente nodo
            actual = actual.siguiente

    def descifrar_mensaje(self, lista_sistema):
            nodo_mensaje = self.cabeza
            #Se Recorren Todos Los Mensajes
            while nodo_mensaje is not None:
                nombre_mensaje=nodo_mensaje.mensaje.nombre_mensaje
                nodo_sistema = lista_sistema.cabeza
                #Se Recorren Los Sistemas Para encontrar Una Coincidencia
                while nodo_sistema is not None:
                    #Si el nombre_sistema_dron de mensaje es igual al nombre sistema del sistema 
                    if nodo_mensaje.mensaje.nombre_sistema_dron == nodo_sistema.sistema.nombre_sistema:
                        nombre_sistema=""
                        nombre_sistema=nodo_sistema.sistema.nombre_sistema
                        nodo_instruccion = nodo_mensaje.mensaje.lista_instruccion.cabeza
                        #Se recorren las instrucciones del mensaje actual
                        mensaje_recibido=""
                        while nodo_instruccion is not None:
                            nodo_dron = nodo_sistema.sistema.lista_dron.cabeza
                            #Se recorren la lista de dron para buscar el nombre_dron 
                            while nodo_dron is not None:
                                #Si el nombre_dron de la instruccion es igual al nombre_dron del dron
                                if nodo_instruccion.instruccion.nombre_dron == nodo_dron.dron.nombre_dron:
                                    nodo_contenido = nodo_dron.dron.lista_contenido.cabeza
                                    #Se Recorre el Contenido del dron actual para buscar su altura
                                    while nodo_contenido is not None:
                                        #Si la altura del Contenido es la misma que la altura de la instruccion
                                        if nodo_instruccion.instruccion.altura_dron == nodo_contenido.contenido.altura_dron:
                                            mensaje_recibido+=nodo_contenido.contenido.simbolo_altura
                                        nodo_contenido=nodo_contenido.siguiente
                                    break #Se rompe la iteracion del dron
                                else:
                                    nodo_dron = nodo_dron.siguiente
                            nodo_instruccion = nodo_instruccion.siguiente
                        print(mensaje_recibido)
                        break # Se rompre la iteracion del sistema
                    else:
                        nodo_sistema=nodo_sistema.siguiente
                nodo_mensaje=nodo_mensaje.siguiente
            return True