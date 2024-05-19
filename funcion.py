#Para que funcionen se deben importar los objetos asignados a cada funcion

#Se crea la funcion Ingresar Paciente
from db.operations import get_medico_by_id, get_pacientes, update_paciente, create_paciente, get_medico_by_name, get_paciente_by_rut
from models.paciente import Paciente

def ingresar_paciente():
    print("Ingrese los datos del paciente:")
    nombre = input("Nombre: ")
    rut = input("Número de Rut: ")
    paciente_found = get_paciente_by_rut(rut)
    if paciente_found is not None:
        print("❌ El paciente ya existe en la base de datos")
        return paciente_found
    paciente = Paciente('',nombre,rut)
    create_paciente(paciente)
    print("✅ Paciente ingresado correctamente:", paciente.show())
    return paciente


#Se crea la funcion Asignar paciente a Medico
def asignar_paciente_a_medico():
    print("Asignar paciente a médico")
    rut = input("Ingrese el rut del paciente: ")
    paciente = get_paciente_by_rut(rut)
    if paciente is None:
        print("❌ El paciente no existe en la base de datos. ")
        return
    
    medico = input("Ingrese el nombre del médico: ")
    medico_encontrado = get_medico_by_name(medico)
    if medico_encontrado is None:
        print("❌ El médico no existe en la base de datos")
        return
    paciente.set_medico_id(medico_encontrado.get_id())
    update_paciente(paciente)
    print("✅ Paciente asignado a médico correctamente:", paciente.show())
    return paciente

#Se crea la funcion Ordenar examen a paciente
#PENDIENTE

#Se crea la funcion Cambiar Medico a un paciente
#PENDIENTE

#Se crea la funcion Diagnosticar enfermedad a un paciente
#PENDIENTE

def listar_pacientes():
    print("Listado de pacientes:")
    pacientes = get_pacientes()
    for paciente in pacientes:
        medico = get_medico_by_id(paciente.get_medico_id())
        medico_name = medico.get_nombre() if medico is not None else "Sin médico asignado"
        print(f"Nombre: {paciente.get_nombre()}")
        print(f"Rut: {paciente.get_rut()}")
        print(f"Medico: {medico_name}")
        print("")
