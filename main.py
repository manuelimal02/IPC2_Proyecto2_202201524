import xml.etree.ElementTree as ET
#Libreria webbrowser
import webbrowser
#Libreria Tkinter
import tkinter as tk
#Libreria Tkinter
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Label
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

from listas.lista_mensaje_recibido import lista_doble_mensaje_recibido


from listas.lista_instruccion import lista_doble_instruccion
from objetos.instruccion import instruccion


#Listas Globales 
lista_drones_general = lista_drones()
lista_sistema_general= lista_doble_sistema()
lista_mensaje_general = lista_doble_mensaje()

lista_mensaje_recibido_general = lista_doble_mensaje_recibido()



class ventana_principal:
    #Al Pasar Por El Botón
    def on_enter(self, event):
        event.widget.config(bg='grey')
    #Al Salir Del Botón
    def on_leave(self, event):
        event.widget.config(bg='#4a6eb0')

    def __init__(self, root):
        #Contenedor Pricipal
        self.root = root
        self.root.title("PROYECTO 2 - CARLOS MANUEL LIMA Y LIMA")
        self.root.geometry("1000x600")
        self.root.configure(bg='white')
        self.root.resizable(0,0)
        #Frame Botones Opciones
        self.opciones_frame=tk.Frame(root,bg='#054279')
        #Botón Cargar
        self.boton_cargar=tk.Button(self.opciones_frame,text="Cargar Archivo Xml", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.cargar_archivo)
        self.boton_cargar.place(x=10, y=10, width=200)
        self.boton_cargar.bind("<Enter>", self.on_enter)
        self.boton_cargar.bind("<Leave>", self.on_leave)
        #Botón Generar
        self.boton_generar=tk.Button(self.opciones_frame,text="Generar Archivo Xml", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black')
        self.boton_generar.place(x=10,y=110, width=200)
        self.boton_generar.bind("<Enter>", self.on_enter)
        self.boton_generar.bind("<Leave>", self.on_leave)
        #Botón Gestion Drones
        self.boton_gestion=tk.Button(self.opciones_frame,text="Gestión De Drones", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.mostrar_frame_gestion_drones)
        self.boton_gestion.place(x=10, y=210, width=200)
        self.boton_gestion.bind("<Enter>", self.on_enter)
        self.boton_gestion.bind("<Leave>", self.on_leave)
        #Botón Gestion Sistema
        self.boton_sistema=tk.Button(self.opciones_frame,text="Gestión Sistema Drones", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=self.graficar_sistema_de_drones)
        self.boton_sistema.place(x=10, y=310, width=200)
        self.boton_sistema.bind("<Enter>", self.on_enter)
        self.boton_sistema.bind("<Leave>", self.on_leave)
        #Botón Gestion Mensajes
        self.boton_mensaje=tk.Button(self.opciones_frame,text="Gestión De Mensaje", bg='#4a6eb0', font=("Verdana", 12), bd=0, fg='white', activeforeground='black', command=self.mostrar_frame_gestion_mensaje)
        self.boton_mensaje.place(x=10, y=410, width=200)
        self.boton_mensaje.bind("<Enter>", self.on_enter)
        self.boton_mensaje.bind("<Leave>", self.on_leave)
        #Botón Ayuda
        self.boton_ayuda=tk.Button(self.opciones_frame,text="Ayuda", bg='#4a6eb0', font=("Verdana", 12), bd=0, fg='white', activeforeground='black', command=self.mostrar_frame_ayuda)
        self.boton_ayuda.place(x=10, y=510, width=200)
        self.boton_ayuda.bind("<Enter>", self.on_enter)
        self.boton_ayuda.bind("<Leave>", self.on_leave)
        #Botón Inicializar Sistema
        self.boton_inicializar=tk.Button(self.opciones_frame,text="Inicializar Sistema", bg='#4a6eb0', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.inicializar)
        self.boton_inicializar.place(x=10, y=610, width=200)
        self.boton_inicializar.bind("<Enter>", self.on_enter)
        self.boton_inicializar.bind("<Leave>", self.on_leave)
        #Configuraciones Frame Botones
        self.opciones_frame.configure(width=230, height=550)
        self.opciones_frame.place(x=0, y=50)
        self.opciones_frame.pack_propagate(False)

        #Frame Titulo
        self.titulo_frame=tk.Frame(root,bg='#085879')
        #Label Titulo
        self.label_titulo = Label(self.titulo_frame, text="Sistema De Drones Del Ejército De Guatemala")
        self.label_titulo.pack(anchor='center')
        self.label_titulo.config(fg="white",bg="#085879", font=("Trebuchet MS",20)) 
        #Configuraciones Frame Titulo
        self.titulo_frame.configure(width=1000, height=50)
        self.titulo_frame.place(x=0, y=0)
        self.titulo_frame.pack_propagate(False)

    #Contenedor Principal
    def mostrar_frame_principal(self):
        self.principal_frame = tk.Frame(root, bg='#43b6d5')
        #Botón Salir
        self.boton_salir_principal=tk.Button(self.principal_frame,text="Salir", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=self.salir)
        self.boton_salir_principal.place(x=510, y=500, width=230, height=30)
        self.boton_salir_principal.bind("<Enter>", self.on_enter)
        self.boton_salir_principal.bind("<Leave>", self.on_leave)
        self.principal_frame.configure(width=768, height=550)
        self.principal_frame.place(x=231, y=50)
        self.principal_frame.pack_propagate(False)

    #Contenedor Gestión De Drones
    def mostrar_frame_gestion_drones(self):
        #Frame Gestion Drones
        self.frame_nuevo_dron = tk.Frame(root, bg='#55bdda')
        #Label1
        self.label1 = Label(self.frame_nuevo_dron, text="Gestión de Drones")
        self.label1.config(fg="black",bg="#55bdda", font=("Verdana",15)) 
        self.label1.pack(anchor='center')
        #Label2
        self.label2 = Label(self.frame_nuevo_dron, text="Escribe el Nombre del Dron:")
        self.label2.place(x=20, y=54)
        self.label2.config(fg="black",bg="#55bdda", font=("Verdana",11)) 
        #Entry
        self.caja_texto = Entry(self.frame_nuevo_dron)
        self.caja_texto.config(font=("Verdana",11))
        self.caja_texto.place(x=240, y=50, width=230, height=30)
        #Boton Agregar
        self.boton_agregar=tk.Button(self.frame_nuevo_dron,text="Agregar Nuevo Dron", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=lambda:self.agregar_dron(self.caja_texto))
        self.boton_agregar.place(x=510, y=50, width=230, height=30)
        self.boton_agregar.bind("<Enter>", self.on_enter)
        self.boton_agregar.bind("<Leave>", self.on_leave)
        #Cuadro Texto
        self.cuadro_texto = scrolledtext.ScrolledText(self.frame_nuevo_dron, font=("Verdana", 10), bg="white", width=87, height=20)
        self.cuadro_texto.place(x=20, y=100)
        #Boton Mostrar
        self.boton_mostrar=tk.Button(self.frame_nuevo_dron,text="Ver Listado Drones", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=self.mostrar_lista_dron)
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
        messagebox.showinfo("Gestión De Drones", "Bienvenido A Gestión De Drones")

    #Función Agregar Dron De Gestión De Drones
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
            messagebox.showinfo("Gestión De Drones", f"Dron '{nombre_dron}' Agregado Correctamente.")

    #Función Ver Listado Drones De Gestión De Drones
    def mostrar_lista_dron(self):
        if lista_drones_general.cabeza is not None:
            lista_drones_general.mostrar_drones_pantalla(self.cuadro_texto)
            messagebox.showinfo("Gestión De Drones", "Lista Drones Mostrada Correctamente")
        else:
            messagebox.showwarning("Error", "No existe Información Previa")

    #Contenedor Gestión De Mensajes
    def mostrar_frame_gestion_mensaje(self):
        #Frame Gestion Drones
        self.frame_gestion_mensaje = tk.Frame(root, bg='#2186b2')
        #Label1
        self.label_titulo_mensaje= Label(self.frame_gestion_mensaje, text="Gestión De Mensajes")
        self.label_titulo_mensaje.config(fg="black",bg="#2186b2", font=("Verdana",15)) 
        self.label_titulo_mensaje.pack(anchor='center')
        #Label2
        self.label_nombre_mensaje = Label(self.frame_gestion_mensaje, text="Escribe el Nombre del Mensaje:")
        self.label_nombre_mensaje.place(x=20, y=54)
        self.label_nombre_mensaje.config(fg="black",bg="#2186b2", font=("Verdana",11)) 
        #Entry
        self.caja_texto_mensaje = Entry(self.frame_gestion_mensaje)
        self.caja_texto_mensaje.config(font=("Verdana",11))
        self.caja_texto_mensaje.place(x=260, y=50, width=230, height=30)
        #Boton Agregar
        self.boton_seleccionar=tk.Button(self.frame_gestion_mensaje,text="Seleccionar Mensaje", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black')
        self.boton_seleccionar.place(x=510, y=50, width=230, height=30)
        self.boton_seleccionar.bind("<Enter>", self.on_enter)
        self.boton_seleccionar.bind("<Leave>", self.on_leave)
        #Cuadro Texto
        self.cuadro_texto_mensaje = scrolledtext.ScrolledText(self.frame_gestion_mensaje, font=("Verdana", 10), bg="white", width=87, height=20)
        self.cuadro_texto_mensaje.place(x=20, y=100)
        #Boton Mostrar
        self.boton_mostrar_mensaje=tk.Button(self.frame_gestion_mensaje,text="Ver Listado Mensajes", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=self.mostrar_lista_mensaje)
        self.boton_mostrar_mensaje.place(x=20, y=500, width=230, height=30)
        self.boton_mostrar_mensaje.bind("<Enter>", self.on_enter)
        self.boton_mostrar_mensaje.bind("<Leave>", self.on_leave)
        #Boton Salir
        self.boton_salir_mensaje=tk.Button(self.frame_gestion_mensaje,text="Salir", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=self.salir)
        self.boton_salir_mensaje.place(x=510, y=500, width=230, height=30)
        self.boton_salir_mensaje.bind("<Enter>", self.on_enter)
        self.boton_salir_mensaje.bind("<Leave>", self.on_leave)
        #Configuracion Frame Gestion Drones
        self.frame_gestion_mensaje.configure(width=768, height=550)
        self.frame_gestion_mensaje.place(x=231, y=50)
        self.frame_gestion_mensaje.pack_propagate(False)
        messagebox.showinfo("Gestión De Mensajes", "Bienvenido A Gestión De Mensajes")

    #Función Ver Listado Mensajes y Sus Instrucciones De Gestión De Mensaje
    def mostrar_lista_mensaje(self):
        if lista_mensaje_general.cabeza is not None:
            lista_mensaje_general.mostrar_mensajes_pantalla(self.cuadro_texto_mensaje)
            messagebox.showinfo("Gestión De Mensajes", "Lista Mensajes Mostrada Correctamente")
        else:
            messagebox.showwarning("Error", "No existe Información Previa")

    #Contenedor Ayuda
    def mostrar_frame_ayuda(self):
        #Frame Gestion Drones
        self.frame_ayuda = tk.Frame(root, bg='#55c1db')
        #Label1
        self.label_titulo_ayuda= Label(self.frame_ayuda, text="Información Del Estudiante")
        self.label_titulo_ayuda.config(fg="black",bg="#55c1db", font=("Verdana",15)) 
        self.label_titulo_ayuda.pack(anchor='center')
        #Label2
        self.label_nombre_ayuda= Label(self.frame_ayuda, text="Nombre: Carlos Manuel Lima Y Lima")
        self.label_nombre_ayuda.place(x=20, y=50)
        self.label_nombre_ayuda.config(fg="black",bg="#55c1db", font=("Verdana",13))
        #Label3
        self.label_carnet= Label(self.frame_ayuda, text="Carné: 20220152")
        self.label_carnet.place(x=20, y=100)
        self.label_carnet.config(fg="black",bg="#55c1db", font=("Verdana",13))
        #Label4
        self.label_curso = Label(self.frame_ayuda, text="Curso: Introducción a la Programación y Computación 2")
        self.label_curso.place(x=20, y=150)
        self.label_curso.config(fg="black",bg="#55c1db", font=("Verdana",13))
        #Label5
        self.label_carrera = Label(self.frame_ayuda, text="Carrera: Ingeniería en Ciencias y Sistemas")
        self.label_carrera.place(x=20, y=200)
        self.label_carrera.config(fg="black",bg="#55c1db", font=("Verdana",13))
        #Label6
        self.label_semestre = Label(self.frame_ayuda, text="Segundo Semestre, 2023")
        self.label_semestre.place(x=20, y=250)
        self.label_semestre.config(fg="black",bg="#55c1db", font=("Verdana",13))
        #Label7
        self.enlace_label = tk.Label(self.frame_ayuda, text="Abrir Documentación del Proyecto", cursor="hand2")
        self.enlace_label.place(x=20, y=300)
        self.enlace_label.config(fg="blue",bg="#55c1db", font=("Verdana",13))
        #Evento Click
        self.enlace_label.bind("<Button-1>", lambda e: self.abrir_documentacion_proyecto())  
        #Boton Salir
        self.boton_salir_ayuda=tk.Button(self.frame_ayuda,text="Salir", bg='#4a6eb0', font=("Verdana", 11), bd=0, fg='white', activeforeground='black', command=self.salir)
        self.boton_salir_ayuda.place(x=510, y=500, width=230, height=30)
        self.boton_salir_ayuda.bind("<Enter>", self.on_enter)
        self.boton_salir_ayuda.bind("<Leave>", self.on_leave)
        #Configuracion Frame Gestion Drones
        self.frame_ayuda.configure(width=768, height=550)
        self.frame_ayuda.place(x=231, y=50)
        self.frame_ayuda.pack_propagate(False)
        messagebox.showinfo("Ayuda", "Bienvenido a Ayuda")

    #Funcion Abrir La Documentación Del Proyecto De Ayuda
    def abrir_documentacion_proyecto(self):
        url = "https://www.facebook.com/?locale=es_LA" 
        webbrowser.open(url)


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
                self.desencriptar_lista_mensaje()

            messagebox.showinfo("Abrir", "Archivo Cargado Correctamente.")
        #except Exception as e:
            #messagebox.showerror("Error", f"No se ha seleccionado ningún archivo: {str(e)}")
            #return
    def desencriptar_lista_mensaje(self):
        nodo_mensaje = lista_mensaje_general.cabeza
        nodo_mensaje_variable = lista_mensaje_general.cabeza
        
        #Variables Globales En La Función
        nombre_mensaje_recibido=""
        nombre_sistema=""
        mensaje_recibido=""

        while nodo_mensaje is not None:
            #Se Recorren Todos Los Mensajes
            while nodo_mensaje_variable is not None:
                if nodo_mensaje.mensaje.nombre_mensaje == nodo_mensaje_variable.mensaje.nombre_mensaje:
                    #--Nombre Del Mensaje
                    nombre_mensaje_recibido=nodo_mensaje.mensaje.nombre_mensaje
                    nodo_sistema = lista_sistema_general.cabeza
                    #Se Recorren Los Sistemas Para encontrar Una Coincidencia
                    while nodo_sistema is not None:
                        #Si el nombre_sistema_dron de mensaje es igual al nombre sistema del sistema 
                        if nodo_mensaje.mensaje.nombre_sistema_dron == nodo_sistema.sistema.nombre_sistema:
                            #--Nombre Del Sistema
                            nombre_sistema=nodo_sistema.sistema.nombre_sistema
                            nodo_instruccion = nodo_mensaje.mensaje.lista_instruccion.cabeza
                            #Se recorren las instrucciones del mensaje actual
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
                                                #--Mensaje Recibido
                                                mensaje_recibido+=nodo_contenido.contenido.simbolo_altura
                                            nodo_contenido=nodo_contenido.siguiente
                                        break #Se rompe la iteracion del dron
                                    else:
                                        nodo_dron = nodo_dron.siguiente
                                nodo_instruccion = nodo_instruccion.siguiente
                            break #Se Rompre La Iteracion Del Sistema
                        else:
                            nodo_sistema=nodo_sistema.siguiente
                    
                    print("--------")
                    print(nombre_mensaje_recibido)
                    print(nombre_sistema)
                    print(mensaje_recibido)
                    mensaje_recibido=""
                    print("--------")
                    break #Se Rompre La Iteración Del Mensaje
                else:
                    nodo_mensaje_variable=nodo_mensaje_variable.siguiente

            nodo_mensaje=nodo_mensaje.siguiente



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
            messagebox.showwarning("Error", "No existe Información Previa")

    def graficar_sistema_de_drones(self):
        self.mostrar_frame_principal()
        nodo_sistema = lista_sistema_general.cabeza
        if nodo_sistema is not None:
            lista_sistema_general.graficar_sistema_drones()
            messagebox.showinfo("Gestión Sistema De Drones", "Sistema de Drones Graficados Correctamente")
        else:
            messagebox.showwarning("Error", "No existe Información Previa")

    def salir(self):
        try:
            messagebox.showinfo("Salir", "Gracias por utilizar el programa.")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error.: {str(e)}")

    def centrar_ventana(self):
        self.root.update_idletasks()
        ancho_ventana = self.root.winfo_width()
        alto_ventana = self.root.winfo_height()
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    aplicacion.mostrar_frame_principal()
    aplicacion.centrar_ventana()
    root.mainloop()