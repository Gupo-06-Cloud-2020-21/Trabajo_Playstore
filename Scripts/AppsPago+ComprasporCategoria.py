#grafica las apps con compras dentro y que ademas sean de pago, y ordenamos por la cantidad que hay por categoria
# MIRAR si hacer o no porque no queda muy bien
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
df14 = df.filter(df['In App Purchases'] == True).filter(df['Rating Count']>0).filter(df['Free'] == False).groupBy('Category').agg({'Rating':'mean', 'Category': 'count'})
df15 = df14.withColumn('NumAppsEnCentenas',(F.col('count(Category)') /100))
df16 = df15.select("Category", "NumAppsEnCentenas", "avg(Rating)")                                                                    
df16.show()
df16 = df16.orderBy('NumAppsEnCentenas', ascending=False)
archivo = df16.toPandas()
archivo.plot.bar(x='Category', rot = 90)
plt.show()