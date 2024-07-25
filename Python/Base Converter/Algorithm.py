#Libraries
import math

#Global Variables
numE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Functions
def sumar(num1,num2,bas):
    #A. Initialise the result
    #A.1. List of digits of the result = res
    res = []
    #A.2. Creation of auxiliary variables = sum1, sum2
    sum1 = num1.copy()
    sum2 = num2.copy()
    #B. Add/subtract digit by digit
    while(sum1 != [] or sum2 != []):
        #B.1 Obtaining the digits to be added = sum1, sum2
        if sum1 == []:
            cif1 = 0
        else:
            cif1 = sum1.pop()
            
        if sum2 == []:
            cif2 = 0
        else:
            cif2 = sum2.pop()
        #B.2. Adding the resulting digit to the result list
        res.append(cif1 + cif2)
    #C. Search for results outside the base 
    #C.1. Surplus/shortfall of the sum = aux
    aux = 0
    #C.2. Adjusting numbers greater than/less than the base
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
    #D. Correct/Reverse the position of numbers
    #D.1 Auxiliary of the result = auxR
    auxR = res
    res = []
    while(auxR != []):
        res.append(auxR.pop())
    return res

def multiplicar(mul1,mul2,bas):
    #A. Initialise the result
    #A.1. List of digits of the result = res
    res = [0]
    #A.2. Surplus of the sum = sumE
    sumE = 0
    #B. Inversion of the digits of the multipliers
    #B.1. Initialisation of the first inverted number and its auxiliary = mul1I, aux1
    aux1 = mul1.copy()
    mul1I = []
    while(aux1 != []):
        mul1I.append(aux1.pop())
    #B.2. Initialisation of the first inverted number and its auxiliary = mul2I, aux2
    aux2 = mul2.copy()
    mul2I = []
    while(aux2 != []):
        mul2I.append(aux2.pop())    
    #C. Multiply digit by digit
    for i in range(0,len(mul2I)):
        for j in range(0,len(mul1I)):
            #C.1. Result position = pos
            pos = i + j
            #C.2. Initialisation of the result of multiplication = resM
            resM = [0]
            #C.3. Iteration of the repeated sum
            for k in range(0,mul2I[i]):
                resM = sumar(resM,[mul1I[j]],bas)
            #C.4. Addition of the result to the total
            for k in range(0,pos):
                resM.append(0)
            res = sumar(res,resM,bas)
    return res

def convertirEnteros(numI,basI,basF):
    #1. Obtain preliminary data
    #1.1. Digitisation of the number to be converted = digI
    digI = []
    #2.1. Number auxiliary = auxN
    auxN = list(numI)
    #2. Correct/Reverse the position of numbers
    while(auxN != []):
        digI.append(auxN.pop())
    #2.1. Conversion of values to numbers
    for i in range(0,len(digI)):
        digI[i] = numE.index(digI[i])
    #2.2. Obtaining the difference between the bases = diffB
    difB = basI-basF
    #2.3. Digitisation of the difference between the bases = digD
    digD = []
    digD.append(int(abs(difB)/basF))
    digD.append(abs(difB)%basF)
    #2.4. Negativity adjustment in case diB < 0 = negD
    negD = False
    if difB < 0:
        negD = True
    #3. Change of base
    #3.1. Resulting number = lisR
    lisR = [digI.pop()]
    #3.2. Adjustment of missing/excess values of each group
    while(digI != []):
        #3.2.1. Group setting = ajuG
        ajuG = multiplicar(lisR,digD,basF)
        #3.2.2. Value shift to the correct base
        lisR.append(0)
        #3.2.2.1. Digitisation of new digit = auxN, auxA, digA
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
    #3.3. Adjustment of the values exceeding the base
    #3.3.3. Position auxiliary = auxP
    auxP = 0
    while(auxP < len(lisR)):
        if lisR[auxP] >= basF:
            lisR = sumar(lisR,[0],basF)
            auxP = 0
        else:
            auxP += 1
    #3.4. Setting the characters to base values
    #3.4.1. Final result = numR
    numR = ''
    for i in range(0,len(lisR)):
        numR += numE[lisR[i]]
    while(numR[0] == '0'):
        numR = numR[1::]
    return numR

def conversorDecimales(decI,basI,basF):
    #1. Obtain preliminary data
    #1.1. Digitisation of the decimal to be converted = digD
    digD = list(decI)
    #1.1.1 Conversion of values to numbers
    for i in range(0,len(digD)):
        digD[i] = numE.index(digD[i])
    #1.2. Digitisation of the final base = digB
    digB = []
    digB.append(int(basF/basI))
    digB.append(basF%basI)
    #1.3. List of results obtained = lisR
    lisR = []
    #2. Make the multiplication of the decimal by the baseF = deR
    decR = multiplicar(digD,digB,basI)
    #3. Get the number of digits of the decimal = numD
    numD = len(decI)
    #4. Get surplus of decimal = excD
    #4.1. List-to-number conversion auxiliary = auxC
    excD = decR[(len(decR)-numD)::]
    #4.4. Association of the values to be added to the final result = decR
    if len(decR) == numD:
        lisR = [0]
    else:
        lisR = decR[0:(len(decR)-numD)]
    #4.3. Infinite loop control variable = varC
    varC = 15
    #4.4 Check if all elements of excD are equal to 0 = revE
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
    #5. Setting the characters to base values
    #5.1. Final result = decR
    decR = ''
    for i in range(0,len(lisR)):
        decR += numE[lisR[i]]
    while(decR[len(decR)-1] == '0'):
        decR = decR[0:len(decR)-1]
    return decR
        

#Process
class Proceso():
    while(True):
        #1. Ordering variables
        #1.1 Number to Convert = numI
        numI = input("Number to Convert: ")
        decI = [0]
        #1.2 Base of the number to be converted = basI
        basI = int(input("Base of the number to be converted: "))
        #1.3 Base to which you want to convert = basF
        basF = int(input("Base to which you want to convert: "))
        #2 Conversion process
        if numI.find(',') != -1:
            #2.1. Decimal separation = decI
            decI = numI[(numI.find(',')+1)::]
            numI = numI[0:numI.find(',')]
            decR = conversorDecimales(decI,basI,basF)
        else:
            decI = '0'
            decR = '0'
        numR = convertirEnteros(numI,basI,basF)
        print("The number " + numI + "," + decI + " in base " + str(basI) + " is equivalent to " + numR + "," + decR + " in base " + str(basF))
        #3 Restart the process
        rep = input("Do you wish to repeat the process? (Y/N)")
        if rep != 'Y':
            break
