"""
Módulo de scraping de datos meteorológicos usando Selenium.

Este módulo proporciona la clase WeatherScraper para extraer datos
del sitio web Meteored.
"""

import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

from . import config


class WeatherScraper:
    """
    Scraper de datos meteorológicos usando Selenium.

    Esta clase maneja la configuración del navegador, la búsqueda de ciudades
    y la extracción de datos meteorológicos del sitio Meteored.

    Atributos:
        driver: Instancia del WebDriver de Selenium.
        ciudad (str): Ciudad a buscar.
        output_dir (str): Directorio donde se guardan los archivos.
    """

    def __init__(self, output_dir=None):
        """
        Inicializa el WeatherScraper.

        Args:
            output_dir (str, optional): Directorio para guardar archivos.
                Si es None, usa el definido en config.
        """
        self.driver = None
        self.ciudad = None
        self.output_dir = output_dir or config.OUTPUT_DIR
        self._ensure_output_dir()

    def _ensure_output_dir(self):
        """Crea el directorio de salida si no existe."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def _configurar_driver(self):
        """
        Configura y retorna el WebDriver de Chrome.

        Returns:
            webdriver.Chrome: Instancia configurada del WebDriver.

        Raises:
            WebDriverException: Si no se puede inicializar el driver.
        """
        options = webdriver.ChromeOptions()

        # Agregar opciones desde config
        for option in config.CHROME_OPTIONS:
            options.add_argument(option)

        try:
            # Intentar obtener la ruta del chromedriver
            driver_path = config.get_chromedriver_path()

            if driver_path:
                print(f"Usando ChromeDriver en: {driver_path}")
                service = Service(driver_path)
                driver = webdriver.Chrome(service=service, options=options)
            else:
                print(
                    "No se encontró ChromeDriver en el sistema. "
                    "Intentando usar el driver del PATH..."
                )
                # Intentar sin especificar la ruta (usa PATH)
                driver = webdriver.Chrome(options=options)

            return driver

        except WebDriverException as e:
            print("\n" + "="*70)
            print("ERROR: No se pudo inicializar ChromeDriver")
            print("="*70)
            print("\nPor favor, sigue estos pasos:")
            print("1. Descarga ChromeDriver desde:")
            print("   https://chromedriver.chromium.org/downloads")
            print("2. Extrae el ejecutable")
            print("3. Agrega la ruta al PATH del sistema, o")
            print("4. Colócalo en una de estas ubicaciones:")

            import platform
            system = platform.system()
            if system == 'Windows':
                print("   - C:\\chromedriver\\chromedriver.exe")
                print("   - %USERPROFILE%\\chromedriver\\chromedriver.exe")
            elif system == 'Linux':
                print("   - /usr/local/bin/chromedriver")
                print("   - /usr/bin/chromedriver")
            else:  # macOS
                print("   - /usr/local/bin/chromedriver")
                print("   - /opt/homebrew/bin/chromedriver")

            print("\n" + "="*70)
            raise WebDriverException(
                f"No se pudo inicializar ChromeDriver: {e}"
            ) from e

    def _buscar_ciudad(self, ciudad):
        """
        Busca una ciudad en el sitio web.

        Args:
            ciudad (str): Nombre de la ciudad a buscar.

        Raises:
            TimeoutException: Si no se puede encontrar el elemento de búsqueda.
        """
        self.driver.get(config.WEATHER_URL)

        try:
            search_box = WebDriverWait(self.driver, config.WAIT_TIMEOUT).until(
                EC.element_to_be_clickable((By.ID, "search_pc"))
            )
            search_box.clear()
            search_box.send_keys(ciudad)
            search_box.send_keys('\ue007')  # Presionar Enter
            print(f"Buscando información para: {ciudad}")
        except TimeoutException as e:
            raise TimeoutException(
                "No se pudo encontrar el cuadro de búsqueda. "
                "Verifica la conexión o el sitio web."
            ) from e

    def _extraer_informacion(self):
        """
        Extrae la información meteorológica de la página.

        Returns:
            pd.DataFrame: DataFrame con los datos extraídos.

        Raises:
            TimeoutException: Si no se puede encontrar la información.
        """
        try:
            bloque_texto = WebDriverWait(
                self.driver,
                config.WAIT_TIMEOUT
            ).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dias_w"))
            ).text

            lineas = bloque_texto.split("\n")
            dias, fechas, temperaturas, vientos = [], [], [], []

            # Procesar bloques de 4 líneas
            for i in range(0, len(lineas), 4):
                if i + 3 < len(lineas):
                    dias.append(lineas[i])
                    fechas.append(lineas[i + 1])
                    temperaturas.append(lineas[i + 2])
                    vientos.append(lineas[i + 3])

            df = pd.DataFrame({
                "Día": dias,
                "Fecha": fechas,
                "Temperatura": temperaturas,
                "Viento": vientos
            })

            print("\nDatos extraídos:")
            print(df)
            return df

        except TimeoutException as e:
            raise TimeoutException(
                "No se pudo extraer la información meteorológica. "
                "La ciudad puede no estar disponible o el sitio cambió su estructura."
            ) from e
        except Exception as e:
            raise Exception(f"Error al procesar los datos: {e}") from e

    def _guardar_datos(self, df, ciudad):
        """
        Guarda el DataFrame en archivos CSV y Excel.

        Args:
            df (pd.DataFrame): DataFrame con los datos a guardar.
            ciudad (str): Nombre de la ciudad (usado para el nombre del archivo).
        """
        # Limpiar nombre de ciudad para usar en archivo
        ciudad_limpia = ciudad.replace(" ", "_").lower()

        archivo_csv = os.path.join(
            self.output_dir,
            f"resultados_{ciudad_limpia}.csv"
        )
        archivo_excel = os.path.join(
            self.output_dir,
            f"resultados_{ciudad_limpia}.xlsx"
        )

        try:
            # Guardar CSV
            df.to_csv(archivo_csv, index=False, encoding="utf-8-sig")
            print(f"\nDatos guardados en: {archivo_csv}")

            # Guardar Excel
            df.to_excel(archivo_excel, index=False, engine="openpyxl")
            print(f"Datos guardados en: {archivo_excel}")

        except Exception as e:
            print(f"\nError al guardar los datos: {e}")
            raise

    def run(self, ciudad=None):
        """
        Ejecuta el flujo completo del scraper.

        Args:
            ciudad (str, optional): Ciudad a buscar. Si es None, solicita al usuario.

        Returns:
            pd.DataFrame: DataFrame con los datos extraídos, o None si hay error.
        """
        try:
            # Configurar driver
            print("Configurando navegador...")
            self.driver = self._configurar_driver()

            # Obtener ciudad si no se proporcionó
            if ciudad is None:
                ciudad = input("Ingresa el nombre de la ciudad a buscar: ")

            self.ciudad = ciudad

            # Buscar ciudad
            self._buscar_ciudad(ciudad)

            # Esperar carga de la página
            time.sleep(5)

            # Extraer información
            df = self._extraer_informacion()

            # Guardar datos
            self._guardar_datos(df, ciudad)

            print("\nProceso completado exitosamente.")
            return df

        except WebDriverException as e:
            print(f"\nError del WebDriver: {e}")
            return None
        except TimeoutException as e:
            print(f"\nError de timeout: {e}")
            return None
        except Exception as e:
            print(f"\nSe produjo un error: {e}")
            return None
        finally:
            if self.driver:
                print("\nCerrando navegador...")
                self.driver.quit()


def main():
    """
    Función principal para ejecutar el scraper.

    Esta función crea una instancia del scraper y ejecuta el flujo completo.
    """
    scraper = WeatherScraper()
    scraper.run()


if __name__ == "__main__":
    main()
