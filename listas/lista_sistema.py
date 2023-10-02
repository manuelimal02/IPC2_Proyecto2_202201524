from nodos.nodo_sistema import nodo_sistema
import os
class lista_doble_sistema:

    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_sistema(self, sistema):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = nodo_sistema(sistema=sistema) 
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

    def mostrar_sistema(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza  
        print("----------------")
        print("Esta es la lista de sistemas")
        while actual:
            # Imprimimos el objeto del nodo actual
            print("Nombre Sistema:", actual.sistema.nombre_sistema, "Altura Máxima Sistema:", actual.sistema.altura_sistema, "Cantidad Drones:", actual.sistema.cantidad_drones)
            actual.sistema.lista_dron.mostrar_drones()
            # Avanzamos al siguiente nodo  
            actual = actual.siguiente 
        print("----------------")

    def graficar_sistema_drones(self):
        actual = self.cabeza
        while actual is not None:
            nombre=actual.sistema.nombre_sistema
            altura=actual.sistema.altura_sistema
            cantidad=actual.sistema.cantidad_drones
            f = open(nombre+'.dot','w')
            texto="""
                digraph G {bgcolor="#0000FF44:#FF000044" gradientangle=90
                subgraph cluster_0 {fillcolor="cyan:blue" style="filled" gradientangle="270"
                    node [ style=filled,shape="box",fillcolor="cyan" ]"Altura Maxima: """+altura+"""";
                    node [ style=filled,shape="box",fillcolor="cyan" ]"Cantidad Drones: """+cantidad+"""";
                    label=" """+nombre+""""
                    }
                a0 [shape=none label=<
                <TABLE border="0" cellspacing="10" cellpadding="10">\n
                <TR><TD bgcolor="#085879" gradientangle="315">Altura</TD>\n"""
            contador_altura=1
            while int(altura)>=contador_altura:
                texto+="""<TD style="radial" bgcolor="#65BABF" gradientangle="60">"""+str(contador_altura)+"""</TD>\n"""
                contador_altura+=1
            texto+="""</TR>"""

            nodo_dron=actual.sistema.lista_dron.cabeza
            while nodo_dron is not None:
                texto+="""<TR>"""
                texto+="""<TD style="radial" bgcolor="#C81D25"  gradientangle="60">"""+nodo_dron.dron.nombre_dron+"""</TD>\n"""
                nodo_contenido = nodo_dron.dron.lista_contenido.cabeza
                while nodo_contenido is not None:
                    texto+="""<TD style="radial" bgcolor="#F45059" gradientangle="60">"""+nodo_contenido.contenido.simbolo_altura+"""</TD>\n"""
                    nodo_contenido=nodo_contenido.siguiente
                nodo_dron=nodo_dron.siguiente
                texto+="""</TR>"""

            texto+="""</TABLE>>];\n}"""
            f.write(texto)
            f.close()
            os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
            os.system(f'dot -Tpdf {nombre}.dot -o sistema_dron_{nombre}.pdf')
            actual=actual.siguiente

            

    def inicializar_lista_sistema(self):
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