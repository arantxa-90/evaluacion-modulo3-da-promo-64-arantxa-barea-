# DECISIONES DE LIMPIEZA DE DATOS

Este documento recoge las decisiones de limpieza aplicadas al dataset tras el análisis exploratorio (EDA), con el objetivo de garantizar la calidad, consistencia y fiabilidad de los datos para su análisis posterior.

---

## 1. INTEGRACIÓN DE LOS DATASETS

**Problema detectado**

El proyecto utiliza dos datasets independientes que contienen información complementaria sobre la actividad de vuelos y el perfil de los clientes.

**Análisis realizado**

Se identificó la columna común `loyalty_number` como clave de unión entre ambos datasets. El análisis de correspondencia confirmó que el 100% de las claves coinciden en ambos conjuntos.

**Acción aplicada**

Se realizó un `INNER JOIN`, integrando ambos datasets en un único DataFrame sin pérdida de información.

**Justificación**

La correspondencia completa garantiza que la unión no elimina registros válidos y permite consolidar toda la información en una única estructura.

---

## 2. NORMALIZACIÓN DE NOMBRES DE COLUMNAS

**Problema detectado**

Los nombres de las columnas presentaban espacios, mayúsculas.

**Acción aplicada**

Se normalizaron todos los nombres de columnas a formato `snake_case`, eliminando espacios y caracteres especiales.

**Justificación**

Esto mejora la legibilidad del código, facilita el mantenimiento y evita errores en el acceso a columnas.

---

## 3. ELIMINACIÓN DE FILAS DUPLICADAS

**Problema detectado**

Se detectaron registros completamente duplicados en el dataset.

**Acción aplicada**

Se eliminaron las filas duplicadas conservando la primera ocurrencia.

**Justificación**

Los registros duplicados no aportan información adicional y pueden introducir sesgos en el análisis.

---

## 4. CORRECCIÓN DE TIPOS DE DATOS

**Problema detectado**

Algunas variables presentaban tipos de datos que no eran adecuados según su naturaleza.

**Acción aplicada**

- Variables discretas con nulos (`cancellation_year`, `cancellation_month`) → convertidas a `Int64`
- Variables continuas (`distance`, `dollar_cost_points_redeemed`) → convertidas a `float64`
- Variables discretas sin nulos (`points_accumulated`) → convertidas a `int64`

**Justificación**

Garantiza la coherencia semántica de las variables y evita problemas en análisis posteriores.

---

## 5. TRATAMIENTO DE VALORES NEGATIVOS

**Problema detectado**

Se detectaron valores negativos en la variable `salary`, que representa el ingreso anual del cliente.

**Acción aplicada**

Los valores negativos fueron convertidos a valores nulos (`NaN`).

**Justificación**

Los valores negativos no son coherentes con la naturaleza de la variable y representan errores de calidad de datos.

---

## 6. TRATAMIENTO DE VALORES NULOS

Se identificaron dos casuísticas distintas:

### 6.1 Variable salary

**Problema detectado**

La variable presentaba valores nulos que representan información faltante.

**Acción aplicada**

Se imputaron los valores utilizando la mediana por grupos definidos por:

- education
- loyalty_card

Como fallback, se utilizó la mediana global.

**Justificación**

Este enfoque preserva la estructura socioeconómica del dataset y reduce el impacto de outliers.

---

### 6.2 Variables cancellation_year y cancellation_month

**Análisis realizado**

Los valores nulos representan clientes que no han cancelado su membresía.

**Acción aplicada**

No se realizó imputación.

**Justificación**

Estos valores nulos representan una condición válida, no un error de datos.

---

## 7. CREACIÓN DE LA VARIABLE customer_status

**Acción aplicada**

Se creó la variable `customer_status` para clasificar a los clientes como:

- Active
- Cancelled

**Justificación**

Facilita el análisis y segmentación de clientes según el estado de su membresía.

---

## 8. LIMPIEZA DE VARIABLES CATEGÓRICAS

**Acción aplicada**

Se aplicó un proceso de limpieza estandarizando el formato de las variables categóricas mediante:

- Eliminación de espacios
- Formato consistente de capitalización

**Justificación**

Garantiza la consistencia del dataset y previene inconsistencias en futuros datos.

---

## 9. VALIDACIÓN DE COHERENCIA LÓGICA

**Acción aplicada**

Se validaron las relaciones entre variables relacionadas con la actividad de vuelo.

**Justificación**

Garantiza la coherencia estructural del dataset y previene errores analíticos.

---

## RESULTADO FINAL

Tras el proceso de limpieza:

- El dataset presenta tipos de datos coherentes
- No contiene registros duplicados
- Los valores inválidos han sido corregidos
- Los valores faltantes han sido tratados adecuadamente
- Se garantiza la consistencia lógica y estructural del dataset

El dataset está preparado para su análisis.
