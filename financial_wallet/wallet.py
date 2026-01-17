"""
Módulo de análisis financiero para visualización y comparación de acciones.

Este módulo proporciona la clase FinancialWallet que permite descargar,
analizar y visualizar datos históricos de acciones.
"""

import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


class FinancialWallet:
    """
    Clase para gestionar y analizar datos financieros de acciones.

    Atributos:
        ticks (list): Lista de tickers de acciones a analizar.
        start (str): Fecha de inicio en formato 'YYYY-MM-DD'.
        end (str): Fecha de fin en formato 'YYYY-MM-DD'.
        data (pd.DataFrame): Datos descargados de las acciones.
        output_dir (str): Directorio donde se guardarán los archivos.
    """

    def __init__(self, output_dir='data/financial'):
        """
        Inicializa la instancia de FinancialWallet.

        Args:
            output_dir (str): Directorio para guardar archivos de salida.
        """
        self.ticks = []
        self.start = None
        self.end = None
        self.data = None
        self.output_dir = output_dir
        self._ensure_output_dir()

    def _ensure_output_dir(self):
        """Crea el directorio de salida si no existe."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def set_ticks(self):
        """
        Solicita al usuario los tickers de acciones a analizar.

        El usuario puede ingresar uno o más tickers separados por comas.
        Los índices DJI, GSPC e IXIC se convierten automáticamente al formato
        requerido por yfinance (con prefijo ^).
        """
        print("Ingresa los tickers de las acciones separados por comas.")
        print("Ejemplo: 'AAPL, DJI, TSLA'")

        while True:
            user_input = input("Tickers: ")
            ticks_raw = [tick.strip().upper() for tick in user_input.split(",")]

            # Convertir índices al formato correcto
            self.ticks = [
                f"^{tick}" if tick in ["DJI", "GSPC", "IXIC"] else tick
                for tick in ticks_raw
            ]

            if len(self.ticks) > 0:
                break
            print("No ingresaste ningún ticker. Por favor, intenta nuevamente.")

        # Informar al usuario sobre las opciones de comparación
        if len(self.ticks) == 1:
            print("Se ingresó 1 ticker. No se puede realizar comparación.")
        elif len(self.ticks) == 2:
            print("Se ingresaron 2 tickers. Activando comparación...")
        else:
            print(
                f"Se ingresaron {len(self.ticks)} tickers. "
                "Podrás elegir pares para comparar."
            )

    def set_dates(self):
        """
        Solicita las fechas de inicio y fin para el análisis.

        Las fechas deben estar en formato 'YYYY-MM-DD'.
        La fecha de inicio debe ser anterior a la fecha de fin.
        """
        print("Ingresa las fechas en formato 'YYYY-MM-DD'.")
        print("Ejemplo: '2024-01-01'")

        while True:
            try:
                self.start = input("Fecha de inicio: ")
                self.end = input("Fecha de fin: ")

                # Verificar formato de las fechas
                datetime.strptime(self.start, "%Y-%m-%d")
                datetime.strptime(self.end, "%Y-%m-%d")

                if self.start >= self.end:
                    print(
                        "La fecha de inicio debe ser anterior a la fecha de fin. "
                        "Intenta nuevamente."
                    )
                else:
                    break
            except ValueError:
                print(
                    "Formato de fecha inválido. "
                    "Por favor, usa el formato 'YYYY-MM-DD'."
                )

    def download_info(self):
        """
        Descarga los datos históricos de los tickers seleccionados.

        Utiliza yfinance para obtener los datos entre las fechas especificadas.
        """
        try:
            print("Descargando datos...")
            self.data = yf.download(self.ticks, start=self.start, end=self.end)

            if self.data.empty:
                print(
                    "No se encontraron datos para los tickers y fechas ingresados. "
                    "Verifica e inténtalo nuevamente."
                )
            else:
                print("La información ha sido descargada con éxito.")
        except Exception as e:
            print(f"Ocurrió un error al descargar los datos: {e}")

    def show_ticks(self):
        """Muestra los tickers seleccionados."""
        print("\nLos tickers seleccionados son:")
        print(", ".join(self.ticks))

    def show_tick(self, tick):
        """
        Visualiza la serie temporal de precios de cierre para un ticker.

        Args:
            tick (str): Ticker a visualizar.
        """
        if tick not in self.ticks:
            print(f"El ticker {tick} no está incluido en la lista actual.")
            return

        plt.figure(figsize=(10, 6))
        plt.title(f'Serie Temporal de Cierre para {tick}')
        plt.xlabel("Fecha")
        plt.ylabel("Precio USD")
        plt.plot(self.data["Close"][tick], label=tick)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def compare_ticks(self):
        """
        Compara los precios de cierre de dos tickers.

        Esta función solo funciona si hay exactamente 2 tickers en la lista.
        """
        if len(self.ticks) != 2:
            print("Se necesitan exactamente 2 tickers para realizar la comparación.")
            return

        tick1, tick2 = self.ticks[0], self.ticks[1]
        plt.figure(figsize=(10, 6))
        plt.title(f'{tick1} versus {tick2}: Valor de Cierre')
        plt.xlabel(tick1)
        plt.ylabel(tick2)
        plt.plot(self.data["Close"][tick1], self.data["Close"][tick2], 'x')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def compare_multiple_ticks(self):
        """
        Permite seleccionar pares de tickers para comparar cuando hay más de 2.

        El usuario puede realizar múltiples comparaciones hasta que decida salir.
        """
        while True:
            print("\nSelecciona los tickers que deseas comparar:")
            for idx, tick in enumerate(self.ticks, start=1):
                print(f"{idx}. {tick}")

            try:
                choice1 = int(
                    input(f"Selecciona el primer ticker (1-{len(self.ticks)}): ")
                )
                if not 1 <= choice1 <= len(self.ticks):
                    print("Número fuera de rango. Intenta nuevamente.")
                    continue

                chosen_tick1 = self.ticks[choice1 - 1]

                choice2 = int(
                    input(f"Selecciona el segundo ticker (1-{len(self.ticks)}): ")
                )
                if not 1 <= choice2 <= len(self.ticks) or choice2 == choice1:
                    print(
                        "Número fuera de rango o seleccionaste el mismo ticker. "
                        "Intenta nuevamente."
                    )
                    continue

                chosen_tick2 = self.ticks[choice2 - 1]

                # Realizar la comparación
                plt.figure(figsize=(10, 6))
                plt.title(f'{chosen_tick1} versus {chosen_tick2}: Valor de Cierre')
                plt.xlabel(chosen_tick1)
                plt.ylabel(chosen_tick2)
                plt.plot(
                    self.data["Close"][chosen_tick1],
                    self.data["Close"][chosen_tick2],
                    'x'
                )
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.show()

                # Preguntar si desea comparar otro par
                again = input(
                    "¿Quieres comparar otro par de tickers? (S/N): "
                ).strip().upper()
                if again != "S":
                    print("Fin de las comparaciones.")
                    break
            except ValueError:
                print("Entrada inválida. Por favor, selecciona números válidos.")

    def returns(self):
        """
        Calcula y visualiza los retornos diarios de un ticker seleccionado.

        Muestra un histograma de la distribución de retornos.
        """
        while True:
            print("\nSelecciona un ticker para calcular los retornos:")
            for idx, tick in enumerate(self.ticks, start=1):
                print(f"{idx}. {tick}")

            try:
                choice = int(
                    input(f"Selecciona el número (1-{len(self.ticks)}): ")
                )
                if not 1 <= choice <= len(self.ticks):
                    print("Número fuera de rango. Intenta nuevamente.")
                    continue

                chosen_tick = self.ticks[choice - 1]
                returns = self.data["Close"][chosen_tick].pct_change().dropna()

                plt.figure(figsize=(10, 6))
                plt.title(f'Histograma de Retornos de {chosen_tick}')
                plt.xlabel('Retorno')
                plt.ylabel('Frecuencia')
                plt.hist(returns, bins=50, edgecolor='black', alpha=0.7)
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.show()
                break
            except ValueError:
                print("Entrada inválida. Por favor, selecciona un número de la lista.")

        # Preguntar si quiere calcular retornos de otra acción
        again = input(
            "¿Quieres calcular los retornos de otra acción? (S/N): "
        ).strip().upper()
        if again == "S":
            self.returns()

    def analyze_volatility(self):
        """
        Calcula y muestra la volatilidad anualizada de tickers seleccionados.

        La volatilidad se calcula como la desviación estándar de los retornos
        diarios escalada anualmente.
        """
        if self.data is None or self.data.empty:
            print("No hay datos disponibles. Descarga los datos primero.")
            return

        while True:
            print("\nSelecciona un ticker para calcular la volatilidad:")
            for idx, tick in enumerate(self.ticks, start=1):
                print(f"{idx}. {tick}")

            try:
                choice = int(
                    input(f"Selecciona el número (1-{len(self.ticks)}): ")
                )
                if not 1 <= choice <= len(self.ticks):
                    print("Número fuera de rango. Intenta nuevamente.")
                    continue

                chosen_tick = self.ticks[choice - 1]
                returns = self.data["Close"][chosen_tick].pct_change().dropna()
                volatility = returns.std() * (252 ** 0.5)  # Anualizada

                print(
                    f"\nLa volatilidad anualizada de {chosen_tick} "
                    f"es: {volatility:.2%}"
                )

                # Preguntar si desea continuar
                another = input(
                    "¿Quieres calcular la volatilidad de otra acción? (S/N): "
                ).strip().upper()
                if another != 'S':
                    print("Análisis de volatilidad finalizado.")
                    break
            except ValueError:
                print("Entrada inválida. Por favor, selecciona un número de la lista.")

    def export_data(self):
        """
        Exporta los datos descargados a un archivo CSV.

        El archivo se guarda en el directorio de salida especificado.
        """
        if self.data is None or self.data.empty:
            print(
                "No hay datos disponibles para exportar. "
                "Asegúrate de descargar primero los datos."
            )
            return

        while True:
            print("\n¿Quieres exportar los datos?")
            print("1. Sí, exportar a CSV")
            print("2. Cancelar")

            try:
                choice = int(input("Selecciona el número (1-2): "))
                if choice == 1:
                    file_name = input(
                        "Ingresa el nombre del archivo (sin extensión): "
                    )
                    file_path = os.path.join(self.output_dir, f"{file_name}.csv")
                    self.data.to_csv(file_path)
                    print(f"Datos exportados exitosamente a {file_path}.")
                    break
                elif choice == 2:
                    print("Exportación cancelada.")
                    break
                else:
                    print("Opción inválida. Intenta nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, selecciona un número de la lista.")


def main():
    """
    Función principal para ejecutar el análisis financiero.

    Guía al usuario a través del proceso completo de configuración,
    descarga de datos y análisis.
    """
    # Inicialización
    wallet = FinancialWallet()

    # Configuración
    wallet.set_ticks()
    wallet.set_dates()
    wallet.download_info()

    # Verificar que se descargaron datos
    if wallet.data is None or wallet.data.empty:
        print("No se pudieron descargar datos. Saliendo del programa.")
        return

    # Uso de funcionalidades
    wallet.show_ticks()

    # Comparación de tickers
    if len(wallet.ticks) == 2:
        wallet.compare_ticks()
    elif len(wallet.ticks) > 2:
        wallet.compare_multiple_ticks()

    # Análisis de retornos
    wallet.returns()

    # Análisis de volatilidad
    wallet.analyze_volatility()

    # Exportación de datos
    wallet.export_data()


if __name__ == "__main__":
    main()
