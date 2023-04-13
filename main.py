from mysql.connector import Error
import mysql.connector
from data_random import data

try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234567890',
        db='carga_m_A'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO usuarios(name, company, job, email, phone, mac_address) 
                                VALUES (%s, %s, %s, %s, %s, %s)""", data)
        if (len(data) == cursor.rowcount):
            connection.commit()
            print("{} Filas insertadas.".format(len(data)))
        else:
            connection.rollback()
except Error as ex:
    print("Error en la conexion: {}".format(ex))
finally:
    if connection.is_connected():
        connection.close()
        print("Conexion cerrada.")

