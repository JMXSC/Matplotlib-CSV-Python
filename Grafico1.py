# Alg. Gráfico 1

import csv
import matplotlib.pyplot as pl

x = []
y = []
f = open("sample-line.csv", 'r')

try:
    leitor = csv.reader(f)
    for linha in leitor:
        x.append(linha[0])
        y.append(linha[1])
finally:
    f.close()

# aqui removemos os nomes do começo:

x = x[1::]
y = y[1::]

x = [int(val) for val in x]
y = [int(val) for val in y]

pl.plot(x, y)
pl.title("Gráfico linear 1")
pl.xlabel("Game Number")
pl.ylabel("Game Lebgth")