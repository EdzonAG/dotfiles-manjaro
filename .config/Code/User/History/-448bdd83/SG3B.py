#!/usr/bin/python

from tkinter import *

data = Tk()
data.title('AXTY DataSheet')

technician = StringVar()
technician.set('Joseph')

client = StringVar()
email = StringVar()
number = StringVar()

data.columnconfigure(0, weight=1)
data.columnconfigure(1, weight=1)
data.columnconfigure(2, weight=1)
data.columnconfigure(3, weight=1)

data.rowconfigure(0, weight=0)
data.rowconfigure(1, weight=0)
data.rowconfigure(2, weight=1)
data.rowconfigure(3, weight=0)
data.rowconfigure(4, weight=1)
data.rowconfigure(5, weight=1)

title = Label(data, text= 'AXTY Technology').grid(padx=10, pady=5, row=0, column=0,columnspan=4,sticky=N)
subtitle = Label(data, text= 'Ficha Técnica').grid(padx=10, pady=5, row=1, column=0,columnspan=4,sticky=N)

label_technician = Label(data, text='Técnico:').grid(padx=10, pady=10, row=2, column=0,columnspan=2,sticky=W+E)
menu_technician = OptionMenu(data, technician, 'Joseph', 'Otro').grid(padx=10, pady=10, row=2, column=2,columnspan=2,sticky=W+E)

subtitle2 = Label(data, text= 'Datos del Cliente').grid(padx=10, pady=5, row=3, column=0,columnspan=4,sticky=N+S)

label_client = Label(data, text='Nombre Cliente:').grid(padx=10, pady=10, row=4, column=0, columnspan=2, sticky=W+E)
entry_client = Entry(data, textvariable=client).grid(padx=10, pady=10, row=4, column= 2, columnspan=2, sticky=W+E)

label_email = Label(data, text='Correo:').grid(padx=10, pady=10, row=5, column=0, sticky=W+E)
entry_email = Entry(data, textvariable=email).grid(padx=10, pady=10, row=5, column= 1, sticky=W+E)

label_number = Label(data, text='Número Telefono:').grid(padx=10, pady=10, row=5, column=2, sticky=W+E)
entry_number = Entry(data, textvariable=number).grid(padx=10, pady=10, row=5, column= 3, sticky=W+E)

subtitle3 = Label(data, text= 'Datos del Equipo').grid(padx=10, pady=5, row=6, column=0,columnspan=4,sticky=N+S)

data.mainloop()
