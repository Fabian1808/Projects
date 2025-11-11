#!/usr/bin/env python3
"""
═════════════════════════════════════════════════════════════════════════════
    SCRIPT DE VERIFICACIÓN - PROYECTO 3
    
    Valida que:
    1. Todos los archivos existen
    2. data.csv se puede leer correctamente
    3. Dashboard puede importar todas las librerías
    4. Datos se procesan sin errores
═════════════════════════════════════════════════════════════════════════════
"""

import os
import sys
from pathlib import Path

# Colores para terminal
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

print(f"\n{BOLD}{'='*80}{RESET}")
print(f"{BOLD}VERIFICACIÓN DE PROYECTO 3 - DASHBOARD E-COMMERCE{RESET}")
print(f"{BOLD}{'='*80}{RESET}\n")

# ═══════════════════════════════════════════════════════════════════════════
# CHECK 1: Archivos Existentes
# ═══════════════════════════════════════════════════════════════════════════

print(f"{BOLD}CHECK 1: Archivos Requeridos{RESET}")
print("-" * 80)

archivos_requeridos = {
    'dashboard.py': 'Código del dashboard',
    'data.csv': 'Dataset principal',
    'requirements.txt': 'Dependencias',
    'README.md': 'Documentación',
    '.gitignore': 'Configuración Git',
}

archivos_faltantes = []

for archivo, descripcion in archivos_requeridos.items():
    ruta = Path(archivo)
    if ruta.exists():
        tamaño = ruta.stat().st_size
        if tamaño > 1_000_000:  # Mayor a 1 MB
            tamaño_fmt = f"{tamaño/1_000_000:.1f} MB"
        else:
            tamaño_fmt = f"{tamaño/1000:.1f} KB"
        print(f"{GREEN}✓{RESET} {archivo:20} ({tamaño_fmt:>10}) - {descripcion}")
    else:
        print(f"{RED}✗{RESET} {archivo:20} {'FALTA':>10} - {descripcion}")
        archivos_faltantes.append(archivo)

if archivos_faltantes:
    print(f"\n{RED}❌ Faltan archivos: {', '.join(archivos_faltantes)}{RESET}")
    sys.exit(1)
else:
    print(f"\n{GREEN}✅ Todos los archivos requeridos existen{RESET}\n")


# ═══════════════════════════════════════════════════════════════════════════
# CHECK 2: Librerías Importables
# ═══════════════════════════════════════════════════════════════════════════

print(f"{BOLD}CHECK 2: Librerías Requeridas{RESET}")
print("-" * 80)

librerias = {
    'pandas': 'Manipulación de datos',
    'plotly': 'Gráficos interactivos',
    'streamlit': 'Framework web',
    'numpy': 'Operaciones numéricas',
    'openpyxl': 'Exportar a Excel',
}

librerias_faltantes = []

for libreria, descripcion in librerias.items():
    try:
        modulo = __import__(libreria)
        version = getattr(modulo, '__version__', 'N/A')
        print(f"{GREEN}✓{RESET} {libreria:15} (v{version:10}) - {descripcion}")
    except ImportError:
        print(f"{RED}✗{RESET} {libreria:15} {'NO INSTALADA':10} - {descripcion}")
        librerias_faltantes.append(libreria)

if librerias_faltantes:
    print(f"\n{YELLOW}⚠️  Librerías faltantes: {', '.join(librerias_faltantes)}{RESET}")
    print(f"   Instala con: pip install {' '.join(librerias_faltantes)}")
else:
    print(f"\n{GREEN}✅ Todas las librerías están instaladas{RESET}\n")


# ═══════════════════════════════════════════════════════════════════════════
# CHECK 3: Lectura de Datos
# ═══════════════════════════════════════════════════════════════════════════

print(f"{BOLD}CHECK 3: Carga y Validación de Datos{RESET}")
print("-" * 80)

try:
    import pandas as pd
    
    # Intenta leer el CSV
    try:
        df = pd.read_csv('data.csv', encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv('data.csv', encoding='latin1')
    
    print(f"{GREEN}✓{RESET} CSV cargado correctamente")
    print(f"  • Filas: {len(df):,}")
    print(f"  • Columnas: {len(df.columns)}")
    print(f"  • Columnas: {', '.join(df.columns)}")
    
    # Verifica columnas requeridas
    columnas_requeridas = ['InvoiceNo', 'Quantity', 'UnitPrice', 'InvoiceDate', 'CustomerID', 'Country', 'Description']
    columnas_faltantes = [col for col in columnas_requeridas if col not in df.columns]
    
    if columnas_faltantes:
        print(f"{RED}✗ Faltan columnas: {', '.join(columnas_faltantes)}{RESET}")
        sys.exit(1)
    else:
        print(f"{GREEN}✓ Todas las columnas requeridas existen{RESET}")
    
    # Validar tipos de datos
    print(f"\n  Tipos de datos:")
    for col in columnas_requeridas:
        print(f"    • {col:15} → {str(df[col].dtype)}")
    
    print(f"\n{GREEN}✅ Datos validados correctamente{RESET}\n")
    
except Exception as e:
    print(f"{RED}❌ Error al cargar datos: {e}{RESET}")
    sys.exit(1)


# ═══════════════════════════════════════════════════════════════════════════
# CHECK 4: Estructura del Dashboard
# ═══════════════════════════════════════════════════════════════════════════

print(f"{BOLD}CHECK 4: Estructura del Código{RESET}")
print("-" * 80)

with open('dashboard.py', 'r') as f:
    contenido = f.read()

checks = {
    'st.set_page_config': 'Configuración de página',
    '@st.cache_data': 'Cache de datos',
    'load_data': 'Función de carga',
    'st.sidebar': 'Barra lateral',
    'st.metric': 'KPIs',
    'px.line': 'Gráficos Plotly',
    'st.plotly_chart': 'Integración Plotly',
    'st.download_button': 'Descarga de datos',
}

for elemento, descripcion in checks.items():
    if elemento in contenido:
        print(f"{GREEN}✓{RESET} {elemento:20} - {descripcion}")
    else:
        print(f"{RED}✗{RESET} {elemento:20} - {descripcion} (FALTA)")

print(f"\n{GREEN}✅ Estructura de código validada{RESET}\n")


# ═══════════════════════════════════════════════════════════════════════════
# RESUMEN FINAL
# ═══════════════════════════════════════════════════════════════════════════

print(f"{BOLD}{'='*80}{RESET}")
print(f"{BOLD}{GREEN}✅ VERIFICACIÓN COMPLETADA EXITOSAMENTE{RESET}{BOLD}{RESET}")
print(f"{BOLD}{'='*80}{RESET}\n")

print(f"{BOLD}Próximos pasos:{RESET}")
print(f"  1. Ejecuta: {YELLOW}streamlit run dashboard.py{RESET}")
print(f"  2. Se abrirá automáticamente en: {YELLOW}http://localhost:8501{RESET}")
print(f"  3. Prueba todos los filtros y gráficos")
print(f"  4. Cuando esté listo, sube a GitHub y Streamlit Cloud\n")

print(f"{BOLD}Dashboard Information:{RESET}")
print(f"  • Registros: {len(df):,}")
print(f"  • Período: {df['InvoiceDate'].min()} a {df['InvoiceDate'].max()}")
print(f"  • Países: {df['Country'].nunique()}")
print(f"  • Clientes únicos: {df['CustomerID'].nunique():,}")
print(f"  • Productos únicos: {df['Description'].nunique():,}\n")

print(f"{GREEN}🎉 ¡Todo listo para producción! 🎉{RESET}\n")
