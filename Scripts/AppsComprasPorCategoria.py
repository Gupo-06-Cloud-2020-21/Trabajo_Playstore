#grafica con el numero de apps con compras dentro (en miles), y ordenamos por la cantidad que hay por categoria DE LOCOS
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
df14 = df.filter(df['In App Purchases'] == True).filter(df['Rating Count']>0).groupBy('Category').agg({'Rating':'mean', 'Category': 'count'})
df15 = df14.withColumn('NumAppsEnMiles',(F.col('count(Category)') / 1000))
df16 = df15.select("Category", "NumAppsEnMiles", "avg(Rating)")                                                                    
df16.show()
df16 = df16.orderBy('NumAppsEnMiles', ascending=False)
archivo = df16.toPandas()
archivo.plot.bar(x='Category', rot = 90)
plt.show()