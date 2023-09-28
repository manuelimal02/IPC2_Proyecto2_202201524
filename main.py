import xml.etree.ElementTree as ET
#Libreria Tkinter
import tkinter as tk
#Libreria Tkinter
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Label
from tkinter import Menu
from tkinter import Entry
#Lista Doble Enlazada
from listas.lista_dron import lista_doble_dron
from objetos.dron import dron

from listas.lista_drones import lista_drones
from objetos.drones import drones

from listas.lista_sistema import lista_doble_sistema
from objetos.sistema import sistema

from listas.lista_contenido import lista_doble_contenido
from objetos.contenido import contenido

from listas.lista_mensaje import lista_doble_mensaje
from objetos.mensaje import mensaje

from listas.lista_instruccion import lista_doble_instruccion
from objetos.instruccion import instruccion

#Listas Globales 
lista_drones_general = lista_drones()
lista_sistema_general= lista_doble_sistema()
lista_mensaje_general = lista_doble_mensaje()


class ventana_principal:
    def __init__(self, root):
        #Ventana Pricipal
        self.root = root
        self.root.title("PROYECTO 2 - CARLOS MANUEL LIMA Y LIMA")
        self.root.geometry("1000x600")
        self.root.configure(bg='white')
        self.root.resizable(0,0)

        #Frame Botones Opciones
        self.opciones_frame=tk.Frame(root,bg='#114c5f')
        #Boton Cargar
        self.boton_cargar=tk.Button(self.opciones_frame,text="Cargar Archivo Xml", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.cargar_archivo)
        self.boton_cargar.place(x=10, y=10, width=200)
        self.boton_cargar.bind("<Enter>", self.on_enter)
        self.boton_cargar.bind("<Leave>", self.on_leave)
        #Boton Generar
        self.boton_generar=tk.Button(self.opciones_frame,text="Generar Archivo Xml", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black')
        self.boton_generar.place(x=10,y=110, width=200)
        self.boton_generar.bind("<Enter>", self.on_enter)
        self.boton_generar.bind("<Leave>", self.on_leave)
        #Boton Gestion Drones
        self.boton_gestion=tk.Button(self.opciones_frame,text="Gestión De Drones", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.mostrar_frame_gestion_drones)
        self.boton_gestion.place(x=10, y=210, width=200)
        self.boton_gestion.bind("<Enter>", self.on_enter)
        self.boton_gestion.bind("<Leave>", self.on_leave)
        #Boton Gestion Sistema
        self.boton_sistema=tk.Button(self.opciones_frame,text="Gestión De Sistema Drones", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.graficar_sistema_de_drones)
        self.boton_sistema.place(x=10, y=310, width=200)
        self.boton_sistema.bind("<Enter>", self.on_enter)
        self.boton_sistema.bind("<Leave>", self.on_leave)
        #Boton Cargar
        self.boton_inicializar=tk.Button(self.opciones_frame,text="Inicializar Sistema", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.inicializar)
        self.boton_inicializar.place(x=10, y=410, width=200)
        self.boton_inicializar.bind("<Enter>", self.on_enter)
        self.boton_inicializar.bind("<Leave>", self.on_leave)
        #Configuraciones Frame Botones
        self.opciones_frame.configure(width=230, height=550)
        self.opciones_frame.place(x=0, y=50)
        self.opciones_frame.pack_propagate(False)

        #Frame Titulo
        self.titulo_frame=tk.Frame(root,bg='pink')
        #Label Titulo
        self.label_titulo = Label(self.titulo_frame, text="Sistema De Drones – Ejército De Guatemala")
        self.label_titulo.pack(anchor='center')
        self.label_titulo.config(fg="black",bg="pink", font=("Verdana",24)) 
        #Configuraciones Frame Titulo
        self.titulo_frame.configure(width=1000, height=50)
        self.titulo_frame.place(x=0, y=0)
        self.titulo_frame.pack_propagate(False)

    def on_enter(self, event):
        event.widget.config(bg='grey')

    def on_leave(self, event):
        event.widget.config(bg='#4a6eb0')


    def agregar_dron(self, caja_texto):
        #Obtiene el nombre del dron desde la caja_texto
        nombre_dron = caja_texto.get()
        #Obtiene la cabeza de la lista de drones
        nodo_dron = lista_drones_general.cabeza
        # Verifica si el nombre del dron es una cadena vacía
        if nombre_dron == "":
            messagebox.showwarning("Error", "Escribe El Nombre del Dron")
        else:
            # Itera a través de la lista de drones para verificar si el nombre del dron ya existe
            while nodo_dron:
                if nodo_dron.dron.nombre == nombre_dron:
                    # Si encuentra un dron con el mismo nombre, muestra un mensaje de advertencia y sale de la función
                    messagebox.showwarning("Error", f"El Dron '{nodo_dron.dron.nombre}' ya existe en la lista.")
                    return
                # Avanza al siguiente nodo en la lista
                nodo_dron = nodo_dron.siguiente
            # Si el nombre del dron no existe en la lista, crea un nuevo dron y lo inserta en la lista
            lista_drones_general.insertar_dron(drones(nombre_dron))
            # Llama a la función para mostrar la lista actualizada
            lista_drones_general.mostrar_drones_pantalla(self.cuadro_texto)
            # Muestra un mensaje informativo
            messagebox.showinfo("Gestión de Drones", f"Dron '{nombre_dron}' Agregado Correctamente.")

    def mostrar_lista_dron(self):
        if lista_drones_general.cabeza is not None:
            lista_drones_general.mostrar_drones_pantalla(self.cuadro_texto)
            messagebox.showinfo("Gestión de Drones", "Lista Drones Mostrada Correctamente")
        else:
            messagebox.showwarning("Error", "La Lista está Vacia")


    def mostrar_frame_principal(self):
        self.principal_frame = tk.Frame(root, bg='skyblue')
        self.principal_frame.configure(width=768, height=550)
        self.principal_frame.place(x=231, y=50)
        self.principal_frame.pack_propagate(False)

    def mostrar_frame_gestion_drones(self):
        #Frame Gestion Drones
        self.frame_nuevo_dron = tk.Frame(root, bg='red')
        #Label1
        self.label1 = Label(self.frame_nuevo_dron, text="Gestión de Drones ")
        self.label1.config(fg="black",bg="red", font=("Verdana",15)) 
        self.label1.pack(anchor='center')
        #Label2
        self.label2 = Label(self.frame_nuevo_dron, text="Escribe el Nombre del Dron:")
        self.label2.place(x=20, y=54)
        self.label2.config(fg="black",bg="red", font=("Verdana",11)) 
        #Entry
        self.caja_texto = Entry(self.frame_nuevo_dron)
        self.caja_texto.config(font=("Verdana",11))
        self.caja_texto.place(x=240, y=50, width=230, height=30)
        texto=self.caja_texto.get()
        #Boton Agregar
        self.boton_agregar=tk.Button(self.frame_nuevo_dron,text="Agregar Nuevo Dron", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=lambda:self.agregar_dron(self.caja_texto))
        self.boton_agregar.place(x=510, y=50, width=230, height=30)
        self.boton_agregar.bind("<Enter>", self.on_enter)
        self.boton_agregar.bind("<Leave>", self.on_leave)
        #Cuadro Texto
        self.cuadro_texto = scrolledtext.ScrolledText(self.frame_nuevo_dron, font=("Verdana", 10), bg="white", width=87, height=20)
        self.cuadro_texto.place(x=20, y=100)
        #Boton Mostrar
        self.boton_mostrar=tk.Button(self.frame_nuevo_dron,text="Ver Lista Drones", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=self.mostrar_lista_dron)
        self.boton_mostrar.place(x=20, y=500, width=230, height=30)
        self.boton_mostrar.bind("<Enter>", self.on_enter)
        self.boton_mostrar.bind("<Leave>", self.on_leave)
        #Boton Salir
        self.boton_salir=tk.Button(self.frame_nuevo_dron,text="Salir", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=self.salir)
        self.boton_salir.place(x=510, y=500, width=230, height=30)
        self.boton_salir.bind("<Enter>", self.on_enter)
        self.boton_salir.bind("<Leave>", self.on_leave)
        #Configuracion Frame Gestion Drones
        self.frame_nuevo_dron.configure(width=768, height=550)
        self.frame_nuevo_dron.place(x=231, y=50)
        self.frame_nuevo_dron.pack_propagate(False)
        messagebox.showinfo("Gestión de Drones", "Bienvenido A Gestión De Drones ")


    def cargar_archivo(self):
            self.mostrar_frame_principal()
            ruta = tk.Tk()
            ruta.withdraw()
            ruta.attributes('-topmost', True)

        #try:
            ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", f"*.xml")])

            with open(ruta_archivo, "r") as archivo:
                tree = ET.parse(ruta_archivo)
                root = tree.getroot()

                #Lista Dron
                nivel_drones = root.find('.//listaDrones')
                for nivel_drones in nivel_drones.findall('.//dron'):
                    nombre_dron=nivel_drones.text
                    nuevo_dron=drones(nombre_dron)
                    lista_drones_general.insertar_dron(nuevo_dron)
                #lista_drones_general.imprimir()
                #Lista Sistema Drones
                nivel_sistemas_drones = root.find('.//listaSistemasDrones')
                for sistema_drones in nivel_sistemas_drones.findall('.//sistemaDrones'):
                    nombre_sistema = sistema_drones.get('nombre')
                    altura_maxima = sistema_drones.find('alturaMaxima').text 
                    cantidad_drones = sistema_drones.find('cantidadDrones').text
                    #Lista Contenido Según El Dron
                    lista_dron=lista_doble_dron()
                    for nivel_contenido in sistema_drones.findall('.//contenido'):
                        nombre_dron_contenido = nivel_contenido.find('dron').text
                        #Se Busca en Lista Dron
                        alturas = nivel_contenido.find('alturas')
                        #Lista Contenido Alturas
                        lista_contenido=lista_doble_contenido()
                        for altura in alturas.findall('altura'):
                            altura_contenido = altura.get('valor') 
                            simbolo_altura = altura.text
                            nuevo_contenido=contenido(altura_contenido, simbolo_altura)
                            lista_contenido.insertar_contenido(nuevo_contenido)
                        
                        nuevo_dron=dron(nombre_dron_contenido, lista_contenido)
                        lista_dron.insertar_dron(nuevo_dron)

                    nuevo_sistema=sistema(nombre_sistema, altura_maxima, cantidad_drones, lista_dron)
                    lista_sistema_general.insertar_sistema(nuevo_sistema)
                #lista_sistema_general.mostrar_sistema()

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
                    lista_mensaje_general.insertar_mensaje(nuevo_mensaje)
                #lista_mensaje_general.mostrar_mensaje()
                #lista_mensaje_general.comparar(lista_sistema_general)
                


            messagebox.showinfo("Abrir", "Archivo Cargado Correctamente.")
        #except Exception as e:
            #messagebox.showerror("Error", f"No se ha seleccionado ningún archivo: {str(e)}")
            #return

    def inicializar(self):
        self.mostrar_frame_principal()
        if lista_drones_general.cabeza is not None and (lista_sistema_general.cabeza is not None or lista_mensaje_general is not None):
            lista_drones_general.inicializar_lista_drones()
            lista_sistema_general.inicializar_lista_sistema()
            lista_mensaje_general.inicializar_lista_mensaje()
            messagebox.showinfo("Inicializar Sistema", "Sistema Inicializado Correctamente")
        else:
            lista_drones_general.mostrar_drones()
            lista_sistema_general.mostrar_sistema()
            lista_mensaje_general.mostrar_mensaje()
            messagebox.showwarning("Inicializar Sistema", "No existe Información Previa")

    def graficar_sistema_de_drones(self):
        lista_sistema_general.graficar_sistema_drones()

    def salir(self):
        try:
            messagebox.showinfo("Salir", "Gracias por utilizar el programa.")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error.: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    aplicacion.mostrar_frame_principal()
    root.mainloop()