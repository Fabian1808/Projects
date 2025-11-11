#!/bin/bash

# ============================================================================
# Script para crear un nuevo proyecto de Data Science
# Los proyectos se crean dentro de projects/
# Uso: bash create_project.sh project_name "Descripción del proyecto"
# ============================================================================

if [ -z "$1" ]; then
    echo "❌ Error: Debes proporcionar un nombre de proyecto"
    echo "Uso: bash create_project.sh <nombre_proyecto> \"<descripción>\""
    echo "Ejemplo: bash create_project.sh project4 \"Análisis de Clientes\""
    exit 1
fi

PROJECT_NAME=$1
PROJECT_DESC=${2:-"Nuevo proyecto de Data Science"}

echo "🚀 Creando proyecto: $PROJECT_NAME"
echo "📝 Descripción: $PROJECT_DESC"
echo ""

# Crear carpeta del proyecto dentro de projects/
mkdir -p "projects/$PROJECT_NAME"
cd "projects/$PROJECT_NAME"

# Crear estructura inicial
mkdir -p data output

# Crear .gitignore del proyecto
cat > .gitignore << 'EOF'
# Virtual Environment
venv/
env/
ENV/
.venv

# Python Cache
__pycache__/
*.py[cod]
*$py.class
*.so

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Data
*.csv
*.xlsx
data/

# Outputs
output/
results/
*.png
*.jpg

# Streamlit
.streamlit/secrets.toml
.streamlit/cache/

# Environment variables
.env
.env.local
EOF

# Crear README.md del proyecto
cat > README.md << EOF
# 📊 $PROJECT_NAME

> **Estado:** En desarrollo 🚀

$PROJECT_DESC

## 📋 Descripción

[Añade aquí la descripción de tu proyecto]

## 🎯 Objetivos

- [ ] Objetivo 1
- [ ] Objetivo 2
- [ ] Objetivo 3

## 📊 Análisis Incluidos

[Describe los análisis que realizarás]

## 📁 Estructura

\`\`\`
$PROJECT_NAME/
├── notebook.ipynb      # Análisis principal
├── data/              # Archivos de datos
├── output/            # Resultados y gráficos
├── README.md          # Este archivo
└── .gitignore         # Configuración Git
\`\`\`

## 🚀 Cómo Usar

1. Activar el entorno virtual:
\`\`\`bash
cd ../..
source venv/bin/activate
\`\`\`

2. Abrir el notebook:
\`\`\`bash
cd projects/$PROJECT_NAME
jupyter notebook notebook.ipynb
\`\`\`

3. Ejecutar las celdas en orden

## 📚 Requisitos

- Python 3.12+
- pandas
- matplotlib
- seaborn
- jupyter

## 📝 Notas

[Añade notas importantes aquí]

## 📈 Resultados

[Los resultados se añadirán aquí después de completar el análisis]

---

**Creado:** $(date '+%d de %B de %Y')

**Autor:** Fabian
EOF

# Inicializar Git
git init
git config user.name "Fabian"
git config user.email "fabian@example.com"

# Crear primer commit
git add .
git commit -m "Initial commit: Setup for $PROJECT_NAME project"

echo ""
echo "✅ Proyecto '$PROJECT_NAME' creado exitosamente!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Navega al proyecto: cd projects/$PROJECT_NAME"
echo "2. Añade tus datos a la carpeta 'data/'"
echo "3. Crea tu notebook: jupyter notebook notebook.ipynb"
echo "4. Actualiza el README.md con detalles del proyecto"
echo "5. Cuando esté listo para GitHub:"
echo "   - Crea un nuevo repositorio en GitHub"
echo "   - Ejecuta: git remote add origin <URL>"
echo "   - Luego: git push -u origin main"
echo ""
echo "💡 Para más información: cat ../../README.md"

