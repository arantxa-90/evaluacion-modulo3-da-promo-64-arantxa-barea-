# ✈️ Customer Loyalty Program Analysis

Análisis del comportamiento de clientes de un programa de fidelización de aerolínea, cubriendo exploración, limpieza, análisis estadístico y visualización de datos.

---

## 📌 Descripción del proyecto

El proyecto integra dos datasets con información complementaria sobre los clientes de un programa de fidelización:

- **Customer Flight Activity**: actividad de vuelos (vuelos reservados, distancia, puntos acumulados y redimidos, entre otros)
- **Customer Loyalty History**: perfil demográfico y estado dentro del programa (ubicación, educación, salario, tipo de tarjeta, fechas de inscripción y cancelación)

El objetivo es comprender el perfil de los clientes, su comportamiento de vuelo y su relación con el programa de fidelización, generando insights relevantes desde una perspectiva analítica y de negocio.

---

## 🎯 Fases del proyecto

### Fase 1 — Exploración de datos (EDA)
- Comprensión de la estructura del dataset
- Identificación de valores nulos
- Análisis de distribuciones y principales estadísticos 
- Validación de la calidad de los datos.

### Fase 2 — Limpieza y transformación
- Integración de datasets mediante unión automática basada en la clave común (`loyalty_number`)
- Normalización de columnas a `snake_case`
- Eliminación de registros duplicados
- Corrección de tipos de datos
- Tratamiento de valores negativos
- Tratamiento de valores nulos
- Creación de la variable `customer_status` 
- Homogeneización de los valores de variables categóricas
- Validación de coherencia lógica.

### Fase 3 — Análisis estadístico
- Estadísticas descriptivas por variables numéricas y categóricas
- Detección de outliers 
- Análisis de correlaciones de variables numéricas.

### Fase 4 — Visualización
- Análisis temporal de vuelos
- Relación distancia–puntos acumulados
- Distribución geográfica por provincia
- Salario promedio por nivel educativo
- Proporción por tipo de tarjeta de fidelización 
- Perfil demográfico por género y estado civil.

---

## 📂 Estructura del repositorio

```
├── data/
│   ├── raw/
│   │   ├── Customer Flight Activity.csv
│   │   └── Customer Loyalty History.csv
│   └── processed/
│       └── customer_loyalty_clean.csv
│
├── notebooks/
│   ├── 00_eda.ipynb               # Exploración inicial
│   ├── 01_data_cleaning.ipynb     # Limpieza y transformación
│   └── 02_data_analysis.ipynb     # Análisis estadístico y visualización
│
├── src/
│   ├── data_cleaning.py           # Pipeline de limpieza automatizado
│   └── main.py                    # Script de ejecución principal
│
├── reports/
│   ├── figures/
│   │   ├── 00_eda/
│   │   └── 01_data_analysis/
│   └── 01_eda_summary.md
│
├── docs/
│   └── data_cleaning_decisions.md # Decisiones y justificaciones de limpieza
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline de limpieza automatizado

El pipeline en `src/data_cleaning.py` automatiza todo el proceso de limpieza:

1. Carga e integración automática de los datasets mediante la clave común (`loyalty_number`)
2. Normalización de nombres de columnas a `snake_case`
3. Eliminación de duplicados
4. Corrección de tipos de datos
5. Conversión de salarios negativos a `NaN`
6. Imputación de `salary` con mediana por grupos (`education` + `loyalty_card`)
7. Creación de la variable `customer_status` (Active / Cancelled)
8. Estandarización de variables categóricas
9. Validación de coherencia lógica entre variables del dataset
10. Exportación del dataset limpio a `data/processed/customer_loyalty_clean.csv`

---

## ▶️ Cómo ejecutar el pipeline

Desde la raíz del proyecto:

```bash
cd src
python main.py
```

Esto ejecutará el proceso completo de limpieza y generará el dataset limpio en `data/processed/`.

---

## 📊 Principales insights

Algunos hallazgos relevantes incluyen:

- **Perfil geográfico:** alta concentración en Ontario (32,3%), British Columbia (26,4%) y Quebec (19,7%)
- **Perfil demográfico:** distribución equilibrada por género (~50/50) y predominio de clientes casados (~58%)
- **Programa de fidelización:** predominio de niveles no Premium (Star, Nova), con un 20% en el segmento Premium Aurora; base mayoritariamente activa (~88%)
- **Comportamiento de vuelo:** relación lineal clara entre distancia volada y puntos acumulados; patrón estacional con mayor actividad en verano
- **Segmentación económica:** diferencias salariales relevantes según nivel educativo

Todas las gráficas y visualizaciones generadas están disponibles en: `reports/figures/`

---

## 🛠️ Tecnologías utilizadas

Python · Pandas · NumPy · Matplotlib · Seaborn · Regex

---

## 📦 Instalación

Clonar el repositorio:

```bash
git clone https://github.com/arantxa-90/evaluacion-modulo3-da-promo-64-arantxa-barea.git
cd evaluacion-modulo3-da-promo-64-arantxa-barea
```
Instalar dependencias:

```bash
pip install -r requirements.txt
```
Opcional: usar entorno virtual (recomendado):

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

# Instalar dependencias dentro del entorno
pip install -r requirements.txt
```

---

## 🎓 Contexto

Proyecto desarrollado como evaluación final del Módulo 3 de Data Analytics, aplicando buenas prácticas de limpieza de datos, análisis estadístico, visualización y reproducibilidad mediante pipeline automatizado.

---

**Arantxa Barea** | [🔗 LinkedIn](https://www.linkedin.com/in/arantxa-barea/) 