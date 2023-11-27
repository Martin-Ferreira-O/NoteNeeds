#!/bin/python
import tkinter
from tkinter import messagebox, IntVar
import webbrowser

# Pensado originalmente para las solemnes en la Universidad Autonoma

def ver_notas():
    WEB = "https://autoservicioestudiante.uautonoma.cl/StudentSelfService/ssb/studentGrades"
    webbrowser.open(WEB)


def calcular():
    n1 = nota1.get()
    n2 = nota2.get()
    n3 = nota3.get()

    p1 = (percent1.get() / 100)
    p2 = (percent2.get() / 100)
    p3 = (percent3.get() / 100)

    promedio_general = (n1 * p1) + (n2 * p2) + (n3 * p3)
    NOTA_MINIMA = 40

    p4 = 1 - (p1 + p2 + p3)

    if (p4 <= 0):
        messagebox.showerror("ERROR", "La suma de los porcentajes no puede ser mayor a 100")
        return
    
    nota_final = (NOTA_MINIMA - promedio_general) / p4

    if nota_final <= 0:
        messagebox.showinfo("ERES UN FUCKING GENIO",f"Ya pasaste, tu nota 4 puede ser 0 y aun asi pasas ({nota_final})!")
        return
    
    messagebox.showinfo("NOTA MINIMA NECESARIA",f"Necesitas como minimo un [{nota_final}] en tu nota 4 para pasar, SUERTE")

tk = tkinter.Tk()

nota1 = IntVar()
nota2 = IntVar()
nota3 = IntVar()

percent1 = IntVar()
percent2 = IntVar()
percent3 = IntVar()
percent4 = IntVar()


tk.title("Calculadora de notas")
tk.geometry("400x400")
tk.config(bg="#ccc")
tk.resizable(0, 0)


tkinter.Label(tk, text="NOTA 1", bg="black", fg="white").grid(row=0, column=0, padx=5, pady=20)
tkinter.Entry(tk, textvariable=nota1).grid(row=1, column=0, padx=5, pady=20)
tkinter.Label(tk, text="PORCENTAJE NOTA 1", bg="black", fg="white").grid(row=0, column=1, padx=5, pady=20)
tkinter.Entry(tk, textvariable=percent1).grid(row=1, column=1, padx=5, pady=20)

tkinter.Label(tk, text="NOTA 2", bg="black", fg="white").grid(row=2, column=0, padx=5, pady=20)
tkinter.Entry(tk, textvariable=nota2).grid(row=3, column=0, padx=5, pady=20)
tkinter.Label(tk, text="PORCENTAJE NOTA 2", bg="black", fg="white").grid(row=2, column=1, padx=5, pady=20)
tkinter.Entry(tk, textvariable=percent2).grid(row=3, column=1, padx=5, pady=20)

tkinter.Label(tk, text="NOTA 3", bg="black", fg="white").grid(row=4, column=0, padx=5, pady=20)
tkinter.Entry(tk, textvariable=nota3).grid(row=5, column=0, padx=5, pady=20)
tkinter.Label(tk, text="PORCENTAJE NOTA 3", bg="black", fg="white").grid(row=4, column=1, padx=5, pady=20)
tkinter.Entry(tk, textvariable=percent3).grid(row=5, column=1, padx=5, pady=20)

tkinter.Button(tk, text="CALCULAR", command=calcular, bg="RED").grid(row=6, column=1)

tkinter.Button(tk, text="VER NOTAS", command=ver_notas, bg="GREEN").grid(row=6, column=0)

tk.mainloop()
