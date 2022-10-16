#!/usr/bin/python

from tkinter import *

#Inicio Ventana Principal
data = Tk()
data.title('AXTY DataSheet')

#Variables de Menu
technician = StringVar()
technician.set('Joseph')
device = StringVar()
device.set('Desktop PC')
disk = StringVar()
disk.set('GB Disco Duro HDD')
ramtype = StringVar()
ramtype.set('GB DDR3')

#Variables de Entrada
client = StringVar()
email = StringVar()
number = StringVar()
brand = StringVar()
model = StringVar()
cpu = StringVar()
memory = StringVar()
capacity = StringVar()

#Redimencionamiento Filas y Columnas
data.columnconfigure(0, weight=1)
data.columnconfigure(1, weight=1)
data.columnconfigure(2, weight=1)
data.columnconfigure(3, weight=1)
data.rowconfigure(2, weight=1)
data.rowconfigure(3, weight=0)
data.rowconfigure(4, weight=1)
data.rowconfigure(5, weight=1)

##INICIO ELEMENTOS VISUALES##

#Titulo Principal Fila 1 y 2
title = Label(data, text= 'AXTY Technology').grid(padx=10, pady=5, row=0, column=0,columnspan=4,sticky=N)
subtitle = Label(data, text= 'Ficha Técnica').grid(padx=10, pady=5, row=1, column=0,columnspan=4,sticky=N)

#Menu Técnico Fila 3
label_technician = Label(data, text='Técnico:').grid(padx=10, pady=10, row=2, column=0,columnspan=2,sticky=W+E)
menu_technician = OptionMenu(data, technician, 'Joseph', 'Otro').grid(padx=10, pady=10, row=2, column=2,columnspan=2,sticky=W+E)

#Datos Cliente Fila 4
subtitle2 = Label(data, text= 'Datos del Cliente').grid(padx=10, pady=5, row=3, column=0,columnspan=4,sticky=N+S)

#Entrada Cliente Fila 5
label_client = Label(data, text='Nombre Cliente:').grid(padx=10, pady=10, row=4, column=0, columnspan=2, sticky=W+E)
entry_client = Entry(data, textvariable=client).grid(padx=10, pady=10, row=4, column= 2, columnspan=2, sticky=W+E)

#Correo y Número Fila 6
label_email = Label(data, text='Correo:').grid(padx=10, pady=10, row=5, column=0, sticky=W+E)
entry_email = Entry(data, textvariable=email).grid(padx=10, pady=10, row=5, column= 1, sticky=W+E)

label_number = Label(data, text='Número Telefono:').grid(padx=10, pady=10, row=5, column=2, sticky=W+E)
entry_number = Entry(data, textvariable=number).grid(padx=10, pady=10, row=5, column= 3, sticky=W+E)

#Datos Equipo Fila 7
subtitle3 = Label(data, text= 'Datos del Equipo').grid(padx=10, pady=5, row=6, column=0,columnspan=4,sticky=N+S)

#Menu Equipo y Marca Fila 8
label_device = Label(data, text='Tipo de Equipo:').grid(padx=10, pady=10, row=7, column=0, sticky=W+E)
menu_device = OptionMenu(data, device, 'Desktop PC', 'Laptop PC', 'Consola', 'Control').grid(padx=10, pady=10, row=7, column=1,sticky=W+E)

label_marca = Label(data, text='Marca:').grid(padx=10, pady=10, row=7, column=2, sticky=W+E)
entry_marca = Entry(data, textvariable=brand).grid(padx=10, pady=10, row=7, column= 3, sticky=W+E)

#CPU y Modelo Fila 9
label_cpu = Label(data, text='CPU:').grid(padx=10, pady=10, row=8, column=0, sticky=W+E)
entry_cpu = Entry(data, textvariable=cpu).grid(padx=10, pady=10, row=8, column= 1, sticky=W+E)

label_modelo = Label(data, text='Modelo:').grid(padx=10, pady=10, row=8, column=2, sticky=W+E)
entry_modelo = Entry(data, textvariable=model).grid(padx=10, pady=10, row=8, column= 3, sticky=W+E)

#Almacenamiento Fila 10
label_disk = Label(data, text='Almacenamiento:').grid(padx=10, pady=10, row=9, column=0,columnspan=2, sticky=W+E)
entry_disk = Entry(data, textvariable=capacity).grid(padx=10, pady=10, row=9, column= 2, sticky=E+W)
menu_disk = OptionMenu(data, disk, 'GB Disco Duro HDD', 'GB Unidad Solida SSD', 'GB M.2 SSD').grid(padx=10, pady=10, row=9, column= 3, sticky=W)

#Memoria RAM Fila 11
label_memory = Label(data, text='Memoria RAM:').grid(padx=10, pady=10, row=10, column=0,columnspan=2, sticky=W+E)
entry_memory = Entry(data, textvariable=memory).grid(padx=10, pady=10, row=10, column= 2, sticky=W+E)
menu_memory = OptionMenu(data, ramtype, 'GB DDR3', 'GB DDR4', 'GB DDR5').grid(padx=10, pady=10, row=10, column= 3, sticky=W)

#

#Fin Ventana Principal
data.mainloop()
