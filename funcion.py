#Para que funcionen se deben importar los objetos asignados a cada funcion

#Se crea la funcion Ingresar Paciente
from db.operations import *
from models.paciente import Paciente

def ingresar_paciente():
    print("Ingrese los datos del paciente:")
    nombre = input("Nombre: ")
    rut = input("Rut: ")

    paciente_por_rut = get_paciente_by_rut(rut)
    if paciente_por_rut is not None:
        print("❌ El paciente ya existe en la base de datos")
        return paciente_por_rut
    paciente = Paciente('',nombre,rut)
    paciente = create_paciente(paciente)

    cama_id = input("ID Cama a asignar: ")
    cama = get_cama_by_id(cama_id)
    if cama is None:
        print("❌ La cama no existe en la base de datos")
    else:
        print(str(paciente))
        print(paciente.get_id())
        cama.set_paciente_id(paciente.get_id())
        update_cama(cama)
        print("✅ Cama asignada correctamente:", cama.show())
        print("HABITACION ID: ", cama.get_habitacion_id())  
        habitacion = get_habitacion_by_id(cama.get_habitacion_id())
        print("🛏️ Habitación Nro.: ", habitacion.get_numero())

    print("✅ Paciente ingresado correctamente:", paciente.show())
    return paciente

def mostrar_paciente():
    print("Mostrar paciente")
    rut = input("Ingrese el rut del paciente: ")
    paciente = get_paciente_by_rut(rut)
    if paciente is None:
        print("❌ El paciente no existe en la base de datos. ")
        return

    print("Nombre: ", paciente.get_nombre())
    print("Rut: ", paciente.get_rut())
    medico = get_medico_by_id(paciente.get_medico_id())
    medico_nombre = medico.get_nombre() if medico is not None else "Sin médico asignado"

    last_examen = get_last_examen_by_paciente_id(paciente.get_id())
    last_examen_resultado = last_examen.get_resultado() if last_examen is not None else "Sin examen asignado"
    diagnostico = get_diagnostico_by_examen_id(last_examen.get_id())
    diagnostico_nombre = diagnostico.get_enfermedad() if diagnostico is not None else "Sin diagnostico asignado"

    cama = get_cama_by_paciente_id(paciente.get_id())
    cama_id = cama.get_id() if cama is not None else "Sin cama asignada"
    habitacion = get_habitacion_by_paciente_id(paciente.get_id())
    habitacion_numero = habitacion.get_numero() if habitacion is not None else "Sin habitación asignada" 

    print("Medico: ", medico_nombre)
    print("Diagnostico: ", diagnostico_nombre)
    print("Ultimo examen: ", last_examen_resultado)
    print("Numero de Habitación: ", habitacion_numero)
    print("Cama: ", cama_id)
    
    return paciente

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

def cambiar_paciente_a_medico():
    print("Cambiar paciente a médico")
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

def cambiar_paciente_de_cama():
    print("Cambiar paciente de cama")
    rut = input("Ingrese el rut del paciente: ")
    paciente = get_paciente_by_rut(rut)
    if paciente is None:
        print("❌ El paciente no existe en la base de datos. ")
        return
    
    cama = input("Ingrese el número de cama: ")
    cama_encontrada = get_cama_by_id(cama)
    if cama_encontrada is None:
        print("❌ La cama no existe en la base de datos")
        return
    paciente.set_cama_id(cama_encontrada.get_id())
    update_paciente(paciente)
    print("✅ Paciente se ha cambiado de cama correctamente:", paciente.show())
    return paciente

def asignar_diagnostico_a_paciente():
    print("Diagnosticar enfermedad a un paciente")
    rut = input("Ingrese el rut del paciente: ")
    paciente = get_paciente_by_rut(rut)
    if paciente is None:
        print("❌ El paciente no existe en la base de datos. ")
        return
    enfermedad = input("Ingrese la enfermedad: ")
    resultado = input("Ingrese el resultado del examen: ")
    tipo = input("Ingrese el tipo de examen: ")
    examen = Examen('',resultado,tipo,paciente.get_id())
    create_examen(examen)
    diagnostico = Diagnostico('',enfermedad,examen.get_id())
    diagnostico.set_examen_id(examen.get_id())
    create_diagnostico(diagnostico)
    print("✅ Diagnóstico realizado correctamente:", diagnostico.show())
    return diagnostico

def listar_pacientes():
    print("Listado de pacientes:")
    pacientes = get_pacientes()
    for paciente in pacientes:
        medico = get_medico_by_id(paciente.get_medico_id())
        medico_name = medico.get_nombre() if medico is not None else "Sin médico asignado"
        print(f"ID: {paciente.get_id()}")
        print(f"Nombre: {paciente.get_nombre()}")
        print(f"Rut: {paciente.get_rut()}")
        print(f"Medico: {medico_name}")
        print("")

def listar_medicos():
    print("Listado de médicos:")
    medicos = get_medicos()
    for medico in medicos:
        print(f"Nombre: {medico.get_nombre()}")
        print(f"Especialidad: {medico.get_especialidad()}")

def crear_cama():
    print("Crear cama")
    numero_habitacion = input("Ingrese el número de habitación: ")
    habitacion = get_habitacion_by_numero(numero_habitacion)
    if habitacion is None:
        print("❌ La habitación no existe en la base de datos")
        return
    cama = Cama('',None,habitacion.get_id(),True)
    create_cama(cama)
    print("✅ Cama creada correctamente:", cama.show())
    return cama

def crear_habitacion():
    print("Crear habitación")
    numero = input("Ingrese el número de habitación: ")
    habitacion_por_numero = get_habitacion_by_numero(numero)
    if habitacion_por_numero is not None:
        print("❌ La habitación ya existe en la base de datos")
        return habitacion_por_numero
    
    habitacion = Habitacion('',numero)
    create_habitacion(habitacion)
    print("✅ Habitación creada correctamente:", habitacion.show())
    return habitacion

def get_habitacion_by_numero(numero):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM habitaciones WHERE numero = %s",
                (numero,)
            )
            habitacion = cursor.fetchone()
    if habitacion is not None:
        return Habitacion(habitacion[0],habitacion[1])
    else:
        return None