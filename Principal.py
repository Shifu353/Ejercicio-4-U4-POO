from tkinter import *
from tkinter import ttk
from functools import partial
import fractions 

class Fraccion ():
    def __init__ (self, op1, op2):
        self.operando_1 = op1
        self.operando_2 = op2
        self.variable = 2

    def __add__ (self,operando): 
        return int(self.operando_1 + operando.operando_2)

    def __sub__ (self,operando):
        return int(self.operando_1 - operando.operando_2)

    def __mul__ (self,operando):
        return int(self.operando_1 * operando.operando_2)
    
    def __truediv__ (self,operando):
        return int(self.operando_1 / self.operando_2)
    
    def Simplificar (self,num,deno):
        nume = float(num)/self.variable
        denomi = float(deno)/self.variable
        
        if(nume.is_integer() and denomi.is_integer()):
            return self.Simplificar(nume,denomi)
        else:
            if(self.variable == num or self.variable == deno or nume <= 1 or denomi <= 1):
                return "{}/{}".format(int(num),int(deno))
            else:
                self.variable +=1
                return self.Simplificar(num,deno)
    

class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperandoF1 = None
    __segundoOperandoF2 = None
    __primerOperandoF3 = None
    __segundoOperadorF4 = None
    __primerOperando=None
    __segundoOperando=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        self.__ventana.resizable(0,0)
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3,sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W) 
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='a/b', command=partial(self.ponerNUMERO, '/')).grid(column=1, row=8, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='Simplificar',command=(self.Actualizar)).grid(column=2, row=8, sticky=W)
        #ttk.Button(mainframe, text='DEL',command=(self.Actualizar)).grid(column=3, row=8, sticky=W)
        #self.__panel.set('0')
        panelEntry.focus()
        self.__ventana.mainloop()
    
    def Actualizar (self):
        if self.__panel.get().count("/") == 1:
            cadena = self.__panel.get()
            separador = "/"
            separado = cadena.split(separador)
            self.__primerOperandoF1=int(separado[0])
            self.__segundoOperandoF2 = int(separado[1])
            print(self.__segundoOperandoF2)
            clase = Fraccion(self.__primerOperandoF1,self.__segundoOperandoF2)
            if self.__primerOperandoF1 == 0:
                self.__panel.set("0")
            elif self.__segundoOperandoF2 == 0:
                self.__panel.set("Math ERROR")
            else:
                simpli = clase.Simplificar(self.__primerOperandoF1,self.__segundoOperandoF2)
                self.__panel.set(str(simpli))

    def ponerNUMERO(self, numero):
        if self.__operadorAux==None:
            valor = self.__panel.get()
            self.__panel.set(valor+numero)
        else:
            self.__operadorAux=None
            if self.__panel.get().count("/") == 1:
                cadena = self.__panel.get()
                separador = "/"
                separado = cadena.split(separador)
                self.__primerOperandoF1=int(separado[0])
                self.__segundoOperandoF2 = int(separado[1])
                self.__panel.set(numero)
            else:
                valor=self.__panel.get()
                self.__primerOperando=int(valor)
                self.__panel.set(numero)
    def borrarPanel(self):
        self.__panel.set('0')
    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            #if(operando1.count("/") == 0):
                #print("Hola")
            clase = Fraccion(operando1,operando2)
            resultado = clase + clase
            #resultado=operando1+operando2
        else:
            if operacion=='-':
                clase = Fraccion(operando1,operando2)
                resultado = clase - clase
                #resultado=operando1-operando2
            else:
                if operacion=='*':
                    clase = Fraccion(operando1,operando2)
                    resultado = clase * clase
                    #resultado=operando1*operando2
                else:
                    if operacion=='%':
                        clase = Fraccion(operando1,operando2)
                        resultado = clase / clase
        self.__panel.set(str(resultado))

    def resolverFraccion (self,fraccion1,fraccion2,fraccion3,fraccion4,signo):
        resultado = 0
        if signo == "+":
            mcd = fraccion2 * fraccion4
            primero = int(mcd / fraccion2)*fraccion1
            segundo = int(mcd / fraccion4)*fraccion3
            suma = primero + segundo 
            resultado = "{}/{}".format(suma,mcd)
        else:
            if (signo == "-"):
                mcd = fraccion2 * fraccion4
                primero = int(mcd / fraccion2)*fraccion1
                segundo = int(mcd / fraccion4)*fraccion3
                suma = primero - segundo 
                resultado = "{}/{}".format(suma,mcd)
            else:
                if (signo == "*"):
                    clase = Fraccion(fraccion1,fraccion3)
                    clase2 = Fraccion(fraccion2,fraccion4)
                    resultado = "{}/{}".format(clase*clase,clase2*clase2)
                else:
                    if (signo == "%"):
                        primero = fraccion1 * fraccion4
                        print(primero)
                        segundo = fraccion2 * fraccion3
                        resultado = "{}/{}".format(primero,segundo)
        self.__panel.set(str(resultado))


    def ponerOPERADOR(self, op):
        if op=='=':
            operacion=self.__operador.get()
            if (self.__panel.get().count("/") == 1):
                cadenas = self.__panel.get()
                separado = "/"
                separa = cadenas.split(separado)
                self.__primerOperandoF3 = int (separa[0])
                self.__segundoOperadorF4=int(separa[1])
                self.resolverFraccion(self.__primerOperandoF1, self.__segundoOperandoF2, self.__primerOperandoF3, self.__segundoOperadorF4, operacion)
                self.__operador.set('')
                self.__operadorAux=None 

            else:
                self.__segundoOperando=int(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion=self.__operador.get()
                self.__segundoOperando=int(self.__panel.get())
                print(self.__segundoOperando)
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)  # VER ESTOOOOOO
                self.__operador.set(op)
                self.__operadorAux=op

def main():
    calculadora=Calculadora()
    
if __name__=='__main__':
    main()
