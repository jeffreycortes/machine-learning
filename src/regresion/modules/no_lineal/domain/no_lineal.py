'''
Si los datos muestran tendencias curas, entonces la regresión lineal no producirá resultados muy exactos
cuando se comparan con una regresión no lineal, porque, como su nombre lo indica, la regresión lineal sume
que los datos son lineales. Aprendamos sobre regresiones no lineales y apliquemos un ejemplo en python.
En este lab, conectaremos un modelo no lineal con los puntos de tendencia correspondientes al GDP de China
entre los años 1960 y 2014.

Importando librerias necesarias
'''
import numpy as np
import pandas as pd
from src.charts.domain.line_chart import LineChart
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
#%matplotlib inline
'''
Aunque la regresión lineal es muy buena para resolver varios problemas, no puede utilizarse en todos los sets de
datos. Primero, recordemos cómo funciona la regresión lineal, se podría modelar un set de datos. Modelar una
relación lineal entre una variable dependiente y una variable independiente x, tendría una simple ecuación de
grado 1, por ejemplo y = 2*(x) + 3.
'''

class NoLineal:
    def __init__(self):
        self.__path_source_data = 'src/regresion/modules/no_lineal/infrastructure/repositories/'
        self._df = None
        self._popt = None
        self._pcov = None
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

    '''
    Ejemplo de Regresión No-Lineal.
    Por ejemplo, intentaremos fijar un modelo no lineal a los puntos correspondientes al GDP de China entre
    los años 1960 y 2014. Descargaremos un set de datos con dos columnas, la primera, un año entre 1960 y 2014,
    la segunda, el ingreso anual de China en dólares estadounidenses para ese año.
    '''
    def read_source_data(self):
        self._df = pd.read_csv( self.__path_source_data + "china_gdp.csv")

    '''
    Marcando el set de datos.
    Asi es como los puntos de datos se ven. Se parece a una función lógica o exponencial. El crecimiento
    es leve, luego a partir de 2005 en adelante, el crecimiento ya es más notorio. Y finalmente, desacelera
    suavemente a principio del año 2010.
    '''
    def no_lineal_demo(self):
        self.read_source_data()

        lineChart = LineChart()
        lineChart.xdata, lineChart.ydata = (self._df["Year"].values, self._df["Value"].values)
        lineChart.plt.figure(figsize = (8,5))
        lineChart.plt.plot(lineChart.xdata, lineChart.ydata, 'ro')
        lineChart.set_labels('Year', 'GDP')
        return lineChart.print_to_imgb64()

    '''
    Eligiendo un modelo
    A primera vista, determinamos que la función lógica podría ser una buena primera aproximación,
    ya que tiene la propiedad de comenzar con un crecimiento leve, aumentando en el medio y luego descendiendo
    nuevamente hacia el final; como se ve debajo:
    '''
    def no_lineal_demo2(self):
        self.read_source_data()

        lineChart = LineChart()
        lineChart.x = np.arange(-5.0, 5.0, 0.1)
        lineChart.y = 1.0 / (1.0 + np.exp(-lineChart.x))
        lineChart.plt.plot(lineChart.x, lineChart.y)
        lineChart.set_labels('Variable independiente', 'Variable dependiente')

        return lineChart.print_to_imgb64()

    '''
    La fórumla para la función logística es la siguiente: 𝑌̂ =11+𝑒𝛽1(𝑋−𝛽2)
    𝛽1: Controla lo llano de la curva,
    𝛽2: Lleva la curva sobre el eje x.

    Construyendo el Modelo
    Ahora, construyamos nuestro modelo de regresión e inicialicemos sus parámetros.
    '''
    def sigmoid(self, x, beta_1, beta_2):
        y = 1 / (1 + np.exp(-beta_1*(x-beta_2)))
        return y

    def print_sigmoid_chart(self, beta_1, beta_2):
        self.read_source_data()

        lineChart = LineChart()
        lineChart.xdata, lineChart.ydata = (self._df["Year"].values, self._df["Value"].values)

        #función logística
        Y_pred = self.sigmoid(lineChart.xdata, beta_1 , beta_2)

        #predicción de puntos
        lineChart.plt.plot(lineChart.xdata, Y_pred*15000000000000.)
        lineChart.plt.plot(lineChart.xdata, lineChart.ydata, 'ro')

        return lineChart.print_to_imgb64()

    '''
    Nuestra tarea aquí es encontrar los mejores parámetros para nuestro modelo.
    Normalicemos primero nuestro x e y:
    '''
    def normalize_data(self, lineChart):
        xdata = lineChart.xdata / max(lineChart.xdata)
        ydata = lineChart.ydata / max(lineChart.ydata)

        lineChart.xdata = xdata
        lineChart.ydata = ydata

    '''
    ¿Cómo podemos encontrar los mejores parámetros para nuestra linea?
    podemos utilizar curve_fit la cual utiliza cuadrados mínimos no lineales para cuadrar con la función sigmoide.
    Los valores óptimos para los parámetros que suman los residuos cuadrados de sigmoid(xdata, *popt) -
    ydata minimizado.

    popt son nuestros parámetros optimizados.
    '''
    def get_normalized_data(self, lineChart):
        self.normalize_data(lineChart)
        self._popt, self._pcov = curve_fit(self.sigmoid, lineChart.xdata, lineChart.ydata)
        print(self._popt)
        #imprimir los parámetros finales
        print(" beta_1 = %f, beta_2 = %f" % (self._popt[0], self._popt[1]))

    '''Ahora dibujamos nuestro modelo de regresión.'''
    def print_regresion_model_chart(self, beta_1, beta_2):
        self.read_source_data()
        lineChart = LineChart()
        lineChart.xdata, lineChart.ydata = (self._df["Year"].values, self._df["Value"].values)
        print('****************')
        print(lineChart.xdata, lineChart.ydata)
        print('****************')

        # Normalización
        self.get_normalized_data(lineChart)
        print('****************')
        print(lineChart.xdata, lineChart.ydata)
        print('****************')

        x = np.linspace(1960, 2015, 55)
        lineChart.x = x / max(x)
        lineChart.plt.figure(figsize=(8,5))
        lineChart.y = self.sigmoid(lineChart.x, *self._popt)
        lineChart.plt.plot(lineChart.xdata, lineChart.ydata, 'ro', label='data')
        lineChart.plt.plot(lineChart.x, lineChart.y, linewidth=3.0, label='fit')
        lineChart.plt.legend(loc='best')
        lineChart.set_labels('Year', 'GDP')

        self.calculate_model_accuracy(lineChart)

        return lineChart.print_to_imgb64()


    '''
    Práctica
    ¿Puedes calcular cual es la exactitud de nuestro modelo?
    '''
    def calculate_model_accuracy(self, lineChart):
        # divide los datos en entrenamiento y prueba
        msk = np.random.rand(len(self._df)) < 0.8
        train_x = lineChart.xdata[msk]
        test_x = lineChart.xdata[~msk]
        train_y = lineChart.ydata[msk]
        test_y = lineChart.ydata[~msk]

        # construye el modelo utilizando el set de entrenamiento
        popt, pcov = curve_fit(self.sigmoid, train_x, train_y)

        # predecir utilizando el set de prueba
        y_hat = self.sigmoid(test_x, *popt)

        # evaluation
        print("Promedio de error absoluto: %.2f" % np.mean(np.absolute(y_hat - test_y)))
        print("Suma residual de cuadrados (MSE): %.2f" % np.mean((y_hat - test_y) ** 2))
        print("R2-score: %.2f" % r2_score(y_hat , test_y) )

noLineal = NoLineal()
