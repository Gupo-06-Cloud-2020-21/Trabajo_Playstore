print("importamos el archivo Salida.csv")
library(readr)
Salida <- read_csv("Salida.csv")

Salida$`App Name` <- gsub(";", " ", Salida$`App Name`)
Salida$`App Id` <- gsub(";", " ", Salida$`App Id`)
Salida$Category <- gsub(";", " ", Salida$Category)
Salida$Rating <- gsub(";", " ", Salida$Rating)
Salida$`Rating Count` <- gsub(";", " ", Salida$`Rating Count`)
Salida$`Maximum Installs` <- gsub(";", " ", Salida$`Maximum Installs`)
Salida$Free <- gsub(";", " ", Salida$Free)
Salida$Price <- gsub(";", " ", Salida$Price)
Salida$Currency <- gsub(";", " ", Salida$Currency)
Salida$Size <- gsub(";", " ", Salida$Size)
Salida$`Minimum Android` <- gsub(";", " ", Salida$`Minimum Android`)
Salida$`Developer Id` <- gsub(";", " ", Salida$`Developer Id`)
Salida$Released <- gsub(";", " ", Salida$Released)
Salida$`Last Updated` <- gsub(";", " ", Salida$`Last Updated`)
Salida$`Content Rating` <- gsub(";", " ", Salida$`Content Rating`)
Salida$`Ad Supported` <- gsub(";", " ", Salida$`Ad Supported`)
Salida$`In App Purchases` <- gsub(";", " ", Salida$`In App Purchases`)
Salida$`Editors Choice` <- gsub(";", " ", Salida$`Editors Choice`)
Salida$Size <- gsub(",", ".", Salida$Size)


print("Quitar el caracter de la derecha")
substrRight <- function(x, n){
substr(x, nchar(x)-n+1, nchar(x))
}
print("Funcion para pasar el size a double, el tamaño esta en kilobytes")

cambiartam <- function(Google_Playstore){

 
 
 sizerow <- Google_Playstore$Size;
 max = nrow(as.data.frame(sizerow));
 print(max)
 gigamega <- 1024 * 1024;
 
	for(i in 1:max){
		mstring <-sizerow[i];
		mstring <- tolower(mstring);
		if(tolower(mstring) == "varies with device"){
		
		sizerow[i] <- 50 * 1024;
		
		}else{
		letra <- substrRight(mstring,1);
		letra <- tolower(letra);
		numero <- strsplit(tolower(mstring), letra);
		numero <- unlist(numero);
		numero <- as.double(numero);
		
		if(letra == "m"){
		numero <- numero * 1024;
		
		}else if(letra == "k"){
		
		
		}else if(letra == "g"){
		numero <- numero * gigamega;
		
		}
		sizerow[i] <- numero;
		
	}
	percent <- (i/max)*100;
		if(percent%%10==0){
			print(percent);
	}
	 
	}
	
	Google_Playstore$Size <- sizerow;
	return(Google_Playstore);
}
Salida <- cambiartam(Salida)
Salida$`Last Updated` <- gsub(" ", "/", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Jan", "1", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Feb", "2", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Mar", "3", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Apr", "4", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("May", "5", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Jun", "6", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Jul", "7", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Aug", "8", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Sep", "9", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Oct", "10", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Nov", "11", Salida$`Last Updated`)
Salida$`Last Updated` <- gsub("Dec", "12", Salida$`Last Updated`)
Salida$Released <- gsub(" ", "/", Salida$Released)
Salida$Released <- gsub("Jan", "1", Salida$Released)
Salida$Released <- gsub("Feb", "2", Salida$Released)
Salida$Released <- gsub("Mar", "3", Salida$Released)
Salida$Released <- gsub("Apr", "4", Salida$Released)
Salida$Released <- gsub("May", "5", Salida$Released)
Salida$Released <- gsub("Jun", "6", Salida$Released)
Salida$Released <- gsub("Jul", "7", Salida$Released)
Salida$Released <- gsub("Aug", "8", Salida$Released)
Salida$Released <- gsub("Sep", "9", Salida$Released)
Salida$Released <- gsub("Oct", "10", Salida$Released)
Salida$Released <- gsub("Nov", "11", Salida$Released)
Salida$Released <- gsub("Dec", "12", Salida$Released)



Salida$Currency <- gsub("XXX", "USD", Salida$Currency)
#quitamos las apps con categoria null, solo eran 3
Salida <- Salida[!is.na(Salida$Category),]

print("Lo escribe en la raiz del dispositivo")
write.csv2(Salida, file = "Salida.csv", row.names = FALSE)
print("Exportación finalizada")

