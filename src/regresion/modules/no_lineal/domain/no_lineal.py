'''
Si los datos muestran tendencias curas, entonces la regresión lineal no producirá resultados muy exactos
cuando se comparan con una regresión no lineal, porque, como su nombre lo indica, la regresión lineal sume
que los datos son lineales. Aprendamos sobre regresiones no lineales y apliquemos un ejemplo en python.
En este lab, conectaremos un modelo no lineal con los puntos de tendencia correspondientes al GDP de China
entre los años 1960 y 2014.

Importando librerias necesarias
'''
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
'''
Aunque la regresión lineal es muy buena para resolver varios problemas, no puede utilizarse en todos los sets de
datos. Primero, recordemos cómo funciona la regresión lineal, se podría modelar un set de datos. Modelar una
relación lineal entre una variable dependiente y una variable independiente x, tendría una simple ecuación de
grado 1, por ejemplo y = 2*(x) + 3.
'''
import pandas as pd
import pylab as pl
from sklearn import linear_model
from sklearn.metrics import r2_score

from src.charts.domain.line_chart import LineChart

class NoLineal:
    def __init__(self):
        pass

    def print_cubic_chart_demo(self):
        lineChart = LineChart()
        lineChart.x = np.arange(-5.0, 5.0, 0.1)
        ##Se puede ajustar la pendiente y la intersección para verificar los cambios en el gráfico
        lineChart.y = 1*(lineChart.x**3) + 1*(lineChart.x**2) + 1*lineChart.x + 3
        y_noise = 20 * np.random.normal(size = lineChart.x.size)
        lineChart.ydata = lineChart.y + y_noise
        #plt.figure(figsize=(8,6))
        lineChart.plot_default()
        lineChart.set_labels('Variable independiente', 'Variable dependiente')
        return lineChart.print_to_imgb64()

    def print_quad_chart_demo(self):
        lineChart = LineChart()
        lineChart.x = np.arange(-5.0, 5.0, 0.1)
        ##Se puede ajustar la pendiente y la intersección para verificar los cambios en el gráfico
        lineChart.y = np.power(lineChart.x,2)
        y_noise = 2 * np.random.normal(size = lineChart.x.size)
        lineChart.ydata = lineChart.y + y_noise
        #plt.figure(figsize=(8,6))
        lineChart.plot_default()
        lineChart.set_labels('Variable independiente', 'Variable dependiente')
        return lineChart.print_to_imgb64()

    def print_exponential_chart_demo(self):
        lineChart = LineChart()
        lineChart.x = np.arange(-5.0, 5.0, 0.1)
        ##Se puede ajustar la pendiente y la intersección para verificar los cambios en el gráfico
        lineChart.y = np.exp(lineChart.x)
        #plt.figure(figsize=(8,6))
        lineChart.plt.plot(lineChart.x, lineChart.y)
        lineChart.set_labels('Variable independiente', 'Variable dependiente')
        return lineChart.print_to_imgb64()

    def print_logarithmic_chart_demo(self):
        lineChart = LineChart()
        lineChart.x = np.arange(-5.0, 5.0, 0.1)
        ##Se puede ajustar la pendiente y la intersección para verificar los cambios en el gráfico
        lineChart.y = np.log(lineChart.x)
        #plt.figure(figsize=(8,6))
        lineChart.plt.plot(lineChart.x, lineChart.y)
        lineChart.set_labels('Variable independiente', 'Variable dependiente')
        return lineChart.print_to_imgb64()

    def print_sigmoidal_chart_demo(self):
        lineChart = LineChart()
        lineChart.x = np.arange(-5.0, 5.0, 0.1)
        ##Se puede ajustar la pendiente y la intersección para verificar los cambios en el gráfico
        lineChart.y = 1-4/( 1 + np.power(3, lineChart.x-2) )
        #plt.figure(figsize=(8,6))
        lineChart.plt.plot(lineChart.x, lineChart.y)
        lineChart.set_labels('Variable independiente', 'Variable dependiente')
        return lineChart.print_to_imgb64()



noLineal = NoLineal()
