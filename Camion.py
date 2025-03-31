__author__ = "Nicolas Alejandro Diaz Acosta"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "nicolas.diazacost@campusucc.edu.co"

class Camion:
    # Constantes

    # Constructor
    def __init__(self, matricula, capacidadCarga, consumoGasolina, cargaActual):
        self.matricula:str = matricula
        self.capacidadCarga:float = capacidadCarga
        self.consumoGasolina:float = consumoGasolina
        self.cargaActual:float = cargaActual

    # Metodos
    
    __method__ = "cambiarMatricula"
    __params__ = "nuevaMatricula"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar la matricula del camión"
    def cambiarMatricula(self, nuevaMatricula):
        self.matricula = nuevaMatricula
    
    __method__ = "darMatricula"
    __params__ = "Ninguno"
    __returns__ = "matricula"
    __descriptions__ = "Metodo que sirve para ver la matricula del camión"
    def darMatricula(self):
        return self.matricula

    __method__ = "cambiarCapacidadCarga"
    __params__ = "nuevaCapacidadCarga"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar la capacidad de carga del camión"
    def cambiarCapacidadCarga(self, nuevaCapacidadCarga):
        self.capacidadCarga = nuevaCapacidadCarga
    
    __method__ = "darCapacidadCarga"
    __params__ = "Ninguno"
    __returns__ = "capacidadCarga"
    __descriptions__ = "Metodo que sirve para ver la capacidad de carga del camión"
    def darCapacidadCarga(self):
        return self.capacidadCarga

    __method__ = "cambiarConsumoGasolina"
    __params__ = "nuevoConsumoGasolina"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar el consumo de gasolina del camión"
    def cambiarConsumoGasolina(self, nuevoConsumoGasolina):
        self.consumoGasolina = nuevoConsumoGasolina
    
    __method__ = "darConsumoGasolina"
    __params__ = "Ninguno"
    __returns__ = "consumoGasolina"
    __descriptions__ = "Metodo que sirve para ver el consumo de gasolina del camión"
    def darConsumoGasolina(self):
        return self.consumoGasolina

    __method__ = "cambiarCargaActual"
    __params__ = "nuevaCargaActual"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar la carga actual del camión"
    def cambiarCargaActual(self, nuevaCargaActual):
        self.cargaActual = nuevaCargaActual
    
    __method__ = "darCargaActual"
    __params__ = "Ninguno"
    __returns__ = "cargaActual"
    __descriptions__ = "Metodo que sirve para ver la carga actual del camión"
    def darCargaActual(self):
        return self.cargaActual
