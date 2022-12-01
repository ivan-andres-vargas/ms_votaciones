from Modelos.candidato import Candidato
from Repositorios.repositorioCandidato import RepositorioCandidato


# ----------------------- #
# CRUD - FUNCIONES PYTHON #
# ----------------------- #

# CREACIÓN - CLASE
class ControladorCandidato:
    def __init__(self):
        # Se debe llamar al repositorio.
        self._repositorio_candidato = RepositorioCandidato()

    # CRUD - Función Listar.
    def listar_candidato(self):
        return self._repositorio_candidato.findAll()

    # CRUD - Función Crear.
    def crear_candidato(self, datos_entrada):
        nuevo_candidato = Candidato(datos_entrada)
        return self._repositorio_candidato.save(nuevo_candidato)

    # CRUD - Función Eliminar.
    def eliminar_estudiante(self, id):
        return self._repositorio_candidato.delete(id)

    # CRUD - Función Modificar.
    # Si NO se establece un ciclo for se debe enviar la petición con TODOS los campos.
    def modificar_candidato(self, id, datos_entrada):
        candidato_bd = Candidato(self._repositorio_candidato.findById(id))
        candidato_bd.resolucion = datos_entrada["resolucion"]
        candidato_bd.cedula = datos_entrada["cedula"]
        candidato_bd.nombre = datos_entrada["nombre"]
        candidato_bd.apellido = datos_entrada["apellido"]
        return self._repositorio_candidato.save(candidato_bd)

    # ----------------------- #
