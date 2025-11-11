# Ejemplos de Uso del .env

## Ejemplo 1: Cargar variables del .env en Python

```python
import os
from dotenv import load_dotenv
import pandas as pd

# Cargar variables de entorno desde .env
load_dotenv('../.env')  # Nota: ../  porque está un nivel arriba

# Obtener variables
project_root = os.getenv('PROJECT_ROOT')
python_version = os.getenv('PYTHON_VERSION')
data_path = os.getenv('DATA_PATH')

print(f"Proyecto: {project_root}")
print(f"Python: {python_version}")
```

## Ejemplo 2: Rutas dinámicas usando .env

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv('../.env')

# Obtener rutas dinámicas
PROJECT_ROOT = Path(os.getenv('PROJECT_ROOT'))
DATA_DIR = PROJECT_ROOT / 'project2' / 'data'
OUTPUT_DIR = PROJECT_ROOT / 'project2' / 'output'

# Crear directorios si no existen
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Usar rutas
df = pd.read_csv(DATA_DIR / 'data.csv')
df.to_csv(OUTPUT_DIR / 'resultados.csv')
```

## Ejemplo 3: Configuración de entorno en Jupyter

```python
# Al inicio del notebook
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Cargar .env
load_dotenv('../.env')

# Configurar rutas
PROJECT_ROOT = Path(os.getenv('PROJECT_ROOT'))
CURRENT_PROJECT = PROJECT_ROOT / 'project2'
DATA_DIR = CURRENT_PROJECT / 'data'
OUTPUT_DIR = CURRENT_PROJECT / 'output'

# Crear directorios
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Verificar
print(f"✓ Proyecto configurado: {CURRENT_PROJECT}")
print(f"✓ Datos en: {DATA_DIR}")
print(f"✓ Salida en: {OUTPUT_DIR}")
```

## Ejemplo 4: Variables sensibles (contraseñas, APIs)

### Editar .env
```
# Variables de entorno
PYTHON_VERSION=3.12
DATABASE_URL=postgresql://user:password@localhost/dbname
API_KEY=your_secret_api_key_here
DEBUG=False
```

### Usar en Python
```python
import os
from dotenv import load_dotenv

load_dotenv('../.env')

# Seguro: No expondrá contraseñas en GitHub
DB_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

# Usar con precaución
conn = connect(DB_URL)
```

## Instalar dependencia

Para usar dotenv, instalar:
```bash
pip install python-dotenv
```

---

**NOTA IMPORTANTE:** El archivo `.env` NUNCA debe estar en GitHub. Está protegido por `.gitignore`.
