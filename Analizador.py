import re
from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Analizador Léxico")

tabla = ttk.Treeview(ventana, columns=("#0","#1"))
tabla.heading("#0",text="Token",anchor=CENTER)
tabla.heading("#1",text="Caracter",anchor=CENTER)
tabla.heading("#2",text="Cantidad",anchor=CENTER)

entradaCadena = Entry(ventana,font=("Arial 72"))
texto = Label(ventana, font=("Arial 30"), text="Ingresar cadena")

texto.grid(row=0, column=0, columnspan=3, padx=5)
entradaCadena.grid(row=1, column=0, columnspan=1, padx=5)
tabla.grid(row=4, column=0,columnspan=2,pady=5)




L = ("([a-z])|([A-Z])")
Lcont = 0
Ncont = 0
LR = ("([a-z])+|([A-Z])+")
LrCont = 0
PInt = "int"
PintCont = 0
PFloat = "float"
PfloatCont = 0
PString = "String"
PStringCont = 0
F = ";"
Fcont = 0
T = "void"
Tcont = 0
P = "()"
Pcont = 0
AP = "{"
APcont = 0
FP = "}"
FPcont = 0
ALG = "printf"
ALGcont = 0
Dcont = 0
DI = "([0-9])?"
DIcont = 0
DR = "([0-9])+"
DRcont = 0
cadena = "(')*([a-z])+|([A-Z])+|([0-9])+"
PRIF = "if"
PRIFcont = 0
ABRIR = "("
ABRIRcont = 0
CERRAR = ")"
CERRARcont = 0
DATO = "([0-9])+|([a-z])+|([A-Z])+"
DATOcont = 0
C = "(<)|(>)|(==)|(!=)|(<=)|(>=)"
Ccont = 0
PRFOR = "for"
PRFORcont = 0
igualador = "="
igualadorCont = 0
operador = "<|>|<=|>="
operadorCont = 0
INCR = "++"
INCR2 = "--"
INCRcont = 0
SumaResta = "+"
SumaResta2 = "-"
SumaCont = 0
desconocidos = []


def PrepararCadena():
    teclado = entradaCadena.get()
    cadenaLimpia = teclado.split(" ")
    return cadenaLimpia

def Match():
    global PintCont, LrCont, Fcont, PStringCont, PfloatCont, desconocidos, T, Tcont, P, Pcont, AP, APcont, ALG, ALGcont, FP, FPcont, DR, DRcont, Dcont, DIcont, PRIF, PRIFcont, ABRIR, ABRIRcont, CERRAR, CERRARcont
    global C, Ccont, DATO, DATOcont, PRFOR, PRFORcont, igualador, igualadorCont, operador, operadorCont, INCRcont, INCR, SumaResta,SumaResta2, SumaCont, INCR2, Ncont, Lcont
    evaluar = PrepararCadena()
    for i in range(len(evaluar)):
        if evaluar[i] == PInt:
            PintCont += 1
        if evaluar[i] == PFloat:
            PfloatCont += 1
        if evaluar[i] == PString:
            PStringCont += 1
        if evaluar[i] == F:
            Fcont += 1
        if evaluar[i] == T:
            Tcont += 1
        if evaluar[i] == P:
            Pcont += 1
        if evaluar[i] == AP:
            APcont += 1
        if evaluar[i] == ALG:
            ALGcont += 1
        if evaluar[i] == FP:
            FPcont += 1
        if evaluar[i] == PRIF:
            PRIFcont += 1
        if evaluar[i] == ABRIR:
            ABRIRcont += 1
        if evaluar[i] == CERRAR:
            CERRARcont += 1
        if evaluar[i] == PRFOR:
            PRFORcont += 1
        if evaluar[i] == igualador:
            igualadorCont += 1
        if evaluar[i] == operador:
            operadorCont += 1
        if evaluar[i] == INCR or evaluar[i] == INCR2:
            INCRcont += 1
        if evaluar[i] == SumaResta or evaluar[i] == SumaResta2:
            SumaCont += 1

        var = re.search(LR, evaluar[i])
        #? Excluir palabras del contador de LR
        if var:
            Ncont += 1
            if evaluar[i] == PInt or evaluar[i] == PString or evaluar[i] == PFloat or evaluar[i] == T or evaluar[i] == P or evaluar[i] == ALG or evaluar[i] == PRIF or evaluar[i] == PRFOR:
                LrCont -= 1
                Ncont -= 1
            if len(evaluar[i]) > 1:
                LrCont += 1
            else:
                Lcont += 1

        if var == False:
            if evaluar[i] not in PString and evaluar[i] not in PInt and evaluar[i] not in PFloat and evaluar[i] not in F:
                desconocidos.append(evaluar[i])

        digito = re.search(DR, evaluar[i])
        if digito:
            Dcont += 1
            if len(evaluar[i]) > 1:
                DRcont += 1
            else:
                DIcont += 1
        condicion = re.search(C, evaluar[i])
        if condicion:
            Ccont += 1
        eldato = re.search(DATO, evaluar[i])
        if eldato:
            DATOcont += 1
            if evaluar[i] == PInt or evaluar[i] == PString or evaluar[i] == PFloat or evaluar[i] == T or evaluar[i] == P or evaluar[i] == ALG or evaluar[i] == PRIF or evaluar[i] == PRFOR:
                DATOcont -= 1

def RecuentoTokens():
    global PintCont, LrCont, Fcont, desconocidos, Tcont, P, Pcont, AP, APcont, ALG, ALGcont, FP, FPcont, DR, DRcont, Dcont, Dicont, PRIF, PRIFcont, ABRIR, ABRIRcont, CERRAR, CERRARcont
    global C, Ccont, DATO, DATOcont, PRFOR, PRFORcont, igualador, igualadorCont, operador, operadorCont, INCRcont, INCR, SumaResta, SumaCont, Ncont, Lcont
    print("---------------- RECUENTO DE TOKENS --------------")
    print("PINT:", PintCont)
    print("PFLOAT:", PfloatCont)
    print("PSTRING:", PStringCont)
    print("LR:", LrCont)
    print("F:", Fcont)
    print("No identificados:", desconocidos)
    print("T:", Tcont)
    print("P:", Pcont)
    print("AP:", APcont)
    print("FP:", FPcont)
    print("ALG:", ALGcont)
    print("DR:", DRcont)
    print("D:", Dcont)
    print("DI:", DIcont)
    print("PRIF:", PRIFcont)
    print("ABRIR:", ABRIRcont)
    print("CERRAR:", CERRARcont)
    print("C:", Ccont)
    print("DATO:", DATOcont)
    print("PRFOR:", PRFORcont)
    print("igualador:", igualadorCont)
    print("operador:", operadorCont)
    print("INCR:", INCRcont)
    print("SumaResta:", SumaCont)

    tabla.insert("",0,text="L",values=("palabrita",Lcont))
    tabla.insert("",1,text="LR",values=("palabrita",LrCont))
    tabla.insert("",2,text="N",values=("palabrita",Ncont))
    tabla.insert("",3,text="PInt",values=("palabrita",PintCont))
    tabla.insert("",4,text="PFloat",values=("palabrita",PfloatCont))
    tabla.insert("",5,text="PString",values=("palabrita",PStringCont))
    tabla.insert("",6,text="F",values=("palabrita",Fcont))
    tabla.insert("",7,text="T",values=("palabrita",Tcont))
    tabla.insert("",9,text="P",values=("palabrita",Pcont))
    tabla.insert("",10,text="AP",values=("palabrita",APcont))
    tabla.insert("",11,text="FP",values=("palabrita",FPcont))
    tabla.insert("",12,text="ALG",values=("palabrita",ALGcont))
    tabla.insert("",13,text="DR",values=("palabrita",DRcont))
    tabla.insert("",14,text="D",values=("palabrita",Dcont))
    tabla.insert("",15,text="DI",values=("palabrita",DIcont))
    tabla.insert("",16,text="PRIF",values=("palabrita",PRIFcont))
    tabla.insert("",17,text="ABRIR",values=("palabrita",ABRIRcont))
    tabla.insert("",18,text="CERRAR",values=("palabrita",CERRARcont))
    tabla.insert("",19,text="C",values=("palabrita",Ccont))
    tabla.insert("",20,text="DATO",values=("palabrita",DATOcont))
    tabla.insert("",21,text="PRFOR",values=("palabrita",PRFORcont))
    tabla.insert("",22,text="Igualador",values=("palabrita",igualadorCont))
    tabla.insert("",23,text="Operador",values=("palabrita",operadorCont))
    tabla.insert("",24,text="INCR",values=("palabrita",INCRcont))
    tabla.insert("",25,text="SumaResta",values=("palabrita",SumaCont))
    tabla.insert("",26,text="Desconodidos",values=("palabrita","--"))


def ReiniciarContadores():
    global Lcont, Ncont,LrCont, PintCont, PfloatCont, PStringCont, Fcont, Tcont, Pcont, APcont, FPcont, ALGcont, Dcont, DIcont, DRcont, PRFORcont, PRIFcont, ABRIRcont, CERRARcont, Ccont
    global igualadorCont, operadorCont, INCRcont, SumaCont
    Lcont = 0
    Ncont = 0
    LrCont = 0
    PintCont = 0
    PfloatCont = 0
    PStringCont = 0
    Fcont = 0
    Tcont = 0
    Pcont = 0
    APcont = 0
    FPcont = 0
    ALGcont = 0
    Dcont = 0
    DIcont = 0
    DRcont = 0
    PRIFcont = 0
    ABRIRcont = 0
    CERRARcont = 0
    Ccont = 0
    PRFORcont = 0
    igualadorCont = 0
    operadorCont = 0
    INCRcont = 0
    SumaCont = 0

def Arrancar():
    Match()
    RecuentoTokens()
    ReiniciarContadores()

boton_iniciar = Button(ventana, text="Verificar", width=10, height=1, font=("Arial 30"), command = lambda: Arrancar())

boton_iniciar.grid(row=3, column=0, columnspan=3)

#tabla.insert("",0,text="L",values=("palabrita",LrCont))

ventana.mainloop()
#ventanaTabla.mainloop()
