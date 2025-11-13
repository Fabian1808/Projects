# 📊 Project 4: Segmentación de Clientes RFM con SQL y Machine Learning

> **Estado:** ✅ COMPLETADO
> 
> Análisis avanzado de segmentación de clientes usando RFM (Recencia, Frecuencia, Monetario) y K-Means clustering

---

## 🎯 Objetivo del Proyecto

Segmentar la base de clientes de un e-commerce en **4 grupos accionables** basado en su comportamiento de compra, usando:
- **SQL**: Para extraer y calcular métricas
- **Machine Learning**: Algoritmo K-Means para clustering automático
- **Business Intelligence**: Interpretación y recomendaciones

### ¿Por qué es importante?
No todos los clientes son iguales. Algunos compran frecuentemente, otros hace mucho tiempo no compran. Con RFM podemos identificar:
- 🏆 **Clientes Campeones**: Los mejores, compran frecuentemente y reciente
- ⚠️ **Clientes en Riesgo**: Que no compran desde hace tiempo
- 💪 **Clientes Leales**: Compradores consistentes
- 🆕 **Clientes Nuevos**: Nuevas adquisiciones

---

## 📚 Conceptos Clave Aprendidos

### 1. **SQL & Bases de Datos**
- Crear bases de datos SQLite desde Python
- Escribir consultas SQL (`SELECT`, `GROUP BY`, agregaciones)
- Conectar Python a BD y ejecutar queries con pandas

### 2. **Machine Learning**
- **Transformación de datos**: Log transform para normalizar distribuciones
- **Estandarización**: StandardScaler para poner características en la misma escala
- **K-Means Clustering**: Algoritmo no supervisado para agrupar clientes
- **Evaluación**: Silhouette Score para medir calidad del clustering

### 3. **Métricas RFM**
- **Recencia (R)**: Días desde la última compra (menor = mejor)
- **Frecuencia (F)**: Número de compras (mayor = mejor)
- **Monetario (M)**: Valor total gastado (mayor = mejor)

---

## 📁 Estructura del Proyecto

```
project4/
├── rfm_segmentation.ipynb          # Notebook principal (análisis completo)
├── ecommerce.db                    # Base de datos SQLite generada
├── clientes_segmentados.csv        # Clientes con sus segmentos
├── resumen_segmentos.csv           # Estadísticas por segmento
├── kmeans_model.pkl                # Modelo K-Means entrenado
├── README.md                       # Este archivo
└── .gitignore                      # Archivos a ignorar en Git
```

---

## 🚀 Cómo Usar Este Proyecto

### 1. Activar Entorno Virtual
```bash
cd ../..
source venv/bin/activate
```

### 2. Instalar Dependencias
```bash
pip install scikit-learn
```

### 3. Ejecutar el Notebook
```bash
cd projects/project4
jupyter notebook rfm_segmentation.ipynb
```

### 4. Ejecutar Celdas en Orden
- **Celda 1-3**: Cargar datos y limpiar
- **Celda 4**: Crear base de datos SQLite
- **Celda 5-6**: Consultas SQL y cálculo de RFM
- **Celda 7**: Preprocesar para Machine Learning
- **Celda 8**: Entrenar K-Means
- **Celda 9-10**: Analizar e interpretar segmentos
- **Celda 11**: Visualizar resultados
- **Celda 12-13**: Recomendaciones de negocio y exportar

---

## � Resultados Esperados

### Segmentos Identificados

| Segmento | Descripción | Clientes | Acción Clave |
|----------|-------------|----------|--------------|
| 🏆 Campeones | Compran frecuente y recientemente | ~25-30% | Programa VIP |
| ⚠️ En Riesgo | No compran hace tiempo | ~15-20% | Campaña reactivación |
| 💪 Leales | Compras consistentes | ~30-35% | Aumentar valor |
| 🆕 Nuevos | Clientes recientes | ~15-20% | Convertir en recurrentes |

### Archivos Generados
1. **ecommerce.db**: Base de datos SQLite con tabla `transacciones`
2. **clientes_segmentados.csv**: Todos los clientes con su segmento asignado
3. **resumen_segmentos.csv**: Estadísticas agregadas por segmento
4. **kmeans_model.pkl**: Modelo entrenado para clasificar nuevos clientes

---

## 💡 Recomendaciones de Negocio

### Para Campeones 🏆
- ✅ Crear programa VIP exclusivo
- ✅ Acceso anticipado a productos nuevos
- ✅ Soporte premium y atención personalizada
- ✅ Recompensas por lealtad (puntos, regalos)

### Para En Riesgo ⚠️
- ✅ Campaña "Te extrañamos" con descuento
- ✅ Email marketing personalizado
- ✅ Ofertas de reactivación con urgencia
- ✅ Encuesta de satisfacción

### Para Leales 💪
- ✅ Programa de puntos acumulables
- ✅ Compras cruzadas (cross-sell)
- ✅ Productos premium (upsell)
- ✅ Comunidad de clientes con beneficios

### Para Nuevos 🆕
- ✅ Bienvenida personalizada
- ✅ Cupón para segunda compra
- ✅ Tutorial de uso de plataforma
- ✅ Emails educativos sobre productos

---

## � Tecnologías Usadas

```python
# Base de datos
import sqlite3

# Data Science
import pandas as pd
import numpy as np

# Machine Learning
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 📈 Métricas del Proyecto

- **Clientes analizados**: 541,909+ transacciones
- **Clientes únicos**: ~4,372
- **Período de datos**: Enero 2010 - Diciembre 2011
- **Silhouette Score**: 0.35-0.45 (calidad del clustering)
- **Clusters**: 4 segmentos

---

## 🎓 Aprendizajes Clave

### Pipeline Completo
```
Datos CSV → Base de Datos SQL → Consultas SQL → Análisis Pandas → 
Preprocesamiento ML → Algoritmo K-Means → Interpretación → Recomendaciones
```

### Diferencia con Proyectos Anteriores
- ✅ **Project 1**: Visualizaciones estáticas
- ✅ **Project 2**: Consolidación de datos
- ✅ **Project 3**: Dashboard interactivo
- ✅ **Project 4**: Análisis predictivo y Machine Learning

---

## 🔐 Archivos Generados

### ecommerce.db
Base de datos SQLite con:
- Tabla: `transacciones`
- Registros: 541,909
- Columnas: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country, TotalPrice

### clientes_segmentados.csv
Estructura:
```
CustomerID, Recencia, Frecuencia, Monetario, Segmento, NombreSegmento
```

### kmeans_model.pkl
Pickle file que contiene:
- Modelo K-Means entrenado
- StandardScaler ajustado
- Listos para usar en nuevos datos

---

## 🚀 Próximos Pasos

1. **Publicar en GitHub**: Subir este proyecto al repositorio central
2. **Compartir en LinkedIn**: Post sobre segmentación RFM
3. **Implementar en BD Real**: Usar con datos de producción
4. **Automatizar**: Crear pipeline de actualización mensual
5. **Ampliar**: Agregar más segmentos o metricas adicionales

---

## 📞 Contacto & Links

- **GitHub**: [Fabian1808/Projects](https://github.com/Fabian1808/Projects)
- **LinkedIn**: [Fabian Urteaga](https://linkedin.com/in/tu-linkedin)
- **Dataset Original**: Project 1 (data.csv)

---

## ✨ Habilidades Demostradas

- ✅ SQL para análisis de datos
- ✅ Python para ciencia de datos
- ✅ Machine Learning (K-Means)
- ✅ Business Intelligence
- ✅ Interpretación de resultados
- ✅ Recomendaciones accionables
- ✅ Visualización de datos

---

**Creado**: 10 de noviembre de 2025  
**Autor**: Fabian Urteaga  
**Versión**: 1.0 ✅ COMPLETADO
