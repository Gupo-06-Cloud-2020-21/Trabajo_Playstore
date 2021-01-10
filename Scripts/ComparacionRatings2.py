#comparamos los ratings diferentes tipos de apps 

from pyspark.sql.functions import lit
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
df2 = df.filter(df['Free'] == False).filter(df['Rating Count']>0).filter(df['Rating']>4.0).withColumn('Rating', lit(5)).groupBy('Rating').agg({'Price':'mean'})
df3 = df.filter(df['Free'] == False).filter(df['Rating Count']>0).filter(df['Rating']<4.0).filter(df['Rating']>3.0).withColumn('Rating', lit(4)).groupBy('Rating').agg({'Price':'mean'})
df4 = df.filter(df['Free'] == False).filter(df['Rating Count']>0).filter(df['Rating']<3.0).filter(df['Rating']>2.0).withColumn('Rating', lit(3)).groupBy('Rating').agg({'Price':'mean'})
df5 = df.filter(df['Free'] == False).filter(df['Rating Count']>0).filter(df['Rating']<2.0).filter(df['Rating']>1.0).withColumn('Rating', lit(2)).groupBy('Rating').agg({'Price':'mean'})

#df2.withColumn('Rating', lit(5)).groupBy('Rating').agg()
#df3.withColumn('Rating', lit(4))
#df4.withColumn('Rating', lit(3))
#df5.withColumn('Rating', lit(2))
df2.show()
df3.show()
df4.show()
df5.show()

a1 = df2.toPandas()
a2 = df3.toPandas()
a3 = df4.toPandas()
a4 = df5.toPandas()

df7 = pd.merge(a1, a2, on='Rating', how='outer')
df8 = pd.merge(df7, a3, on='Rating', how='outer')
df9 = pd.merge(df8, a4, on='Rating', how='outer')

#df7 = df6.select("Category", "avg(Rating)")
#df6.show()
#archivo = df2.toPandas()
plt.xlabel("Rating")
plt.ylabel("Price")
df9.plot.bar(x='Rating', rot = 90)
plt.show()