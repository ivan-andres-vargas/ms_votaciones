from Modelos.conteo import Conteo
from Repositorios.repositorioConteo import RepositorioConteo


# ----------------------- #
# CRUD - FUNCIONES PYTHON #
# ----------------------- #

# CREACIÓN - CLASE
class ControladorConteo:
    def __init__(self):
        # Se debe llamar al repositorio.
        self._repositorio_conteo = RepositorioConteo()

    # CRUD - Función Listar.
    def listar_conteo(self):
        return self._repositorio_conteo.findAll()

    # CRUD - Función Crear.
    def crear_conteo(self, datos_entrada):
        nuevo_conteo = Conteo(datos_entrada)
        return self._repositorio_conteo.save(nuevo_conteo)

    # CRUD - Función Eliminar.
    def eliminar_conteo(self, id):
        return self._repositorio_conteo.delete(id)

    # CRUD - Función Modificar.
    # Si NO se establece un ciclo for se debe enviar la petición con TODOS los campos.
    def modificar_conteo(self, id, datos_entrada):
        conteo_bd = Conteo(self._repositorio_conteo.findById(id))
        conteo_bd.numero_formulario = datos_entrada["numero_formulario"]
        conteo_bd.conteo_votos = datos_entrada["conteo_votos"]
        conteo_bd.partido = datos_entrada["partido"]
        conteo_bd.id_candidato = datos_entrada["id_candidato"]
        return self._repositorio_conteo.save(conteo_bd)

    # ----------------------- #
