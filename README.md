# 📊 Data Science Projects Hub

Bienvenido a mi espacio de proyectos de Data Science. Esta carpeta contiene múltiples proyectos independientes, cada uno con su propio repositorio de GitHub y documentación.

# � Data Science Portfolio - Multi-Project Repository

Bienvenido a mi repositorio central de Data Science con múltiples proyectos. Aquí encontrarás análisis de datos profesionales, dashboards interactivos y notebooks de exploración.

## 📁 Estructura del Repositorio

```
data-science-portfolio/
│
├── projects/                          # Carpeta con todos los proyectos
│   │
│   ├── project1/                      # Análisis de Ventas E-Commerce
│   │   ├── data_analytics.ipynb       # Notebook con análisis y visualizaciones
│   │   ├── data.csv                   # Dataset de ventas
│   │   ├── README.md                  # Documentación específica
│   │   └── .gitignore
│   │
│   ├── project2/                      # Consolidación y Reportes de Datos
│   │   ├── data_analytics2.ipynb      # Notebook de consolidación
│   │   ├── ventas_semana_*.csv        # Datasets semanales
│   │   ├── README.md                  # Documentación específica
│   │   └── .gitignore
│   │
│   ├── project3/                      # Dashboard Streamlit Cloud Ready
│   │   ├── dashboard.py               # Aplicación Streamlit
│   │   ├── data.csv                   # Dataset de 541k registros
│   │   ├── requirements.txt           # Dependencias
│   │   ├── test_dashboard.py          # Script de verificación
│   │   ├── README.md                  # Documentación específica
│   │   ├── DEPLOY_GUIA.sh             # Guía de deployment
│   │   ├── .streamlit/config.toml     # Configuración Streamlit
│   │   └── .gitignore
│   │
│   └── project4/                      # Próximos proyectos...
│       └── (estructura similar)
│
├── venv/                              # Entorno virtual Python (shared)
├── .env                               # Variables de entorno (PROTEGIDO)
├── .gitignore                         # Configuración global de Git
├── create_project.sh                  # Script para crear nuevos proyectos
└── README.md                          # Este archivo
```

## 🚀 Proyectos Disponibles

### 📊 Project 1: Análisis de Ventas E-Commerce
**Tipo:** Notebook Jupyter  
**Tecnologías:** Python, Pandas, Matplotlib, Seaborn  
**Descripción:** Análisis profesional de datos de ventas e-commerce con visualizaciones interactivas, valores, porcentajes y análisis estadísticos.

**Características:**
- ✅ 3 gráficos principales con labels y porcentajes
- ✅ 400+ líneas de código comentado en español
- ✅ Análisis estadísticos avanzados
- ✅ Publicado en GitHub para LinkedIn

**Cómo usar:**
```bash
cd projects/project1
jupyter notebook data_analytics.ipynb
```

---

### 📈 Project 2: Consolidación y Reportes de Datos
**Tipo:** Notebook Jupyter  
**Tecnologías:** Python, Pandas, OpenPyXL, Excel  
**Descripción:** Sistema automatizado para cargar, consolidar y generar reportes desde múltiples archivos CSV.

**Características:**
- ✅ Carga automática de archivos CSV
- ✅ Consolidación inteligente de datos
- ✅ Generación de reportes Excel profesionales
- ✅ 200+ líneas de código comentado

**Cómo usar:**
```bash
cd projects/project2
jupyter notebook data_analytics2.ipynb
```

---

### 🎯 Project 3: Dashboard Streamlit Cloud Ready
**Tipo:** Aplicación Web (Streamlit)  
**Tecnologías:** Python, Streamlit, Plotly, Pandas  
**Descripción:** Dashboard profesional interactivo listo para Streamlit Community Cloud con URL pública.

**Características:**
- ✅ 5 gráficos interactivos con Plotly
- ✅ 7 KPIs en tiempo real
- ✅ 3 filtros dinámicos (País, Fechas, Cantidad)
- ✅ Exportación a CSV y Excel
- ✅ 541,909 registros sin lag
- ✅ Production-ready para cloud

**Cómo usar:**
```bash
cd projects/project3
source ../../venv/bin/activate
streamlit run dashboard.py
```

---

## 🛠️ Configuración del Entorno

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Fabian1808/data-science-portfolio.git
cd data-science-portfolio
```

### 2. Activar Entorno Virtual
```bash
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
# Para todos los proyectos
pip install pandas jupyter matplotlib seaborn plotly streamlit openpyxl
```

---

## 🚀 Crear Nuevos Proyectos

Para crear un nuevo proyecto manteniendo la estructura:

```bash
bash create_project.sh project4 "Descripción del proyecto"
```

Esto creará automáticamente la estructura dentro de `projects/project4/`

---

## 📊 Estadísticas

| Métrica | Valor |
|---------|-------|
| **Proyectos** | 3+ |
| **Líneas Código** | 1,200+ |
| **Gráficos** | 15+ |
| **Registros Procesados** | 541,909+ |
| **KPIs** | 7+ |

---

## 🔒 Seguridad

- ✅ `.env` protegido (nunca se sube a GitHub)
- ✅ `__pycache__` ignorado
- ✅ Variables de entorno locales

---

**Última actualización:** 10 Nov 2025  
**Autor:** [Fabian Urteaga](https://github.com/Fabian1808)

## 🚀 Proyectos

### 1. Project 1: Análisis de Ventas E-commerce 📊
**Descripción:** Análisis completo de datos de ventas con visualizaciones profesionales

**Características:**
- Top 10 países por volumen de ventas
- Top 10 productos más vendidos
- Evolución temporal de ventas
- Gráficos con valores y porcentajes

**GitHub:** [Fabian1808/Project1](https://github.com/Fabian1808/Project1)

**Tecnologías:** Python, Pandas, Matplotlib, Jupyter

---

### 2. Project 2: [Descripción pendiente]
**Estado:** En desarrollo

---

## 📋 Requisitos Generales

```bash
# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install pandas matplotlib seaborn jupyter notebook
```

## 🔒 Manejo de Variables de Entorno

El archivo `.env` en la raíz contiene configuraciones compartidas y **NUNCA debe ser commiteado a GitHub**.

Cada proyecto individual puede tener su propio `.env` si es necesario.

## 📝 Notas Importantes

- ✅ Cada proyecto tiene su **propio repositorio Git independiente**
- ✅ El archivo `.env` principal está protegido por `.gitignore`
- ✅ Los proyectos pueden compartir el entorno virtual `venv/`
- ✅ Documentación completa en cada carpeta de proyecto

## 💡 Para Crear un Nuevo Proyecto

1. Crear carpeta: `mkdir project3`
2. Crear notebook: `touch project3/notebook.ipynb`
3. Inicializar Git: `cd project3 && git init`
4. Crear README con documentación
5. Hacer primer commit
6. Crear repositorio en GitHub y conectar

```bash
cd project3
git remote add origin https://github.com/Fabian1808/Project3.git
git push -u origin main
```

---

**Última actualización:** 10 de noviembre de 2025

**Autor:** Fabian

Puedes encontrar todos mis proyectos en: [GitHub](https://github.com/Fabian1808)
