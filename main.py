#COMO USAR PANDAS PARA CREAR FILTROS 

#1.IMPORTARLOS

import pandas as pd
#2.TRAER LOS DATOS 
from data.simulador import generar_ventas

#3.CONVERTIR LOS DATOS EM UN  EL DATAFRAME

dataFrame=pd.DataFrame(generar_ventas())

#4. APLICAR FILTROS (5)
#print(dataFrame)
#YO COMO ADMINISTRADOR DE LA TIENDA QUIERO OBTENER LAS VENTAS DE lizeth PALACIOS
#Filtrouno=dataFrame.query("vendedor=='Lizeth Palacios'")
#print(Filtrouno)
#YO COMO ADMINISTRADOR DE LA TIENDA QUIERO VER VENTAS CON MAS DE TRES PRODUCTOS 
#FiltradoDos=dataFrame.query("cantidad>=3")
#print(FiltradoDos)
#YO COMO ADMINISTRADOR DE LA TIENDA QUIERO VER VENTAS POR VALORES DE MAS DE 900 MIL
#Filtrotres=dataFrame.query("total>900000")
#print(Filtrotres)

#YO COMO ADMINISTRADOR DE LA TIENDA QUIERO VER VENTAS  DE LAS CAMISASETAS POLO 
#FiltroCuatro=dataFrame.query("producto=='Camiseta Polo'")
#print(FiltroCuatro)
#YO COMO ADMINISTRADOR DE LA TIENDA QUIERO VER VENTAS DE LOS PRODUCTOS QUE MENOS SE VENDEN
FiltroCinco=dataFrame.query("cantidad<=1")
print(FiltroCinco)
