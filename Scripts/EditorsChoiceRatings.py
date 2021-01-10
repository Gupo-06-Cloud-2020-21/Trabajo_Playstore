#Las aplicaciones con el editors choice y su puntuacion

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
df2 = df.filter(df['Editors Choice'] == True).groupBy('App Name').agg({'Rating':'mean'})
df2 = df2.orderBy('avg(Rating)', ascending = True)
df3 = df2.orderBy('avg(Rating)', ascending = False)
df2.show()
df3.show()