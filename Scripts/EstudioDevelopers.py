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

#primero observamos cuales son los mejores developers
df2 = df.filter(df['Rating Count']>100).filter(df['Editors Choice'] == True).groupBy('Developer Id').agg({'Rating':'mean'})
df2 = df2.orderBy('avg(Rating)', ascending = False)
df2.show()

#Esta consulta es para coger el developer que queramos (incluyendo su nombre en el filter de Developer Id) y que nos muestre la info de sus apps
df20 = df.filter(df['Developer Id'] == "Notes").filter(df['Rating Count']>100).orderBy('Rating', ascending = False).select('App Name','Editors Choice','Developer Id', 'Category', 'Maximum Installs', 'Rating', 'Rating Count') 
df20.show()