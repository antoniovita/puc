def calculadora (num1, operador, num2):
    if(operador == "+"):
       return num1 + num2
    elif(operador == "-"):
        return num1 - num2
    elif(operador == "*"):
        return num1 * num2
    elif(operador == "/"):
        return num1 / num2
    elif(operador == "%"):
        operação = num1/100*num2
        return operação
    elif(operador == "^"):
        return num1 ** num2

numero1 = int(input("Entre com o primeiro operando:"))
operador = input("Entre com o operador:")
numero2 = int(input("Entre com o segundo operando:"))
    
print(f' Saída: {calculadora(numero1, operador, numero2)}')

    
    