import pandas as pd

# Cargar los datos
file_path = 'static/tabla_de_clasificacion/tabla_de_clasificacion.csv'  # Cambiar por la ruta al archivo
tabla_clasificacion = pd.read_csv(file_path)

# Calcular estadísticas adicionales
tabla_clasificacion['Eficiencia Ofensiva (GF/PJ)'] = tabla_clasificacion['GF'] / tabla_clasificacion['PJ']
tabla_clasificacion['Eficiencia Defensiva (GC/PJ)'] = tabla_clasificacion['GC'] / tabla_clasificacion['PJ']
tabla_clasificacion['% Ganados'] = (tabla_clasificacion['PG'] / tabla_clasificacion['PJ'])
tabla_clasificacion['% Empatados'] = (tabla_clasificacion['PE'] / tabla_clasificacion['PJ'])
tabla_clasificacion['% Perdidos'] = (tabla_clasificacion['PP'] / tabla_clasificacion['PJ'])

# Crear rankings
tabla_clasificacion['Ranking GF'] = tabla_clasificacion['GF'].rank(ascending=False, method='min')
tabla_clasificacion['Ranking GC'] = tabla_clasificacion['GC'].rank(ascending=True, method='min')
# tabla_clasificacion['Ranking Eficiencia Ofensiva'] = tabla_clasificacion['Eficiencia Ofensiva (GF/PJ)'].rank(ascending=False, method='min')
# tabla_clasificacion['Ranking Eficiencia Defensiva'] = tabla_clasificacion['Eficiencia Defensiva (GC/PJ)'].rank(ascending=True, method='min')

# Seleccionar las columnas relevantes para el resumen
tabla_resumen = tabla_clasificacion[[
    'Equipo', 'PJ', 'PG', 'PE', 'PP',
    '% Ganados', '% Empatados', '% Perdidos',
    'GF', 'GC',
    'Ranking GF', 'Ranking GC',
    'Eficiencia Ofensiva (GF/PJ)', 'Eficiencia Defensiva (GC/PJ)'
    # 'Ranking Eficiencia Ofensiva', 'Ranking Eficiencia Defensiva'
]]

# Exportar la tabla a formato XLSX
file_path_xlsx = 'static/tabla_de_clasificacion/Resumen_Equipos.xlsx'
tabla_resumen.to_excel(file_path_xlsx, index=False)

