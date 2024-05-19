
from funcion import *

def mostrar_menu():
    opcion = None
    while opcion != 0:
        print("Menú:")
        print("1. Ingresar un nuevo paciente")
        print("2. Mostrar paciente")
        print("3. Asignar paciente a médico")
        print("4. Ordenar examen para un paciente")
        print("5. Cambiar paciente de cama")
        print("6. Cambiar paciente de medico")
        print("7. Diagnosticar enfermedad a un paciente")
        print("8. Listar Pacientes Clinica")
        print("9. Listar Medicos Clinica")
        print("10. Crear cama")
        print("11. Crear habitacion")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            print("Seleccionaste: Ingresar un nuevo paciente")
            ingresar_paciente()
        elif opcion == 2:
            print("Seleccionaste: Mostrar paciente")
            mostrar_paciente()
        elif opcion == 3:
            print("Seleccionaste: Asignar paciente a médico")
            asignar_paciente_a_medico()
        elif opcion == 4:
            print("Seleccionaste: Ordenar examen para un paciente")
            # Lógica para ordenar examen para un paciente
        elif opcion == 5:
            print("Seleccionaste: Cambiar paciente de cama")
            cambiar_paciente_de_cama()
        elif opcion == 6:
            print("Seleccionaste: Cambiar médico de un paciente")
            cambiar_paciente_a_medico()
        elif opcion == 7:
            print("Seleccionaste: Diagnosticar enfermedad a un paciente")
            # diagnosticar_enfermedad_a_paciente()
        elif opcion == 8:
            print("Seleccionaste: Listar Pacientes Clinica")
            listar_pacientes()
        elif opcion == 9:
            print("Seleccionaste: Listar Medicos Clinica")
            # listar_medicos()
        elif opcion == 10:
            print("Seleccionaste: Crear cama")
            # crear_cama()
        elif opcion == 11:
            print("Seleccionaste: Crear habitacion")
            # crear_habitacion()
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    mostrar_menu()