"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */

"""
def num_prim():
    for i in range(1,101):
        if i >= 2:
            num_primo = True
            for j in range(2,i):
                if i%j==0:
                    num_primo = False
                    break
            if num_primo:
                print(i,"Es Primo")
                    
            
        
num_prim()

def num_prim():
    for i in range(1, 101):  # Recorre los números del 1 al 100
        if i >= 2:  # Los números menores que 2 no son primos
            es_primo = True  # Suponemos que 'i' es primo
            for j in range(2, i):  # Buscamos divisores desde 2 hasta i-1
                if i % j == 0:  # Si 'i' es divisible entre 'j'
                    es_primo = False  # Entonces no es primo
                    break  # Salimos del bucle porque ya sabemos que no es primo
            if es_primo:  # Si no se encontró ningún divisor
                print(i, "es primo")  # Imprimimos que es primo
