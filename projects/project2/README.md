# 📊 Project 2 - Análisis Consolidado de Ventas

> **Estado:** ✅ Completado y funcional

Análisis completo de ventas semanales con consolidación de datos, cálculo de ingresos y exportación a Excel.

## 📋 Descripción

Este proyecto automatiza el proceso de:
1. **Cargar** múltiples archivos CSV de ventas semanales
2. **Consolidar** todos los datos en una sola tabla
3. **Analizar** ventas por producto
4. **Exportar** resultados a Excel profesional

Es útil cuando tienes datos de ventas separados por semana/mes/sucursal y necesitas un reporte consolidado rápidamente.

## 🎯 Objetivos

- ✅ Encontrar y cargar automáticamente archivos CSV
- ✅ Consolidar datos de múltiples fuentes
- ✅ Calcular ingresos totales por producto
- ✅ Generar reportes en Excel
- ✅ Código completamente comentado y educativo

## 📊 Análisis Incluidos

1. **Carga Automática de Datos**: Usa `glob` para encontrar archivos con patrón
2. **Consolidación**: Une múltiples DataFrames con `pd.concat()`
3. **Cálculo de Ingresos**: Cantidad × Precio = Ingreso Total
4. **Resumen por Producto**: `groupby()` y `agg()` para totalizar
5. **Exportación Multi-hoja**: Excel con 2 pestañas (resumen y datos crudos)

## 📁 Estructura

```
project2/
├── data_analytics2.ipynb           # Notebook con todo el análisis
├── ventas_semana_1.csv             # Datos semana 1
├── ventas_semana_2.csv             # Datos semana 2
├── ventas_semana_3.csv             # Datos semana 3
├── Reporte_Consolidado_Ventas.xlsx # ⬅️ Archivo generado
├── README.md                        # Este archivo
└── .gitignore                       # Configuración Git
```

## 🚀 Cómo Usar

### Opción 1: Ejecutar desde VS Code
```bash
# 1. Abre el notebook
# 2. El kernel usa automáticamente: venv (Python 3.12)
# 3. Ejecuta todas las celdas
# 4. Se generará: Reporte_Consolidado_Ventas.xlsx
```

### Opción 2: Ejecutar desde terminal
```bash
cd /home/fabian/data\ science
source venv/bin/activate
jupyter notebook project2/data_analytics2.ipynb
```

### Opción 3: Usar Python directamente
```bash
python << 'EOF'
import pandas as pd
import glob

# Tu código aquí...
EOF
```

## 📚 Requisitos

- Python 3.12+
- **pandas** - Manipulación de datos
- **jupyter** - Cuadernos interactivos
- **openpyxl** - Exportación a Excel

Todas las dependencias ya están instaladas en `venv/`.

## 📝 Explicación del Código

### Paso 1: Cargar Archivos
```python
import glob
lista_archivos = sorted(glob.glob("ventas_*.csv"))
```
- Encuentra automáticamente todos los archivos que comienzan con "ventas_"
- El asterisco `*` es un comodín

### Paso 2: Consolidar
```python
df_consolidado = pd.concat(lista_dataframes, ignore_index=True)
```
- Pega todos los DataFrames en uno
- `ignore_index=True` evita índices duplicados

### Paso 3: Analizar
```python
resumen = df_consolidado.groupby('Producto').agg(
    Total=('Cantidad', 'sum'),
    Ingresos=('Ingreso', 'sum')
)
```
- Agrupa por producto y suma valores
- Crea un resumen ejecutivo

### Paso 4: Exportar
```python
with pd.ExcelWriter('reporte.xlsx') as writer:
    resumen.to_excel(writer, sheet_name='Resumen')
    df_consolidado.to_excel(writer, sheet_name='Datos')
```
- Escribe 2 pestañas en un archivo Excel
- Listo para compartir con gerentes

## 📈 Resultados Generados

**Reporte_Consolidado_Ventas.xlsx** contiene:

### Pestaña 1: Resumen_Por_Producto
| Producto | Total Unidades | Total Ingresos |
|----------|-----------------|-----------------|
| Laptop   | 10              | $12,000         |
| Monitor  | 12              | $3,600          |
| Mouse    | 31              | $775            |
| Teclado  | 25              | $1,750          |
| Webcam   | 15              | $1,200          |
| **TOTAL**| **93**          | **$19,325**     |

### Pestaña 2: Datos_Consolidados
Todos los 15 registros crudos con fecha, producto, cantidad, precio y fuente

## � Personalización

Para adaptarlo a tus datos:

### 1. Cambiar la ruta de búsqueda
```python
# En lugar de:
ruta_archivos = "ventas_*.csv"

# Usa:
ruta_archivos = "datos_semanales/ventas_*.csv"  # Si están en otra carpeta
ruta_archivos = "*.csv"                          # Si quieres todos los CSV
```

### 2. Cambiar las columnas de análisis
```python
resumen_productos = df_consolidado.groupby('Producto').agg(
    TotalUnidades=('Cantidad', 'sum'),
    TotalVentas=('IngresoTotal', 'sum'),
    UnidadPromedio=('Cantidad', 'mean'),  # ⬅️ Agregar esta línea
    PrecioPromedio=('PrecioUnitario', 'mean')  # ⬅️ O esta
)
```

### 3. Cambiar el nombre del Excel
```python
nombre_archivo_salida = 'Mi_Reporte_Personalizado.xlsx'
```

## 💡 Conceptos Clave Aprendidos

- **glob**: Búsqueda de archivos con patrones
- **pd.concat()**: Unir múltiples DataFrames
- **groupby()**: Agrupar y agregar datos
- **agg()**: Aplicar funciones de agregación
- **ExcelWriter**: Escribir múltiples hojas en Excel
- **Manejo de errores**: try/except para robustez

## 🤝 Próximos Pasos

Sugerencias para expandir este análisis:

1. **Agregar gráficos**: Matplotlib/Seaborn para visualizar ventas
2. **Análisis temporal**: Ver tendencias por semana
3. **Comparación**: Qué semana fue mejor
4. **Predicción**: Usar tendencias para predecir futuro
5. **Email automático**: Enviar el reporte por correo

---

**Último actualizado:** 10 de noviembre de 2025
**Estado:** ✅ Funcional y listo para producción
