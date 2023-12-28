from tkinter import *
import tkinter as tk
from tkinter import messagebox
from User import *
# Create la clase TK
class Login:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("650x550")
        self.ventana.title("EcoTecno")
        self.ventana.resizable(0,0)
        self.textoUsuario = StringVar()
        self.textoPass = StringVar()
        self.frameLogin = None
        self.titulo = None
        self.lblUsuario = None
        self.ingresarUser = None
        self.lblPass = None
        self.ingresarPass = None
        self.botonEntrar = None
        self.widgetsLogin()
        
    def widgetsLogin(self):
        self.ventana.config(background="white")
        self.frameLogin = Frame(self.ventana, bg="#9CCC65")
        self.frameLogin.place(x=130,y=100,height=340,width=400)
        #Imagenes
        #fotoUser = PhotoImage(file="imageLog.png")
        #lblFoto = Label(self.frameLogin, image=fotoUser,bd=0).pack()
        #ingreso de lablel y entry
        self.titulo = Label(self.ventana, text="Inicie Sesión", font=("time new roman",20,"bold"),fg="black",bg="white")
        self.titulo.place(x=245,y=25)
        self.lblUsuario = Label(self.frameLogin, text="Nombre de usuario",font=("time new roman",13), bg="#9CCC65")
        self.lblUsuario.place(x=120, y=90)
        self.ingresarUser = Entry(self.frameLogin, textvariable = self.textoUsuario, font=("times new roman",12))
        self.ingresarUser.place(x=40,y=120,width=325)
        self.lblPass = Label(self.frameLogin, text="Contraseña", font=("time new roman",13),fg="black",bg="#9CCC65")
        self.lblPass.place(x=145,y=165)
        self.ingresarPass = Entry(self.frameLogin, textvariable = self.textoPass, show="*", font=("times new roman",12))
        self.ingresarPass.place(x=40,y=195,width=325)
        #Boton
        self.botonEntrar = Button(self.frameLogin,command= self.uiLogin,text="Ingresar",fg="black",bg="white", font=("times new roman", 15))
        self.botonEntrar.place(x=147,y=255)

    def uiLogin(self):
        if self.textoUsuario.get() == "" or self.textoPass.get() == "":
            messagebox.showerror("Error", "Los campos son obligatorios")
        elif self.textoUsuario.get() != "Proyecto Poo" or self.textoPass.get() != "12345":
            messagebox.showerror("Error", "Usuario o contraseña incorrectas")
        else:
            self.ventana.withdraw()
            entrarUser = PerfilUser(tk.Toplevel())
        
if __name__ == "__main__":
    root = Tk()
    uiSistema = Login(root)
    root.mainloop()     
        
            
          


