from bson import ObjectId
from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
from flask_cors import CORS

import json

from Controladores.controladorCandidato import ControladorCandidato
from Controladores.controladorPartido import ControladorPartido
from Controladores.controladorMesa import ControladorMesa
from Controladores.controladorConteo import ControladorConteo

ms_votos = Flask(__name__)
CORS(ms_votos)
#cors = CORS(ms_votos, resources=(r"\api\*":("origins":"*")))

# ------------------------- #
# INSTANCIA - CONTROLADORES #
# ------------------------- #

_controlador_candidato = ControladorCandidato()
_controlador_partido = ControladorPartido()
_controlador_mesa = ControladorMesa()
_controlador_conteo = ControladorConteo()


# ------------------------- #

# ----------------------- #
# PATH - PRUEBA DE SALUDO #
# ----------------------- #

@ms_votos.route('/')
def saludo():
    return '<h1>Saludo de Prueba<h1>'


# ----------------------- #

# ---------------------------------- #
# PATH - ADMINISTRADOR DE CANDIDATOS #
# ---------------------------------- #

# PATH - GET PARA CANDIDATO
@ms_votos.route('/candidatos', methods=['GET'])
def listar_candidatos():
    datos_salida = _controlador_candidato.listar_candidato()
    return jsonify(datos_salida)


# PATH - POST PARA CANDIDATO
@ms_votos.route('/candidatos', methods=['POST'])
def crear_candidatos():
    datos_entrada = request.get_json()
    datos_salida = _controlador_candidato.crear_candidato(datos_entrada)
    return jsonify(datos_salida)


# PATH - DELETE PARA CANDIDATO
@ms_votos.route('/candidatos/<string:id>', methods=['DELETE'])
def eliminar_candidatos(id):
    datos_salida = _controlador_candidato.eliminar_estudiante(id)
    return jsonify(datos_salida)


# PATH - PUT PARA CANDIDATO
@ms_votos.route('/candidatos/<string:id>', methods=['PUT'])
def modificar_candidatos(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_candidato.modificar_candidato(id, datos_entrada)
    return jsonify(datos_salida)


# ---------------------------------- #

# -------------------------------- #
# PATH - ADMINISTRADOR DE PARTIDOS #
# -------------------------------- #

# PATH - GET PARA CANDIDATO
@ms_votos.route('/partidos', methods=['GET'])
def listar_partidos():
    datos_salida = _controlador_partido.listar_partido()
    return jsonify(datos_salida)


# PATH - POST PARA CANDIDATO
@ms_votos.route('/partidos', methods=['POST'])
def crear_partidos():
    datos_entrada = request.get_json()
    datos_salida = _controlador_partido.crear_partido(datos_entrada)
    return jsonify(datos_salida)


# PATH - DELETE PARA CANDIDATO
@ms_votos.route('/partidos/<string:id>', methods=['DELETE'])
def eliminar_partidos(id):
    datos_salida = _controlador_partido.eliminar_partido(id)
    return jsonify(datos_salida)


# PATH - PUT PARA CANDIDATO
@ms_votos.route('/partidos/<string:id>', methods=['PUT'])
def modificar_partidos(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_partido.modificar_partido(id, datos_entrada)
    return jsonify(datos_salida)


# ---------------------------------- #

# ----------------------------- #
# PATH - ADMINISTRADOR DE MESAS #
# ----------------------------- #

# PATH - GET PARA CANDIDATO
@ms_votos.route('/mesas', methods=['GET'])
def listar_mesas():
    datos_salida = _controlador_mesa.listar_mesa()
    return jsonify(datos_salida)


# PATH - POST PARA CANDIDATO
@ms_votos.route('/mesas', methods=['POST'])
def crear_mesas():
    datos_entrada = request.get_json()
    datos_salida = _controlador_mesa.crear_mesa(datos_entrada)
    return jsonify(datos_salida)


# PATH - DELETE PARA CANDIDATO
@ms_votos.route('/mesas/<string:id>', methods=['DELETE'])
def eliminar_mesas(id):
    datos_salida = _controlador_mesa.eliminar_mesa(id)
    return jsonify(datos_salida)


# PATH - PUT PARA CANDIDATO
@ms_votos.route('/mesas/<string:id>', methods=['PUT'])
def modificar_mesas(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_mesa.modificar_mesa(id, datos_entrada)
    return jsonify(datos_salida)


# ---------------------------------- #

# ------------------------------ #
# PATH - ADMINISTRADOR DE CONTEO #
# ------------------------------ #

# PATH - GET PARA CANDIDATO
@ms_votos.route('/conteo', methods=['GET'])
def listar_conteo():
    datos_salida = _controlador_conteo.listar_conteo()
    return jsonify(datos_salida)


# PATH - POST PARA CANDIDATO
@ms_votos.route('/conteo', methods=['POST'])
def crear_conteo():
    datos_entrada = request.get_json()
    datos_salida = _controlador_conteo.crear_conteo(datos_entrada)
    return jsonify(datos_salida)


# PATH - DELETE PARA CANDIDATO
@ms_votos.route('/conteo/<string:id>', methods=['DELETE'])
def eliminar_conteo(id):
    datos_salida = _controlador_conteo.eliminar_conteo(id)
    return jsonify(datos_salida)


# PATH - PUT PARA CANDIDATO
@ms_votos.route('/conteo/<string:id>', methods=['PUT'])
def modificar_conteo(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_conteo.modificar_conteo(id, datos_entrada)
    return jsonify(datos_salida)


# ---------------------------------- #


# -------------------------- #
# CONFIGURACIÓN DEL SERVIDOR #
# -------------------------- #

# CONFIGURACIÓN DEL SERVIDOR CON ARCHIVO CONFIG
def cargar_config():
    with open("Configuración/config.json") as archivo:
        _datos_configuracion = json.load(archivo)
    return _datos_configuracion


if __name__ == '__main__':
    datos_configuracion = cargar_config()
    print('Servidor ejecutandose...' + " " + "http://" + datos_configuracion["servidor"] + ":" + datos_configuracion[
        "puerto"])
    serve(ms_votos, host=datos_configuracion["servidor"], port=datos_configuracion["puerto"])

# -------------------------- #
