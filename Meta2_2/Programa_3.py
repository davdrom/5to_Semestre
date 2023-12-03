# David Romero Ramos 952

import mysql.connector
from Programa_1 import MySQLConnect
"""
Desarrollar una clase llamada OlimpiadaMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre. 
"""

class OlimpiadaMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, year):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Validar que el año no exista en la tabla antes de insertar
            cursor.execute("SELECT id FROM Olimpiada WHERE year = %s", (year,))
            existing_id = cursor.fetchone()

            if existing_id is not None:
                print(f"El año '{year}' ya existe en la tabla.")
                return False

            # Insertar el nuevo registro en la tabla Olimpiada
            cursor.execute("INSERT INTO Olimpiada (id, year) VALUES (%s, %s)", (id, year))
            connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al insertar en la tabla Olimpiada: {err}")
            return False
        finally:
            cursor.close()
            self.desconectar()

    def editar(self, year, nuevo_year):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Validar que el nuevo año no exista en la tabla
            cursor.execute("SELECT id FROM Olimpiada WHERE year = %s", (nuevo_year,))
            existing_id = cursor.fetchone()

            if existing_id is not None:
                print(f"El nuevo año '{nuevo_year}' ya existe en la tabla.")
                return False

            # Actualizar el año en la tabla Olimpiada
            cursor.execute("UPDATE Olimpiada SET year = %s WHERE year = %s", (nuevo_year, year))
            connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al editar el año en la tabla Olimpiada: {err}")
            return False
        finally:
            cursor.close()
            self.desconectar()

    def eliminar(self, id):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Eliminar el registro en la tabla Olimpiada
            cursor.execute("DELETE FROM Olimpiada WHERE id = %s", (id,))
            connection.commit()

            if cursor.rowcount > 0:
                return True
            else:
                print(f"No se encontró ningún registro con id = {id}.")
                return False
        except mysql.connector.Error as err:
            print(f"Error al eliminar en la tabla Olimpiada: {err}")
            return False
        finally:
            cursor.close()
            self.desconectar()

    def consultar(self, filtro):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Consultar la tabla Olimpiada con el filtro proporcionado
            query = f"SELECT * FROM Olimpiada WHERE {filtro}"
            cursor.execute(query)

            results = cursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print(f"Error al consultar la tabla Olimpiada: {err}")
            return []
        finally:
            cursor.close()
            self.desconectar()
