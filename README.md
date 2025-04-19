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

-Se importan los módulos necesarios para graficación, manejo de tiempo, ejecución de comandos del sistema, escritura de archivos CSV y manejo de archivos.

2. Configuración del archivo CSV

archivo_csv = 'src/test_datos_Temp.csv'

Define la ruta del archivo donde se almacenarán los datos históricos de temperatura.

### CLASE: MonitorTemperaturaRPI

def __init__(self, duracion_max=60, intervalo=0.5, archivo_csv=archivo_csv)

duracion_max: Duración máxima (en segundos) para mantener los datos en la gráfica (por defecto: 60s).

intervalo: Tiempo de espera entre lecturas de temperatura (en segundos).

archivo_csv: Ruta del archivo donde se guardan los datos recolectados.

*Inicializa:*

Listas para almacenar el tiempo transcurrido y las temperaturas.

El archivo CSV, escribiendo encabezados si no existe.

Una figura interactiva (matplotlib) para graficar en tiempo real.

### MÉTODOS: 

# *Leer_temperatura()*

--def leer_temperatura(self)

Ejecuta el comando vcgencmd measure_temp para obtener la temperatura actual del CPU. Devuelve el valor como float. En caso de error, devuelve None.

# *Actualizar_datos()*

--def actualizar_datos(self)

Calcula el tiempo transcurrido desde el inicio. Llama a leer_temperatura() para obtener la temperatura. Almacena tiempo y temperatura en listas y en el archivo CSV. Elimina datos antiguos si exceden la duracion_max.

# *graficar()*

--def graficar(self)

Limpia el gráfico actual. Dibuja una línea roja con los datos actualizados. Añade títulos, etiquetas de ejes y grilla. Actualiza el canvas gráfico en tiempo real.

# *ejecutar()*

--def ejecutar(self)

Ciclo principal del programa.

Mientras la ventana de la gráfica esté activa: Actualiza los datos, redibuja la gráfica, espera el intervalo definido.

Se puede interrumpir con Ctrl+C, cerrando limpiamente la interfaz gráfica.

# *guardar_datos_csv()*

--def guardar_datos_csv(self, tiempo, temperatura)

Abre el archivo CSV en modo de anexado y escribe una nueva línea con el tiempo y la temperatura actual.


### BLOQUE PRINCIPAL DE LA EJECUCIÓN

if __name__ == "__main__":
    monitor = MonitorTemperaturaRPI()
    monitor.ejecutar()

Instancia la clase y ejecuta el proceso de monitoreo si el archivo es ejecutado directamente como script.


### SALIDA ESPERADA

Gráfica en tiempo real que muestra la evolución de la temperatura del CPU en función del tiempo.
Archivo CSV con registros históricos con formato:

Tiempo (s), Temperatura (°C)

1.0, 53.2
1.5, 53.6

### FINAL

La clase MonitorTemperaturaRPI encapsula toda la funcionalidad, haciendo el código modular, reutilizable y fácilmente integrable en otros sistemas de monitoreo o automatización.

## Preguntas

1. ¿Qué función cumple ```plt.fignum_exists(self.fig.number)``` en el ciclo principal?

Verifica si la ventana de la figura de matplotlib sigue abierta. Permite que el ciclo de monitoreo se ejecute solo mientras la ventana gráfica esté activa. Cuando el usuario cierra la ventana, la condición se vuelve falsa y el bucle se detiene limpiamente.

2. ¿Por qué se usa ```time.sleep(self.intervalo)``` y qué pasa si se quita?

Se utiliza para pausar la ejecución del bucle durante un tiempo definido (intervalo) entre cada lectura de temperatura. Esto reduce la carga sobre el sistema y establece una frecuencia constante de muestreo.

Si se elimina, el bucle se ejecutaría de forma continua sin pausas, generando un exceso de lecturas, sobrecargando la CPU y dificultando la visualización en tiempo real.

3. ¿Qué ventaja tiene usar ```__init__``` para inicializar listas y variables?

Permite establecer el estado inicial del objeto al momento de su creación. Sus ventajas son: encapsula toda la configuración y variables necesarias para el funcionamiento del objeto. Evita errores por variables no inicializadas. Facilita la reutilización y personalización del objeto mediante parámetros.

4. ¿Qué se está midiendo con ```self.inicio = time.time()```?

Captura el tiempo en segundos desde la época UNIX al inicio del monitoreo. Se usa como referencia para calcular el tiempo transcurrido desde que comenzó el script, útil para representar el eje X en la gráfica.

5. ¿Qué hace exactamente ```subprocess.check_output(...)```?

Ejecuta un comando del sistema operativo desde Python (en este caso, vcgencmd measure_temp) y captura su salida como texto. Permite obtener datos del sistema, como la temperatura del CPU, desde la terminal sin intervención del usuario

6. ¿Por qué se almacena ```ahora = time.time() - self.inicio``` en lugar del tiempo absoluto?

Se calcula el tiempo transcurrido desde que inició el monitoreo para: Mostrar valores relativos más comprensibles en la gráfica (por ejemplo, “25 segundos desde el inicio”). Evitar trabajar con timestamps absolutos que son más difíciles de leer y graficar.

8. ¿Por qué se usa ```self.ax.clear()``` antes de graficar?

9. ¿Qué captura el bloque ```try...except``` dentro de ```leer_temperatura()```?

10. ¿Cómo podría modificar el script para guardar las temperaturas en un archivo .```csv```?
