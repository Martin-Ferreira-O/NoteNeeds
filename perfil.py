from tkinter import *
from tkinter import messagebox

from main import db # De esta forma, nos conectaremos siempre a la misma base de datos que estamos conectados en el main

root = Tk()
# Configuracion de la ventana 
root.title("Crea tu perfil")
root.geometry("1000x600")
root.config(bg="#ccc")
root.resizable(0, 0)

# Variables

nombre = StringVar()
rut = StringVar()
universidad = StringVar()

# Funciones

def verificar_cuenta_unica():
    if db.get_profile(rut.get()):
        messagebox.showerror("Perfil", "Ya existe un perfil con ese rut")
        return False
    else:
        return True

def guardar_perfil():
    if nombre.get() != "" and rut.get() != "" and universidad.get() != "":
        print("Guardando un nuevo perfil")
        db.create_profile(nombre.get(), rut.get(), universidad.get())

        messagebox.showinfo("Perfil", "Perfil guardado correctamente")
        root.destroy() # Cerramos la ventana
    else:
        messagebox.showerror("Perfil", "Debes completar todos los campos")



# Widgets

# Label

if __name__ == '__main__':

    label_nombre = Label(root, text="Nombre", font=("Arial", 20), bg="#ccc")
    label_nombre.place(x=50, y=50)

    label_rut = Label(root, text="Rut", font=("Arial", 20), bg="#ccc")
    label_rut.place(x=50, y=100)

    label_universidad = Label(root, text="Universidad", font=("Arial", 20), bg="#ccc")
    label_universidad.place(x=50, y=150)

    # Entry

    entry_nombre = Entry(root, font=("Arial", 20), textvariable=nombre)
    entry_nombre.place(x=250, y=50)

    entry_rut = Entry(root, font=("Arial", 20), textvariable=rut)
    entry_rut.place(x=250, y=100)

    entry_universidad = Entry(root, font=("Arial", 20), textvariable=universidad)
    entry_universidad.place(x=250, y=150)

    # Button

    button_guardar = Button(root, text="Guardar", font=("Arial", 20), command=guardar_perfil)
    button_guardar.place(x=50, y=200)

    root.mainloop()