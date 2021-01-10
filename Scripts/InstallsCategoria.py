#grafica de las instalaciones de todas las apps por cada categoria

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
df20 = df.groupBy('Category').agg({'Maximum Installs':'sum'})
df20.show()
df20 = df20.orderBy('sum(Maximum Installs)', ascending=False)
archivo = df20.toPandas()
archivo.plot.bar(x='Category', y='sum(Maximum Installs)', rot = 90)
plt.show()