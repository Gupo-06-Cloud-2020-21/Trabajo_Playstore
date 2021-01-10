#grafica de los porcentajes del nº de aplicaciones por categorias

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

import numpy as np
import pandas as pd
import string
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt

conf = SparkConf().setMaster('local').setAppName('Proyecto.py')
sc = SparkContext(conf = conf)
ss = SparkSession(sc)

df = ss.read.csv("Salida.csv", header="true", sep=";")
df2 = df.groupBy('Category').count().withColumnRenamed('count', 'Categoria').withColumn('Porcentaje',(F.col('Categoria') / df.count()) * 100)
df2.show()
df3 = df2.select("Category","Porcentaje")
df3.show()
#grafico circular general 
archivo = df3.toPandas()
archivo.set_index('Category',inplace=True)
archivo.plot(kind='pie', subplots=True, autopct='%1.1f%%', startangle=90, shadow=False, legend = False, fontsize=7)
plt.show()
#grafico de barras de las categorias y su porcentaje
df3 = df3.orderBy("Porcentaje", ascending=False)
archivo2 = df3.toPandas()
archivo2.plot.bar(x='Category', y='Porcentaje', rot = 90, fontsize=7)
plt.show()