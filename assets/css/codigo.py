from tkinter import *
import math

ventana = Tk()
ventana.geometry("500x420")
ventana.config(bg="steelblue")
ventana.title("Calculadora de Areas - 6 Figuras")

res = StringVar()
res.set("Resultado:")
num1 = DoubleVar()
num2 = DoubleVar()
num3 = DoubleVar()

def area_cuadrado():
    try:
        a = num1.get() * num1.get()
        res.set(f"Cuadrado: {a}")
    except: res.set("Error en datos")

def area_rectangulo():
    try:
        a = num1.get() * num2.get()
        res.set(f"Rectangulo: {a}")
    except: res.set("Error en datos")

def area_triangulo():
    try:
        a = (num1.get() * num2.get()) / 2
        res.set(f"Triangulo: {a}")
    except: res.set("Error en datos")

def area_circulo():
    try:
        a = round(math.pi * num1.get() * num1.get(), 3)
        res.set(f"Circulo: {a}")
    except: res.set("Error en datos")

def area_trapecio():
    try:
        a = ((num1.get() + num2.get()) * num3.get()) / 2
        res.set(f"Trapecio: {a}")
    except: res.set("Error en datos")

def area_rombo():
    try:
        a = (num1.get() * num2.get()) / 2
        res.set(f"Rombo: {a}")
    except: res.set("Error en datos")

# Entradas
Label(ventana, text="Dato 1 (lado, base, radio):", bg="steelblue", fg="white").place(x=30, y=10)
Entry(ventana, textvariable=num1, width=20).place(x=30, y=35)

Label(ventana, text="Dato 2 (altura, base menor, diagonal):", bg="steelblue", fg="white").place(x=30, y=65)
Entry(ventana, textvariable=num2, width=20).place(x=30, y=90)

Label(ventana, text="Dato 3 (solo para Trapecio = altura):", bg="steelblue", fg="white").place(x=30, y=120)
Entry(ventana, textvariable=num3, width=20).place(x=30, y=145)

Label(ventana, textvariable=res, bg="white", fg="black", width=35, anchor="w", font=("Arial", 12, "bold")).place(x=30, y=180)

# BOTONES EN FORMA DE CALCULADORA
Button(ventana, text="Cuadrado", bg="#F9FBFD", fg="white", width=10, command=area_cuadrado).place(x=30, y=230)
Button(ventana, text="Rectangulo", bg="#E2EBF3", fg="white", width=10, command=area_rectangulo).place(x=140, y=230)
Button(ventana, text="Triangulo", bg="#EDF1F5", fg="white", width=10, command=area_triangulo).place(x=250, y=230)

Button(ventana, text="Circulo", bg="steelblue", fg="white", width=10, command=area_circulo).place(x=30, y=270)
Button(ventana, text="Trapecio", bg="steelblue", fg="white", width=10, command=area_trapecio).place(x=140, y=270)
Button(ventana, text="Rombo", bg="#steelblue", fg="white", width=10, command=area_rombo).place(x=250, y=270)

Label(ventana, text="Cuadrado: Lado*Lado | Rect: base*altura | Tri: base*alt/2", bg="steelblue", fg="white", font=("Arial", 8)).place(x=30, y=330)
Label(ventana, text="Circulo: pi*r² | Trapecio: (B+b)*h/2 | Rombo: D*d/2", bg="steelblue", fg="white", font=("Arial", 8)).place(x=30, y=350)

ventana.mainloop()



