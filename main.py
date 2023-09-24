import xml.etree.ElementTree as ET
import tkinter as tk
#Libreria Tkinter
from tkinter import messagebox
from tkinter import filedialog
#Lista Doble Enlazada
from listas.lista_dron import lista_doble_dron
from objetos.dron import dron

from listas.lista_sistema import lista_doble_sistema
from objetos.sistema import sistema

from listas.lista_contenido import lista_doble_contenido
from objetos.contenido import contenido

from listas.lista_mensaje import lista_doble_mensaje
from objetos.mensaje import mensaje

from listas.lista_instruccion import lista_doble_instruccion
from objetos.instruccion import instruccion

#Listas Globales 
lista_drones_temporal = lista_doble_dron()
lista_sistema_temporal = lista_doble_sistema()
lista_mensaje_temporal = lista_doble_mensaje()


class ventana_principal:
    def __init__(self, root):
        #Ventana Pricipal
        self.root = root
        self.root.title("PROYECTO 2 - CARLOS MANUEL LIMA Y LIMA")
        self.root.geometry("1000x600")
        self.root.configure(bg='white')
        self.root.resizable(0,0)
        #Frame Botones Opciones
        opciones_frame=tk.Frame(root,bg='#114c5f')

        #Boton Cargar
        boton_cargar=tk.Button(opciones_frame,text="Cargar Archivo Xml", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.cargar_archivo)
        boton_cargar.place(x=10, y=200, width=200)
        #Boton Generar
        boton_generar=tk.Button(opciones_frame,text="Generar Archivo Xml", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black')
        boton_generar.place(x=10,y=300, width=200)
        #Boton Gestion Drones
        boton_gestion=tk.Button(opciones_frame,text="Gestión De Drones", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black')
        boton_gestion.place(x=10, y=400, width=200)

        #Configuraciones Frame Botones
        opciones_frame.configure(width=300, height=600)
        opciones_frame.place(x=0, y=0)
        opciones_frame.pack_propagate()



    def cargar_archivo(self):
        ruta = tk.Tk()
        ruta.withdraw()
        ruta.attributes('-topmost', True)

        try:
            ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", f"*.xml")])
            with open(ruta_archivo, "r") as archivo:
                tree = ET.parse(ruta_archivo)
                root = tree.getroot()
                #Lista Drones
                nivel_drones = root.find('.//listaDrones')
                for drones in nivel_drones.findall('.//dron'):
                    nombre_dron=drones.text
                    nuevo_dron=dron(nombre_dron)
                    lista_drones_temporal.insertar_dron(nuevo_dron)
                lista_drones_temporal.mostrar_drones()


                #Lista Sistema Drones
                nivel_sistemas_drones = root.find('.//listaSistemasDrones')
                for sistema_drones in nivel_sistemas_drones.findall('.//sistemaDrones'):
                    nombre_sistema = sistema_drones.get('nombre')
                    altura_maxima = sistema_drones.find('alturaMaxima').text 
                    cantidad_drones = sistema_drones.find('cantidadDrones').text 
                    #Lista_Contenido
                    lista_contenido_temporal = lista_doble_contenido()
                    for nivel_contenido in sistema_drones.findall('.//contenido'):
                        nombre_dron_contenido = nivel_contenido.find('dron').text
                        #Contenido Alturas
                        alturas = nivel_contenido.find('alturas')
                        for altura in alturas.findall('altura'):
                            altura_contenido = altura.get('valor') 
                            simbolo_altura = altura.text
                            nuevo_contenido=contenido(nombre_dron_contenido, altura_contenido, simbolo_altura)
                            lista_contenido_temporal.insertar_contenido(nuevo_contenido)
                    nuevo_sistema=sistema(nombre_sistema, altura_maxima, cantidad_drones, lista_contenido_temporal)
                    lista_sistema_temporal.insertar_sistema(nuevo_sistema)
                lista_sistema_temporal.mostrar_sistema()

            # Encuentra la sección <listaMensajes>
            lista_mensajes = root.find('.//listaMensajes')
            for nivel_mensaje in lista_mensajes.findall('.//Mensaje'):
                nombre_mensaje = nivel_mensaje.get('nombre') 
                sistema_drones_mensaje = nivel_mensaje.find('sistemaDrones').text
                #Contenido Instrucciones
                nivel_instrucciones = nivel_mensaje.find('instrucciones')
                #Lista_Intruccion
                lista_instruccion_temporal=lista_doble_instruccion()
                for nivel_instruccion in nivel_instrucciones.findall('instruccion'):
                    dron_instruccion = nivel_instruccion.get('dron')
                    altura_dron = nivel_instruccion.text
                    nueva_instruccion=instruccion(dron_instruccion, altura_dron)
                    lista_instruccion_temporal.insertar_instruccion(nueva_instruccion)
                nuevo_mensaje=mensaje(nombre_mensaje, sistema_drones_mensaje, lista_instruccion_temporal)
                lista_mensaje_temporal.insertar_mensaje(nuevo_mensaje)
            lista_mensaje_temporal.mostrar_mensaje()

            messagebox.showinfo("Abrir", "Archivo Cargado Correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se ha seleccionado ningún archivo: {str(e)}")
            return

    def procesar_archivo():
        print("Prueba")


if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    root.mainloop()