# 📑 ÍNDICE DE DOCUMENTACIÓN

Bienvenido a tu espacio de proyectos de Data Science. Usa este índice para encontrar lo que necesitas rápidamente.

## 📚 DOCUMENTACIÓN POR PROPÓSITO

### 🚀 **Quiero CREAR un NUEVO PROYECTO**

**Archivo:** [`EJEMPLO_CREAR_PROYECTO.txt`](EJEMPLO_CREAR_PROYECTO.txt)
- Guía paso a paso
- 11 pasos detallados
- Ejemplo práctico
- Checklist de verificación

**Comando rápido:**
```bash
bash create_project.sh project3 "Mi descripción"
```

---

### 📋 **Quiero ver la ESTRUCTURA GENERAL**

**Archivo:** [`README.md`](README.md)
- Descripción de la carpeta raíz
- Listado de proyectos
- Estructura de carpetas
- Requisitos generales

---

### ⚡ **Necesito COMANDOS RÁPIDOS**

**Archivo:** [`COMANDOS_RAPIDOS.md`](COMANDOS_RAPIDOS.md) ⭐ **RECOMENDADO**
- Comando para crear proyecto
- Navegar y activar entorno
- Jupyter
- Git básico
- GitHub
- Python
- Búsqueda
- Limpiar

---

### 📖 **Quiero una GUÍA COMPLETA**

**Archivo:** [`GUIA_RAPIDA.md`](GUIA_RAPIDA.md)
- Estructura creada
- Punto importante sobre .env
- Crear nuevo proyecto
- Comenzar a trabajar
- Actualizar en GitHub
- Conectar con GitHub
- Gestión del .env
- Checklist
- Troubleshooting

---

### 🔒 **Necesito información sobre el .env**

**Archivo:** [`EJEMPLOS_ENV.md`](EJEMPLOS_ENV.md)
- Cómo cargar variables en Python
- Rutas dinámicas
- Configuración en Jupyter
- Variables sensibles
- Instalación de dependencias

**Ubicación del archivo:**
```
/home/fabian/data science/.env
```

---

### 📊 **Quiero un RESUMEN COMPLETO**

**Archivo:** [`RESUMEN_CONFIGURACION.txt`](RESUMEN_CONFIGURACION.txt)
- Problema original y solución
- Estructura creada
- Protección del .env
- Archivos creados
- Características
- Próximos pasos

---

## 🏗️ ESTRUCTURA DE CARPETAS

```
/home/fabian/data science/
│
├── 📁 project1/                    ← Análisis de Ventas E-commerce
│   ├── data_analytics.ipynb
│   ├── data.csv
│   ├── README.md
│   └── .git/
│
├── 📁 project2/                    ← Plantilla para nuevo proyecto
│   ├── README.md
│   └── .gitignore
│
├── 📁 venv/                        ← Entorno Python compartido
│
├── 🔒 .env                         ← Variables de entorno (PROTEGIDO)
├── .gitignore                      ← Protege .env
│
├── 📚 README.md                    ← Descripción general
├── 📚 GUIA_RAPIDA.md              ← Guía completa
├── 📚 COMANDOS_RAPIDOS.md         ← Referencia rápida ⭐
├── 📚 EJEMPLOS_ENV.md             ← Ejemplos Python
├── 📄 RESUMEN_CONFIGURACION.txt   ← Resumen completo
├── 📄 EJEMPLO_CREAR_PROYECTO.txt  ← Guía paso a paso
│
└── ⚙️  create_project.sh           ← Script automatizado
```

---

## 🎯 FLUJOS DE TRABAJO

### Flujo 1: Crear proyecto nuevo
1. Lee: [`EJEMPLO_CREAR_PROYECTO.txt`](EJEMPLO_CREAR_PROYECTO.txt)
2. Ejecuta: `bash create_project.sh projectX "Descripción"`
3. Consulta: [`COMANDOS_RAPIDOS.md`](COMANDOS_RAPIDOS.md)

### Flujo 2: Trabajar en un proyecto
1. Navega: `cd project1`
2. Activa: `source ../venv/bin/activate`
3. Abre: `jupyter notebook notebook.ipynb`
4. Consulta: [`COMANDOS_RAPIDOS.md`](COMANDOS_RAPIDOS.md)

### Flujo 3: Subir a GitHub
1. Lee: [`GUIA_RAPIDA.md`](GUIA_RAPIDA.md) - Sección "Conectar con GitHub"
2. Crea repositorio en GitHub
3. Ejecuta comandos de git
4. Consulta: [`COMANDOS_RAPIDOS.md`](COMANDOS_RAPIDOS.md) - Sección Git/GitHub

### Flujo 4: Usar variables de entorno
1. Lee: [`EJEMPLOS_ENV.md`](EJEMPLOS_ENV.md)
2. Edita: `/home/fabian/data science/.env`
3. Usa en código: `from dotenv import load_dotenv`

---

## ❓ PREGUNTAS FRECUENTES

### ¿Dónde está mi .env?
```
/home/fabian/data science/.env
```
Está protegido por `.gitignore`, nunca se subirá a GitHub.

### ¿Se perderá el .env si creo otro proyecto?
No, está fuera de los proyectos individuales. Está en la raíz compartida.

### ¿Cómo cargo variables del .env?
Ver: [`EJEMPLOS_ENV.md`](EJEMPLOS_ENV.md) - Ejemplo 1

### ¿Cómo creo un nuevo proyecto?
Opción 1 (recomendado):
```bash
bash create_project.sh project3 "Descripción"
```
Ver: [`EJEMPLO_CREAR_PROYECTO.txt`](EJEMPLO_CREAR_PROYECTO.txt)

### ¿Puedo tener múltiples proyectos en GitHub?
Sí, cada proyecto tiene su propio repositorio Git independiente.

---

## 🔍 BÚSQUEDA RÁPIDA

| Necesito... | Ver archivo... |
|-------------|-----------------|
| Crear proyecto | EJEMPLO_CREAR_PROYECTO.txt |
| Estructura general | README.md |
| Comandos rápidos | COMANDOS_RAPIDOS.md ⭐ |
| Guía completa | GUIA_RAPIDA.md |
| Ejemplos Python | EJEMPLOS_ENV.md |
| Resumen todo | RESUMEN_CONFIGURACION.txt |

---

## 🎓 RECOMENDACIÓN

**Para principiantes:** Empieza por [`EJEMPLO_CREAR_PROYECTO.txt`](EJEMPLO_CREAR_PROYECTO.txt)

**Para referencia rápida:** Usa [`COMANDOS_RAPIDOS.md`](COMANDOS_RAPIDOS.md)

**Para entendimiento profundo:** Lee [`GUIA_RAPIDA.md`](GUIA_RAPIDA.md)

---

## 📞 AYUDA RÁPIDA

```bash
# Ver todos los archivos
ls -lh /home/fabian/data science/

# Ver estructura
tree -L 2 /home/fabian/data science/

# Ver contenido de .env
cat /home/fabian/data science/.env

# Ver .gitignore
cat /home/fabian/data science/.gitignore
```

---

**Última actualización:** 10 de noviembre de 2025

**Estado:** ✅ Sistema listo para usar

**Próximo paso:** Ejecuta `bash create_project.sh project3 "Mi proyecto"`
