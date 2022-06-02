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
C = "(<)|(>)|(==)|(is not)|(<=)|(>=)"
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
desconocidosCont = 0
auxDesconocidos = 0

PintV = []
PfloatV = []
PStringV = []
LrV = []
Lv = []
Nv = []
Fv = []
Tv = []
Pv = []
APv = []
FPv = []
ALGv = []
DRv = []
Dv = []
DIv = []
PRIFv = []
ABRIRv = []
CERRARv = []
Cv = []
DATOv = []
PRFORv = []
igualadorV = []
operadorV = []
INCRv = []
SumaRestaV = []

# proband ; ( { 45 2 s void if
def PrepararCadena():
    teclado = entradaCadena.get()
    cadenaLimpia = teclado.split(" ")
    return cadenaLimpia

def Match():
    global PintCont, LrCont, Fcont, PStringCont, PfloatCont, desconocidos, T, Tcont, P, Pcont, AP, APcont, ALG, ALGcont, FP, FPcont, DR, DRcont, Dcont, DIcont, PRIF, PRIFcont, ABRIR, ABRIRcont, CERRAR, CERRARcont
    global C, Ccont, DATO, DATOcont, PRFOR, PRFORcont, igualador, igualadorCont, operador, operadorCont, INCRcont, INCR, SumaResta,SumaResta2, SumaCont, INCR2, Ncont, Lcont
    global auxDesconocidos, desconocidosCont
    evaluar = PrepararCadena()
    for i in range(len(evaluar)):
        if evaluar[i] == PInt:
            PintCont += 1
            PintV.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == PFloat:
            PfloatCont += 1
            PfloatV.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == PString:
            PStringCont += 1
            PStringV.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == F:
            Fcont += 1
            Fv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == T:
            Tcont += 1
            Tv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == P:
            Pcont += 1
            Pv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == AP:
            APcont += 1
            APv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == ALG:
            ALGcont += 1
            ALGv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == FP:
            FPcont += 1
            FPv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == PRIF:
            PRIFcont += 1
            PRIFv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == ABRIR:
            ABRIRcont += 1
            ABRIRv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == CERRAR:
            CERRARcont += 1
            CERRARv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == PRFOR:
            PRFORcont += 1
            PRFORv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == igualador:
            igualadorCont += 1
            igualadorV.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == operador:
            operadorCont += 1
            operadorV.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == INCR or evaluar[i] == INCR2:
            INCRcont += 1
            INCRv.append(evaluar[i])
        else:
            auxDesconocidos += 1
        if evaluar[i] == SumaResta or evaluar[i] == SumaResta2:
            SumaCont += 1
            SumaRestaV.append(evaluar[i])
        else:
            auxDesconocidos += 1

        var = re.search(LR, evaluar[i])
        #? Excluir palabras del contador de LR
        if var:
            Ncont += 1
            if evaluar[i] == PInt or evaluar[i] == PString or evaluar[i] == PFloat or evaluar[i] == T or evaluar[i] == P or evaluar[i] == ALG or evaluar[i] == PRIF or evaluar[i] == PRFOR:
                LrCont -= 1
                Ncont -= 1
            if evaluar[i] is not PInt or evaluar[i] is not PString or evaluar[i] is not PFloat or evaluar[i] is not T or evaluar[i] is not P or evaluar[i] is not ALG or evaluar[i] is not PRIF or evaluar[i] is not PRFOR:
                Nv.append(evaluar[i])
            if len(evaluar[i]) > 1:
                LrCont += 1
                LrV.append(evaluar[i])
            else:
                Lcont += 1
                Lv.append(evaluar[i])
        else:
            auxDesconocidos += 1

        digito = re.search(DR, evaluar[i])
        if digito:
            Dcont += 1
            Dv.append(evaluar[i])
            if len(evaluar[i]) > 1:
                DRcont += 1
                DRv.append(evaluar[i])
            else:
                DIcont += 1
                DIv.append(evaluar[i])
        else:
            auxDesconocidos += 1

        condicion = re.search(C, evaluar[i])
        if condicion:
            Ccont += 1
            Cv.append(evaluar[i])
        else:
            auxDesconocidos += 1

        eldato = re.search(DATO, evaluar[i])
        if eldato:
            DATOcont += 1
            if evaluar[i] == PInt or evaluar[i] == PString or evaluar[i] == PFloat or evaluar[i] == T or evaluar[i] == P or evaluar[i] == ALG or evaluar[i] == PRIF or evaluar[i] == PRFOR:
                DATOcont -= 1
        else:
            auxDesconocidos += 1

        if auxDesconocidos >= 21 and evaluar[i] is not "":
            desconocidos.append(evaluar[i])
            desconocidosCont += 1
        auxDesconocidos = 0

def RecuentoTokens():
    global PintCont, LrCont, Fcont, desconocidos, Tcont, P, Pcont, AP, APcont, ALG, ALGcont, FP, FPcont, DR, DRcont, Dcont, Dicont, PRIF, PRIFcont, ABRIR, ABRIRcont, CERRAR, CERRARcont
    global C, Ccont, DATO, DATOcont, PRFOR, PRFORcont, igualador, igualadorCont, operador, operadorCont, INCRcont, INCR, SumaResta, SumaCont, Ncont, Lcont, desconocidosCont
    print("---------------- RECUENTO DE TOKENS --------------")
    print("PINT:", PintCont)
    print("PFLOAT:", PfloatCont)
    print("PSTRING:", PStringCont)
    print("LR:", LrCont,"Contiene:",LrV)
    print("F:", Fcont)
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
    print("No identificados:", desconocidos,"Cantidad:",desconocidosCont)

    tabla.insert("",0,text="L",values=(Lv,Lcont))
    tabla.insert("",1,text="LR",values=(LrV,LrCont))
    tabla.insert("",2,text="N",values=(Nv,Ncont))
    tabla.insert("",3,text="PInt",values=(PintV,PintCont))
    tabla.insert("",4,text="PFloat",values=(PfloatV,PfloatCont))
    tabla.insert("",5,text="PString",values=(PStringV,PStringCont))
    tabla.insert("",6,text="F",values=(Fv,Fcont))
    tabla.insert("",7,text="T",values=(Tv,Tcont))
    tabla.insert("",9,text="P",values=(Pv,Pcont))
    tabla.insert("",10,text="AP",values=(APv,APcont))
    tabla.insert("",11,text="FP",values=(FPv,FPcont))
    tabla.insert("",12,text="ALG",values=(ALGv,ALGcont))
    tabla.insert("",13,text="DR",values=(DRv,DRcont))
    tabla.insert("",14,text="D",values=(Dv,Dcont))
    tabla.insert("",15,text="DI",values=(DIv,DIcont))
    tabla.insert("",16,text="PRIF",values=(PRIFv,PRIFcont))
    tabla.insert("",17,text="ABRIR",values=(ABRIRv,ABRIRcont))
    tabla.insert("",18,text="CERRAR",values=(CERRARv,CERRARcont))
    tabla.insert("",19,text="C",values=(Cv,Ccont))
    tabla.insert("",20,text="DATO",values=(DATOv,DATOcont))
    tabla.insert("",21,text="PRFOR",values=(PRFORv,PRFORcont))
    tabla.insert("",22,text="Igualador",values=(igualadorV,igualadorCont))
    tabla.insert("",23,text="Operador",values=(operadorV,operadorCont))
    tabla.insert("",24,text="INCR",values=(INCRv,INCRcont))
    tabla.insert("",25,text="SumaResta",values=(SumaRestaV,SumaCont))
    tabla.insert("",26,text="Desconodidos",values=(desconocidos,desconocidosCont))


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
ventana.mainloop()
