# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def leeParImpar():
    parImpar = input("¿Desea calcular la suma de pares o impares? (par/impar): ")
    if parImpar != "par" and parImpar != "impar":
        raise ValueError("Input invalido")
    return parImpar  

def leeNumero(mensaje):
    numero = input(mensaje)
    if not str.isdigit(numero):
        raise ValueError("No es un numero")
    return int(numero)

def compruebaMultiplo(numero_comprobado, numero):
    if numero_comprobado % numero == 0:
        return True
    else:
        return False

def compruebaMultiplo10(numero_comprobado):
    if numero_comprobado % 10 == 0:
        return True
    else:
        raise ValueError("No es multiplo de 10")

def sumaNumeros(parImpar, numero_inicio, numero_fin):

    suma = 0
    if parImpar == "par":
        for numero in range(numero_inicio, numero_fin+1):
            if compruebaMultiplo(numero, 2):
                if not compruebaMultiplo(numero, 3):
                    suma += numero
    elif parImpar == "impar":
        for numero in range(numero_inicio, numero_fin+1):
            if not compruebaMultiplo(numero, 2):
                if not compruebaMultiplo(numero, 3):
                    suma += numero
    return suma

def mensaje(par_impar, numero):
    return f"La suma de los números {par_impar} que no son múltiplos de 3 en el rango de 10 a 20 es: {numero}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    par_impar = leeParImpar()
    numero1 = leeNumero("Ingrese el número inicial: ")
    numero2 = leeNumero("Ingrese el número final: ")
    compruebaMultiplo10(numero1)
    compruebaMultiplo10(numero2)
    
    suma = sumaNumeros(par_impar, numero1, numero2)
    
    print(mensaje(par_impar, suma))
    
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
