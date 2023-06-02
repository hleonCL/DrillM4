from clases import Vehiculo, Automovil, Bicicleta, Particular, Carga, Motocicleta

particular = Particular("Ford ", "Fiesta", 4, "180", "500", 50)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta ("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta ("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)


particular.guardar_datos_csv()
carga.guardar_datos_csv()
bicicleta.guardar_datos_csv()
motocicleta.guardar_datos_csv()

print("")

#particular.leer_datos_csv()

"""
clase iltima 2:17:53 / 3:05:33
"""
