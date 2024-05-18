#Estos datos son ejemplo de lo visto en clases, hay que modificar
import psycopg2 as psy
import config

def InsertBook(l):
    #establecemos la conexion
    conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
    #fin establecemos la conexion
    inserta = conexion.cursor()#instancia un objeto cursor
    inserta.execute("INSERT INTO Libro VALUES(%s,%s,%s,%s,%s,%s)",(new_id(),l.GetTitulo(),l.GetAutor(),l.GetGenero(),l.GetPaginas(),l.GetFormato()))
    conexion.commit()
    #cerramos la conexion
    conexion.close()
    #fin cerramos la conexion

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