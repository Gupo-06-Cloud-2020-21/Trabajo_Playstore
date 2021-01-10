from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import numpy as np
import pandas as pd
import string
import sys
import re

reload(sys)
sys.setdefaultencoding('UTF8')
np.random.seed(0)
conf = SparkConf().setMaster('local').setAppName('Proyecto.py')
sc = SparkContext(conf = conf)
ss = SparkSession(sc)
df = ss.read.option("delimiter", ";").csv("Salida_clean.csv")
#df = ss.read.format("csv").load("Salida_clean.csv")
#df.columns = ['App Name', 'App Id', 'Category', 'Rating', 'Rating Count', 'Installs', 'Free', 'Price', 'Currency', 'Size', 'Minimum Android Version', 'Developer Id', 'Release Date', 'Last Update Date', 'Content Rating', 'Ads Supoorted', 'In-App Purchases', 'Editors Choice']
df = df.withColumnRenamed("_c0", "App Name")
df = df.withColumnRenamed("_c1", "App Id")
df = df.withColumnRenamed("_c2", "Category")
df = df.withColumnRenamed("_c3", "Ratings")
df = df.withColumnRenamed("_c4", "Rating Count")
df = df.withColumnRenamed("_c5", "Installs")
df = df.withColumnRenamed("_c6", "Free")
df = df.withColumnRenamed("_c7", "Price")
df = df.withColumnRenamed("_c8", "Currency")
df = df.withColumnRenamed("_c9", "Size")
df = df.withColumnRenamed("_c10", "Minimum Android Version")
df = df.withColumnRenamed("_c11", "Developer Id")
df = df.withColumnRenamed("_c12", "Release Date")
df = df.withColumnRenamed("_c13", "Last Update Date")
df = df.withColumnRenamed("_c14", "Content Rating")
df = df.withColumnRenamed("_c15", "Ads Supported")
df = df.withColumnRenamed("_c16", "In-App Purchases")
df = df.withColumnRenamed("_c17", "Editors Choice")
#total = df.count()
df100 = df.groupBy().agg(F.sum("Installs")).collect()
df2 = df.groupBy('Category').agg({'Installs':'sum','Ratings':'mean'})#Agrupamos por categoria mostrando descargas y ratings medios  2 SCRIPT
df3 = df.groupBy('Developer Id').agg({'Installs': 'mean', 'Ratings':'mean'})#Agrupamos por Id del developer y mostramos su rating medio y sus descargas 1 SCRIPT
df4 = df.groupBy('Free').agg({'Ratings':'mean'})#El rating medio de las aplicaciones gratis y de pago  1 SCRIPT
df5 = df.filter(df['Free'] == False).groupBy('Free').agg({'Price': 'mean'}) #El precio medio de las apps de pago  1 SCRIPT
#PODEMOS HACER EL PRECIO MEDIO POR CATEGORIA ---> HECHO 1 SCRIPT
df6 = df.groupBy('Category').count().withColumnRenamed('count', 'Categoria').withColumn('Porcentaje',(F.col('Categoria') / df.count()) * 100)
#La cantidad de apps de cada categoria y su porcentaje#done 1 SCRIPT
df7 = df.groupBy('Developer Id').count() #Numero de diferentes developers  1 SCRIPT
df8 = df.filter(df['Editors Choice'] == True).groupBy('App Name').agg({'Ratings':'mean'})#Las aplicaciones con el editors choice y su puntuacion#No porque son muchas
df9 = df.filter(df['Ads Supported'] == True).filter(df['Free'] == False).groupBy('Category').agg({'Ratings':'mean'})#Aplicaciones de pago con anuncions y sus ratings por categoria 1 SCRIPT
df10 = df.groupBy('Free').count()  # 1 SCRIPT
df11 = df.groupBy('Content Rating').agg({'Ratings':'mean'}) #categorias de edad y sus ratings medios # 1 SCRIPT
df12 = df.orderBy('Ratings', ascending=False).select('Ratings', 'Release Date', 'Last Update Date')#valoraciones en orden descendente con su fecha de salida y sy ultima actualizacion 1 SCRIPT
df13 = df.filter(df['Size'] > 100000).select('App Name', 'Size','Minimum Android Version').orderBy('Size', ascending = False).show()#comparamos el tamanio con el sistema operativo# 1 SCRIPT
df14 = df.filter(df['In-App Purchases'] == True).groupBy('Category').agg({'Ratings':'mean', 'Category': 'count'})
df15 = df14.orderBy('count(Category)',ascending = False) #filtramos las apps con compras dentro, y ordenamos por la cantidad que hay por categoria 1 SCRIPT
#df12.show()
df16 = df.filter(df['In-App Purchases'] == True).filter(df['Free'] == False).groupBy('Category').agg({'Ratings':'mean','Category':'count'}).orderBy('count(Category)', ascending = False) #comentario para jesus CERDOOOOOO  esto filtra por las que tienen compras dentro y son de pago, y agrupamos por la categoria mostrando el numero que hay en cada una, sus ratings y  Si hay grafica
#df17 = df.groupBy('Category').agg({'Installs':'sum'}).withColumnRenamed('sum(Installs)', 'Instalaciones').withColumn('POrcentaje',(F.col('Instalaciones') / df100) * 100)Porcentaje de instalaciones por categoria#Grafica de tarta

