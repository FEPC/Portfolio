#Librerias
import math

#Variables Globales
numE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Funciones
def sumar(num1,num2,bas):
    #A. Inicializar el resultado
    #A.1. Lista de los digitos del resultado = res
    res = []
    #A.2. Creación de vairables auxiliares = sum1, sum2
    sum1 = num1.copy()
    sum2 = num2.copy()
    #B. Sumar/Restar digito a digito
    while(sum1 != [] or sum2 != []):
        #B.1 Obtención de los digitos a sumar = sum1, sum2
        if sum1 == []:
            cif1 = 0
        else:
            cif1 = sum1.pop()
            
        if sum2 == []:
            cif2 = 0
        else:
            cif2 = sum2.pop()
        #B.2. Adición del digito resultante a la lista de resultado
        res.append(cif1 + cif2)
    #C. Buscar los resultados fuera de la base 
    #C.1. Excedente/Faltante de la suma = aux
    aux = 0
    #C.2. Ajuste de números mayores/menores que la base
    for i in range(0,len(res)):
        if res[i] + aux >= bas:
            res[i] = res[i] + aux - bas
            aux = 1
        elif res[i] + aux < 0:
            res[i] = bas + res[i] + aux
            aux = -1
        else:
            res[i] = res[i] + aux
            aux = 0
    if aux > 0:
        res.append(aux)
    #D. Corregir/Invertir la posición de los números
    #D.1 Auxiliar del resultado = auxR
    auxR = res
    res = []
    while(auxR != []):
        res.append(auxR.pop())
    return res

def multiplicar(mul1,mul2,bas):
    #A. Inicializar el resultado
    #A.1. Lista de los digitos del resultado = res
    res = [0]
    #A.2. Excedente de la suma = sumE
    sumE = 0
    #B. Inversión de los digitos de los multiplos
    #B.1. Inicialización del primer número invertido y su auxiliar = mul1I, aux1
    aux1 = mul1.copy()
    mul1I = []
    while(aux1 != []):
        mul1I.append(aux1.pop())
    #B.2. Inicialización del primer número invertido y su auxiliar = mul2I, aux2
    aux2 = mul2.copy()
    mul2I = []
    while(aux2 != []):
        mul2I.append(aux2.pop())    
    #C. Multiplicar digito a digito
    for i in range(0,len(mul2I)):
        for j in range(0,len(mul1I)):
            #C.1. Posición del resultado = pos
            pos = i + j
            #C.2. Inicialización del resultado de la multiplicación = resM
            resM = [0]
            #C.3. Iteración de la suma reiterada
            for k in range(0,mul2I[i]):
                resM = sumar(resM,[mul1I[j]],bas)
            #C.4. Adición del resultado al total
            for k in range(0,pos):
                resM.append(0)
            res = sumar(res,resM,bas)
    return res

def convertirEnteros(numI,basI,basF):
    #1. Obtener datos preliminares
    #1.1. Digitalización del número a convertir = digI
    digI = []
    #2.1. Auxiliar del número = auxN
    auxN = list(numI)
    #2. Corregir/Invertir la posición de los números
    while(auxN != []):
        digI.append(auxN.pop())
    #2.1. Conversión de valores a números
    for i in range(0,len(digI)):
        digI[i] = numE.index(digI[i])
    #2.2. Obtención de la diferencia entre las bases = difB
    difB = basI-basF
    #2.3. Digitalización de la diferencia entre las bases = digD
    digD = []
    digD.append(int(abs(difB)/basF))
    digD.append(abs(difB)%basF)
    #2.4. Ajuste de negatividad en caso diB < 0 = negD
    negD = False
    if difB < 0:
        negD = True
    #3. Cambio de base
    #3.1. Número resultante = lisR
    lisR = [digI.pop()]
    #3.2. Ajuste del los valores faltantes/sobrantes de cada grupo
    while(digI != []):
        #3.2.1. Ajuste del grupo = ajuG
        ajuG = multiplicar(lisR,digD,basF)
        #3.2.2. Corrimiento del valor a la base correcta
        lisR.append(0)
        #3.2.2.1. Digitalización del nuevo digito = auxN, auxA, digA
        auxN = digI.pop()
        auxA = str(int(auxN/basF) * 10 + auxN%basF)
        digA = list(auxA)
        for i in range(0,len(digA)):
            digA[i] = numE.index(digA[i])
        lisR = sumar(lisR,digA,basF)
        if negD:
            for i in range(0,len(ajuG)):
                ajuG[i] *= -1
        lisR = sumar(lisR,ajuG,basF)
    #3.3. Ajuste de los valores que sobrepasan la base
    #3.3.3. Auxiliar de la posición = auxP
    auxP = 0
    while(auxP < len(lisR)):
        if lisR[auxP] >= basF:
            lisR = sumar(lisR,[0],basF)
            auxP = 0
        else:
            auxP += 1
    #3.4. Ajuste de los caracteres a valores de la base
    #3.4.1. Resultado final = numR
    numR = ''
    for i in range(0,len(lisR)):
        numR += numE[lisR[i]]
    while(numR[0] == '0'):
        numR = numR[1::]
    return numR

def conversorDecimales(decI,basI,basF):
    #1. Obtener datos preliminares
    #1.1. Digitalización del decimal a convertir = digD
    digD = list(decI)
    #1.1.1 Conversión de valores a números
    for i in range(0,len(digD)):
        digD[i] = numE.index(digD[i])
    #1.2. Digitalización de la base final = digB
    digB = []
    digB.append(int(basF/basI))
    digB.append(basF%basI)
    #1.3. Lista de los resultados obtenidos = lisR
    lisR = []
    #2. Hacer la multiplicacion del decimal por la baseF = deR
    decR = multiplicar(digD,digB,basI)
    #3. Obtener el número de digitos del decimal = numD
    numD = len(decI)
    #4. Obtener excedente del decimal = excD
    #4.1. Auxiliar de conversión de lista a número = auxC
    excD = decR[(len(decR)-numD)::]
    #4.4. Asociacion de los valores que se añadiran al resultado final = decR
    if len(decR) == numD:
        lisR = [0]
    else:
        lisR = decR[0:(len(decR)-numD)]
    #4.3. Variable de control de ciclo infinito = varC
    varC = 15
    #4.4 Revisar si todos los elementos de excD son iguales a 0 = revE
    revE = 0
    for i in range(0,len(excD)):
        revE += int(excD[i])
    while(revE != 0 and varC > 0):
        decR = multiplicar(excD,digB,basI)
        excD = decR[(len(decR)-numD)::]
        if len(decR) == numD:
            lisR.append(0)
        else:
            for i in range(0,len(decR)-numD):
                lisR.append(decR[i])
        revE = 0
        for i in range(0,len(excD)):
            revE += int(excD[i])
        varC -= 1
    #5. Ajuste de los caracteres a valores de la base
    #5.1. Resultado final = decR
    decR = ''
    for i in range(0,len(lisR)):
        decR += numE[lisR[i]]
    while(decR[len(decR)-1] == '0'):
        decR = decR[0:len(decR)-1]
    return decR
        

#Proceso
class Proceso():
    while(True):
        #1. Pedir variables
        #1.1 Número a Convertir = numI
        numI = input("Número a Convertir: ")
        decI = [0]
        #1.2 Base del número a convertir = basI
        basI = int(input("Base del número a convertir: "))
        #1.3 Base a la que se quiere convertir = basF
        basF = int(input("Base a la que se quiere convertir: "))
        #2 Proceso de conversión
        if numI.find(',') != -1:
            #2.1. Separación del decimal = decI
            decI = numI[(numI.find(',')+1)::]
            numI = numI[0:numI.find(',')]
            decR = conversorDecimales(decI,basI,basF)
        else:
            decI = '0'
            decR = '0'
        numR = convertirEnteros(numI,basI,basF)
        print("El número " + numI + "," + decI + " en base " + str(basI) + " es equivalente a " + numR + "," + decR + " en base " + str(basF))
        #3 Reinicio del proceso
        rep = input("¿Desea repetir el proceso? (Y/N)")
        if rep != 'Y':
            break
