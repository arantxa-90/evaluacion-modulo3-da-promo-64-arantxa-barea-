import pandas as pd
import numpy as np
import regex as re


def lectura_ficheros(path_df1, path_df2):
    """
    Carga dos datasets, detecta automáticamente la columna común entre ambos,
    analiza el grado de correspondencia de dicha clave y realiza la unión recomendada.

    Parámetros
    ----------
    path_df1 : str
        Ruta al primer fichero CSV.

    path_df2 : str
        Ruta al segundo fichero CSV.

    Devuelve
    --------
    df : pandas.DataFrame
        DataFrame resultante de la unión de ambos datasets mediante la clave común detectada.

    Qué hace
    --------
    1. Carga ambos datasets desde las rutas especificadas.
    2. Detecta automáticamente la(s) columna(s) común(es).
    3. Selecciona la primera columna común como clave de unión.
    4. Calcula el porcentaje de correspondencia de dicha clave entre ambos datasets.
    5. Determina el tipo de unión recomendado (inner, left, right u outer).
    6. Realiza el merge utilizando la clave y el tipo de unión recomendado.
    7. Muestra información básica del resultado.

    Notas
    -----
    Esta función permite automatizar el proceso de unión sin depender de un nombre de columna
    específico, haciendo el código reutilizable en distintos datasets.
    """

    print("LECTURA DE FICHEROS")

    # Carga de datos
    df1 = pd.read_csv(path_df1)
    df2 = pd.read_csv(path_df2)

    print(f"Dataset 1: {df1.shape[0]} filas × {df1.shape[1]} columnas")
    print(f"Dataset 2: {df2.shape[0]} filas × {df2.shape[1]} columnas")

    # Detectar columnas comunes
    columnas_comunes = list(set(df1.columns).intersection(df2.columns))

    if not columnas_comunes:
        raise ValueError("ERROR: No se encontraron columnas comunes entre los datasets.")

    print("\nColumnas comunes detectadas:")
    for col in columnas_comunes:
        print(f"  - {col}")

    # Seleccionar la primera columna común como clave
    key = columnas_comunes[0]
    print(f"\nClave seleccionada: {key}")

    # ==================================================
    # ANÁLISIS DE CORRESPONDENCIA
    # ==================================================

    match_df1 = df1[key].isin(df2[key]).mean() * 100
    match_df2 = df2[key].isin(df1[key]).mean() * 100

    print("\nANÁLISIS DE CORRESPONDENCIA")
    print(f"% claves de df1 presentes en df2: {match_df1:.2f}%")
    print(f"% claves de df2 presentes en df1: {match_df2:.2f}%")

    # Determinar join recomendado
    if match_df1 == 100 and match_df2 == 100:
        join_type = "inner"
        print("Correspondencia completa → recomendado: INNER JOIN")

    elif match_df1 < 100 and match_df2 == 100:
        join_type = "left"
        print("df1 tiene claves sin correspondencia → recomendado: LEFT JOIN")

    elif match_df1 == 100 and match_df2 < 100:
        join_type = "right"
        print("df2 tiene claves sin correspondencia → recomendado: RIGHT JOIN")

    else:
        join_type = "outer"
        print("Correspondencia parcial → recomendado: OUTER JOIN")

    # ==================================================
    # MERGE
    # ==================================================

    df = df1.merge(df2, on=key, how=join_type)

    print(f"\nRESULTADO DEL MERGE ({join_type.upper()})")
    print(f"Shape final: {df.shape[0]} filas × {df.shape[1]} columnas")

    return df


def normalizar_nombres_columnas(lista_columnas, mostrar_resumen=True):
    """
    Normaliza los nombres de las columnas a formato snake_case.

    El proceso incluye:
    - Eliminar espacios al inicio y al final
    - Reemplazar espacios intermedios y caracteres especiales por guiones bajos
    - Convertir de CamelCase/PascalCase a snake_case
    - Convertir todo a minúsculas
    - Eliminar guiones bajos duplicados

    Parámetros
    ----------
    lista_columnas : list
        Lista con los nombres originales de las columnas.

    mostrar_resumen : bool, default=True
        Si True, muestra el resumen de cambios realizados.

    Devuelve
    --------
    list
        Lista con los nombres normalizados en formato snake_case.

    Ejemplo
    -------
    >>> normalizar_nombres_columnas(['Loyalty Number', 'CLV'])
    ['loyalty_number', 'clv']
    """

    nombres_normalizados = []

    for nombre in lista_columnas:

        # 1. eliminar espacios extremos
        limpia = nombre.strip()

        # 2. reemplazar espacios y caracteres especiales por _
        limpia = re.sub(r"[^0-9a-zA-Z]+", "_", limpia)

        # 3. convertir a minúsculas
        limpia = limpia.lower()

        # 4. eliminar _ duplicados
        limpia = re.sub(r"_+", "_", limpia)

        # 5. eliminar _ inicial o final
        limpia = limpia.strip("_")

        nombres_normalizados.append(limpia)

    if mostrar_resumen:
        print("Normalización de nombres de columnas finalizada.")
        print(f"Total columnas procesadas: {len(nombres_normalizados)}")
        print("Resumen de cambios:")
        for orig, nuevo in zip(lista_columnas, nombres_normalizados):
            print(f"  '{orig}' → '{nuevo}'")

    return nombres_normalizados


def renombrar_columnas_semanticas(df, mostrar_resumen=True):
    """
    Renombra columnas para mejorar la claridad semántica y eliminar ambigüedades.

    Este paso se aplica después de la normalización a snake_case y permite
    asignar nombres más descriptivos a variables cuyo significado no es
    evidente o puede generar confusión.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame cuyas columnas serán renombradas.

    mostrar_resumen : bool, default=True
        Si True, muestra el resumen de los cambios realizados.

    Devuelve
    --------
    pandas.DataFrame
        DataFrame con las columnas renombradas.

    Cambios aplicados
    -----------------
    - year → flight_year
    - month → flight_month
    - clv → customer_lifetime_value

    Notas
    -----
    Este paso mejora la interpretabilidad del dataset y evita ambigüedades,
    especialmente cuando existen múltiples variables relacionadas con fechas.
    """

    # Se define un diccionario de mapeo donde la clave representa el nombre original de la columna
    # y el valor el nuevo nombre asignado, con el objetivo de mejorar la claridad semántica.
    rename_map = {
        "year": "flight_year",
        "month": "flight_month",
        "clv": "customer_lifetime_value",
    }

    # Mediante el método .rename(), se aplican estos cambios al DataFrame, alineando la nomenclatura
    # con el estándar definido previamente en las funciones de homogeneización de columnas.
    df.rename(columns=rename_map, inplace=True)

    if mostrar_resumen:
        print("Renombrado semántico de columnas aplicado:")
        for original, nuevo in rename_map.items():
            if original in df.columns or nuevo in df.columns:
                print(f"  '{original}' → '{nuevo}'")

    return df


def eliminar_filas_duplicadas(df, keep="first"):
    """
    Elimina filas completamente duplicadas del DataFrame.

    Se consideran duplicados aquellas filas que tienen valores idénticos en
    todas las columnas.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame a procesar.

    keep : {'first', 'last', False}, default='first'
        Determina qué ocurrencia conservar:
        - 'first' : conserva la primera aparición
        - 'last'  : conserva la última aparición
        - False   : elimina todas las ocurrencias duplicadas

    Devuelve
    --------
    pandas.DataFrame
        DataFrame sin filas duplicadas.
    """

    print("ELIMINACIÓN DE FILAS DUPLICADAS")
    # Crear copia de seguridad
    df = df.copy()

    filas_originales = df.shape[0]

    #Elimina duplicados
    df.drop_duplicates(keep=keep, inplace=True)

    filas_tras_depuracion = df.shape[0]
    filas_eliminadas = filas_originales - filas_tras_depuracion

    print(f"Filas iniciales: {filas_originales}")
    print(f"Filas eliminadas: {filas_eliminadas}")
    print(f"Filas finales: {filas_tras_depuracion}")

    if filas_eliminadas == 0:
        print("No se detectaron duplicados exactos.")
    else:
        print("Duplicados eliminados correctamente.")

    return df


def corregir_tipos_datos(df, mostrar_resumen=True):
    """
    Corrige los tipos de datos de las columnas de un DataFrame según su naturaleza.

    Esta función permite convertir variables a su tipo más adecuado utilizando
    un diccionario de mapeo columna → tipo. Es especialmente útil para:

    - Convertir variables discretas con nulos a entero nullable (Int64)
    - Convertir variables discretas sin nulos a entero (int64)
    - Convertir variables continuas o monetarias a float (float64)

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame cuyas columnas serán convertidas.

    mostrar_resumen : bool, default=True
        Si True, muestra el resumen de los cambios realizados.

    Devuelve
    --------
    pandas.DataFrame
        DataFrame con los tipos de datos corregidos.

    Notas
    -----
    Solo se aplican conversiones a columnas existentes en el DataFrame,
    permitiendo que la función sea reutilizable en distintos datasets.
    """

    df = df.copy()

    # Diccionario columna → tipo destino
    dtype_map = {
        # Variables discretas con nulos → entero nullable
        "cancellation_year": "Int64",
        "cancellation_month": "Int64",
        # Variables discretas sin nulos → entero
        "points_accumulated": "int64",
        # Variables continuas / monetarias → float
        "distance": "float64",
        "dollar_cost_points_redeemed": "float64",
    }

    if mostrar_resumen:
        print("CORRECCIÓN DE TIPOS DE DATOS")
        print("Columnas convertidas:")

    # Aplicar conversiones solo si la columna existe
    for col, dtype in dtype_map.items():
        if col in df.columns:
            dtype_original = df[col].dtype
            df[col] = df[col].astype(dtype)

            if mostrar_resumen:
                print(f"  {col}: {dtype_original} → {dtype}")

    return df


def convertir_negativos_a_nulos(df, columna, mostrar_resumen=True):
    """
    Convierte valores negativos de una columna numérica en valores nulos (NaN).

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame a procesar.

    columna : str
        Nombre de la columna donde se corregirán los valores negativos.

    mostrar_resumen : bool, default=True
        Si True, muestra el número de valores corregidos.

    Devuelve
    --------
    pandas.DataFrame
        DataFrame con los valores negativos convertidos a NaN.

    Qué hace
    --------
    - Identifica valores negativos en la columna especificada.
    - Sustituye dichos valores por NaN, al considerarse inconsistentes con la
      naturaleza de la variable.
    - Muestra un resumen del número de valores corregidos (opcional).
    """

    df = df.copy()

    # Calcular el número de registros con valores negativos en la columna especificada,
    # lo que permite cuantificar el alcance de la corrección aplicada
    n_negativos = (df[columna] < 0).sum()

    # Reemplazar los valores negativos por NaN, ya que representan valores inválidos
    # según la naturaleza de la variable y deben ser tratados como datos faltantes
    df.loc[df[columna] < 0, columna] = np.nan

    if mostrar_resumen:
        print(f"{columna}: {n_negativos} valores negativos convertidos a NaN")

    return df


def imputar_salary_por_grupos(df, columna="salary", mostrar_resumen=True):
    """
    Imputa valores nulos en una variable continua utilizando la mediana
    calculada por grupos de variables estructurales relacionadas.

    En este caso, la imputación se realiza de forma jerárquica:
    Mediana por grupo de education y loyalty_card

    Este enfoque permite imputar valores de forma más realista, preservando
    las diferencias salariales entre segmentos de clientes y evitando el uso
    exclusivo de la mediana global.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame que contiene la variable a imputar.

    columna : str, default="salary"
        Nombre de la columna sobre la que se realizará la imputación.

    mostrar_resumen : bool, default=True
        Si True, muestra un resumen del proceso de imputación.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con los valores imputados.
    """

    df = df.copy()

    nulos_antes = df[columna].isnull().sum()

    # 1) Mediana por grupos (si el grupo tiene mediana NaN, no imputa)
    mediana_grupo = df.groupby(["education", "loyalty_card"])[columna].transform("median")
    df[columna] = df[columna].fillna(mediana_grupo)

    # 2) Fallback por education (para los grupos que no se hayan podido imputar en el paso anterior)
    mediana_edu = df.groupby("education")[columna].transform("median")
    df[columna] = df[columna].fillna(mediana_edu)

    # 3) Fallback final: mediana global (para los nulos restantes)
    mediana_global = df[columna].median()
    df[columna] = df[columna].fillna(mediana_global)

    nulos_despues = df[columna].isnull().sum()

    if mostrar_resumen:
        print("IMPUTACIÓN DE SALARY FINALIZADA")
        print(f"Valores nulos antes: {nulos_antes:,}")
        print(f"Valores imputados: {nulos_antes - nulos_despues:,}")
        print(f"Valores nulos restantes: {nulos_despues:,}")

    return df


def clasificar_estado_cliente(valor):
    """
    Clasifica el estado del cliente en función del año de cancelación.

    Devuelve "Active" si el cliente no presenta año de cancelación (NaN),
    y "Cancelled" si el cliente ha cancelado su membresía.
    """

    if pd.isna(valor):
        return "Active"
    else:
        return "Cancelled"


def limpiar_categoricas(df, columnas=None):
    """
    Limpia variables categóricas eliminando espacios y unificando el formato del texto.

    Aplica .str.strip().str.title() para garantizar consistencia en las categorías.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame a procesar.

    columnas : list, default=None
        Columnas a limpiar. Si es None, se aplicará a todas las columnas categóricas.

    Devuelve
    --------
    pandas.DataFrame
        DataFrame con las variables categóricas limpias.
    """

    df = df.copy()

    # Si no se especifican columnas, detectar todas las categóricas
    if columnas is None:
        columnas = df.select_dtypes(include="O").columns

    # Aplicar limpieza básica
    for col in columnas:
        df[col] = df[col].str.strip().str.title()

    return df


def revisar_incoherencias_vuelos(df):
    """
    Detecta posibles incoherencias lógicas en las variables relacionadas.
    """

    df = df.copy()

    incoherencias = {}

    incoherencias["booked > total"] = (df["flights_booked"] > df["total_flights"]).sum()

    incoherencias["companions > total"] = (
        df["flights_with_companions"] > df["total_flights"]
    ).sum()

    incoherencias["distance > 0 pero total_flights = 0"] = (
        (df["total_flights"] == 0) & (df["distance"] > 0)
    ).sum()

    incoherencias["points_accumulated > 0 pero total_flights = 0"] = (
        (df["total_flights"] == 0) & (df["points_accumulated"] > 0)
    ).sum()

    print("REVISIÓN DE INCOHERENCIAS LÓGICAS")
    for k, v in incoherencias.items():
        print(f"{k}: {v}")

    return incoherencias


def main():
    path_df1 = "../data/raw/Customer Flight Activity.csv"
    path_df2 = "../data/raw/Customer Loyalty History.csv"

    df = lectura_ficheros(path_df1, path_df2)

    df.columns = normalizar_nombres_columnas(df.columns.tolist())
    df = renombrar_columnas_semanticas(df)
    df = eliminar_filas_duplicadas(df)
    df = corregir_tipos_datos(df)
    df = convertir_negativos_a_nulos(df, "salary")
    df = imputar_salary_por_grupos(df)

    df["customer_status"] = df["cancellation_year"].apply(clasificar_estado_cliente)

    df = limpiar_categoricas(df)

    revisar_incoherencias_vuelos(df)
    df = corregir_tipos_datos(df)

    output_path = "../data/processed/customer_loyalty_clean.csv"
    df.to_csv(output_path, index=False)

    print(f"Dataset limpio exportado a: {output_path}")


if __name__ == "__main__":
    main()


