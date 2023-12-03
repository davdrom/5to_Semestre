# Romero Ramos David 952

"""
Desarrollar una clase llamada MySQLConnect que tenga como atributos: host, user, password, database. Debe crear sus métodos set y get (property, setters).
"""
import mysql.connector

class MySQLConnect:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, value):
        self._database = value

    def conectar(self):
        if not self._connection:
            try:
                self._connection = mysql.connector.connect(
                    host=self._host,
                    user=self._user,
                    password=self._password,
                    database=self._database
                )
                print("Conexion exitosa")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
        return self._connection

    def desconectar(self):
        if self._connection:
            self._connection.close()
            self._connection = None
            print("Desconexion exitosa")
