#Para que funcionen se deben importar los objetos asignados a cada funcion

#Se crea la funcion Ingresar Paciente
from db.operations import create_paciente, get_paciente_by_rut
from models.paciente import Paciente

def ingresar_paciente():
    print("Ingrese los datos del paciente:")
    nombre = input("Nombre: ")
    rut = input("Número de Rut: ")
    paciente_found = get_paciente_by_rut(rut)
    if paciente_found is not None:
        print("❌ El paciente ya existe en la base de datos")
        return paciente_found
    paciente = Paciente(nombre, rut)
    create_paciente(paciente)
    print("✅ Paciente ingresado correctamente:", paciente.show())
    return paciente


#Se crea la funcion Asignar paciente a Medico
#PENDIENTE

#Se crea la funcion Ordenar examen a paciente
#PENDIENTE

#Se crea la funcion Cambiar Medico a un paciente
#PENDIENTE

#Se crea la funcion Diagnosticar enfermedad a un paciente
#PENDIENTE

#Se crea la funcion listar pacientes
#PENDIENTE REVISAR Y CORREGIR 
def listar_pacientes(lista_pacientes):
    print("Listado de pacientes:")
    for paciente in lista_pacientes:
        print(f"Nombre: {paciente.nombre}")
        print(f"Rut: {paciente.rut}")
        print(f"Diagnostico: {paciente.diagnostico}")
        print(f"Medico: {paciente.medico}")
        print(f"Habitacion: {paciente.habitacion}")

listar_pacientes()        