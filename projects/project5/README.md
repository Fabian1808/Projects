# � Project 5: Pronóstico de Ventas con Prophet

> **Estado:** ✅ COMPLETADO
> 
> Análisis avanzado de pronóstico de series temporales para predecir ventas futuras

---

## 🎯 Objetivo del Proyecto

Responder la pregunta más importante de cualquier negocio: **¿Cuánto vamos a vender el próximo trimestre?**

Usando **Prophet**, una librería de Meta diseñada específicamente para pronósticos de series de tiempo, construiremos un modelo que predice los ingresos diarios de los próximos **90 días** con intervalos de confianza.

### ¿Por Qué Prophet?
- ✅ Detecta automáticamente tendencias
- ✅ Identifica patrones semanales (qué día vende más)
- ✅ Identifica patrones anuales (qué mes tiene picos)
- ✅ Genera intervalos de confianza (mejora y peor escenario)
- ✅ Extremadamente rápido y preciso
- ✅ Desarrollado por Meta (Facebook) en producción

---

## 📚 Conceptos Clave Aprendidos

### 1. **Time Series Analysis (Series Temporales)**
- Estructura especial de datos con dimensión temporal
- Dependencias secuenciales (hoy afecta mañana)
- Agregación temporal con `resample()`

### 2. **Prophet & Forecast**
- Algoritmo bayesiano para pronósticos
- Descomposición de series en componentes
- Manejo automático de estacionalidad
- Generación de intervalos de confianza

### 3. **Componentes del Modelo**
- **Trend (Tendencia)**: Dirección general a lo largo del tiempo
- **Yearly (Estacionalidad Anual)**: Patrones que se repiten año tras año
- **Weekly (Estacionalidad Semanal)**: Patrones que se repiten cada semana

### 4. **Interpretación Empresarial**
- ¿Crece o decrece el negocio?
- ¿Qué día de la semana vende más?
- ¿Qué mes del año tiene picos de venta?
- ¿Cuál es el rango de incertidumbre en las predicciones?

---

## 📁 Estructura del Proyecto

```
project5/
├── sales_forecasting.ipynb         # Notebook principal (análisis completo)
├── pronóstico_general.png          # Gráfico: histórico + pronóstico futuro
├── componentes_pronóstico.png      # Gráfico: trend, yearly, weekly
├── pronóstico_completo.csv         # CSV con todas las predicciones
├── pronóstico_90_días.csv          # CSV solo con los 90 días futuros
├── modelo_prophet.pkl              # Modelo entrenado para reutilizar
├── resumen_pronóstico.txt          # Resumen ejecutivo de resultados
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
pip install prophet
```

### 3. Ejecutar el Notebook
```bash
cd projects/project5
jupyter notebook sales_forecasting.ipynb
```

### 4. Secciones del Notebook

| Paso | Sección | Descripción |
|------|---------|-------------|
| 1 | Setup & Imports | Configurar librerías y entorno |
| 2 | Load & Explore | Cargar datos del Proyecto 1 |
| 3 | Data Cleaning | Limpieza y validación de datos |
| 4 | Resample | Agregar ventas por día |
| 5 | Format for Prophet | Preparar formato específico |
| 6 | Train Model | Entrenar modelo Prophet |
| 7 | Create Forecast | Generar pronóstico 90 días |
| 8 | Analyze Forecast | Examinar resultados |
| 9 | Plot General | Visualizar pronóstico general |
| 10 | Plot Components | Visualizar componentes (MÁS IMPORTANTE) |
| 11 | Interpret Components | Análisis profundo de patrones |
| 12 | Export Results | Guardar archivos para stakeholders |
| 13 | Summary | Conclusiones y próximos pasos |

---

## 📊 Resultados Esperados

### Pronóstico de 90 Días
```
Período predicho: [Fecha inicio] a [Fecha fin]
Ingresos totales estimados: $XXX,XXX.XX
Rango de confianza (95%):
  - Escenario optimista: $XXX,XXX.XX
  - Escenario pesimista: $XXX,XXX.XX
Promedio diario: $XXX.XX
```

### Análisis de Componentes
1. **Tendencia**: ¿Crece o decrece? ¿En qué porcentaje?
2. **Patrones Semanales**: ¿Qué días son mejores/peores?
3. **Patrones Anuales**: ¿Qué meses tienen picos?

---

## 💡 Insights de Negocio

### Ejemplo de Análisis Semanal
```
Lunes:     +15% vs promedio → Día fuerte
Martes:    +12% vs promedio → Día fuerte
Miércoles: +8% vs promedio  → Día normal
Jueves:    +10% vs promedio → Día normal
Viernes:   -5% vs promedio  → Día débil
Sábado:    -20% vs promedio → Día muy débil
Domingo:   -18% vs promedio → Día muy débil
```

**Acción**: Ejecutar campañas de marketing en viernes/fin de semana para compensar la caída

### Ejemplo de Análisis Anual
```
Noviembre: +35% vs promedio → PICO DE VENTAS
Diciembre: +40% vs promedio → PICO MÁS ALTO
Enero:     -25% vs promedio → Caída post-navidad
Febrero:   -20% vs promedio → Caída continua
```

**Acción**: Preparar inventario con 3 meses de anticipación para noviembre/diciembre

---

## 🔧 Tecnologías Usadas

```python
# Time Series & Forecasting
from prophet import Prophet

# Data Processing
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
```

### Versiones Recomendadas
```
prophet >= 1.2.0
pandas >= 2.0.0
numpy >= 1.20.0
matplotlib >= 3.0.0
seaborn >= 0.11.0
```

---

## � Pipeline Completo

```
Datos CSV
   ↓
Limpieza (validación de calidad)
   ↓
Agregación Diaria (resample)
   ↓
Formato Prophet (ds, y)
   ↓
Entrenamiento (fit model)
   ↓
Pronóstico 90 días (predict)
   ↓
Análisis de Componentes
   ↓
Visualización + Exportación
   ↓
Recomendaciones Estratégicas
```

---

## 🎓 Diferencia con Proyectos Anteriores

| Proyecto | Tipo | Técnica |
|----------|------|---------|
| Proyecto 1 | Análisis | Visualización estática |
| Proyecto 2 | Automatización | Consolidación de datos |
| Proyecto 3 | BI Interactivo | Dashboard en web |
| Proyecto 4 | Machine Learning | Clustering (K-Means) |
| **Proyecto 5** | **Predicción** | **Time Series (Prophet)** |

**Proyecto 5** es el único que **predice el futuro** basado en patrones históricos.

---

## 📊 Gráficos Generados

### 1. Pronóstico General (`pronóstico_general.png`)
Muestra:
- **Puntos negros**: Datos históricos reales
- **Línea azul**: Pronóstico principal
- **Área azul clara**: Intervalo de confianza (95%)
- **Línea roja punteada**: Límite entre histórico y futuro

### 2. Componentes (`componentes_pronóstico.png`)
Muestra 3 sub-gráficos:
1. **Trend**: La tendencia general (crecimiento/decrecimiento)
2. **Yearly**: Variación por mes del año
3. **Weekly**: Variación por día de la semana

---

## 🔐 Archivos Generados

### pronóstico_completo.csv
Estructura:
```
Fecha, Predicción, Límite_Inferior_95%, Límite_Superior_95%, Tendencia, Estacionalidad_Anual, Estacionalidad_Semanal
```

### pronóstico_90_días.csv
Solo los 90 días futuros (simplificado para stakeholders)

### modelo_prophet.pkl
Archivo pickle con el modelo entrenado:
- Puede usarse para hacer predicciones en nuevas fechas
- Reutilizable sin reentrenamiento
- Incluye todos los parámetros ajustados

### resumen_pronóstico.txt
Documento ejecutivo con:
- Estimaciones de ingresos
- Patrones identificados
- Recomendaciones estratégicas
- Listo para presentar a gerencia

---

## � Caso de Uso Real

**Escenario**: Startup de e-commerce con crecimiento variable

**Problema**: "¿Cuánto inventario debe comprar para el próximo trimestre?"

**Solución con Prophet**:
1. Entrenar modelo con histórico de 24 meses
2. Generar pronóstico de 90 días
3. Identificar que noviembre tiene +35% de ventas
4. Alertar que fin de semana baja 20%
5. Recomendar comprar 35% más inventario para noviembre
6. Ajustar marketing para fin de semana

**Resultado**: Reducir stockouts en picos y excess inventory en valles

---

## � Próximos Pasos

### Para Consolidar Aprendizaje
1. ✅ Ejecutar notebook completamente
2. ✅ Analizar los gráficos de componentes
3. ✅ Escribir interpretación de patrones encontrados
4. ✅ Exportar archivos CSV para stakeholders

### Para Llevar a Producción
1. Reentrenar modelo mensualmente con nuevos datos
2. Comparar pronósticos vs actuals para medir precisión
3. Crear dashboard para monitoreo automático
4. Implementar alertas si las ventas se desvían del pronóstico

### Para Expandir el Proyecto
1. Agregar análisis por categoría de producto
2. Incluir factores externos (marketing, competencia)
3. Crear modelos separados por región geográfica
4. Implementar automatización con airflow/luigi

---

## 📚 Fórmula de Prophet

Prophet utiliza un modelo aditivo/multiplicativo:

$$y(t) = \text{Trend}(t) + \text{Seasonal}(t) + \text{Holiday}(t) + \epsilon(t)$$

Donde:
- **Trend(t)**: Componente de tendencia (crecimiento/decrecimiento)
- **Seasonal(t)**: Componente estacional (semanal + anual)
- **Holiday(t)**: Efectos de días festivos
- **ε(t)**: Ruido/error residual

Prophet estima automáticamente cada componente.

---

## 📞 Contacto & Links

- **GitHub**: [Fabian1808/Projects](https://github.com/Fabian1808/Projects)
- **LinkedIn**: [Fabian Urteaga](https://linkedin.com/in/tu-linkedin)
- **Dataset Original**: Project 1 (data.csv)
- **Librería Prophet**: [facebook/prophet](https://github.com/facebook/prophet)

---

## ✨ Habilidades Demostradas

- ✅ Time Series Analysis (Análisis de Series de Tiempo)
- ✅ Prophet Forecasting (Pronósticos avanzados)
- ✅ Descomposición de series en componentes
- ✅ Detección de tendencias y estacionalidad
- ✅ Interpretación de resultados para business
- ✅ Visualización de incertidumbre
- ✅ Exportación de modelos para producción

---

**Creado**: 10 de noviembre de 2025  
**Autor**: Fabian Urteaga  
**Versión**: 1.0 ✅ COMPLETADO
