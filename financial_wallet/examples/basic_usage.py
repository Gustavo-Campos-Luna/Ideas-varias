"""
Ejemplos de uso básico de Financial Wallet.

Este script muestra diferentes formas de usar la clase FinancialWallet
para analizar datos financieros.
"""

from financial_wallet import FinancialWallet


def ejemplo_interactivo():
    """
    Ejemplo de uso interactivo completo.

    El usuario ingresa todos los datos manualmente.
    """
    print("="*70)
    print("EJEMPLO 1: USO INTERACTIVO COMPLETO")
    print("="*70)

    wallet = FinancialWallet()

    # Configuración interactiva
    wallet.set_ticks()
    wallet.set_dates()
    wallet.download_info()

    # Verificar que se descargaron datos
    if wallet.data is None or wallet.data.empty:
        print("No se pudieron descargar datos.")
        return

    # Mostrar tickers
    wallet.show_ticks()

    # Comparación según número de tickers
    if len(wallet.ticks) == 2:
        wallet.compare_ticks()
    elif len(wallet.ticks) > 2:
        wallet.compare_multiple_ticks()

    # Análisis de retornos
    wallet.returns()

    # Análisis de volatilidad
    wallet.analyze_volatility()

    # Exportar datos
    wallet.export_data()


def ejemplo_programatico():
    """
    Ejemplo de uso programático (sin interacción del usuario).

    Todos los parámetros se configuran en el código.
    """
    print("\n" + "="*70)
    print("EJEMPLO 2: USO PROGRAMÁTICO")
    print("="*70)

    # Crear instancia
    wallet = FinancialWallet()

    # Configuración manual
    wallet.ticks = ['AAPL', 'GOOGL']
    wallet.start = '2024-01-01'
    wallet.end = '2024-12-31'

    print(f"\nAnalizando: {', '.join(wallet.ticks)}")
    print(f"Período: {wallet.start} a {wallet.end}")

    # Descargar datos
    wallet.download_info()

    # Verificar datos
    if wallet.data is None or wallet.data.empty:
        print("No se pudieron descargar datos.")
        return

    # Mostrar información básica
    print("\nDatos descargados exitosamente.")
    print(f"Forma del DataFrame: {wallet.data.shape}")

    # Mostrar ticker individual
    wallet.show_tick('AAPL')

    # Comparar los dos tickers
    wallet.compare_ticks()


def ejemplo_analisis_volatilidad():
    """
    Ejemplo enfocado en análisis de volatilidad.

    Compara la volatilidad de múltiples acciones tecnológicas.
    """
    print("\n" + "="*70)
    print("EJEMPLO 3: ANÁLISIS DE VOLATILIDAD")
    print("="*70)

    # Crear instancia
    wallet = FinancialWallet()

    # Configurar múltiples acciones tecnológicas
    wallet.ticks = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']
    wallet.start = '2023-01-01'
    wallet.end = '2024-12-31'

    print(f"\nAnalizando volatilidad de: {', '.join(wallet.ticks)}")

    # Descargar datos
    wallet.download_info()

    if wallet.data is None or wallet.data.empty:
        print("No se pudieron descargar datos.")
        return

    # Calcular volatilidad para cada ticker
    print("\n" + "-"*70)
    print("VOLATILIDAD ANUALIZADA")
    print("-"*70)

    for tick in wallet.ticks:
        returns = wallet.data["Close"][tick].pct_change().dropna()
        volatility = returns.std() * (252 ** 0.5)
        print(f"{tick:10s}: {volatility:>6.2%}")

    print("-"*70)


def ejemplo_indices():
    """
    Ejemplo de uso con índices del mercado.

    Analiza índices principales como DJI, S&P 500, y NASDAQ.
    """
    print("\n" + "="*70)
    print("EJEMPLO 4: ANÁLISIS DE ÍNDICES")
    print("="*70)

    # Crear instancia
    wallet = FinancialWallet()

    # Configurar índices (se convierten automáticamente al formato correcto)
    wallet.ticks = ['^DJI', '^GSPC', '^IXIC']
    wallet.start = '2024-01-01'
    wallet.end = '2024-12-31'

    print(f"\nAnalizando índices: DJI, S&P 500, NASDAQ")

    # Descargar datos
    wallet.download_info()

    if wallet.data is None or wallet.data.empty:
        print("No se pudieron descargar datos.")
        return

    # Mostrar cada índice
    for tick in wallet.ticks:
        print(f"\nVisualizando {tick}...")
        wallet.show_tick(tick)


def ejemplo_exportacion():
    """
    Ejemplo de descarga y exportación de datos.

    Descarga datos y los exporta a CSV.
    """
    print("\n" + "="*70)
    print("EJEMPLO 5: EXPORTACIÓN DE DATOS")
    print("="*70)

    # Crear instancia con directorio personalizado
    wallet = FinancialWallet(output_dir='data/financial/ejemplos')

    # Configurar
    wallet.ticks = ['AAPL', 'MSFT']
    wallet.start = '2024-01-01'
    wallet.end = '2024-12-31'

    print(f"\nDescargando datos de: {', '.join(wallet.ticks)}")

    # Descargar
    wallet.download_info()

    if wallet.data is None or wallet.data.empty:
        print("No se pudieron descargar datos.")
        return

    # Exportar programáticamente
    import os
    file_path = os.path.join(wallet.output_dir, 'tech_stocks_2024.csv')
    wallet.data.to_csv(file_path)
    print(f"\nDatos exportados a: {file_path}")


def main():
    """
    Función principal que ejecuta todos los ejemplos.

    Comenta los ejemplos que no quieras ejecutar.
    """
    print("\n")
    print("="*70)
    print("EJEMPLOS DE USO - FINANCIAL WALLET")
    print("="*70)

    # Descomentar el ejemplo que quieras ejecutar

    # Ejemplo 1: Interactivo completo
    # ejemplo_interactivo()

    # Ejemplo 2: Uso programático
    ejemplo_programatico()

    # Ejemplo 3: Análisis de volatilidad
    # ejemplo_analisis_volatilidad()

    # Ejemplo 4: Análisis de índices
    # ejemplo_indices()

    # Ejemplo 5: Exportación de datos
    # ejemplo_exportacion()

    print("\n" + "="*70)
    print("EJEMPLOS COMPLETADOS")
    print("="*70)


if __name__ == "__main__":
    main()
