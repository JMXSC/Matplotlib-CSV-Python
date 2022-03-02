# Alg. Gráfico 2

import csv
import matplotlib.pyplot as plt
import numpy as np

country = []
median_W = []
mean_W = []
population = []

f = open("wealth-per-country.csv", 'r')
try:

    leitor = csv.reader(f)
    for linha in leitor:
        country.append(linha[0])
        median_W.append(linha[1])
        mean_W.append(linha[2])
        population.append(linha[3])

finally:
    f.close()

country = country[1::]
median_W = median_W[1::]
mean_W = mean_W[1::]
population = population[1::]
x = np.arange(len(country))
largura = 0.35

'''

deveriamos transformar os dados em inteiros para o gráfico 
ficar certinho, mas como os dados estão separados por 
vírgulas isso fica bem complicado prof.(na real até da pra fazer, 
mas da muito trabalho, OBS: sobre o que falei com o Sr. no telegram.)

median_W = [float(val) for val in median_W]
mean_W = [float(val) for val in mean_W]
population = [float(val) for val in population]
'''

fig, ax = plt.subplots()
plt.bar(country, median_W, color='c')
# plt.bar(country, mean_W,color ='b')
# plt.bar(country, population, color = 'k')

plt.show()