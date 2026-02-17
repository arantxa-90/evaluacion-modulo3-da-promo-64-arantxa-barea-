# Informe de Análisis Exploratorio de Datos (EDA)

## 1. Descripción general del dataset

El dataset contiene información sobre la actividad de vuelo y el programa de fidelización de clientes de una aerolínea.

Es importante destacar que:

- Cada fila representa la actividad de un cliente en un mes concreto.

Dimensiones del dataset:

- Número total de registros: 405,624
- Número total de variables: 25
- Número de clientes únicos: 16,737
- Periodo temporal: 2017–2018
- Registros duplicados: 1,864 (0.46%)

Esto implica que cada cliente tiene múltiples registros a lo largo del tiempo.

---

## 2. Evaluación de calidad de los datos

### 2.1 Valores nulos

Se detectaron valores nulos en las siguientes variables:

| Variable | % Nulos | Interpretación |
|--------|---------|----------------|
| Cancellation Year | 87.66% | Clientes que no han cancelado su membresía |
| Cancellation Month | 87.66% | Consistente con la variable anterior |
| Salary | 25.31% | Valores faltantes que requieren tratamiento |

No se detectaron valores nulos en variables categóricas.

Los valores nulos en las variables de cancelación no representan un error, sino que indican clientes activos.

---

### 2.2 Tipos de datos

Se identificaron variables con tipos de datos incorrectos:

- Cancellation Year tipada como float64 en lugar de entero nullable
- Cancellation Month tipada como float64 en lugar de entero nullable
- Points Accumulated tipada como float64 cuando representa valores enteros
- Distance tipada como int64 cuando representa una magnitud continua
- Dollar Cost Points Redeemed tipada como int64 cuando representa una magnitud monetaria

Estas variables requieren conversión de tipo en la fase de limpieza.

---

### 2.3 Registros duplicados

Se detectaron:

- 1,864 registros duplicados (0.46%)

Dado que el dataset es longitudinal, es necesario verificar si estos duplicados corresponden a errores o registros válidos repetidos.

---

## 3. Análisis de variables numéricas

### 3.1 Salary

Estadísticas principales:

- Media: 79,269
- Mediana: 73,479
- Desviación estándar: 34,992
- Rango: -58,486 a 407,228

🚩 Problema detectado:

Se identificaron valores negativos, lo cual es inconsistente desde el punto de vista lógico y sugiere errores en los datos.

Además, presenta:

- 25.31% de valores nulos
- Presencia de outliers a ambas colas de la distribución

---

### 3.2 Variables de cancelación

Las variables:

- Cancellation Year
- Cancellation Month

presentan aproximadamente un 88% de valores nulos.

Esto es consistente con el hecho de que la mayoría de clientes no han cancelado su membresía.

Por tanto, estos valores nulos representan una condición válida y no un problema de calidad de datos.

---

## 4. Variables categóricas

Las variables categóricas presentan una estructura consistente:

- Country: 1 categoría (Canada)
- Province: 11 categorías
- City: 29 categorías
- Postal Code: 55 categorías
- Gender: 2 categorías
- Education: 5 categorías
- Marital Status: 3 categorías
- Loyalty Card: 3 categorías
- Enrollment Type: 2 categorías

No se detectaron inconsistencias ni valores anómalos.

---

## 5. Análisis de outliers

Se detectaron valores atípicos en varias variables:

| Variable | % Outliers |
|--------|-------------|
| Flights Booked | 0.13% |
| Flights with Companions | 17.64% |
| Total Flights | 0.49% |
| Distance | 0.04% |
| Points Accumulated | 0.03% |
| Salary | 4.40% |
| CLV | 8.92% |

La mayoría de estos outliers representan comportamientos reales de clientes con alta actividad, no errores.

---

## 6. Conclusiones principales

### Problemas identificados

- Valores negativos en Salary
- Valores nulos en Salary (25%)
- Presencia de registros duplicados
- Tipado de algunas variables

### Situaciones esperadas

- Valores nulos en variables de cancelación corresponden a clientes activos
- Outliers coherentes con comportamiento real de clientes

### Calidad general

El dataset presenta una alta calidad estructural y es adecuado para análisis tras aplicar un proceso de limpieza moderado.

No se detectaron problemas críticos que comprometan la integridad del dataset.
