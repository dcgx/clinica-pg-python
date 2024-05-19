
from funcion import *

def mostrar_menu():
    opcion = None
    while opcion != 0:
        print("Menú:")
        print("1. Ingresar un nuevo paciente")
        print("2. Asignar paciente a médico")
        print("3. Ordenar examen para un paciente")
        print("4. Cambiar médico de un paciente")
        print("5. Diagnosticar enfermedad a un paciente")
        print("6. Listar Pacientes Clinica")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            print("Seleccionaste: Ingresar un nuevo paciente")
            ingresar_paciente()
        elif opcion == 2:
            print("Seleccionaste: Asignar paciente a médico")
            asignar_paciente_a_medico()
        elif opcion == 3:
            print("Seleccionaste: Ordenar examen para un paciente")
            # Lógica para ordenar examen para un paciente
        elif opcion == 4:
            print("Seleccionaste: Cambiar médico de un paciente")
            # Lógica para cambiar médico de un paciente
        elif opcion == 5:
            print("Seleccionaste: Diagnosticar enfermedad a un paciente")
            # Lógica para diagnosticar enfermedad a un paciente
        elif opcion == 6:
            print("Seleccionaste: Listar Pacientes Clinicae")
            # Lógica para listar pacientes
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    mostrar_menu()