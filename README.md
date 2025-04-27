[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19144093&assignment_repo_type=AssignmentRepo)
# Lab03: Visualización de Datos en Raspberry Pi Zero W

# Lab03: Visualización de Datos en Raspberry Pi Zero W

## Integrantes

- [David Santiago Laiton Gutierrez](https://github.com/dslaitong)
- [Edgar Giovanni Neira Lugo](https://github.com/Gioneira)
- [Johana Stephany Toro Echeverria](https://github.com/JohanaT97)

## Documentación

### MÉTODOS PRINCIPALES

#### 1. `__init__(self, duracion_max=60, intervalo=0.5, archivo_csv=archivo_csv)`
- **Propósito**: Constructor de la clase que inicializa el monitor de temperatura
- **Parámetros**:
  - `duracion_max`: Tiempo máximo en segundos para mantener datos (default: 60s)
  - `intervalo`: Tiempo entre lecturas de temperatura (default: 0.5s)
  - `archivo_csv`: Ruta del archivo para almacenar datos
- **Funcionamiento**:
  - Inicializa listas vacías para tiempos y temperaturas
  - Configura el archivo CSV
  - Prepara la interfaz gráfica de matplotlib

#### 2. `leer_temperatura(self)`
- **Propósito**: Obtiene la temperatura actual del CPU
- **Retorno**: 
  - Float: Temperatura en grados Celsius
  - None: En caso de error
- **Funcionamiento**:
  - Ejecuta comando vcgencmd
  - Procesa la salida para extraer el valor numérico
  - Maneja posibles errores de ejecución

#### 3. `actualizar_datos(self)`
- **Propósito**: Actualiza las listas de datos con nuevas lecturas
- **Funcionamiento**:
  - Calcula tiempo transcurrido
  - Obtiene nueva temperatura
  - Almacena datos en listas
  - Guarda en CSV
  - Elimina datos antiguos fuera de ventana temporal

#### 4. `graficar(self)`
- **Propósito**: Actualiza la visualización gráfica en tiempo real
- **Funcionamiento**:
  - Limpia gráfico anterior
  - Dibuja nuevos datos
  - Actualiza títulos y etiquetas
  - Refresca visualización

#### 5. `ejecutar(self)`
- **Propósito**: Inicia el ciclo principal de monitoreo
- **Funcionamiento**:
  - Ejecuta bucle mientras la ventana esté abierta
  - Actualiza datos y gráfica periódicamente
  - Maneja interrupciones de usuario
  - Cierra recursos al finalizar

#### 6. `guardar_datos_csv(self, tiempo, temperatura)`
- **Propósito**: Almacena los datos en archivo CSV
- **Parámetros**:
  - `tiempo`: Tiempo transcurrido en segundos
  - `temperatura`: Valor de temperatura medido
- **Funcionamiento**:
  - Abre archivo en modo append
  - Escribe nueva línea con tiempo y temperatura

### INTRODUCCIÓN
Este script implementa una herramienta de monitoreo en tiempo real de la temperatura del procesador de una Raspberry. Utiliza matplotlib para graficar dinámicamente los datos obtenidos desde el sistema mediante el comando vcgencmd. Además, los datos recolectados se almacenan en un archivo CSV para su posterior análisis.

### DIAGRAMA DE FLUJO

El siguiente diagrama representa el flujo de ejecución del monitor de temperatura, ilustrando los procesos principales y la lógica del programa:

![Diagrama de Flujo](src/img/Diagrama%20de%20Flujo.png)

El diagrama muestra:
- Proceso de inicialización del monitor
- Verificación y creación del archivo CSV
- Ciclo principal de monitoreo
- Procesos de actualización de datos
- Visualización gráfica en tiempo real
- Lógica de finalización del programa

// ...existing code...

### ESTRUCTURA DEL CÓDIGO

#### 1. Importaciones

```python
import matplotlib.pyplot as plt
import time
import subprocess
import csv
import random
import os
```
MÉTODOS:
1. leer_temperatura()

Ejecuta el comando vcgencmd measure_temp para obtener la temperatura actual del CPU. Devuelve el valor como float. En caso de error, devuelve None.

2. actualizar_datos()

Calcula el tiempo transcurrido desde el inicio. Llama a leer_temperatura() para obtener la temperatura. Almacena tiempo y temperatura en listas y en el archivo CSV. Elimina datos antiguos si exceden la duracion_max.

3. graficar()

Limpia el gráfico actual. Dibuja una línea roja con los datos actualizados. Añade títulos, etiquetas de ejes y grilla. Actualiza el canvas gráfico en tiempo real.

4. ejecutar()

Ciclo principal del programa.

Mientras la ventana de la gráfica esté activa: Actualiza los datos, redibuja la gráfica, espera el intervalo definido.

Se puede interrumpir con Ctrl+C, cerrando limpiamente la interfaz gráfica

5. guardar_datos_csv()

Abre el archivo CSV en modo de anexado y escribe una nueva línea con el tiempo y la temperatura actual.

BLOQUE PRINCIPAL DE LA EJECUCIÓN

````
if __name__ == "__main__":
    monitor = MonitorTemperaturaRPI()
    monitor.ejecutar()
````
Instancia la clase y ejecuta el proceso de monitoreo si el archivo es ejecutado directamente como script.

SALIDA ESPERADA

Gráfica en tiempo real que muestra la evolución de la temperatura del CPU en función del tiempo.

Archivo CSV con registros históricos con formato:

````
Tiempo (s), Temperatura (°C)
1.0, 53.2
1.5, 53.6
````

FINAL
La clase MonitorTemperaturaRPI encapsula toda la funcionalidad, haciendo el código modular, reutilizable y fácilmente integrable en otros sistemas de monitoreo o automatización.

Preguntas
¿Qué función cumple plt.fignum_exists(self.fig.number) en el ciclo principal?

Verifica si la ventana de la figura de matplotlib sigue abierta. Permite que el ciclo de monitoreo se ejecute solo mientras la ventana gráfica esté activa. Cuando el usuario cierra la ventana, la condición se vuelve falsa y el bucle se detiene limpiamente.

¿Por qué se usa time.sleep(self.intervalo) y qué pasa si se quita?

Se utiliza para pausar la ejecución del bucle durante un tiempo definido (intervalo) entre cada lectura de temperatura. Esto reduce la carga sobre el sistema y establece una frecuencia constante de muestreo.

Si se elimina, el bucle se ejecutaría de forma continua sin pausas, generando un exceso de lecturas, sobrecargando la CPU y dificultando la visualización en tiempo real.

¿Qué ventaja tiene usar __init__ para inicializar listas y variables?

Permite establecer el estado inicial del objeto al momento de su creación. Sus ventajas son: encapsula toda la configuración y variables necesarias para el funcionamiento del objeto. Evita errores por variables no inicializadas. Facilita la reutilización y personalización del objeto mediante parámetros.

¿Qué se está midiendo con self.inicio = time.time()?

Captura el tiempo en segundos desde la época UNIX al inicio del monitoreo. Se usa como referencia para calcular el tiempo transcurrido desde que comenzó el script, útil para representar el eje X en la gráfica.

¿Qué hace exactamente subprocess.check_output(...)?

Ejecuta un comando del sistema operativo desde Python (en este caso, vcgencmd measure_temp) y captura su salida como texto. Permite obtener datos del sistema, como la temperatura del CPU, desde la terminal sin intervención del usuario.

¿Por qué se almacena ahora = time.time() - self.inicio en lugar del tiempo absoluto?

Se calcula el tiempo transcurrido desde que inició el monitoreo para: Mostrar valores relativos más comprensibles en la gráfica (por ejemplo, “25 segundos desde el inicio”). Evitar trabajar con timestamps absolutos que son más difíciles de leer y graficar.

¿Por qué se usa self.ax.clear() antes de graficar?

Se limpia el contenido previo del eje (ax) para evitar que las gráficas antiguas se dibujen encima de las nuevas. Permite una visualización clara y actualizada de los datos en cada iteración.

¿Qué captura el bloque try...except dentro de leer_temperatura()?

Captura cualquier error que pueda ocurrir al ejecutar el comando externo o convertir el resultado en número. Por ejemplo: Si el comando vcgencmd falla. Si el formato de salida cambia. Si la conversión a float lanza una excepción.

Esto evita que el programa se detenga por errores puntuales durante la lectura.

¿Cómo podría modificar el script para guardar las temperaturas en un archivo .csv?

Cambia la ruta del archivo CSV en el parámetro archivo_csv del constructor. Agregar una marca de tiempo legible (datetime.now()) si se quiere formato de fecha real.// ...existing code...

