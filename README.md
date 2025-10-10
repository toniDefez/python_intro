# Clasificador "Bird or Not"

Este repositorio contiene un experimento sencillo con **fastai** para entrenar un modelo que distingue entre fotos de aves y fotos de bosques. El flujo principal vive en el notebook `is_a_bird/is_a_bird.ipynb`, donde se descarga un pequeño conjunto de datos usando DuckDuckGo, se procesan las imágenes y se entrena un `vision_learner` basado en `resnet18`.

## Requisitos

- Python 3.10 o superior.
- Dependencias listadas en `requirements2.txt` (`ddgs`, `fastdownload`, `fastai`, `matplotlib`).  
  > Nota: `requirements.txt` se usa para pruebas rápidas y puede no contener todas las librerías necesarias.

## Puesta en marcha rápida

```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows; usa `source .venv/bin/activate` en Linux/macOS
pip install -r requirements2.txt
```

## Uso del notebook

1. Abre `is_a_bird/is_a_bird.ipynb` en tu editor o en Jupyter Lab.
2. Ejecuta las celdas en orden:
   - Se configuran las dependencias y el backend de Matplotlib.
   - Se descargan imágenes ejemplo (aves y bosques) y se aplican transformaciones rápidas.
   - Se construye una carpeta `bird_or_not/` con imágenes etiquetadas automáticamente.
   - Se valida y limpia el dataset, se crea un `DataBlock` y se entrena el modelo.
   - Finalmente se evalúa el clasificador con una imagen externa (`forest.jpg`).
3. El notebook deja comentarios en cada paso para documentar la lógica aplicada.

## Carpetas y archivos generados

- `bird_or_not/`: contenido descargado automáticamente; está listado en `.gitignore`.
- `bird.jpg` y `forest.jpg`: imágenes de ejemplo utilizadas en las pruebas.
- `.ipynb_checkpoints/`: metadatos de Jupyter, también ignorados por Git.

Si necesitas repetir el experimento o probar con otras clases, puedes ajustar la búsqueda en las funciones del notebook y volver a ejecutar las celdas de descarga y entrenamiento.
