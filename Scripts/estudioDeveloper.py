df20 = df.filter(df['Developer Id'] == "").select('Category', 'Installs', 'Rating') #Este es para coger el developer que queramos y que nos muestre la info de sus apps

df21 =  df.filter(df['Developer Id'] == "").filter(df['Editors Choice'] == True).select('Category', 'Installs', 'Rating') #Esto es para comparar los developers mejores que nos salen antes y mirar si tienen apps en los editors choice que son las mejores, y que nos saquen las cosas
