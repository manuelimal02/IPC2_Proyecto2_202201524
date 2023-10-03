import xml.etree.ElementTree as ET
# Importa tkinter
import tkinter as tk
from tkinter import messagebox
from nodos.nodo_mensaje_recibido import nodo_mensaje_recibido
import os

class lista_doble_mensaje_recibido:

    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_mensaje_recibido(self, mensaje_recibido):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = nodo_mensaje_recibido(mensaje_recibido=mensaje_recibido) 
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

    def mostrar_mensaje_recibido(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza  
        print("----------------")
        while actual:
            # Imprimimos el objeto del nodo actual
            print("Nombre Mensaje:", actual.mensaje_recibido.nombre_mensaje, "Sistema Dron:", actual.mensaje_recibido.nombre_sistema_dron, "Tiempo Optimo:", actual.mensaje_recibido.tiempo_optimo, "Mensaje Recibido:", actual.mensaje_recibido.mensaje_recibido)
            print(" ")
            actual.mensaje_recibido.lista_dron_recibido.mostrar_dron_recibido()
            # Avanzamos al siguiente nodo  
            actual = actual.siguiente 
            # Imprimimos "None" al final para indicar el final de la lista
        print("----------------")

    def mostrar_mensajes_recibido_pantalla(self,nombre_mensaje,scrolled_text):
        #Borra El Contenido Actual
        scrolled_text.delete(1.0, tk.END)
        # Comenzamos desde la cabeza de la lista
        actual = self.cabeza  
        while actual:
            if actual.mensaje_recibido.nombre_mensaje==nombre_mensaje:
                # Agrega el nombre del mensaje al scrolledtext
                scrolled_text.insert(tk.END, "Nombre Del Mensaje: "+ actual.mensaje_recibido.nombre_mensaje +'\n')
                scrolled_text.insert(tk.END, "Nombre Sistema Utilizado: "+ actual.mensaje_recibido.nombre_sistema_dron +'\n')
                scrolled_text.insert(tk.END, "Mensaje A Enviar: "+actual.mensaje_recibido.mensaje_recibido+'\n')
                scrolled_text.insert(tk.END, "Tiempo Optimo: "+str(actual.mensaje_recibido.tiempo_optimo)+'\n')
                break
            else:
                # Avanzamos al siguiente nodo
                actual = actual.siguiente

    def graficar_instruccion_mensaje(self, nombre_mensaje):
        actual = self.cabeza
        while actual is not None:
            if actual.mensaje_recibido.nombre_mensaje==nombre_mensaje:
                nombre_mensaje_recibido=actual.mensaje_recibido.nombre_mensaje
                nombre_sistema_dron=actual.mensaje_recibido.nombre_sistema_dron
                tiempo_optimo=actual.mensaje_recibido.tiempo_optimo
                mensaje_recibido=actual.mensaje_recibido.mensaje_recibido
                f = open(nombre_mensaje_recibido+'.dot','w')
                texto="""
                    digraph G {bgcolor="#0000FF44:#FF000044" gradientangle=90
                    subgraph cluster_0 {fillcolor="cyan:blue" style="filled" gradientangle="270"
                        node [ style=filled,shape="box",fillcolor="cyan" ]"Mensaje A Enviar: """+mensaje_recibido+"""";
                        node [ style=filled,shape="box",fillcolor="cyan" ]"Tiempo Optimo: """+str(tiempo_optimo)+"""";
                        node [ style=filled,shape="box",fillcolor="cyan" ]"Sistema Dron: """+nombre_sistema_dron+"""";
                        node [ style=filled,shape="box",fillcolor="cyan" ]"Nombre Mensaje: """+nombre_mensaje+"""";
                        label=" """+nombre_mensaje_recibido+""""
                        }
                    a0 [shape=none label=<
                    <TABLE border="0" cellspacing="10" cellpadding="10">\n
                    <TR><TD bgcolor="#085879" gradientangle="315">Tiempo</TD>\n"""
                contador_altura=1
                while int(tiempo_optimo)>=contador_altura:
                    texto+="""<TD style="radial" bgcolor="#65BABF" gradientangle="60">"""+str(contador_altura)+"""</TD>\n"""
                    contador_altura+=1
                texto+="""</TR>"""
                nodo_dron=actual.mensaje_recibido.lista_dron_recibido.cabeza
                while nodo_dron is not None:
                    texto+="""<TR>"""
                    texto+="""<TD style="radial" bgcolor="#C81D25"  gradientangle="60">"""+nodo_dron.dron_recibido.nombre_dron+"""</TD>\n"""
                    nodo_instruccion = nodo_dron.dron_recibido.lista_instruccion_dron.cabeza
                    while nodo_instruccion is not None:
                        texto+="""<TD style="radial" bgcolor="#F45059" gradientangle="60">"""+nodo_instruccion.instruccion_dron.accion+"""</TD>\n"""
                        nodo_instruccion=nodo_instruccion.siguiente
                    nodo_dron=nodo_dron.siguiente
                    texto+="""</TR>"""
                texto+="""</TABLE>>];\n}"""
                f.write(texto)
                f.close()
                os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
                os.system(f'dot -Tpdf {nombre_mensaje_recibido}.dot -o {nombre_mensaje_recibido}.pdf')
                break
            else:
                actual=actual.siguiente

    def escribir_archivo_salida(self):
        actual=self.cabeza
        respuesta = ET.Element("respuesta")
        lista_mensajes = ET.SubElement(respuesta, "listaMensajes") 
    
        while actual is not None:
            mensaje = ET.SubElement(lista_mensajes, "mensaje")
            mensaje.set("nombre", actual.mensaje_recibido.nombre_mensaje)

            sistema_drones = ET.SubElement(mensaje, "sistemaDrones")
            sistema_drones.text = actual.mensaje_recibido.nombre_sistema_dron
            
            tiempo_optimo = ET.SubElement(mensaje, "tiempoOptimo")
            tiempo_optimo.text = str(actual.mensaje_recibido.tiempo_optimo)
            
            mensaje_recibido = ET.SubElement(mensaje, "mensajeRecibido")
            mensaje_recibido.text = actual.mensaje_recibido.mensaje_recibido

            instrucciones = ET.SubElement(mensaje, "instrucciones")
            tiempo_optimo_mensaje=actual.mensaje_recibido.tiempo_optimo

            contador_tiempo=1
            while int(tiempo_optimo_mensaje)>=contador_tiempo:
                tiempo= ET.SubElement(instrucciones, "tiempo")
                tiempo.set("valor", str(contador_tiempo))
                acciones=ET.SubElement(tiempo, "acciones")
                nodo_dron=actual.mensaje_recibido.lista_dron_recibido.cabeza
                while nodo_dron is not None:
                    nodo_instruccion=nodo_dron.dron_recibido.lista_instruccion_dron.cabeza
                    while nodo_instruccion is not None:
                        if nodo_instruccion.instruccion_dron.tiempo==contador_tiempo:
                            dron=ET.SubElement(acciones, "Dron")
                            dron.set("nombre",  nodo_dron.dron_recibido.nombre_dron)
                            dron.text=nodo_instruccion.instruccion_dron.accion
                            break
                        else:
                            nodo_instruccion=nodo_instruccion.siguiente
                    nodo_dron=nodo_dron.siguiente
                contador_tiempo+=1
            actual = actual.siguiente

        datos=ET.tostring(respuesta)
        datos=str(datos)
        self.xml_identado(respuesta)
        arbol_xml=ET.ElementTree(respuesta)
        arbol_xml.write("xml_Salida.xml",encoding="UTF-8",xml_declaration=True)

    def xml_identado(self, element, indent='  '):
    # Esta función puede utilizarse para obtener la indentación adecuada en el XML.
        queue = [(0, element)]
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level + 1)
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                element.tail = '\n' + indent * (level - 1)
            queue[0:0] = children