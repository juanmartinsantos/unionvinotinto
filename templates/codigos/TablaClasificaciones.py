import pandas as pd

# Datos de la tabla "Clasificación"
data = {
    'Equipo': [
        "VALDELOSA FS",
        "DOÑINOS-LOW COST CARBURANTES",
        "BIZAS",
        "LIVERPOOL PUB",
        "PAPELERIA SAN FERNANDO B",
        "UNIÓN VINOTINTO FS",
        "TRIANGLE CREATIVE-BAR VERDI",
        "LA ROSA IBÉRICA",
        "CASTELLANOS DE MORISCOS",
        "DOÑINOS FS",
        "FC HIDRAFRESA SONNER"
    ],
    'PJ': [7, 7, 6, 7, 6, 6, 6, 6, 6, 6, 7],  # Partidos Jugados
    'PG': [4, 3, 4, 4, 3, 3, 3, 2, 2, 1, 0],  # Partidos Ganados
    'PE': [1, 4, 0, 0, 2, 2, 1, 1, 1, 0, 1],  # Partidos Empatados
    'PP': [2, 0, 2, 3, 1, 1, 2, 3, 3, 5, 6],  # Partidos Perdidos
    'GF': [36, 35, 34, 31, 26, 21, 31, 35, 10, 23, 24],  # Goles a Favor
    'GC': [27, 28, 22, 20, 16, 17, 23, 51, 20, 36, 46],  # Goles en Contra
    'DG': [9, 7, 12, 11, 10, 4, 8, -16, -10, -13, -22],  # Diferencia de Goles
    'SN': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Sin Novedades (puede no ser usado)
    'PT': [13, 13, 12, 12, 11, 11, 10, 7, 6, 3, 1]   # Puntos
}



# Crear el DataFrame
df_clasificacion = pd.DataFrame(data)

# Ordenar el DataFrame por Puntos, Diferencia de Goles y Goles a Favor
df_sorted = df_clasificacion.sort_values(by=['PT', 'DG', 'GF'], ascending=False)

# Reiniciar el índice
df_sorted.reset_index(drop=True, inplace=True)

# import os
# user = os.getlogin()
# df_sorted.to_csv(f"C:/Users/{user}/OneDrive/Doctorado/codigo_Python/WebUnion/static/tabla_de_clasificacion/tabla_de_clasificacion.csv", index=False)

# Mostrar el DataFrame
# print(df_clasificacion)
