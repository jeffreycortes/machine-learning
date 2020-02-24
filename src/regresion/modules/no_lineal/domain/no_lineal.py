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


class NoLineal:
    def __init__(self):
        self._df = None
        self._cdf = None

    #Leyendo los datos
    def leer_datos(self, force = False):
        if(self._df != None && not(force))
            return
        self._df = pd.read_csv("FuelConsumption.csv")

    def mostrar_datos(self, force = False):
        self.leer_datos(force)
        # un vistazo dentro del set de datos
        self._df.head()

    def sumarizar_datos(self):
        self.leer_datos()
        # Sumarizar los datos
        self._df.describe()

    def seleccionar_caracteristicas(self):
        self.leer_datos()
        self._cdf = self._df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
        self._cdf.head(9)

    def dibujar_caracteristicas(self):
        viz = self._cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
        viz.hist()
        plt.show()

    def dibujar_grafico_de_dispersion(self):
        #comparams caracteristicas anteriores con emision de carbono
        plt.scatter(self._cdf.FUELCONSUMPTION_COMB, self._cdf.CO2EMISSIONS,  color='blue')
        plt.xlabel("FUELCONSUMPTION_COMB")
        plt.ylabel("Emission")
        plt.show()

    def dibujar_grafico_dispersion2(self):
        plt.scatter(self._cdf.ENGINESIZE, self._cdf.CO2EMISSIONS,  color='blue')
        plt.xlabel("Engine size")
        plt.ylabel("Emission")
        plt.show()

    def dibujar_grafico_dispersion3(self):
        plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='blue')
        plt.xlabel("Cylinders")
        plt.ylabel("Emission")
        plt.show()

    def crearSetDeDatosYPrueba(self):
        msk = np.random.rand(len(self._df)) < 0.8
        self._train = self._cdf[msk]
        self._test = self._cdf[~msk]

    #Modelo de Regresión Simple
    def entrenar_distribucion_datos(self):
        #modelo_regresion_simple
        plt.scatter(self._train.ENGINESIZE, self._train.CO2EMISSIONS,  color='blue')
        plt.xlabel("Engine size")
        plt.ylabel("Emission")
        plt.show()

    def modelar_datos():
        regr = linear_model.LinearRegression()
        train_x = np.asanyarray(self._train[['ENGINESIZE']])
        train_y = np.asanyarray(self._train[['CO2EMISSIONS']])
        regr.fit (train_x, train_y)
        # The coefficients
        print ('Coefficients: ', regr.coef_)
        print ('Intercept: ',regr.intercept_)

    def trazar_Salidas(self):
        #Trazar las salidas: podemos marcar la recta de ajuste sobre los datos
        plt.scatter(self._train.ENGINESIZE, self._train.CO2EMISSIONS,  color='blue')
        plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
        plt.xlabel("Engine size")
        plt.ylabel("Emission")

    def test(self):
        test_x = np.asanyarray(self._test[['ENGINESIZE']])
        test_y = np.asanyarray(self._test[['CO2EMISSIONS']])
        test_y_ = regr.predict(test_x)

        print("Error medio absoluto: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
        print("Suma residual de los cuadrados (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
        print("R2-score: %.2f" % r2_score(test_y_ , test_y) )
