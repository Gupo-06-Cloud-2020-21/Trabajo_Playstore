#grafica de los ratings medios por cada categoria de edad
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
df2 = df.filter(df['Rating Count']>0).groupBy('Content Rating').agg({'Rating':'mean'})
df2.show()
df2 = df2.orderBy('avg(Rating)', ascending=False)
archivo = df2.toPandas()
archivo.plot.bar(x='Content Rating', y='avg(Rating)', rot = 90)
plt.show()