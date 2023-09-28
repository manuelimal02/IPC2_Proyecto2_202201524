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

    def mostrar_mensaje(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza  
        print("----------------")
        print("Esta es la lista mensajes")
        while actual:
            # Imprimimos el objeto del nodo actual
            print("Nombre Sistema:", actual.mensaje.nombre_mensaje, "Sistema Dron:", actual.mensaje.nombre_sistema_dron)
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


    def comparar(self, lista_sistema):
            nodo_mensaje = self.cabeza
            #Se Recorren Todos Los Mensajes
            while nodo_mensaje is not None:
                print(nodo_mensaje.mensaje.nombre_mensaje)
                nodo_sistema = lista_sistema.cabeza
                #Se Recorren Los Sistemas Para encontrar Una Coincidencia
                while nodo_sistema is not None:
                    #Si el nombre_sistema_dron de mensaje es igual al nombre sistema del sistema 
                    if nodo_mensaje.mensaje.nombre_sistema_dron == nodo_sistema.sistema.nombre_sistema:
                        print("---------------------------------")
                        nodo_instruccion = nodo_mensaje.mensaje.lista_instruccion.cabeza
                        #Se recorren las instrucciones del mensaje actual
                        while nodo_instruccion is not None:
                            nodo_dron = nodo_sistema.sistema.lista_dron.cabeza
                            #Se recorren la lista de dron para buscar el nombre_dron 
                            while nodo_dron is not None:
                                #Si el nombre_dron de la instruccion es igual al nombre_dron del dron
                                if nodo_instruccion.instruccion.nombre_dron == nodo_dron.dron.nombre_dron:
                                    nodo_contenido = nodo_dron.dron.lista_contenido.cabeza
                                    print("----")
                                    print(nodo_dron.dron.nombre_dron)
                                    print("----")
                                    contador_altura=0
                                    emitir_luz=False
                                    while nodo_contenido is not None:
                                        if nodo_instruccion.instruccion.altura_dron == nodo_contenido.contenido.altura_dron:
                                            contador_altura+=1
                                            emitir_luz=True
                                            print("Emitir Luz, "+ nodo_contenido.contenido.simbolo_altura + " Altura: "+ str(contador_altura))
                                        else:
                                            contador_altura+=1
                                            if emitir_luz:
                                                print("Esperar, Altura: "+ str(contador_altura))
                                            else:
                                                print("Subir, Altura: "+ str(contador_altura))
                                            nodo_contenido.siguiente
                                        nodo_contenido=nodo_contenido.siguiente
                                    
                                    break
                                else:
                                    nodo_dron = nodo_dron.siguiente

                            nodo_instruccion = nodo_instruccion.siguiente
                        break
                    else:
                        nodo_sistema=nodo_sistema.siguiente

                nodo_mensaje=nodo_mensaje.siguiente
            return True


