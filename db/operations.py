#Estos datos son ejemplo de lo visto en clases, hay que modificar
import psycopg2 as psy
from db import config

from db.connection import get_connection

from models.paciente import Paciente

def create_paciente(paciente):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO pacientes (nombre, rut, medico_id) VALUES (%s, %s, %s)",
                (paciente.get_nombre(), paciente.get_rut(), None)  # Llama a los métodos
            )
            conn.commit()
    return paciente

def get_paciente_by_rut(rut):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM pacientes WHERE rut = %s",
                (rut,)
            )
            paciente = cursor.fetchone()
    if paciente is not None:
        return Paciente(paciente[1], paciente[2])
    else:
        return None    

def ShowAllBook():
    #establecemos la conexion
    conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
    #fin establecemos la conexion
    select_all_book = conexion.cursor() #establecemos el cursor
    select_all_book.execute("SELECT * FROM Libro")
    if select_all_book.rowcount > 0:#rowcount cuenta la cantidad de filas.
        row = select_all_book.fetchone() #Itera en el resultado, obtenidno los datos de la sigueinte fila
        while row is not None:
            print('\n**********************\n')
            print(f'Nombre: {str(row[1])}\nAutor: {str(row[2])}\nGenero: {str(row[3])}\nPaginas: {str(row[4])}\nFormato: {str(row[5])}')
            print('\n**********************\n')
            row = select_all_book.fetchone()
    else:
        print('\n**********************\n')
        print('No existen registros en la base de datos')
    #cerramos la conexión
    conexion.close()
    #fin cerramos la conexión

def ShowFilterBook(search):
    #establecemos la conexion
    conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
    #fin establecemos la conexion
    select_filter_book = conexion.cursor() #establecemos el cursor
    select_filter_book.execute("SELECT * FROM Libro WHERE libro_genero = %s",(search,))
    if select_filter_book.rowcount > 0:#rowcount cuenta la cantidad de filas.
        row = select_filter_book.fetchone() #Itera en el resultado, obtenidno los datos de la sigueinte fila
        while row is not None:
            print('\n**********************\n')
            print(f'Nombre: {str(row[1])}\nAutor: {str(row[2])}\nGenero: {str(row[3])}\nPaginas: {str(row[4])}\nFormato: {str(row[5])}')
            print('\n**********************\n')
            row = select_filter_book.fetchone()
    else:
        print('\n**********************\n')
        print('No existen registros en la base de datos')
    #cerramos la conexión
    conexion.close()
    #fin cerramos la conexión
    
def ShowByAutor(search):
    #establecemos la conexion
    conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
    #fin establecemos la conexion
    select_filter_book = conexion.cursor() #establecemos el cursor
    select_filter_book.execute("SELECT * FROM Libro WHERE lower(libro_autor) like %s", ('%' + search + '%',))

    if select_filter_book.rowcount > 0:#rowcount cuenta la cantidad de filas.
        row = select_filter_book.fetchone() #Itera en el resultado, obtenidno los datos de la sigueinte fila
        while row is not None:
            print('\n**********************\n')
            print(f'Nombre: {str(row[1])}\nAutor: {str(row[2])}\nGenero: {str(row[3])}\nPaginas: {str(row[4])}\nFormato: {str(row[5])}')
            print('\n**********************\n')
            row = select_filter_book.fetchone()
    else:
        print('\n**********************\n')
        print(f"Sin Resultados.\n")
    #cerramos la conexión
    conexion.close()
    return select_filter_book.rowcount
    #fin cerramos la conexión    