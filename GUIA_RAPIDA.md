# 🚀 GUÍA RÁPIDA - Múltiples Proyectos

## Estructura Creada

Tu carpeta "data science" ahora está organizada así:

```
data science/
├── project1/              # Tu primer proyecto (GitHub: Project1)
│   ├── data_analytics.ipynb
│   ├── data.csv
│   └── .git/             # Repositorio Git independiente
│
├── project2/              # Plantilla para segundo proyecto
│   └── README.md
│
├── venv/                  # Entorno virtual compartido
├── .env                   # 🔒 Variables de entorno (NO en GitHub)
├── .gitignore             # Protege el .env
├── README.md              # Documentación general
└── create_project.sh      # Script para crear proyectos
```

## 📌 Punto Importante: El .env

Tu archivo `.env` está **PROTEGIDO** por `.gitignore` en la raíz:
- ✅ NO se subirá a GitHub
- ✅ NO se perderá al actualizar repositorios
- ✅ Puedes usarlo para variables compartidas

## 🎯 Para Crear un Nuevo Proyecto

### Opción 1: Usar el script (RECOMENDADO)

```bash
cd "/home/fabian/data science"
bash create_project.sh project3 "Mi análisis de clientes"
```

Esto crea automáticamente:
- 📁 Carpeta `project3/`
- 📝 README.md
- 🔧 .gitignore
- 💾 Repositorio Git local

### Opción 2: Manual

```bash
cd "/home/fabian/data science"
mkdir project3
cd project3
git init
# Luego copia los templates de project2
```

## 💻 Comenzar a Trabajar en un Proyecto

```bash
# Activar entorno virtual (desde cualquier proyecto)
cd "/home/fabian/data science"
source venv/bin/activate

# Ir al proyecto
cd project3

# Abrir Jupyter
jupyter notebook notebook.ipynb
```

## 🔄 Actualizar un Proyecto en GitHub

```bash
cd "/home/fabian/data science/project3"

# Ver estado
git status

# Añadir cambios
git add .

# Hacer commit
git commit -m "Descripción de cambios"

# Push (después de conectar con GitHub)
git push origin main
```

## 🌐 Conectar un Proyecto con GitHub

1. **Crea un repositorio en GitHub.com** (Ej: `Project3`)

2. **Conecta desde terminal:**

```bash
cd "/home/fabian/data science/project3"
git remote add origin https://github.com/Fabian1808/Project3.git
git branch -M main
git push -u origin main
```

## 🔒 Gestión del .env

### Usar variables del .env

```python
# En tu notebook
import os
from dotenv import load_dotenv

# Cargar variables
load_dotenv()
project_root = os.getenv('PROJECT_ROOT')
```

### Editar el .env

```bash
nano "/home/fabian/data science/.env"
```

Variables disponibles:
- `PYTHON_VERSION=3.12`
- `VENV_PATH=./venv`
- `PROJECT_ROOT=/home/fabian/data science`
- Añade las tuyas cuando sea necesario

## ✅ Checklist para Nuevo Proyecto

- [ ] Crear proyecto con `bash create_project.sh`
- [ ] Actualizar `README.md` con descripción
- [ ] Crear/Subir datos a carpeta `data/`
- [ ] Crear `notebook.ipynb`
- [ ] Testear código
- [ ] Crear repositorio en GitHub
- [ ] Conectar con `git remote add origin`
- [ ] Hacer push inicial

## 📚 Archivos Importantes

| Archivo | Propósito |
|---------|-----------|
| `.env` | Variables de entorno (🔒 NO en GitHub) |
| `.gitignore` (raíz) | Protege .env globalmente |
| `.gitignore` (proyecto) | Protege archivos del proyecto |
| `create_project.sh` | Script para crear proyectos |

## 🆘 Solucionar Problemas

### El .env no está protegido
```bash
cd "/home/fabian/data science"
git check-ignore .env
```

### Limpiar repositorio local
```bash
cd proyecto
git clean -fd
git reset --hard
```

### Ver historial de Git
```bash
git log --oneline
```

---

**¡Listo para empezar con project2 o cualquier otro proyecto! 🚀**
