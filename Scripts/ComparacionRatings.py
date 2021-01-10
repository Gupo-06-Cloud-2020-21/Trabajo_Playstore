#comparamos los ratings diferentes tipos de apps 
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
df2 = df.filter(df['Free'] == True).filter(df['Rating Count']>0).groupBy('Category').agg({'Rating':'mean'})
df3 = df.filter(df['Free'] == False).filter(df['Rating Count']>0).groupBy('Category').agg({'Rating':'mean'})
df4 = df.filter(df['In App Purchases'] == True).filter(df['Rating Count']>0).groupBy('Category').agg({'Rating':'mean'})
df5 = df.filter(df['In App Purchases'] == False).filter(df['Rating Count']>0).groupBy('Category').agg({'Rating':'mean'})
df2.show()
df3.show()
df4.show()
df5.show()
a1 = df2.toPandas()
a2 = df3.toPandas()
a3 = df4.toPandas()
a4 = df5.toPandas()
df6 = pd.merge(a1, a2, on='Category')
df7 = pd.merge(df6, a3, on='Category')
df8 = pd.merge(df7, a4, on='Category')
#df7 = df6.select("Category", "avg(Rating)")
#df6.show()
#archivo = df2.toPandas()
df8.plot.bar(x='Category', rot = 90)
plt.show()