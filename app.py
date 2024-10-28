from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    # Leer el archivo CSV en un DataFrame
    # user = os.getlogin()
    # df_clasificacion = pd.read_csv(f"C:/Users/{user}/OneDrive/Doctorado/codigo_Python/WebUnion/static/tabla_de_clasificacion/tabla_de_clasificacion.csv")
    url = "https://raw.githubusercontent.com/juanmartinsantos/unionvinotinto/main/static/tabla_de_clasificacion/tabla_de_clasificacion.csv"
    df_clasificacion = pd.read_csv(url)

    # Convertir el DataFrame a una lista de diccionarios
    equipos = df_clasificacion.to_dict(orient='records')

    # Renderizar la plantilla HTML con los datos de los equipos
    return render_template('inicio.html', equipos=equipos)

@app.route('/equipo')
def equipo():
    return render_template('equipo.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

if __name__ == '__main__':
    app.run(debug=True)
