#Estos datos son ejemplo de lo visto en clases, hay que modificar
import psycopg2 as psy
from db import config

from db.connection import get_connection

from models.cama import Cama
from models.diagnostico import Diagnostico
from models.examen import Examen
from models.habitacion import Habitacion
from models.medico import Medico
from models.paciente import Paciente

def create_paciente(paciente) -> Paciente:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO pacientes (nombre, rut, medico_id) VALUES (%s, %s, %s)",
                (paciente.get_nombre(), paciente.get_rut(), None)  # Llama a los métodos
            )
            conn.commit()

            cursor.execute(
                "SELECT * FROM pacientes WHERE rut = %s",
                (paciente.get_rut(),)
            )
            paciente = Paciente(cursor.fetchone()[0], paciente.get_nombre(), paciente.get_rut(), None)
    return paciente

def update_paciente(paciente):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE pacientes SET nombre = %s, medico_id = %s WHERE rut = %s",
                (paciente.get_nombre(), paciente.get_medico_id(), paciente.get_rut())
            )
            conn.commit()
    return paciente

def get_pacientes():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM pacientes"
            )
            pacientes = cursor.fetchall()
    return [Paciente(p[0],p[1], p[2], p[3]) for p in pacientes]

def get_paciente_by_rut(rut):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM pacientes WHERE rut = %s",
                (rut,)
            )
            paciente = cursor.fetchone()
    if paciente is not None:
        return Paciente(paciente[0],paciente[1], paciente[2], paciente[3])
    else:
        return None    
    
def get_medicos():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM medicos"
            )
            medicos = cursor.fetchall()
    return [Medico(m[0],m[1], m[2]) for m in medicos]

def get_medico_by_id(id_medico):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM medicos WHERE medico_id = %s",
                (id_medico,)
            )
            medico = cursor.fetchone()
    if medico is not None:
        return Medico(medico[0], medico[1], medico[2])
    else:
        return None

def get_medico_by_name(nombre_medico):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM medicos WHERE nombre = %s",
                (nombre_medico,)
            )
            medico = cursor.fetchone()
    if medico is not None:
        return Medico(medico[0], medico[1], medico[2])
    else:
        return None

def get_examen_by_paciente_id(paciente_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM examenes WHERE paciente_id = %s",
                (paciente_id,)
            )
            examen = cursor.fetchone()
    if examen is not None:
        return Examen(examen[0], examen[1], examen[2], examen[3])

def get_last_examen_by_paciente_id(paciente_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM examenes WHERE paciente_id = %s ORDER BY fecha DESC LIMIT 1",
                (paciente_id,)
            )
            examen = cursor.fetchone()
    if examen is not None:
        return Examen(examen[0], examen[1], examen[2], examen[3])   

def get_diagnostico_by_examen_id(examen_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM diagnosticos WHERE examen_id = %s",
                (examen_id,)
            )
            diagnostico = cursor.fetchone()
    if diagnostico is not None:
        return Diagnostico(diagnostico[0], diagnostico[1])    

def create_habitacion(habitacion: Habitacion):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO habitaciones (numero) VALUES (%s)",
                (habitacion.get_numero(),)
            )
            conn.commit()
    return habitacion

def get_habitacion_by_id(habitacion_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM habitaciones WHERE habitacion_id = %s",
                (habitacion_id,)
            )
            habitacion = cursor.fetchone()
    if habitacion is not None:
        return Habitacion(habitacion[0], habitacion[1])

def get_habitacion_by_paciente_id(paciente_id):
    cama = get_cama_by_paciente_id(paciente_id)
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM habitaciones WHERE habitacion_id = %s",
                (cama.get_habitacion_id(),)
            )
            habitacion = cursor.fetchone()
    if habitacion is not None:
        return Habitacion(habitacion[0], habitacion[1])

def create_cama(cama: Cama):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO camas (paciente_id, habitacion_id, habilitada) VALUES (%s, %s, %s)",
                (cama.get_paciente_id(), cama.get_habitacion_id(), cama.get_habilitada())
            )
            conn.commit()
    return cama

def get_cama_by_id(cama_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM camas WHERE cama_id = %s",
                (cama_id,)
            )
            cama = cursor.fetchone()
    if cama is not None:
        return Cama(cama[0], cama[1], cama[2], cama[3])

def get_cama_by_paciente_id(paciente_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM camas WHERE paciente_id = %s",
                (paciente_id,)
            )
            cama = cursor.fetchone()
    if cama is not None:
        return Cama(cama[0], cama[1], cama[2], cama[3])

def update_cama(cama: Cama):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE camas SET paciente_id = %s WHERE cama_id = %s",
                (cama.get_paciente_id(), cama.get_id())
            )
            conn.commit()
    return cama


def create_examen(examen: Examen):
    examen_id = None
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO examenes (resultado, tipo, paciente_id) VALUES (%s, %s, %s)",
                (examen.get_resultado(), examen.get_tipo(), examen.get_paciente_id())
            )
            conn.commit()
    last_examen = get_last_examen()
    if last_examen is not None:
        examen_id = last_examen.get_id()
    examen.set_id(examen_id)
    return examen

def get_last_examen():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM examenes ORDER BY fecha DESC LIMIT 1"
            )
            examen = cursor.fetchone()
    if examen is not None:
        return Examen(examen[0], examen[1], examen[2], examen[3])

def create_diagnostico(diagnostico: Diagnostico):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO diagnosticos (enfermedad, examen_id) VALUES (%s, %s)",
                (diagnostico.get_enfermedad(), diagnostico.get_examen_id())
            )
            conn.commit()
    return diagnostico