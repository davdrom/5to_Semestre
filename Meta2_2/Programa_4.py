# David Romero Ramos 952

import mysql.connector
from Programa_1 import MySQLConnect

"""
Desarrollar una clase llamada ResultadosMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre. 
"""
class ResultadosMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Validar que los valores de oro, plata y bronce sean enteros positivos
            if oro < 0 or plata < 0 or bronce < 0:
                print("Los valores de oro, plata y bronce deben ser enteros positivos.")
                return False

            # Insertar el nuevo registro en la tabla Resultados
            cursor.execute("INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) VALUES (%s, %s, %s, %s, %s, %s)",
                           (idOlimpiada, idPais, idGenero, oro, plata, bronce))
            connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al insertar en la tabla Resultados: {err}")
            return False
        finally:
            cursor.close()
            self.desconectar()

    def editar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Validar que los valores de oro, plata y bronce sean enteros positivos
            if oro < 0 or plata < 0 or bronce < 0:
                print("Los valores de oro, plata y bronce deben ser enteros positivos.")
                return False

            # Actualizar los valores de oro, plata y bronce en la tabla Resultados
            cursor.execute("UPDATE Resultados SET oro = %s, plata = %s, bronce = %s WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s",
                           (oro, plata, bronce, idOlimpiada, idPais, idGenero))
            connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al editar en la tabla Resultados: {err}")
            return False
        finally:
            cursor.close()
            self.desconectar()

    def eliminar(self, idOlimpiada, idPais, idGenero):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Eliminar el registro en la tabla Resultados
            cursor.execute("DELETE FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s",
                           (idOlimpiada, idPais, idGenero))
            connection.commit()

            if cursor.rowcount > 0:
                return True
            else:
                print(f"No se encontró ningún registro con idOlimpiada = {idOlimpiada}, idPais = {idPais}, idGenero = {idGenero}.")
                return False
        except mysql.connector.Error as err:
            print(f"Error al eliminar en la tabla Resultados: {err}")
            return False
        finally:
            cursor.close()
            self.desconectar()

    def consultar(self, filtro):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Consultar la tabla Resultados con el filtro proporcionado
            query = f"SELECT * FROM Resultados WHERE {filtro}"
            cursor.execute(query)

            results = cursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print(f"Error al consultar la tabla Resultados: {err}")
            return []
        finally:
            cursor.close()
            self.desconectar()
