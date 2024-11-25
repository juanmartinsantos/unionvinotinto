import pandas as pd

# Datos de la tabla "Clasificación"
data = {
    'Equipo': [
        "PAPELERIA SAN FERNANDO B",
        "LIVERPOOL PUB",
        "BIZAS",
        "DOÑINOS-LOW COST CARBURANTES",
        "VALDELOSA FS",
        "CASTELLANOS DE MORISCOS",
        "UNIÓN VINOTINTO FS",
        "TRIANGLE CREATIVE-BAR VERDI",
        "LA ROSA IBÉRICA",
        "DOÑINOS FS",
        "FC HIDRAFRESA SONNER"
    ],
    'PJ': [8, 9, 8, 9, 8, 8, 8, 8, 8, 8, 8],  # Partidos Jugados
    'PG': [5, 5, 5, 3, 4, 4, 3, 3, 2, 2, 0],  # Partidos Ganados
    'PE': [2, 1, 1, 3, 0, 0, 2, 1, 1, 1, 2],  # Partidos Empatados
    'PP': [1, 3, 2, 3, 4, 4, 3, 4, 5, 5, 6],  # Partidos Perdidos
    'GF': [33, 44, 50, 43, 47, 27, 26, 34, 42, 34, 34],  # Goles a Favor
    'GC': [18, 28, 35, 36, 38, 29, 26, 31, 67, 42, 50],  # Goles en Contra
    'DG': [15, 16, 15, 7, 9, -2, 0, 3, -25, -8, -16],  # Diferencia de Goles
    'SN': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Sin Novedades (no se usa)
    'PT': [17, 16, 16, 15, 14, 12, 11, 10, 7, 6, 6]   # Puntos
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
