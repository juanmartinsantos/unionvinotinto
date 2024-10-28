# import os
import pandas as pd

# Datos de la tabla "Clasificación"
data = {
    'Equipo': [
        "VALDELOSA FS",
        "DOÑINOS-LOW COST CARBURANTES",
        "UNIÓN VINOTINTO FS",
        "TRIANGLE CREATIVE-BAR VERDI",
        "BIZAS",
        "LIVERPOOL PUB",
        "PAPELERIA SAN FERNANDO B",
        "CASTELLANOS DE MORISCOS",
        "LA ROSA IBÉRICA",
        "DOÑINOS FS",
        "FC HIDRAFRESA SONNER"
    ],
    'PJ': [6, 6, 5, 6, 5, 6, 5, 5, 5, 5, 6],  # Partidos Jugados
    'PG': [4, 3, 3, 3, 3, 3, 2, 2, 1, 1, 0],  # Partidos Ganados
    'PE': [0, 3, 2, 1, 0, 0, 2, 0, 1, 0, 1],  # Partidos Empatados
    'PP': [2, 0, 0, 2, 2, 3, 1, 3, 3, 4, 5],  # Partidos Perdidos
    'GF': [30, 29, 18, 31, 30, 21, 23, 10, 27, 17, 22],  # Goles a Favor
    'GC': [21, 22, 13, 23, 19, 18, 16, 17, 45, 28, 36],  # Goles en Contra
    'DG': [9, 7, 5, 8, 11, 3, 7, -7, -18, -11, -14],  # Diferencia de Goles
    'SN': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Sin Novedades (ejemplo, puede no ser usado)
    'PT': [12, 12, 11, 10, 9, 9, 8, 6, 4, 3, 1]   # Puntos
}


# Crear el DataFrame
df_clasificacion = pd.DataFrame(data)

# Ordenar el DataFrame por Puntos, Diferencia de Goles y Goles a Favor
df_sorted = df_clasificacion.sort_values(by=['PT', 'DG', 'GF'], ascending=False)

# Reiniciar el índice
df_sorted.reset_index(drop=True, inplace=True)

# user = os.getlogin()
# df_sorted.to_csv(f"C:/Users/{user}/OneDrive/Doctorado/codigo_Python/WebUnion/static/tabla_de_clasificacion/tabla_de_clasificacion.csv", index=False)

# Mostrar el DataFrame
# print(df_clasificacion)
