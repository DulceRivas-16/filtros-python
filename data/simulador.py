#construir un codigo de python que genera
#1000 datos asociados a las ventas de un local de ropa 

#MOCK
import random
from datetime import datetime,timedelta


def generar_ventas():

    productos=[
        {"nombre":"Camiseta Polo","precio":150000},
        {"nombre":"Pantalon Americano","precio":500000},
        {"nombre":"Boxer Calvin","precio":80000},
        {"nombre":"Camisa Ajustable","precio":300000},
        {"nombre":"Chaqueta Cuerina","precio":1000000},
        {"nombre":"Falda","precio":150000},
        {"nombre":"Pantalon jean","precio":85000},
        {"nombre":"Pantis","precio":16000},
        {"nombre":"Pijama","precio":50000},
        {"nombre":"Short","precio":30000},
    
    ]

    tallas=[
        "S","M","L","XL"
    ]
    vendedores=[
        "Lizeth Palacios","Valentina Montoya ","Emely Pacheco","Dulce Rivas","Iham Nava"

    ]
    tiendas=[
        "Centro Comercial Unicentro","Centro Comercial Andino","Centro Comercial Santafe","Centro Comercial Titan","Centro Comercial Gran Estacion","Centro Comercial Plaza de las Americas","Centro Comercial Hayuelos","Centro Comercial Bulevar Niza","Centro Comercial Calima","Centro Comercial Fontanar"
    ]

    fechaInicio=datetime(2025,1,1)

    #Generando 1000 ventas 
    ventas=[]
    for _ in range(1000):
        producto=random.choice(productos)
        cantidad=random.randint(1,8)
        fecha=fechaInicio+timedelta(days=random.randint(0,90))
        ventas.append(
            {
                "producto":producto["nombre"],
                "precio unitario":producto["precio"],
                "talla":random.choice(tallas),
                "tienda":random.choice(tiendas),
                "cantidad":cantidad,
                "vendedor":random.choice(vendedores),
                "total":cantidad*producto["precio"]
             }
        )
    return(ventas)


#llamando la funcion generadora de datos 
