[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19144093&assignment_repo_type=AssignmentRepo)
# Lab03: Visualización de Datos en Raspberry Pi Zero W

## Integrantes

- [David Santiago Laiton Gutierrez](https://github.com/dslaitong)
- [Edgar Giovanni Neira Lugo](https://github.com/Gioneira)
- [Johana Stephany Toro Echeverria](https://github.com/JohanaT97)

## Documentación
### INTRODUCCION
Este script implementa una herramienta de monitoreo en tiempo real de la temperatura del procesador de una Raspberry. Utiliza matplotlib para graficar dinámicamente los datos obtenidos desde el sistema mediante el comando vcgencmd. Además, los datos recolectados se almacenan en un archivo CSV para su posterior análisis.

### ESTRUCTURA CODIGO
1. Importaciones
import matplotlib.pyplot as plt
import time
import subprocess
import csv
import random
import os

Se importan los módulos necesarios para graficación, manejo de tiempo, ejecución de comandos del sistema, escritura de archivos CSV y manejo de archivos.


## Preguntas

1. ¿Qué función cumple ```plt.fignum_exists(self.fig.number)``` en el ciclo principal?

2. ¿Por qué se usa ```time.sleep(self.intervalo)``` y qué pasa si se quita?

3. ¿Qué ventaja tiene usar ```__init__``` para inicializar listas y variables?

4. ¿Qué se está midiendo con ```self.inicio = time.time()```?

5. ¿Qué hace exactamente ```subprocess.check_output(...)```?

6. ¿Por qué se almacena ```ahora = time.time() - self.inicio``` en lugar del tiempo absoluto?

7. ¿Por qué se usa ```self.ax.clear()``` antes de graficar?

8. ¿Qué captura el bloque ```try...except``` dentro de ```leer_temperatura()```?

9. ¿Cómo podría modificar el script para guardar las temperaturas en un archivo .```csv```?
