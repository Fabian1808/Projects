"""
═════════════════════════════════════════════════════════════════════════════
    DASHBOARD DE VENTAS E-COMMERCE - PROFESIONAL Y AVANZADO
    
    Características:
    • Interfaz moderna con Streamlit
    • Gráficos interactivos con Plotly
    • Filtros dinámicos (País, Fechas, Cantidad mínima)
    • KPIs actualizados en tiempo real
    • Análisis estadísticos avanzados
    • Exportación de datos (descarga)
    • Caché optimizado para rendimiento
    
    Autor: Data Science Team
    Versión: 2.0 (Optimizado para Streamlit Cloud)
═════════════════════════════════════════════════════════════════════════════
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ═════════════════════════════════════════════════════════════════════════════
# 1. CONFIGURACIÓN INICIAL DE STREAMLIT (DEBE SER LO PRIMERO)
# ═════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Dashboard E-Commerce | Ventas",
    page_icon="📊",
    layout="wide",  # Usa todo el ancho de la pantalla
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para mejor apariencia
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    h1 {
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# 2. FUNCIONES AUXILIARES
# ═════════════════════════════════════════════════════════════════════════════

@st.cache_data
def load_data(filepath):
    """
    Carga y limpia los datos del archivo CSV.
    
    Parámetros:
    -----------
    filepath : str
        Ruta al archivo CSV
    
    Retorna:
    --------
    pd.DataFrame
        DataFrame limpio y procesado
    """
    try:
        # Intenta leer el archivo con diferentes encodings
        df = pd.read_csv(filepath, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(filepath, encoding='latin1')
    except FileNotFoundError:
        return None
    
    # ===== LIMPIEZA Y PROCESAMIENTO DE DATOS =====
    
    # 1. Convertir InvoiceDate a datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')
    
    # 2. Eliminar filas con valores críticos faltantes
    df = df.dropna(subset=['CustomerID', 'InvoiceNo', 'Country'])
    
    # 3. Filtrar valores positivos (rechaza transacciones anormales)
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    
    # 4. Crear columnas derivadas útiles
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']  # Ingreso por transacción
    df['YearMonth'] = df['InvoiceDate'].dt.to_period('M').astype(str)  # Período mensual
    df['Month'] = df['InvoiceDate'].dt.strftime('%Y-%m')  # Formato para series de tiempo
    df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()  # Día de la semana
    
    return df


@st.cache_data
def calcular_metricas(df):
    """
    Calcula métricas clave del DataFrame.
    
    Retorna un diccionario con KPIs principales
    """
    return {
        'ingresos_totales': df['TotalPrice'].sum(),
        'pedidos_totales': df['InvoiceNo'].nunique(),
        'clientes_unicos': df['CustomerID'].nunique(),
        'cantidad_productos': df['Description'].nunique(),
        'ticket_promedio': df.groupby('InvoiceNo')['TotalPrice'].sum().mean(),
        'ingresos_promedio_cliente': df.groupby('CustomerID')['TotalPrice'].sum().mean(),
    }


def format_numero(numero):
    """Formatea números con separadores de miles."""
    return f"{numero:,.0f}"


def format_moneda(numero):
    """Formatea números como moneda USD."""
    return f"${numero:,.2f}"


# ═════════════════════════════════════════════════════════════════════════════
# 3. CARGA DE DATOS
# ═════════════════════════════════════════════════════════════════════════════

# Intenta cargar datos desde el archivo
df = load_data('data.csv')

if df is None:
    st.error("❌ Error: No se puede encontrar 'data.csv' en la carpeta del proyecto.")
    st.info("📋 Asegúrate de que el archivo data.csv esté en la misma carpeta que dashboard.py")
    st.stop()

# Información de datos cargados
data_info = {
    'filas': len(df),
    'columnas': len(df.columns),
    'fecha_inicio': df['InvoiceDate'].min(),
    'fecha_fin': df['InvoiceDate'].max(),
}


# ═════════════════════════════════════════════════════════════════════════════
# 4. BARRA LATERAL - FILTROS AVANZADOS
# ═════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.title("🎛️ Filtros del Dashboard")
    
    # Información de los datos
    with st.expander("📊 Información de Datos", expanded=False):
        st.info(f"""
        **Datos Disponibles:**
        - 📈 Filas: {format_numero(data_info['filas'])}
        - 📋 Columnas: {data_info['columnas']}
        - 📅 Período: {data_info['fecha_inicio'].date()} a {data_info['fecha_fin'].date()}
        - 🌍 Países: {df['Country'].nunique()}
        """)
    
    st.divider()
    
    # Filtro 1: País
    st.subheader("1️⃣ País")
    paises_unicos = ['🌍 Todos los Países'] + sorted(df['Country'].unique().tolist())
    pais_seleccionado = st.selectbox(
        "Selecciona un país:",
        paises_unicos,
        help="Filtra los datos por país específico"
    )
    
    st.divider()
    
    # Filtro 2: Rango de fechas
    st.subheader("2️⃣ Rango de Fechas")
    fecha_min = df['InvoiceDate'].min().date()
    fecha_max = df['InvoiceDate'].max().date()
    
    col_fecha1, col_fecha2 = st.columns(2)
    with col_fecha1:
        fecha_inicio = st.date_input(
            "Desde:",
            fecha_min,
            min_value=fecha_min,
            max_value=fecha_max,
            help="Fecha de inicio del análisis"
        )
    with col_fecha2:
        fecha_fin = st.date_input(
            "Hasta:",
            fecha_max,
            min_value=fecha_min,
            max_value=fecha_max,
            help="Fecha de fin del análisis"
        )
    
    # Validar fechas
    if fecha_inicio > fecha_fin:
        st.sidebar.error("❌ La fecha inicio no puede ser posterior a la fecha fin")
        st.stop()
    
    st.divider()
    
    # Filtro 3: Cantidad mínima de ventas (avanzado)
    st.subheader("3️⃣ Cantidad Mínima de Ventas")
    cantidad_min = st.slider(
        "Cantidad mínima por transacción:",
        min_value=1,
        max_value=100,
        value=1,
        step=1,
        help="Filtra transacciones por cantidad mínima"
    )
    
    st.divider()
    
    # Botón para resetear filtros
    if st.button("🔄 Resetear Filtros", use_container_width=True):
        st.session_state.clear()
        st.rerun()


# ═════════════════════════════════════════════════════════════════════════════
# 5. APLICAR FILTROS AL DATAFRAME
# ═════════════════════════════════════════════════════════════════════════════

fecha_inicio_dt = pd.to_datetime(fecha_inicio)
fecha_fin_dt = pd.to_datetime(fecha_fin) + timedelta(days=1)

df_filtrado = df[
    (df['InvoiceDate'] >= fecha_inicio_dt) &
    (df['InvoiceDate'] < fecha_fin_dt) &
    (df['Quantity'] >= cantidad_min)
]

# Aplicar filtro de país
if not pais_seleccionado.startswith('🌍'):
    df_filtrado = df_filtrado[df_filtrado['Country'] == pais_seleccionado]


# ═════════════════════════════════════════════════════════════════════════════
# 6. CUERPO PRINCIPAL - HEADER Y RESUMEN
# ═════════════════════════════════════════════════════════════════════════════

st.title("📊 Dashboard de Ventas E-Commerce")

# Asegurarse de que TotalPrice existe en el DataFrame filtrado
if 'TotalPrice' not in df_filtrado.columns:
    df_filtrado['TotalPrice'] = df_filtrado['Quantity'] * df_filtrado['UnitPrice']

st.markdown(f"""
**Período:** `{fecha_inicio}` → `{fecha_fin}` | 
**País:** `{pais_seleccionado}` | 
**Cantidad Mínima:** `{cantidad_min}` unidades
""")

# Validación de datos filtrados
if len(df_filtrado) == 0:
    st.warning("⚠️ No hay datos que coincidan con los filtros seleccionados. Intenta cambiar los filtros.")
    st.stop()

st.info(f"✅ Mostrando {format_numero(len(df_filtrado))} transacciones de {format_numero(df_filtrado['InvoiceNo'].nunique())} pedidos")


# ═════════════════════════════════════════════════════════════════════════════
# 7. MÉTRICAS CLAVE (KPIs) - ROW 1
# ═════════════════════════════════════════════════════════════════════════════

st.header("📈 Métricas Clave")

metricas = calcular_metricas(df_filtrado)

# 4 columnas para los KPIs principales
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="💰 Ingresos Totales",
        value=format_moneda(metricas['ingresos_totales']),
        delta=f"{metricas['ingresos_totales']/len(df_filtrado):.2f} promedio por transacción" if len(df_filtrado) > 0 else "N/A"
    )

with col2:
    st.metric(
        label="📦 Pedidos Totales",
        value=format_numero(metricas['pedidos_totales']),
        delta=f"{metricas['ingresos_totales']/metricas['pedidos_totales']:.2f} ingresos/pedido" if metricas['pedidos_totales'] > 0 else "N/A"
    )

with col3:
    st.metric(
        label="👥 Clientes Únicos",
        value=format_numero(metricas['clientes_unicos']),
        delta=f"{metricas['pedidos_totales']/metricas['clientes_unicos']:.1f} pedidos/cliente" if metricas['clientes_unicos'] > 0 else "N/A"
    )

with col4:
    st.metric(
        label="🏷️ Productos Diferentes",
        value=format_numero(metricas['cantidad_productos']),
        delta=f"{metricas['ingresos_totales']/metricas['cantidad_productos']:.2f} ingresos/producto" if metricas['cantidad_productos'] > 0 else "N/A"
    )


# ═════════════════════════════════════════════════════════════════════════════
# 8. GRÁFICOS PRINCIPALES
# ═════════════════════════════════════════════════════════════════════════════

st.header("📊 Visualizaciones Avanzadas")

# GRÁFICO 1: Evolución de Ingresos (Serie de tiempo)
st.subheader("1. Evolución de Ingresos a lo Largo del Tiempo")

ventas_por_mes = df_filtrado.groupby('Month')['TotalPrice'].agg(['sum', 'count']).reset_index()
ventas_por_mes.columns = ['Month', 'TotalPrice', 'Transacciones']

fig_tiempo = go.Figure()

fig_tiempo.add_trace(go.Scatter(
    x=ventas_por_mes['Month'],
    y=ventas_por_mes['TotalPrice'],
    mode='lines+markers',
    name='Ingresos',
    line=dict(color='#1f77b4', width=3),
    marker=dict(size=8),
    yaxis='y1'
))

fig_tiempo.add_trace(go.Bar(
    x=ventas_por_mes['Month'],
    y=ventas_por_mes['Transacciones'],
    name='Transacciones',
    marker=dict(color='rgba(158, 202, 225, 0.5)'),
    yaxis='y2',
    opacity=0.6
))

fig_tiempo.update_layout(
    title="Ingresos vs Número de Transacciones",
    xaxis=dict(title='Mes'),
    yaxis=dict(title='Ingresos (USD)', side='left'),
    yaxis2=dict(title='Cantidad de Transacciones', side='right', overlaying='y'),
    hovermode='x unified',
    height=450,
    showlegend=True
)

st.plotly_chart(fig_tiempo, use_container_width=True)


# FILA 2: Gráficos lado a lado
col_graf1, col_graf2 = st.columns(2)

# GRÁFICO 2: Top 10 Productos
with col_graf1:
    st.subheader("2. Top 10 Productos Más Vendidos")
    
    top_productos = df_filtrado.groupby('Description').agg({
        'Quantity': 'sum',
        'TotalPrice': 'sum'
    }).nlargest(10, 'Quantity').reset_index()
    
    fig_productos = px.bar(
        top_productos,
        x='Quantity',
        y='Description',
        color='TotalPrice',
        color_continuous_scale='Viridis',
        labels={'Quantity': 'Cantidad Vendida', 'Description': 'Producto', 'TotalPrice': 'Ingresos (USD)'},
        title='Por cantidad vendida (coloreado por ingresos)',
        orientation='h'
    )
    
    fig_productos.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        height=400,
        showlegend=True
    )
    
    st.plotly_chart(fig_productos, use_container_width=True)


# GRÁFICO 3: Top 10 Clientes
with col_graf2:
    st.subheader("3. Top 10 Clientes Por Ingresos")
    
    top_clientes = df_filtrado.groupby('CustomerID').agg({
        'TotalPrice': 'sum',
        'InvoiceNo': 'count'
    }).nlargest(10, 'TotalPrice').reset_index()
    
    top_clientes['CustomerID'] = top_clientes['CustomerID'].astype(str)
    
    fig_clientes = px.bar(
        top_clientes,
        x='TotalPrice',
        y='CustomerID',
        color='InvoiceNo',
        color_continuous_scale='Plasma',
        labels={'TotalPrice': 'Ingresos (USD)', 'CustomerID': 'ID Cliente', 'InvoiceNo': 'Compras'},
        title='Por ingresos totales (coloreado por # de compras)',
        orientation='h'
    )
    
    fig_clientes.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        height=400,
        showlegend=True
    )
    
    st.plotly_chart(fig_clientes, use_container_width=True)


# FILA 3: Análisis adicional
col_graf3, col_graf4 = st.columns(2)

# GRÁFICO 4: Distribución de Ingresos por País
with col_graf3:
    st.subheader("4. Distribución de Ingresos por País")
    
    ingresos_pais = df_filtrado.groupby('Country')['TotalPrice'].sum().nlargest(10).reset_index()
    
    fig_pais = px.pie(
        ingresos_pais,
        names='Country',
        values='TotalPrice',
        title='Top 10 Países por Ingresos',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig_pais.update_layout(height=400)
    
    st.plotly_chart(fig_pais, use_container_width=True)


# GRÁFICO 5: Heatmap de Día de la Semana
with col_graf4:
    st.subheader("5. Patrón de Ventas por Día de Semana")
    
    # Crear tabla de frecuencia
    dia_orden = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ventas_dia = df_filtrado.groupby('DayOfWeek')['TotalPrice'].sum().reindex(dia_orden)
    
    fig_dia = go.Figure(data=[
        go.Bar(
            x=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
            y=ventas_dia.values,
            marker=dict(
                color=ventas_dia.values,
                colorscale='Greens',
                showscale=False
            ),
            text=[f"${v:,.0f}" for v in ventas_dia.values],
            textposition='outside'
        )
    ])
    
    fig_dia.update_layout(
        title="Ingresos por Día de Semana",
        xaxis_title="Día",
        yaxis_title="Ingresos (USD)",
        height=400
    )
    
    st.plotly_chart(fig_dia, use_container_width=True)


# ═════════════════════════════════════════════════════════════════════════════
# 9. ANÁLISIS ESTADÍSTICOS
# ═════════════════════════════════════════════════════════════════════════════

st.header("📊 Análisis Estadísticos")

col_stat1, col_stat2, col_stat3 = st.columns(3)

with col_stat1:
    ticket_promedio = df_filtrado.groupby('InvoiceNo')['TotalPrice'].sum().mean()
    st.metric(
        "🎫 Ticket Promedio",
        format_moneda(ticket_promedio),
        help="Promedio de ingresos por pedido"
    )

with col_stat2:
    ingresos_cliente = df_filtrado.groupby('CustomerID')['TotalPrice'].sum().mean()
    st.metric(
        "💳 Ingresos Promedio por Cliente",
        format_moneda(ingresos_cliente),
        help="Promedio gastado por cliente"
    )

with col_stat3:
    cantidad_promedio = df_filtrado['Quantity'].mean()
    st.metric(
        "📦 Cantidad Promedio por Transacción",
        f"{cantidad_promedio:.1f} unidades",
        help="Promedio de artículos por transacción"
    )


# ═════════════════════════════════════════════════════════════════════════════
# 10. SECCIÓN DE DATOS CRUDOS CON OPCIÓN DE DESCARGA
# ═════════════════════════════════════════════════════════════════════════════

st.header("📥 Descargar Datos")

col_down1, col_down2 = st.columns(2)

with col_down1:
    # Opción para descargar datos filtrados como CSV
    csv_data = df_filtrado.to_csv(index=False)
    st.download_button(
        label="⬇️ Descargar Datos Filtrados (CSV)",
        data=csv_data,
        file_name=f"ventas_{fecha_inicio}_{fecha_fin}.csv",
        mime="text/csv"
    )

with col_down2:
    # Opción para descargar datos como Excel
    try:
        excel_data = df_filtrado.to_excel(index=False)
        st.download_button(
            label="⬇️ Descargar Datos Filtrados (Excel)",
            data=excel_data,
            file_name=f"ventas_{fecha_inicio}_{fecha_fin}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except:
        st.info("💡 Instala 'openpyxl' para descargar en formato Excel")


# Vista previa de datos
if st.checkbox("👀 Ver Datos Crudos (preview)", value=False):
    st.subheader("Preview de Datos Filtrados")
    st.dataframe(
        df_filtrado.head(100).style.format({
            'TotalPrice': '${:,.2f}',
            'UnitPrice': '${:,.2f}',
            'InvoiceDate': '{:%Y-%m-%d %H:%M}'
        }),
        use_container_width=True
    )
    
    st.info(f"Mostrando 100 de {len(df_filtrado)} registros")


# ═════════════════════════════════════════════════════════════════════════════
# 11. FOOTER
# ═════════════════════════════════════════════════════════════════════════════

st.divider()
st.markdown("""
---
<div style='text-align: center; color: gray; font-size: 0.85rem;'>
    📊 Dashboard de Ventas E-Commerce | Versión 2.0 | Powered by Streamlit & Plotly
    <br>
    ⚡ Últimas actualizaciones: Datos en tiempo real | Filtros avanzados | Análisis estadístico
</div>
""", unsafe_allow_html=True)