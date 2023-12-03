# Romero Ramos David 952

"""
Desarrollar una clase llamada PaisMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre.
"""
import mysql.connector
from Programa_1 import MySQLConnect

class PaisMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, nombre):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Validar que el nombre no exista en la tabla antes de insertar
            cursor.execute("SELECT id FROM Pais WHERE nombre = %s", (nombre,))
            existing_id = cursor.fetchone()

            if existing_id is not None:
                print(f"El nombre '{nombre}' ya existe en la tabla.")
                return False

            # Insertar el nuevo registro en la tabla Pais
            cursor.execute("INSERT INTO Pais (id, nombre) VALUES (%s, %s)", (id, nombre))
            connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al insertar en la tabla Pais: {err}")
            return False
        finally:
            cursor.close()
            self.desconectar()

    def editar(self, nombre, nuevo_nombre):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Validar que el nuevo nombre no exista en la tabla
            cursor.execute("SELECT id FROM Pais WHERE nombre = %s", (nuevo_nombre,))
            existing_id = cursor.fetchone()

            if existing_id is not None:
                print(f"El nuevo nombre '{nuevo_nombre}' ya existe en la tabla.")
                return False

            # Actualizar el nombre en la tabla Pais
            cursor.execute("UPDATE Pais SET nombre = %s WHERE nombre = %s", (nuevo_nombre, nombre))
            connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al editar el nombre en la tabla Pais: {err}")
            return False
        finally:
            cursor.close()
            self.desconectar()

    def eliminar(self, id):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Eliminar el registro en la tabla Pais
            cursor.execute("DELETE FROM Pais WHERE id = %s", (id,))
            connection.commit()

            if cursor.rowcount > 0:
                return True
            else:
                print(f"No se encontró ningún registro con id = {id}.")
                return False
        except mysql.connector.Error as err:
            print(f"Error al eliminar en la tabla Pais: {err}")
            return False
        finally:
            cursor.close()
            self.desconectar()

    def consultar(self, filtro):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            # Consultar la tabla Pais con el filtro proporcionado
            query = f"SELECT * FROM Pais WHERE {filtro}"
            cursor.execute(query)

            results = cursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print(f"Error al consultar la tabla Pais: {err}")
            return []
        finally:
            cursor.close()
            self.desconectar()
