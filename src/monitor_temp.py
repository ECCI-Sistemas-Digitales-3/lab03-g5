import matplotlib.pyplot as plt
import time
import subprocess
import csv
import random
import os

archivo_csv = 'src/test_datos_Temp.csv'

class MonitorTemperaturaRPI:
    def __init__(self, duracion_max=60, intervalo=0.5, archivo_csv=archivo_csv):

        self.duracion_max = duracion_max
        self.intervalo = intervalo

        self.tiempos = []
        self.temperaturas = []

        self.archivo_csv = archivo_csv # Nombre del archivo CSV        

        self.inicio = time.time() # Guarda el tiempo de inicio


        plt.ion() #Activa la libreria interactiva de matplotlib
        self.fig, self.ax = plt.subplots() # Crea una figura y un eje



        self.ax.set_title("Temperatura CPU Raspberry Pi")

        if not os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Tiempo (s)', 'Temperatura (°C)']) 
                # Escribe los encabezados en el archivo CSV



    def leer_temperatura(self):
        try:
            salida = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
            temp_str = salida.strip().replace("temp=", "").replace("'C", "")
            return float(temp_str)
        except Exception as e:
            print("Error leyendo temperatura:", e)
            return None

    def actualizar_datos(self):
        ahora = time.time() - self.inicio 
        temp = self.leer_temperatura() # Lee la temperatura actual
        if temp is not None:
            self.tiempos.append(ahora) # Guarda el tiempo actual
            self.temperaturas.append(temp) # Guarda la temperatura actual
            self.guardar_datos_csv(ahora, temp) # Guarda los datos en el archivo CSV

            while self.tiempos and self.tiempos[0] < ahora - self.duracion_max:
                self.tiempos.pop(0)
                self.temperaturas.pop(0)

    def graficar(self):
        self.ax.clear()
        self.ax.plot(self.tiempos, self.temperaturas, color='red')
        self.ax.set_title("Temperatura CPU Raspberry Pi")
        self.ax.set_xlabel("Tiempo transcurrido (s)")
        self.ax.set_ylabel("Temperatura (°C)")
        self.ax.grid(True)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def ejecutar(self):
        try:
            while plt.fignum_exists(self.fig.number):
                self.actualizar_datos()
                self.graficar()
                time.sleep(self.intervalo)

        except KeyboardInterrupt:
            print("Monitoreo interrumpido por el usuario.")

        finally:
            print("Monitoreo finalizado.")
            plt.ioff()
            plt.close(self.fig)

    def guardar_datos_csv(self, tiempo, temperatura):
        with open(self.archivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([tiempo, temperatura])


if __name__ == "__main__":
    monitor = MonitorTemperaturaRPI()
    monitor.ejecutar()