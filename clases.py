import csv
class Vehiculo():
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv", "a", newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print( "no existe el archivo vehiculos.csv")    
        except Exception as e:
            print("Error Reportado",e)
    

    def leer_datos_csv(self):
        try:
            with open ("vehiculos.csv", "r") as archivo:
               vehiculos= csv.reader(archivo)
               for item in vehiculos:
                   print(item)

        except FileNotFoundError:
            print( "no existe el archivo vehiculos.csv")    
        except Exception as e:
            print("Error Reportado",e)



    def __str__(self):
        return f"Marca {self.marca} + modelo {self.modelo} + {self.nro_ruedas} Ruedas"



class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindraje):
       super().__init__(marca, modelo, nro_ruedas)    
       self.velocidad = velocidad
       self.cilindraje = cilindraje

    def __str__(self):
        return super().__str__() + f" + {self.velocidad}, {self.cilindraje} cc"
class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindraje, npuestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindraje)
        self.npuestos = npuestos

    def get_npuestos(self):
        return self.npuestos

    def set_npuestos(self, npuestos_new):
        self.npuestos = npuestos_new
    
    def __str__(self):
        return super().__str__() + f"Puestos {self.npuestos}"
    
class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindraje,carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindraje)
        self.carga = carga

    def get_carga(self):
        return self.carga

    def set_carga(self, carga_new):
        self.carga = carga_new
    
    def __str__(self):
        return super().__str__() + f"Carga : {self.carga} Kg"
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)    
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self)+f"Tipo: {self.tipo}"
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nradio,cuadro, motor):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.nradio= nradio
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return Bicicleta.__str__(self) + f"Motor: {self.motor}, Cuadro : {self.cuadro}, Nro Radios : {self.nradio}"




 
    
    