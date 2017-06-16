#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pyro4
from Tkinter import *
import tkMessageBox
from functools import partial
import getpass
import json
import mysql.connector
import MySQLdb
import MySQLdb
from requests import get    # http
import re, string  # patron o expresion regular para la busqueda de una subcadena

HOST = '127.0.0.1'
PORT = '3306'
USER = 'root'
PASSWORD = ''       # conexion a base de datos en otro conputador
DATABASE = 'estacion'

#Conectar
def conexion():
    estacion = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", passwd="luciana", db="estacion")
    cursor = estacion.cursor()

def run_query(query):                  #La funcion Run Query permite realizar llamados a la base de datos
    estacion = mysql.connector.connect(host=HOST,
                                       database=DATABASE,
                                       user=USER,
                                       password=PASSWORD)
    cursor = estacion.cursor()
    cursor.execute(query)



def amd():
    ## Crea la ventana amd.
    t1 = Toplevel(root)

    ## Establece el tamaño para la ventana.
    t1.geometry('1000x500+200+10')

    ## Provoca que la ventana tome el focus
    t1.focus_set()

    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t1.grab_set()

    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t1.transient(master=root)

    ## Crea un widget Label en la ventana
    Label(t1, text='ADMINISTRADOR',  font=('chiller', 40), fg='blue').pack()

    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.

    gasboton = PhotoImage(file='gasolina.gif')
    Button(t1, text="GASOLINA", image=gasboton, bg="SILVER", relief="groove", borderwidth=5, width=180, height=180,
           anchor="nw", command=gasolina).place(x=100, y=100)
    usuboton = PhotoImage(file='usu.gif')
    Button(t1, text="USUARIOS", image=usuboton, bg="SILVER", relief="groove", borderwidth=5, width=180, height=180,
           anchor="nw", command=usuarios).place(x=730, y=100)
    venboton = PhotoImage(file='ventas.gif')
    Button(t1, text="VENTAS", image=venboton, bg="SILVER", relief="groove", borderwidth=5, width=180, height=180,
           anchor="nw", command=ventas).place(x=520, y=100)
    aleboton = PhotoImage(file='alerta.gif')
    Button(t1, text="ALERTAS", image=aleboton, bg="SILVER", relief="groove", borderwidth=5, width=180, height=180,
           anchor="nw", command=alertas).place(x=310, y=100)

    salir1boton = PhotoImage(file='salir1.gif')
    Button(t1, image=salir1boton, relief="groove", borderwidth=5, width=100, height=50, anchor="nw", command=t1.destroy).place(x=450, y=400)

    ## Pausa el mainloop de la ventana de donde se hizo la invocación.
    t1.wait_window(t1)


def gasolina():
    ## Crea una sub ventana gasolina.
    t3 = Toplevel(root)

    ## Establece el tamaño para la ventana.
    t3.geometry('1000x500+200+10')

    ## Provoca que la ventana tome el focus
    t3.focus_set()

    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t3.grab_set()

    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t3.transient(master=root)

    ## Crea un widget Label en la ventana
    Label(t3, text='ADMINISTRADOR', font=('chiller', 40), fg='blue').pack()

    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.

    Label(t3, text="TIPOS DE GASOLINA", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
          anchor="nw").place(x=100, y=100)
    Label(t3, text="AGREGAR TIPO DE GASOLINA", bg="SILVER", relief="groove", borderwidth=5, width=30, height=2,
          anchor="nw").place(x=400, y=100)
    entrada_gas = StringVar()
    Label(t3, text="ACTUALIZAR", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
          anchor="nw").place(x=750, y=100)

    def agregar():
        query = "INSERT INTO gasolina (tipo_gas) VALUES ('%s')" % (entrada_gas.get())
        run_query(query)
        #print entrada_gas.get()



    ##PRECIOS DE LA GASOLINA
    Radiobutton(t3, text="Extra       $ 10.000", value=1).place(x=100, y=150)
    Radiobutton(t3, text="Corriente   $ 8.000", value=2).place(x=100, y=180)
    Radiobutton(t3, text="A.C.P.M     $ 7.000", value=3).place(x=100, y=210)

    ## Crea un entry tipo gasolina.
    tpg = Entry(t3, text=entrada_gas)
    ## Establece el focus en el entry.
    tpg.focus()
    tpg.place(x=450, y=150)


    Button(t3, text='AGREGAR', font=('chiller', 20), bg='white', width=10, height=2, command=agregar).place(x=460, y=200)

    #salirboton = PhotoImage(file='salir2.gif')
    Button(t3, text='SALIR', relief="groove", borderwidth=5, width=10, height=2, anchor="nw", command=t3.destroy).place(x=450, y=400)



def usuarios():
        ## Crea la ventana usuarios
        t4 = Toplevel(root)

        ## Establece el tamaño para la ventana.
        t4.geometry('1000x500+200+10')

        ## Provoca que la ventana tome el focus
        t4.focus_set()

        ## Deshabilita todas las otras ventanas hasta que
        ## esta ventana sea destruida.
        t4.grab_set()

        ## Indica que la ventana es de tipo transient, lo que significa
        ## que la ventana aparece al frente del padre.
        t4.transient(master=root)

        ## Crea un widget Label en la ventana
        Label(t4, text='ADMINISTRADOR', font=('E', 40), fg='blue').pack()

        ## Crea un widget que permite cerrar la ventana,
        ## para ello indica que el comando a ejecutar es el
        ## metodo destroy de la misma ventana.

        Button(t4, text="SALIR", bg="white", relief="groove", borderwidth=5, width=20, height=2,
               anchor="nw", command=t4.destroy).place(x=400, y=400)
        Label(t4, text="VER LISTADO + PUNTOS", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
               anchor="nw").place(x=400, y=100)

        ##crear la lista
        lsusuarios = Listbox(t4, width=100)
        lsusuarios.insert(0, 'usuario1', 'usuario2', 'usuario3', 'usuario4')
        lsusuarios.place(x=200, y=200)


def ventas():
    ## Crea la ventana ventas.
    t5 = Toplevel(root)

    ## Establece el tamaño para la ventana.
    t5.geometry('1000x500+200+10')

    ## Provoca que la ventana tome el focus
    t5.focus_set()

    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t5.grab_set()

    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t5.transient(master=root)

    ## Crea un widget Label en la ventana
    Label(t5, text='ADMINISTRADOR', font=('chiller', 40), fg='blue').pack()

    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.

    Button(t5, text="SALIR", bg="pink", relief="groove", borderwidth=5, width=20, height=2,
           anchor="nw", command=t5.destroy).place(x=430, y=400)
    Label(t5, text="LISTADO DE FACTURAS", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
           anchor="nw").place(x=100, y=100)
    Label(t5, text="DETALLE DE FACTURAS", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
          anchor="nw").place(x=425, y=100)
    Label(t5, text="INGRESE EL NUMERO DE FACTURA", bg="SILVER", relief="groove", borderwidth=5, width=27, height=2,
          anchor="nw").place(x=400, y=150)
    num_fact = IntVar()

    Button(t5, text="TOTAL VENTAS DEL DIA", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
           anchor="nw").place(x=750, y=100)

    def numero_factura():
        query = "SELECT num_fact FROM factura"
        result = run_query(query)
        #return result
        print result

    ##crear la lista de facturas adm
    lsverfact = Listbox(t5)
    lsverfact.insert(0, 'factura1', 'factura2', 'factura3', 'factura4')
    lsverfact.place(x=100, y=150)

    ## Crea un entry user.
    nf = Entry(t5, text=num_fact, width=10)

    ## Establece el focus en el entry.
    nf.focus()
    nf.place(x=470, y=200)

    Button(t5, text='ACEPTAR', font=('chiller', 14), bg='gold', command=numero_factura).place(x=460, y=250)



def alertas():
    ## Crea la ventana alertas.
    t6 = Toplevel(root)

    ## Establece el tamaño para la ventana.
    t6.geometry('1000x550+200+10')

    ## Provoca que la ventana tome el focus
    t6.focus_set()

    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t6.grab_set()

    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t6.transient(master=root)

    ## Crea un widget Label en la ventana
    Label(t6, text='ADMINISTRADOR', font=('chiller', 40), fg='blue').pack()

    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.

    Button(t6, text="SALIR", bg="green", relief="groove", borderwidth=5, width=20, height=2,
           anchor="nw", command=t6.destroy).place(x=400, y=450)
    Button(t6, text="PRODUCTOS OK", bg="SILVER", relief="groove", borderwidth=5, width=20, height=5,
           anchor="nw", command=t6.destroy).place(x=100, y=100)
    Button(t6, text="ADQUIRIR PRODUCTO", bg="SILVER", relief="groove", borderwidth=5, width=20, height=5,
           anchor="nw", command=t6.destroy).place(x=750, y=100)

    ##mensaje de alerta
    tkMessageBox.showinfo('¡BIENVENIDO!', message='PRODUCTO ESTA POR AGOTARSE')




def cliente():
    ## Crea la ventana cliente.
    t2 = Toplevel(root)

    ## Establece el tamaño para la ventana.
    t2.geometry('1000x500+200+10')

    ## Provoca que la ventana tome el focus
    t2.focus_set()

    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t2.grab_set()

    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t2.transient(master=root)

    ## Crea un widget Label en la ventana
    Label(t2, text='CLIENTE',  font=('E', 40), fg='skyblue').pack()

    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.


    Label(t2, text="COMPRA DE GASOLINA", bg="SILVER", relief="groove", borderwidth=5, width=25, height=2, anchor="nw").place(x=100, y=100)
    comboton = PhotoImage(file='pantalla.gif')
    Button(t2, image=comboton, relief="groove", borderwidth=5, width=180, height=180, anchor="nw", command=compra_gasolina).place(x=100, y=150)

    Label(t2, text="PUNTOS", bg="SILVER", relief="groove", borderwidth=5, width=25, height=2, anchor="nw").place(x=750, y=100)
    ptsboton = PhotoImage(file='puntos.gif')
    Button(t2, image=ptsboton, relief="groove", borderwidth=5, width=180, height=180, anchor="nw", command=puntos).place(x=750, y=150)

    Label(t2, text="FACTURAS", bg="SILVER", relief="groove", borderwidth=5, width=25, height=2, anchor="nw").place(x=430, y=100)
    factboton = PhotoImage(file='fact.gif')
    Button(t2, image=factboton, relief="groove", borderwidth=5, width=180, height=180, anchor="nw", command=facturas).place(x=430, y=150)

    salirboton = PhotoImage(file='salir.gif')
    Button(t2, image=salirboton, relief="groove", borderwidth=5, width=100, height=50, anchor="nw", command=t2.destroy).place(x=450, y=400)

    ## Pausa el mainloop de la ventana de donde se hizo la invocación.
    t2.wait_window(t2)

def compra_gasolina():
        ## Crea la ventana compra de gasolina.
        t7 = Toplevel(root)

        ## Establece el tamaño para la ventana.
        t7.geometry('1000x550+200+10')

        ## Provoca que la ventana tome el focus
        t7.focus_set()

        ## Deshabilita todas las otras ventanas hasta que
        ## esta ventana sea destruida.
        t7.grab_set()

        ## Indica que la ventana es de tipo transient, lo que significa
        ## que la ventana aparece al frente del padre.
        t7.transient(master=root)

        ## Crea un widget Label en la ventana
        Label(t7, text='CLIENTE', font=('E', 40), fg='skyblue').pack()

        ## Crea un widget que permite cerrar la ventana,
        ## para ello indica que el comando a ejecutar es el
        ## metodo destroy de la misma ventana.

        Button(t7, text="SALIR", bg="orange", relief="groove", borderwidth=5, width=20, height=2,
               anchor="nw", command=t7.destroy).place(x=400, y=450)
        Label(t7, text="TIPOS DE GASOLINA", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
               anchor="nw").place(x=100, y=100)

        Label(t7, text="CANTIDAD A TANQUEAR", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
               anchor="nw").place(x=300, y=100)
        cant_tan = StringVar()
        Button(t7, text="NOMBRE USUARIO", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
               anchor="nw").place(x=550, y=100)
        usuario = StringVar()


        def agregarusu():
            query = "INSERT INTO factura (nombre,cantidad,tipo_gasolina) VALUES ('%s','%s','%s')" % (usuario.get(),cant_tan.get())
            run_query(query)

        ##PRECIOS DE LA GASOLINA
        Radiobutton(t7, text="Extra        $ 10.000", value=1).place(x=100, y=150)
        Radiobutton(t7, text="Corriente   $ 8.000", value=2).place(x=100, y=180)
        Radiobutton(t7, text="A.C.P.M     $ 7.000", value=3).place(x=100, y=210)

        ## Crea un entry cant a tanquear.
        ctg = Entry(t7, text=cant_tan)
        ## Establece el focus en el entry.
        ctg.focus()
        ctg.place(x=300, y=150)

        usu = Entry(t7, text=usuario)
        ## Establece el focus en el entry.
        usu.focus()
        usu.place(x=550, y=150)
        Button(t7, text="PAGAR", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2, command=agregarusu).place(x=750, y=100)

def pagar():
    tkMessageBox.showinfo('¡MUY BIEN!', message='PAGO PROCESADO')


def puntos():
    ## Crea la ventana puntos.
    t8 = Toplevel(root)

    ## Establece el tamaño para la ventana.
    t8.geometry('1000x400+200+10')

    ## Provoca que la ventana tome el focus
    t8.focus_set()

    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t8.grab_set()

    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t8.transient(master=root)

    ## Crea un widget Label en la ventana
    Label(t8, text='CLIENTE', font=('E', 40), fg='blue').pack()

    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.

    Button(t8, text="SALIR", bg="blue", relief="groove", borderwidth=5, width=20, height=2,
           anchor="nw", command=t8.destroy).place(x=430, y=300)
    Button(t8, text="VER PUNTOS", bg="SILVER", relief="groove", borderwidth=5, width=20, height=5,
           anchor="nw", command=puntos).place(x=100, y=100)
    Button(t8, text="CAMBIAR PUNTOS X PRODUCTOS", bg="SILVER", relief="groove", borderwidth=5, width=30, height=5,
           anchor="nw", command=puntos).place(x=750, y=100)


def facturas():
    ## Crea la ventana facturas.
    t9 = Toplevel(root)

    ## Establece el tamaño para la ventana.
    t9.geometry('1000x500+200+10')

    ## Provoca que la ventana tome el focus
    t9.focus_set()

    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t9.grab_set()

    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t9.transient(master=root)

    ## Crea un widget Label en la ventana
    Label(t9, text='CLIENTE', font=('E', 40), fg='blue').pack()

    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.

    Button(t9, text="SALIR", bg="YELLOW", relief="groove", borderwidth=5, width=20, height=2,
           anchor="nw", command=t9.destroy).place(x=400, y=400)

    Label(t9, text="DETALLE DE FACTURAS", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
           anchor='nw').place(x=750, y=100)
    Label(t9, text="INGRESE EL NUMERO DE FACTURA", bg="SILVER", relief="groove", borderwidth=5, width=27, height=2,
          anchor="nw").place(x=400, y=100)

    def verfact():
        query = "SELECT id_fact, nombre FROM factura"
        resultado=run_query(query)
        return resultado

    Button(t9, text="VER LISTADO DE FACTURAS", bg="SILVER", relief="groove", borderwidth=5, width=20, height=2,
           anchor="nw", command=verfact).place(x=100, y=100)
    v = StringVar()
    ##crear la lista de facturas cliente
    #lsverfactcli = Listbox(t9)
    #lsverfactcli.insert('factura1', 'factura2', 'factura3', 'factura4')
    #lsverfactcli.place(x=100, y=150)


    nf = Entry(t9, width=10)
    nf.focus()
    nf.place(x=400, y=150)

    listad = Label(t9, text= '')
    listad.place(x=100, y=150)
    resu = verfact()
    #listad['text'] = resu
    print verfact()



########################################################################################################################

## Crea la ventana para la aplicación
root = Tk()


## Establece un título y un tamaño para la ventana
root.title('ESTACION DE GASOLINA FALIPA')
root.geometry('1350x650+1+1')

## Crea una etiqueta.
Label(root, text='BIENVENIDOS', font=('chiller', 50), fg='blue').pack()

'''usuario = StringVar()
def user():
    query = "SELECT adm_nom FROM admin"
    result = run_query(query)
    return result
'''

##Crear etiquetas y cajas de texto para validacion de usuario
Label(root, text='USER', font=('chiller', 20), fg='black').pack()

## Crea un entry user
u = Entry(root)

## Establece el focus en el entry.
u.focus()
u.pack()
Label(root, text='PASSWORD', font=('chiller', 20), fg='black').pack()

'''clave = StringVar()
def password():
'''

## Crea un entry password.
p = Entry(root)
p.pack()



def aceptar():
    #if usuario == fausto & clave == luciana:
        tkMessageBox.showinfo('¡BIENVENIDO!', message='USUARIO CORRECTO')
    #else:
     #   tkMessageBox.showinfo('¡ERROR!', message='USUARIO INCORRECTO')


Button(root, text='ACEPTAR', command=aceptar, font=('chiller', 14), bg='red').place(x=640, y=250)

## Crea un botón, desde el cual se puede lanzar una
## ventana de tipo modal.
amdboton= PhotoImage(file='adm2.gif')
Button(root, text="ADMINISTRADOR", image=amdboton,  command=amd, relief="groove", borderwidth=10, width=230, height=210, anchor="nw").place(x=100, y=100)
cliboton= PhotoImage(file='cliente.gif')
Button(root, text="CLIENTE", image=cliboton, command=cliente, relief="groove", borderwidth=10, width=225, height=225, anchor="nw").place(x=1000, y=100)
exitboton= PhotoImage(file='to.gif')
Button(root, text="HASTA PRONTO", image=exitboton, bg="purple", relief="groove", borderwidth=5, width=220, height=220, anchor="nw", command=root.destroy).place(x=550, y=400)

#def admin():
 #   if query = "SELECT  adm_nom, adm_pass, FROM admin":
  #      result = run_query(query)
   # return result
    #else

root.mainloop()

