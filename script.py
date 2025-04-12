class Vehiculo:
    """
    Class usada para crear objetos de tipo vehiculo
    """

    def __init__(self, marca, modelo,color, placa, anio, tipo_de_puerta, combustible, kilometraje, caja_de_cambio, seguro, gama, chasis,
        pais_de_origen, llanta_de_emergencia, numero_de_puertas):
        self.marca = marca
        self.modelo= modelo
        self.color = color
        self.placa = placa
        self.anio = anio
        self.tipo_de_puerta = tipo_de_puerta
        self.combustible = combustible
        self.kilometraje = kilometraje
        self.caja_de_cambio = caja_de_cambio
        self.seguro = seguro
        self.gama = gama
        self.chasis = chasis
        self.pais_de_origen = pais_de_origen
        self.llanta_de_emergencia = llanta_de_emergencia
        self.numero_de_puertas = numero_de_puertas


if __name__ == "__main__":
    objVehiculo1 = Vehiculo("Lamborghini", "Huracán", "Negra", "GRE2588", 2019, tipo_de_puerta="Tijera",
    combustible="Gasolina", kilometraje="Cero kilometro", caja_de_cambio="Automatico", seguro="Contra todo daños", gama="Alta",
    chasis="Mediano", pais_de_origen="USA", llanta_de_emergencia="Si", numero_de_puertas="4")
    print("marca:",objVehiculo1.marca)
    print("modelo:",objVehiculo1.modelo)
    print("color:",objVehiculo1.color)
    print("placa:",objVehiculo1.placa)
    print("anio:",objVehiculo1.anio)
    print("tipo_de_puerta:",objVehiculo1.tipo_de_puerta)
    print("combustible:",objVehiculo1.combustible)
    print("kilometraje:",objVehiculo1.kilometraje)
    print("caja_de_cambio:",objVehiculo1.caja_de_cambio)
    print("seguro:",objVehiculo1.seguro)
    print("gama:",objVehiculo1.gama)
    print("chasis:",objVehiculo1.chasis)
    print("pais_de_origen:",objVehiculo1.pais_de_origen)
    print("llanta_de_emergencia:",objVehiculo1.llanta_de_emergencia)
    print("numero_de_puertas:",objVehiculo1.numero_de_puertas)




