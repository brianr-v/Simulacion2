# Generador de números seudoaleatorios (método del cuadrado medio)

print("Método del cuadrado medio")

def midSquareRandom(inicio):
    
    #global inicio
    inicio = str(inicio)
    if len(inicio) < 4:
        inicio = int(inicio)
        inicio = '{:04d}'.format(inicio)
        inicio = int(inicio)
        inicio = inicio * inicio
        inicio = int((inicio / 100) % 10000) #Tomar los 4 dígitos del medio
        
    else:
        inicio = int(inicio)
        inicio = inicio * inicio
        inicio = int((inicio / 100) % 10000) #Tomar los 4 dígitos del medio
        
    
    return inicio

#Creamos una lista para guardar los números que cumplan la condición
numeros = []

# Genera y muestra los números pseudoaleatorios de 1000 a 9999
for i in range(1000,9999):
    aleatorio = midSquareRandom(i)
    if aleatorio == i:
        numeros.append(aleatorio)
        

print("Semillas que son iguales a la primera iteración: ",numeros)

