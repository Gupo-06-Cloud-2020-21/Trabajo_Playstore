# Trabajo Playstore
Este trabajo ha sido realizado por:

-**Álvaro Casado Molinero**

-**Sergio Morán Agüero**

-**Jesús Sánchez Granado**

-**Daniel Sanz Mayo**

Se pretende hacer un estudio a gran escala de las aplicaciones en la playstore para ver cuales son las más exitosas, las que han sido descargadas más veces,tienen mejores 
valoraciones… 

Con el objetivo de encontrar los patrones que siguen estas aplicaciones para tener tanto éxito.

# Limpieza del dataset
Una vez tenemos el Dataset con toda la información empezamos a analizarlo.

Originalmente el Dataset contenía algunas erratas que tuvimos que eliminar. Para ello, realizamos un preprocesado del Dataset para quitar los datos que no necesitábamos, modificar valores nulos...

En primer lugar, nos ocupamos de eliminar las columnas que no necesitábamos porque no aportaban información útil para el estudio (por ejemplo, la web del desarrollador). 

Además, debido a que algunas columnas contenían un pequeño porcentaje de valores nulos, tuvimos que modificarlas (por ejemplo, la valoración de la app). Para que estos valores no afectasen a los resultados del estudio, no los tendremos en cuenta a la hora de realizar las consultas.

Para ello generamos el script prepro.py el cual, selecciona las columnas que queremos del Dataset, e introduce un valor de 0 en aquellas columnas que no tienen ningún valor. Para ejecutarlo:

**$ python prepro.py GooglePlaystore.csv**

Una vez hicimos este preprocesado, tuvimos que realizar otra fase de limpieza ya que había datos que no estaban en el formato que deseábamos. Para ello utilizamos el lenguaje “R” que nos permitía modificar estas erratas de forma sencilla. 

Script.R completamos esta primera fase de limpieza del Dataset, y empezamos a trabajar en el estudio.
**$ Rscript script.R**

#Luego hay que quitar todas las comillas dobles del fichero que ha generado R

**$ sed -i 's/"//g' Salida.csv**

Pero para hacerlo todo más facil hemos creado dos scripts, uno instala todos los paquetes necesarios para correr prepro.py y script.R, y el otro, coge el archivo original Google-Playstore.csv y devuelve otro csv ya con todo el preprocesado realizado, que se llama Salida.csv.

#Primero tenemos que dar permisos de ejecución al los scripts

**$ chmod +x instalar_R.script && chmod +x limpieza_salida.script**

**$ sudo ./instalar_R.script**

**$ ./limpieza_salida.script**


Tenemos 2 formas de ejecutar las opciones del programa, en modo local, y a través de una instancia de Amazon Web Services. A continuación, se explica como utilizar cada una de ellas.

# Modo local

Si queremos ejecutar este programa en modo local, ya sea en vuestro sistema operativo Linux Ubuntu o en Windows pero a través de una máquina virtual de Ubuntu (con VirtualBox, por ejemplo), es necesario tener instalado en nuestro equipo Spark en modo local, si no lo tienes o no sabes como hacerlo, aquí tienes un tutorial para conseguirlo.

Instalación Spark en nuestra máquina Ubuntu

Aunque pensemos que podemos tener todo instalado, si no estamos correctamente seguros, realizaremos los siguientes pasos:

Primero, instalaremos Java, ya que es necesario para arrancar Apache Spark

**$ sudo apt-get update
$ sudo apt install default-jdk**

Después, será necesario instalar Scala y comprobar la correcta instalación y version.

**$ sudo apt-get install scala**

Tras esto, instalaremos Python

**$ sudo apt-get install python**

Para comprobar la instalación, ejecutamos:

**$ python -h**

Por último, instalamos Spark

**$ sudo curl -o http://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-hadoop2.7.tgz**
$ **sudo tar xvf ./spark-2.2.0-bin-hadoop2.7.tgz**
$ **sudo mkdir /usr/local/spark**
$ **sudo cp -r spark-2.2.0-bin-hadoop2.7/* /usr/local/spark**

Puede ser que nuestra máquina no reconozca el comando curl, en este caso, procederemos a instalarlo y a continuación, volveremos a realizar el paso anterior

**$ sudo apt install curl**

También tendrás que instalar los paquete Pandas, Numpy y unicodecsv, que puedes conseguir mediante estos comandos

**$ sudo apt-get install python-pip**
**$ sudo pip install numpy**
**$ sudo pip install pandas**
**$ sudo pip install unicodecsv**

# Amazon Web Services

Para ejecutar la aplicación mediante un clúster, será necesario iniciar un clúster con Spark en Hadoop a través de Amazon AWS. Después de iniciar el clúster, instalaremos 
Pandas, Numpy y unicodecsv igual que para la ejecución en modo local, esta vez sin sudo:

**$ sudo apt-get install python-pip**
**$ pip install numpy**
**$ pip install pandas**
**$ pip install unicodecsv**

En caso de aparecer un error con el comando pip, tendremos que actualizarlo:

**$ pip install --upgrade pip**

Al estar ejecutando la aplicación en un clúster, los comandos cambian, para ejecutar cualquier opcion, lo haremos de la siguiente forma (donde N y M son los número que queramos poner):

**$ spark-submit --num-executors N --executor-cores M "script"**

Una vez ejecutado el script, necesitamos obtener la carpeta de salida del hadoop file system, para ello:

**$ hadoop fs -get "nombreDirectorioSalida"**

Si queremos volver a ejecutar el mismo código con otras opciones habría que borrar los ficheros de salida generados en la ejecución anterior, para ello, utilizamos los siguientes comandos:

**$ hadoop fs -rm -r "nombreDirectorioSalida"**

Para consultar los directorios:

**$ hadoop fs -ls**



Para poder obtener las gráficas y estudiar nuestros resultados de una forma mas visual necesitamos utilizar pyspark en Windows mediante la herramienta de Anaconda, ya que linux no tiene una herramienta para mostrar las gráficas que generamos en los scripts.

# Uso en Windows

Lo primero que tenemos que hacer es descargar el programa de Anaconda para Windows. Para ello, simplemente descargar la ultima versión disponible en su pagina web https://www.anaconda.com/products/individual.

Después de tener Anaconda Instalado debemos de abrir “Anaconda Navigator”. Dentro de esta interfaz podremos lanzar una consola haciendo click (izquierdo) en el botón de “play” que se encuentra cerca de base(root).

En la consola lo primero que vamos a hacer es colocarnos en la carpeta donde se encuentran nuestros scripts y datos.

**$ cd "ruta de la carpeta"**

Instalamos pyspark con el siguiente comando:

**$ pip install pyspark**

Si tenemos algun problema con la instalacion de pyspark es posible que sea debido a que no tenemos “pip” en su ultima version, para ello:

**$ pip install --upgrade pip**

Una vez instalado pyspark lo unico que tenemos que hacer es lanzarlo mediante el comando “pyspark”.

**$ pyspark**

Una vez dentro de la “interfaz” de pyspark que nos aparece en la consola simplemente ejecutar los scripts para obtener los resultados y las gráficas, para ello, hay que seguir los pasos especificados en la sección de “Modo Local” dentro de la pagina de “Guia de Uso” ya que necesitaremos tener instalado el pandas y otros paquetes que se describen en esa sección.

Una vez tengas todo instalado en el sistema, te mostramos como ejecutar nuestros scripts

# Ejecución

Cabe destacar que algunos de nuestros scripts generan tanto una tabla como un gráfico, aunque se pueden ejecutar tanto en Windows como en Linux, es necesario utilizar Windows para poder ver las gráficas.

Lo primero que tenemos que hacer es abrir una terminal y desplazarnos hasta el directorio en el que se encuentran nuestros scripts, para que funcionen correctamente es necesario que además el fichero .csv se enucentre en el mismo directorio.

Tras esto arrancaríamos spark ejecutando

**$ pyspark**

Para ejecutar nuestros scripts simplemente utilizariamos el comando:

**$ spark-submit nombre_script.py**
