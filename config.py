import os

SECRET_KEY = os.urandom(32)
DEBUG = True

# Credenciales SQL
server = r"DESKTOP-NVV3NVR\SQLEXPRESS"
database = "agenda_telefonica"
driver = "ODBC Driver 17 for SQL Server"

SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://@{server}/{database}?driver={driver}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
