import itertools
import random
import matplotlib.pyplot as plt
import pandas as pd


"""n = 10000
num = list(range(1, n + 1))
u = list(itertools.repeat(0, n))
x = list(itertools.repeat(0, n))
g = list(itertools.repeat(0, n))

for i in range(0,n,1):
    u[i] = random.uniform(0, 1)
    x[i] = (3 - 0.5)*u[i] + 0.5
    g[i] = x[i]*x[i]

# Crear un DataFrame de pandas
data = {'num':n, 'u':u, 'x': x, 'g': g}
df = pd.DataFrame(data)

# Exportar el DataFrame a un archivo Excel
df.to_excel('datos.xlsx', index=False)

# Graficar x en el eje x y g en el eje y
plt.scatter(x, g, marker='o', color='#BB8FCE')
plt.title('Gráfico de x²')
plt.xlabel('Valor de x')
plt.ylabel('Valor de g')

# Guardar la imagen en formato JPG
plt.savefig('grafico.jpg')

# Mostrar el gráfico
plt.show()
"""

n = 10000

num = list(range(1, n + 1))
m = list(itertools.repeat(0, n))
v = list(itertools.repeat(0, n))
t = list(itertools.repeat(0, n))
a = list(itertools.repeat(0, n))
f = list(itertools.repeat(0, n))

for i in range(0, n, 1):
    m[i] = random.uniform(18, 25) 
    v[i] = random.gauss(80, 14)
    t[i] = random.uniform(0, 2)
    a[i] = v [i]/t[i]
    f[i] = m[i] * a[i] 

# Crear un DataFrame de pandas
data2 = {'num':n, 'm':m, 'v':v, 't': t, 'a': a, 'f':f}
df2 = pd.DataFrame(data2)

# Exportar el DataFrame a un archivo Excel
df2.to_excel('datos2.xlsx', index=False)

# Graficar x en el eje x y g en el eje y
plt.scatter(a, m, marker='o', color = "#E74C3C")
plt.title('Gráfico de F')
plt.xlabel('Valor de a')
plt.ylabel('Valor de m')

# Guardar la imagen en formato JPG
plt.savefig('grafico2.jpg')

# Mostrar el gráfico
plt.show()


# Graficar x en el eje x y g en el eje y
plt.scatter(num, f, marker='o', color = "#48C9B0")
plt.title('Gráfico de F')
plt.xlabel('Valor de n')
plt.ylabel('Valor de f')

# Guardar la imagen en formato JPG
plt.savefig('grafico3.jpg')

# Mostrar el gráfico
plt.show()

