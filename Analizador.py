import re


L = ("([a-z])|([A-Z])")
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
    print("Ingresar cadena:")
    teclado = input()
    cadenaLimpia = teclado.split(" ")
    # print(cadenaLimpia)
    return cadenaLimpia

def Match():
    global PintCont, LrCont, Fcont, PStringCont, PfloatCont, desconocidos, T, Tcont, P, Pcont, AP, APcont, ALG, ALGcont, FP, FPcont, DR, DRcont, Dcont, DIcont, PRIF, PRIFcont, ABRIR, ABRIRcont, CERRAR, CERRARcont
    global C, Ccont, DATO, DATOcont, PRFOR, PRFORcont, igualador, igualadorCont, operador, operadorCont, INCRcont, INCR, SumaResta,SumaResta2, SumaCont, INCR2
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
        #! Excluir palabras del contador de LR
        if var:
            LrCont += 1
            if evaluar[i] == PInt or evaluar[i] == PString or evaluar[i] == PFloat or evaluar[i] == T or evaluar[i] == P or evaluar[i] == ALG or evaluar[i] == PRIF or evaluar[i] == PRFOR:
                LrCont -= 1
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
            if evaluar[i] == PInt or evaluar[i] == PString or evaluar[i] == PFloat or evaluar[i] == T or evaluar[i] == P or evaluar[i] == ALG or evaluar[i] == PRIF or evaluar[i] == PRFOR:
                DATOcont += 1

        #checarSuma = re.search(SumaResta, evaluar[i])
        #if checarSuma:
           # SumaCont += 1

def RecuentoTokens():
    global PintCont, LrCont, Fcont, desconocidos, Tcont, P, Pcont, AP, APcont, ALG, ALGcont, FP, FPcont, DR, DRcont, Dcont, Dicont, PRIF, PRIFcont, ABRIR, ABRIRcont, CERRAR, CERRARcont
    global C, Ccont, DATO, DATOcont, PRFOR, PRFORcont, igualador, igualadorCont, operador, operadorCont, INCRcont, INCR, SumaResta, SumaCont
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

def Arrancar():
    Match()
    RecuentoTokens()


Arrancar()
