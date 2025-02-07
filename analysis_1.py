import pandas as pd
ruta_csv = "data/sample.csv"
df = pd.read_csv(ruta_csv)


# Verificar valores nulos
print("Valores nulos por columna:\n", df.isnull().sum())

# Manejo de valores nulos (rellenando con media en columnas numéricas)
df["edad"] = df["edad"].fillna(df["edad"].mean())
df["salario"] = df["salario"].fillna(df["salario"].mean())


# Convertir tipos de datos
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
df["salario"] = pd.to_numeric(df["salario"], errors="coerce")
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

# Filtrar datos (ejemplo: personas con salario mayor a 3500)
df_filtrado = df[df["salario"] > 3500]

# Agrupar por edad y calcular el salario promedio
df_agrupado = df.groupby("edad")["salario"].mean()

# Crear una nueva columna calculada (doble del salario)
df["salario_doble"] = df["salario"] * 2

# Mostrar primeras filas después del procesamiento
print(df.head())

# Guardar el DataFrame limpio en un nuevo archivo dentro de 'data/'
df.to_csv("data/sample_cleaned.csv", index=False)

print("Procesamiento completado. Archivo guardado en 'data/sample_cleaned.csv'.")
