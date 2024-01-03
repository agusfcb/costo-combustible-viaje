# esta aplicacion debe servir para estimar el gasto de dinero en combustible en un viaje.
# interfaz grafica pendiente
from tkinter import *
from tkinter import ttk

def function_consumo(*args):
    try:
        consumo_prom = float(consumo.get())
        kilometros_prom = float(kilometros.get())
        precio_aprox = float(precio.get())
        total = round((kilometros_prom * consumo_prom/100) * precio_aprox, 2)
        return total_calculo.set("$ " + str(total))
    except ValueError:
        total_calculo.set("Error, coloque solo numeros sin letras ni simbolos")
        function_consumo()


root = Tk()
root.title("Calculo de costo")

mainframe = ttk.Frame(root, padding="3 3 12 12")

mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

consumo = StringVar()
entrada_consumo = ttk.Entry(mainframe, width=7, textvariable=consumo)
entrada_consumo.grid(column=2, row=1, sticky=(W,E))
ttk.Label(mainframe, text="promedio consumo: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text=" /100 Km").grid(column=3, row=1, sticky=W)

kilometros = StringVar()
entrada_kilometros = ttk.Entry(mainframe, width=7, textvariable=kilometros)
entrada_kilometros.grid(column=2, row=2, sticky=(W,E))
ttk.Label(mainframe, text="Total Km: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text=" Kms").grid(column=3, row=2, sticky=W)

precio = StringVar()
entrada_precio = ttk.Entry(mainframe, width=7, textvariable=precio)
entrada_precio.grid(column=2, row=3, sticky=(W,E))
ttk.Label(mainframe, text="Precio promedio del combustible: ").grid(column=1, row=3, sticky=W)

total_calculo = StringVar()
linea0 = ttk.Label(mainframe, textvariable=total_calculo)
linea0.grid(column=2, row=4, sticky=(W,E))
ttk.Label(mainframe, text="Total:").grid(column=1, row=4, sticky=(W,E))

boton_1 = ttk.Button(mainframe, text="Calcular", command=function_consumo).grid(column=4, row=5, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", function_consumo)
entrada_consumo.focus()

root.mainloop()
