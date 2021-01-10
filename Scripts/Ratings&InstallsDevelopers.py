#Agrupamos por Id del developer y mostramos su rating medio y sus descargas
#filtramos por aquellos que tengan mas de 100 valoraciones y sus installs sean como minimo 500.000

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

import numpy as np
import pandas as pd
import string
import sys
import re

conf = SparkConf().setMaster('local').setAppName('Proyecto.py')
sc = SparkContext(conf = conf)
ss = SparkSession(sc)

df = ss.read.csv("Salida.csv", header="true", sep=";")
df2 = df.filter(df['Rating Count']>100).filter(df['Maximum Installs']>500000).groupBy('Developer Id').agg({'Maximum Installs': 'mean', 'Rating':'mean'})
df2 = df2.orderBy('avg(Rating)', ascending=False)
df2.show()