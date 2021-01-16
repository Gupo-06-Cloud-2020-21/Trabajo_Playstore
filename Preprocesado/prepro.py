import pandas as pd
import numpy as np
import string
import sys
import re


df = pd.read_csv("Google-Playstore.csv", header=0)
df = df.drop(['Developer Website', 'Privacy Policy', 'Developer Email', 'Installs', 'Minimum Installs'], axis = 1)
df_numeric = df.select_dtypes(include =[np.number])
numeric_cols = df_numeric.columns.values

for col in numeric_cols:
	missing = df[col].isnull()
	num_missing = np.sum(missing)
	
	if num_missing > 0:
		med = 0
		df[col] = df[col].fillna(med)
		
df.to_csv(r'Salida.csv', index=False)
