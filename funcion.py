#Para que funcionen se deben importar los objetos asignados a cada funcion

#Se crea la funcion Ingresar Paciente
from models.paciente import Paciente


def ingresar_paciente():
    print("Ingrese los datos del paciente:")
    nombre = input("Nombre: ")
    rut = input("Número de Rut: ")
    diagnostico = input("Nombre del diagnostico: ")
    medico = input("Nombre del Medico tratante: ")
    habitacion = input("Número de Habitacion: ")

    # Crea una instancia de la clase Paciente con los datos ingresados
    paciente = Paciente(nombre, rut, diagnostico, medico, habitacion)
    return paciente

nuevo_paciente = ingresar_paciente()
print("Se ha ingresado al paciente:", nuevo_paciente.nombre)

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

listar_pacientes(lista_pacientes)        