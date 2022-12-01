from Modelos.mesa import Mesa
from Repositorios.repositorioMesa import RepositorioMesa


# ----------------------- #
# CRUD - FUNCIONES PYTHON #
# ----------------------- #

# CREACIÓN - CLASE
class ControladorMesa:
    def __init__(self):
        # Se debe llamar al repositorio.
        self._repositorio_mesa = RepositorioMesa()

    # CRUD - Función Listar.
    def listar_mesa(self):
        return self._repositorio_mesa.findAll()

    # CRUD - Función Crear.
    def crear_mesa(self, datos_entrada):
        nueva_mesa = Mesa(datos_entrada)
        return self._repositorio_mesa.save(nueva_mesa)

    # CRUD - Función Eliminar.
    def eliminar_mesa(self, id):
        return self._repositorio_mesa.delete(id)

    # CRUD - Función Modificar.
    # Si NO se establece un ciclo for se debe enviar la petición con TODOS los campos.
    def modificar_mesa(self, id, datos_entrada):
        mesa_bd = Mesa(self._repositorio_mesa.findById(id))
        mesa_bd.ciudad = datos_entrada["ciudad"]
        mesa_bd.departamento = datos_entrada["departamento"]
        mesa_bd.sede = datos_entrada["sede"]
        mesa_bd.numero_mesa = datos_entrada["numero_mesa"]
        return self._repositorio_mesa.save(mesa_bd)

    # ----------------------- #
