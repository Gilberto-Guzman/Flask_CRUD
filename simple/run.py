# Este archivo será el punto de entrada de nuestra aplicación. Contendrá el código para ejecutar la aplicación Flask.

from app import app

if __name__ == "__main__":
    app.run(debug=True)
