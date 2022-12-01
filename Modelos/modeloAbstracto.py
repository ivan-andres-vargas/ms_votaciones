from abc import ABCMeta


# CREACIÓN - MODELO
# Base genérica para el resto de modelos.
class ModeloAbstracto:
    def __init__(self, datos):
        for key, value in datos.items():
            setattr(self, key, value)
            print("Se ha creado un objeto con" + key + " " + value)
