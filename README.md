# 📊 Data Science Portfolio - 5 Proyectos Avanzados

Bienvenido a mi repositorio central de Data Science con **5 proyectos profesionales y production-ready**. Aquí encontrarás desde análisis exploratorios hasta predicciones de series temporales con Machine Learning.

---

## 📁 Estructura del Repositorio

```
projects/
├── project1/                          # Análisis de Ventas E-Commerce
│   ├── data_analytics.ipynb           # Notebook con visualizaciones
│   ├── data.csv                       # Dataset (541,909 registros)
│   ├── README.md                      # Documentación
│   └── .gitignore
│
├── project2/                          # Consolidación y Reportes
│   ├── data_analytics2.ipynb          # Notebook de consolidación
│   ├── ventas_semana_*.csv            # Datasets fuente
│   ├── README.md                      # Documentación
│   └── .gitignore
│
├── project3/                          # Dashboard Streamlit Cloud Ready
│   ├── dashboard.py                   # App web interactivo
│   ├── test_dashboard.py              # Verificación automática
│   ├── data.csv                       # Dataset
│   ├── requirements.txt               # Dependencias
│   ├── .streamlit/config.toml         # Configuración
│   ├── README.md                      # Documentación
│   └── .gitignore
│
├── project4/                          # Segmentación RFM + ML
│   ├── rfm_segmentation.ipynb         # SQL + K-Means clustering
│   ├── ecommerce.db                   # Base de datos SQLite
│   ├── clientes_segmentados.csv       # Resultados
│   ├── README.md                      # Documentación
│   └── .gitignore
│
└── project5/                          # Pronóstico de Ventas
    ├── sales_forecasting.ipynb        # Prophet time series
    ├── pronóstico_general.png         # Gráficos
    ├── componentes_pronóstico.png
    ├── README.md                      # Documentación
    └── .gitignore
```

---

## 🚀 Los 5 Proyectos

### 1️⃣ Project 1: Análisis de Ventas E-Commerce 📊

**Tecnologías:** Python, Pandas, Matplotlib, Seaborn  
**Tipo:** Notebook Jupyter  

Análisis profesional de datos de e-commerce con **3 gráficos interactivos** que incluyen valores, porcentajes y análisis estadísticos.

**Características:**
- ✅ Top 10 países y productos
- ✅ Evolución temporal de ventas
- ✅ 400+ líneas de código comentado
- ✅ Production-ready para LinkedIn

**Cómo usar:**
```bash
cd projects/project1
jupyter notebook data_analytics.ipynb
```

---

### 2️⃣ Project 2: Consolidación y Reportes 📈

**Tecnologías:** Python, Pandas, OpenPyXL  
**Tipo:** Notebook Jupyter  

Sistema automatizado para cargar, consolidar y generar reportes desde **múltiples archivos CSV** hacia Excel profesional.

**Características:**
- ✅ Carga automática de archivos con glob patterns
- ✅ Consolidación inteligente de 541,909 registros
- ✅ Generación de Excel con 2 sheets
- ✅ 200+ líneas de código comentado

**Cómo usar:**
```bash
cd projects/project2
jupyter notebook data_analytics2.ipynb
```

---

### 3️⃣ Project 3: Dashboard Streamlit Cloud Ready 🎯

**Tecnologías:** Python, Streamlit, Plotly, Pandas  
**Tipo:** Aplicación Web Interactiva  

Dashboard profesional **production-ready para Streamlit Community Cloud** con 5 gráficos interactivos, 7 KPIs y 3 filtros dinámicos.

**Características:**
- ✅ 5 gráficos Plotly interactivos
- ✅ 7 KPIs en tiempo real
- ✅ 3 filtros dinámicos (País, Fechas, Cantidad)
- ✅ Exportación a CSV y Excel
- ✅ 541,909 registros sin lag
- ✅ Cache optimizado
- ✅ 600+ líneas de código comentado

**Cómo usar:**
```bash
cd projects/project3
source ../../venv/bin/activate
streamlit run dashboard.py
```

**URL en vivo:** https://share.streamlit.io (deploy aquí cuando esté listo)

---

### 4️⃣ Project 4: Segmentación RFM + Machine Learning 💪

**Tecnologías:** Python, SQL, SQLite, Pandas, Scikit-Learn  
**Tipo:** Notebook Jupyter con Database  

Segmentación avanzada de clientes usando **RFM (Recencia, Frecuencia, Monetario)** + **K-Means clustering** para agrupar en 4 segmentos accionables.

**Características:**
- ✅ Creación de base de datos SQLite
- ✅ Consultas SQL para cálculo de métricas RFM
- ✅ Preprocesamiento con StandardScaler + log transform
- ✅ K-Means clustering con 4 segmentos
- ✅ Análisis de componentes
- ✅ Recomendaciones de negocio por segmento
- ✅ 600+ líneas de código comentado

**Segmentos Identificados:**
- 🏆 **Campeones**: Alta frecuencia, alto monetario, baja recencia
- ⚠️ **En Riesgo**: Alta recencia, bajo monetario, baja frecuencia
- 💪 **Leales**: Métricas consistentes mid-to-high
- 🆕 **Nuevos**: Baja recencia, baja frecuencia, bajo monetario

**Cómo usar:**
```bash
cd projects/project4
jupyter notebook rfm_segmentation.ipynb
```

---

### 5️⃣ Project 5: Pronóstico de Ventas con Prophet 📈

**Tecnologías:** Python, Prophet, Pandas, Matplotlib  
**Tipo:** Notebook Jupyter + Time Series  

Predicción avanzada de **ventas para los próximos 90 días** usando Prophet de Meta, con detección automática de tendencias y estacionalidad.

**Características:**
- ✅ Agregación temporal con resample (diario, semanal, mensual)
- ✅ Entrenamiento de modelo Prophet
- ✅ Pronóstico 90 días con intervalos de confianza
- ✅ Análisis de componentes:
  - Tendencia (crecimiento/decrecimiento)
  - Estacionalidad semanal (patrones por día)
  - Estacionalidad anual (patrones por mes)
- ✅ Exportación de resultados para stakeholders
- ✅ 600+ líneas de código comentado

**Salidas Generadas:**
- `pronóstico_general.png`: Gráfico histórico + futuro
- `componentes_pronóstico.png`: Análisis de componentes
- `pronóstico_90_días.csv`: Predicciones en formato CSV
- `resumen_pronóstico.txt`: Reporte ejecutivo

**Cómo usar:**
```bash
cd projects/project5
jupyter notebook sales_forecasting.ipynb
```

---

## 🛠️ Configuración Inicial

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Fabian1808/Projects.git
cd Projects
```

### 2. Activar Entorno Virtual
```bash
source venv/bin/activate
```

### 3. Instalar Dependencias Principales
```bash
# Básicas (para proyecto 1 y 2)
pip install pandas jupyter matplotlib seaborn

# Streamlit (para proyecto 3)
pip install streamlit plotly openpyxl

# Machine Learning (para proyecto 4)
pip install scikit-learn

# Time Series (para proyecto 5)
pip install prophet
```

O instalar todo de una vez:
```bash
pip install pandas jupyter matplotlib seaborn streamlit plotly openpyxl scikit-learn prophet
```

---

## 📊 Estadísticas del Portfolio

| Métrica | Valor |
|---------|-------|
| **Proyectos** | 5 |
| **Líneas de Código** | 2,500+ |
| **Notebooks** | 4 |
| **Gráficos** | 20+ |
| **Registros Procesados** | 541,909+ |
| **Modelos ML** | 2 (K-Means, Prophet) |
| **Bases de Datos** | SQLite |
| **KPIs** | 7+ |

---

## 🎓 Habilidades Demostradas

### Data Processing & Analysis
- ✅ Limpieza y validación de datos
- ✅ Aggregación temporal (resample)
- ✅ Consolidación de múltiples fuentes
- ✅ Consultas SQL

### Machine Learning
- ✅ Clustering con K-Means
- ✅ Time Series Forecasting con Prophet
- ✅ Preprocesamiento (StandardScaler, log transform)
- ✅ Evaluación de modelos (Silhouette Score)

### Visualization
- ✅ Matplotlib (gráficos estáticos)
- ✅ Plotly (gráficos interactivos)
- ✅ Streamlit (dashboards web)

### Software Engineering
- ✅ Código limpio y comentado
- ✅ Git workflow profesional
- ✅ Documentation en Markdown
- ✅ Export de modelos para producción

---

## 🚀 Crear Nuevo Proyecto

Para crear un nuevo proyecto manteniendo la estructura:

```bash
bash create_project.sh project6 "Descripción del proyecto"
cd projects/project6
jupyter notebook notebook.ipynb
```

---

## 🔒 Seguridad

- ✅ `.env` protegido en `.gitignore`
- ✅ `__pycache__` y `.ipynb_checkpoints` ignorados
- ✅ Variables de entorno locales
- ✅ Secretos de Streamlit no commiteados

---

## 📚 Recursos Útiles

- [Prophet Documentation](https://facebook.github.io/prophet/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Docs](https://scikit-learn.org/stable/)
- [Plotly Docs](https://plotly.com/python/)

---

## 📞 Contacto

- **GitHub:** [Fabian1808](https://github.com/Fabian1808)
- **LinkedIn:** [Fabian Urteaga](https://linkedin.com/in/fabian-urteaga)
- **Repositorio:** [github.com/Fabian1808/Projects](https://github.com/Fabian1808/Projects)

---

## 📝 Changelog

### v1.0 - 12 de Noviembre de 2025
- ✅ Project 1: Sales Analytics con Matplotlib
- ✅ Project 2: Data Consolidation con Pandas
- ✅ Project 3: Interactive Dashboard con Streamlit
- ✅ Project 4: Customer Segmentation con SQL + K-Means
- ✅ Project 5: Sales Forecasting con Prophet

---

**Estado:** 🟢 Activo  
**Última actualización:** 12 de noviembre de 2025  
**Autor:** Fabian Urteaga  
**Versión:** 1.0
