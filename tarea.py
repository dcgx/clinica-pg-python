"""Objetivo: Diseñar e implementar una aplicación de consola, utilizando Python y el motor de base de datos PostGreSQL.

Antes de trabajar en esta tarea debes:

-Conocer los elementos del modelo relacional,
-Comprender el proceso de modelamiento, normalización, sintaxis del lenguaje SQL.
-Entender y aplicar los fundamentos de la programación en Python, siendo capaz de gestionar a través de este la base de datos solicitada.
-Utilizar un entorno de desarrollo como miniconda, con todas las librerías necesarias para poder realizar el trabajo.
-*Recuerda haber instalado PostgresSQL*

Instrucciones para la elaboración de la tarea:

1. Revisa el caso que aparece más abajo y conforme a lo solicitado realiza las actividades listadas:

“En una clínica, Los pacientes ingresan y se les asigna una cama. 
Las camas están en habitaciones, y cada una de estas tiene muchas camas. 
Cada paciente tiene asignado un médico el cual puede tratar a muchos pacientes. 
El médico puede ordenar diferentes exámenes para un paciente, estos exámenes están tipificados y en la orden de examen, el
médico indica un posible diagnóstico. 
El paciente puede cambiar de médico durante su estadía en el hospital. 
Cada médico puede o pudo diagnosticar una o más enfermedades a un paciente. Las enfermedades están tipificadas, sin embargo, 
el médico debe especificar qué exámenes de laboratorio consideró para el diagnóstico de cada enfermedad.”

1.1 Diseño un modelo relacional de acuerdo a lo solicitado en el caso.

RECORDAR: Un modelo relacional en Python debe contener todo lo necesario para interactuar con una base de datos relacional, 
incluida la definición de la estructura de la tabla, el mapeo entre objetos y filas de la tabla, operaciones CRUD 
y manejo de relaciones entre tablas.

Subtareas:

*Se deben definir los objetos paciente, habitacion, examen, medico, enfermedad, otros?

*Se deben crear las funciones: 
-menu
-listarPacientes (todos con nombre, rut, diagnostico, medico y habitacion),
-mostrarPaciente (debe mostrar rut, nombre, diagnostico, medico tratante, último examen realizado, habitación y cama en la
que se encuentra)
-cambiarPaciente (de una cama a otra) 
-cambiarMedico (un paciente que cambie de médico)
-crearCama
-crearHabitacion

1.2 A partir del diseño, crea la base de datos en tu servidor PostgresSQL.


1.3 Genera un script que te permita poblar la base de datos con al menos 10 registros por tabla.


1.4 Implemente una aplicación de consola que contemple las funciones citadas en el punto 1.1

"""