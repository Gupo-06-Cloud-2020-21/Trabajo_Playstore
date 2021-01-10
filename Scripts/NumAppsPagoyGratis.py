#Número de las apps de pago y apps gratis

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
df2 = df.groupBy('Free').count()
df2.show()