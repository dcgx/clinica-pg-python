#Estos datos son ejemplo de lo visto en clases, hay que modificar
import psycopg2 as psy
import config

def connect():
    #establecemos la conexion
    conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
    #fin establecemos la conexion
    select_id = conexion.cursor()
    select_id.execute("SELECT libro_id FROM Libro ORDER BY libro_id DESC LIMIT 1")
    if select_id.rowcount > 0:#rowcount cuenta la cantidad de filas.
        row = select_id.fetchone() #Itera en el resultado, obtenidno los datos de la sigueinte fila
        while row is not None:
            book_id = int(row[0])
            row = select_id.fetchone()
        book_id += 1
    else:
        book_id = 1
    #cerramos la conexion
    conexion.close()
    #fin cerramos la conexion
    return book_id