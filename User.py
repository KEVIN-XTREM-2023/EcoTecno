from tkinter import *
import tkinter as tk
from Login import Login

class PerfilUser:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("650x400")
        self.ventana.title("EcoTecno")
        self.ventana.resizable(0,0)
        self.frameUser = None
        self.titulo = None
        self.botonEquipo = None
        self.botonComponente = None
        self.botonSalir = None
        self.widgetsUser()

    def widgetsUser(self):
        self.ventana.config(background="white")
        self.frameUser = Frame(self.ventana, bg="#9CCC65")
        self.frameUser.place(x=120,y=100,height=200,width=420)
        self.titulo = Label(self.ventana, text="Bienvenidos a EcoTecno", 
                        font=("time new roman",20,"bold"),fg="black",bg="white")
        self.titulo.place(x=150,y=20)
        self.botonEquipo = Button(self.frameUser,command=self.mostrarEq,text="Donar Equipo",
                        fg="black",bg="white", font=("times new roman", 15))
        self.botonEquipo.place(x=40,y=50)
        self.botonComponente = Button(self.frameUser,command=self.mostrarCom,text="Donar Componente",
                        fg="black",bg="white", font=("times new roman", 15))
        self.botonComponente.place(x=200,y=50)

        self.historialEquipo = Button(self.frameUser,command=self.archivoEquipos,text="Historial Equipo",
                        fg="black",bg="white", font=("times new roman", 15))
        self.historialEquipo.place(x=20,y=100)
        self.historialComponente = Button(self.frameUser,command=self.archivoComponentes,text="Historial Componente",
                        fg="black",bg="white", font=("times new roman", 15))
        self.historialComponente.place(x=200,y=100)
        self.botonSalir = Button(self.ventana, command = self.salirUser, text = "SALIR", fg = "black", 
                        bg = "#D50000", font = ("calibre",16, "bold"))
        self.botonSalir.place(x=530,y=335)
        
    def archivoEquipos(self):
        ventanaEquipos=Tk()
        ventanaEquipos.title('Listado de Equipos')
        ventanaEquipos.resizable(0,0)
        ventanaEquipos.geometry('400x200')
        archivoE = open("Equipos.txt")
        lblArchivo = Label(ventanaEquipos,text=f"{archivoE.read()}" ,font=("Agency FB",14))
        lblArchivo.place(x=10,y=0)
        ventanaEquipos.mainloop()

    def archivoComponentes(self):
        ventanaComponentes=Tk()
        ventanaComponentes.title('Listado de Componentes')
        ventanaComponentes.resizable(0,0)
        ventanaComponentes.geometry('400x200')
        archivoC = open("Componentes.txt")
        lblArchivo = Label(ventanaComponentes,text=f"{archivoC.read()}" ,font=("Agency FB",14))
        lblArchivo.place(x=10,y=0)
        ventanaComponentes.mainloop()

    def salirUser(self):
        self.ventana.withdraw()
        root = Tk()
        uiSitema = Login(root)
        root.mainloop()

    def mostrarEq(self):
        añadirDonativo = AgregarEquipo(tk.Toplevel())

    def mostrarCom(self):
        añadirDonativo = AgregarComponente(tk.Toplevel())

class AgregarEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("300x360")
        self.ventana.title("EcoTecno")
        self.ventana.resizable(0,0)
        self.titulo = None
        self.frameEquipo = None
        self.marca = StringVar()
        self.modelo = StringVar()
        self.año = StringVar()
        self.descripcion = StringVar()
        self.marcaEntrada = None
        self.modeloEntrada = None
        self.añoEntrada = None
        self.descripcionEntrada = None
        self.formularioEquipo()
    
    def formularioEquipo(self):
        self.frameEquipo = Frame(self.ventana, bg="white")
        self.frameEquipo.place(height=360, width=300)
        # Definir los labels
        self.titulo = Label(self.frameEquipo, text="Formulario Equipo", 
                        font=("time new roman",15,"bold"),fg="black",bg="white")
        self.titulo.place(x=50,y=9)
        lblMArca = Label(self.frameEquipo, text="Marca", bg="white",font=("bold"))
        lblMArca.place(x=18, y=50)   
        lblModelo = Label(self.frameEquipo, text="Modelo", bg="white",font=("bold"))
        lblModelo.place(x=18, y=110)
        lblAño = Label(self.frameEquipo, text="Año", bg="white",font=("bold"))
        lblAño.place(x=18, y=170)
        lblDescripcion = Label(self.frameEquipo, text="Descripcion del estado", bg="white",font=("bold"))
        lblDescripcion.place(x=18, y=230)
        # Obtener la informacion del usuario
        self.marcaEntrada = Entry(self.frameEquipo, textvariable=self.marca, width="30").place(x=18, y=80)
        self.modeloEntrada = Entry(self.frameEquipo, textvariable=self.modelo, width="30").place(x=18, y=140)
        self.añoEntrada = Entry(self.frameEquipo, textvariable= self.año, width="30").place(x=18, y=200)
        self.descripcionEntrada = Entry(self.frameEquipo, textvariable= self.descripcion, width="30").place(x=18, y=260)

        # Boton de confirmar
        botonConfir = Button(self.frameEquipo, text="Confirmar", width="15",
                            height="1", command=self.datosEquipo, bg="#9CCC65").place(x=70, y=300)

    def datosEquipo(self):
        self.ventana.withdraw()
        marcaEquipo = self.marca.get()
        modeloEquipo = self.modelo.get()
        añoEquipo = str(self.año.get())
        descripcionEquipo = self.descripcion.get()

        #Abrir un archivo
        file = open("Equipos.txt", "a")
        file.write(marcaEquipo)
        file.write("\t")
        file.write(modeloEquipo)
        file.write("\t")
        file.write(añoEquipo)
        file.write("\t")
        file.write(descripcionEquipo)
        file.write("\t\n")
        file.close()

class AgregarComponente:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("300x320")
        self.ventana.title("EcoTecno")
        self.ventana.resizable(0,0)
        self.titulo = None
        self.frameComp = None
        self.marca = StringVar()
        self.modelo = StringVar()
        self.descripcion = StringVar()
        self.marcaEntrada = None
        self.modeloEntrada = None
        self.descripcionEntrada = None
        self.formularioComp()

    def formularioComp(self):
        self.frameComp = Frame(self.ventana, bg="white")
        self.frameComp.place(height=320, width=300)
        # Definir los labels
        self.titulo = Label(self.frameComp, text="Formulario Componente", font=("time new roman",15,"bold"),
                                    fg="black",bg="white").place(x=13,y=9)
        lblMArca = Label(self.frameComp, text="Marca", bg="white",font=("bold")).place(x=18, y=50)   
        lblModelo = Label(self.frameComp, text="Modelo", bg="white",font=("bold")).place(x=18, y=110)
        lblDescripcion = Label(self.frameComp, text="Descripcion del estado", bg="white",font=("bold")).place(x=18, y=170)
        # Obtener la informacion del usuario
        self.marcaEntrada = Entry(self.frameComp, textvariable=self.marca, width="30").place(x=18, y=80)
        self.modeloEntrada = Entry(self.frameComp, textvariable=self.modelo, width="30").place(x=18, y=140)
        self.descripcionEntrada = Entry(self.frameComp, textvariable= self.descripcion, width="30").place(x=18, y=200)

        # Boton de confirmar
        botonConfir = Button(self.frameComp, text="Confirmar", width="15",
                            height="1", command=self.datosComp, bg="#9CCC65").place(x=70, y=240)

    def datosComp(self):
        self.ventana.withdraw()
        marcaComp = self.marca.get()
        modeloComp = self.modelo.get()
        descripcionComp = self.descripcion.get()

        #Abrir un archivo
        file = open("Componentes.txt", "a")
        file.write(marcaComp)
        file.write("\t")
        file.write(modeloComp)
        file.write("\t")
        file.write(descripcionComp)
        file.write("\t\n")
        file.close()
