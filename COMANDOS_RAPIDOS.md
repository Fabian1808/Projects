# ⚡ Comandos Rápidos

## 🚀 Crear Nuevo Proyecto

```bash
cd "/home/fabian/data science"
bash create_project.sh project3 "Descripción de tu proyecto"
```

## 📂 Navegar y Activar

```bash
# Ir a un proyecto
cd "/home/fabian/data science/project1"

# Activar entorno virtual
source ../venv/bin/activate

# Desactivar
deactivate
```

## 📓 Jupyter Notebook

```bash
# Abrir Jupyter
jupyter notebook notebook.ipynb

# O si estás en otra carpeta
jupyter notebook ../project1/notebook.ipynb
```

## 📝 Git - Básico

```bash
# Ver estado
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "Descripción de cambios"

# Ver historial
git log --oneline
```

## 🌐 GitHub - Conectar Proyecto

```bash
# En la carpeta del proyecto
git remote add origin https://github.com/Fabian1808/ProjectX.git
git branch -M main
git push -u origin main
```

## 🌐 GitHub - Actualizar Proyecto

```bash
# Después de cambios locales
git add .
git commit -m "Descripción"
git push
```

## 📦 Python - Instalar Paquetes

```bash
# Con entorno activado
pip install pandas numpy matplotlib seaborn jupyter

# Ver instalados
pip list

# Crear requirements
pip freeze > requirements.txt
```

## 🔒 .env - Editar

```bash
# Editar archivo .env
nano /home/fabian/data science/.env

# O con editor favorito
vim /home/fabian/data science/.env
```

## 📊 Ver Estructura

```bash
# Ver árbol de carpetas
tree -L 2

# O alternativa
find . -maxdepth 2 -type d | head -20
```

## 🔍 Buscar en Proyectos

```bash
# Buscar archivos
find . -name "*.csv"
find . -name "*.ipynb"

# Buscar contenido
grep -r "palabra" --include="*.py"
```

## 🧹 Limpiar

```bash
# Eliminar archivos de caché
find . -type d -name __pycache__ -exec rm -rf {} +

# Eliminar archivos .ipynb_checkpoints
find . -type d -name .ipynb_checkpoints -exec rm -rf {} +
```

## 📈 Versiones

```bash
# Ver versión Python
python --version

# Ver versión pip
pip --version

# Ver entorno
which python
```

## 📚 Ayuda Documentación

```bash
# Ver guías creadas
cat README.md
cat GUIA_RAPIDA.md
cat EJEMPLO_CREAR_PROYECTO.txt
cat RESUMEN_CONFIGURACION.txt
```

---

**Tip:** Guarda este archivo en favoritos para referencia rápida 📌
