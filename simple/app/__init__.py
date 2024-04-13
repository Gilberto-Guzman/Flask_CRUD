# Este archivo inicializa la aplicación Flask y configura la conexión a la base de datos.

from flask import Flask
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

from app import routes
