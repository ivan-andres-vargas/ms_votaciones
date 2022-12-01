from Modelos.partido import Partido
from Repositorios.repositorioPartido import RepositorioPartido


# ----------------------- #
# CRUD - FUNCIONES PYTHON #
# ----------------------- #

# CREACIÓN - CLASE
class ControladorPartido:
    def __init__(self):
        # Se debe llamar al repositorio.
        self._repositorio_partido = RepositorioPartido()

    # CRUD - Función Listar.
    def listar_partido(self):
        return self._repositorio_partido.findAll()

    # CRUD - Función Crear.
    def crear_partido(self, datos_entrada):
        nuevo_partido = Partido(datos_entrada)
        return self._repositorio_partido.save(nuevo_partido)

    # CRUD - Función Eliminar.
    def eliminar_partido(self, id):
        return self._repositorio_partido.delete(id)

    # CRUD - Función Modificar.
    # Si NO se establece un ciclo for se debe enviar la petición con TODOS los campos.
    def modificar_partido(self, id, datos_entrada):
        partido_bd = Partido(self._repositorio_partido.findById(id))
        partido_bd.nombre = datos_entrada["nombre"]
        partido_bd.lema = datos_entrada["lema"]
        return self._repositorio_partido.save(partido_bd)

    # ----------------------- #
