"""
Ejemplos de uso básico de Weather Scraper.

Este script muestra diferentes formas de usar la clase WeatherScraper
para extraer datos meteorológicos.
"""

from weather_scraper import WeatherScraper


def ejemplo_interactivo():
    """
    Ejemplo de uso interactivo.

    El usuario ingresa el nombre de la ciudad manualmente.
    """
    print("="*70)
    print("EJEMPLO 1: USO INTERACTIVO")
    print("="*70)

    scraper = WeatherScraper()
    scraper.run()


def ejemplo_programatico():
    """
    Ejemplo de uso programático (sin interacción del usuario).

    La ciudad se especifica en el código.
    """
    print("\n" + "="*70)
    print("EJEMPLO 2: USO PROGRAMÁTICO")
    print("="*70)

    # Crear instancia
    scraper = WeatherScraper()

    # Ejecutar con ciudad específica
    ciudad = "Santiago"
    print(f"\nObteniendo datos para: {ciudad}")

    df = scraper.run(ciudad=ciudad)

    # Mostrar resultados
    if df is not None:
        print("\nDatos obtenidos:")
        print(df)
        print(f"\nTotal de días: {len(df)}")


def ejemplo_multiples_ciudades():
    """
    Ejemplo de extracción de múltiples ciudades.

    Extrae datos de varias ciudades en una sola ejecución.
    """
    print("\n" + "="*70)
    print("EJEMPLO 3: MÚLTIPLES CIUDADES")
    print("="*70)

    # Lista de ciudades a consultar
    ciudades = ["Santiago", "Valparaíso", "Concepción", "La Serena"]

    # Crear instancia
    scraper = WeatherScraper()

    # Diccionario para almacenar resultados
    resultados = {}

    print(f"\nExtrayendo datos de {len(ciudades)} ciudades...\n")

    for ciudad in ciudades:
        print(f"\nProcesando: {ciudad}")
        print("-" * 50)

        # Crear nueva instancia para cada ciudad
        scraper = WeatherScraper()
        df = scraper.run(ciudad=ciudad)

        if df is not None:
            resultados[ciudad] = df
            print(f"✓ {ciudad}: {len(df)} días de pronóstico")
        else:
            print(f"✗ {ciudad}: Error al obtener datos")

    # Resumen
    print("\n" + "="*70)
    print("RESUMEN")
    print("="*70)
    print(f"Ciudades exitosas: {len(resultados)}/{len(ciudades)}")

    for ciudad, df in resultados.items():
        print(f"  - {ciudad}: {len(df)} días")


def ejemplo_directorio_personalizado():
    """
    Ejemplo con directorio de salida personalizado.

    Los archivos se guardan en una ubicación específica.
    """
    print("\n" + "="*70)
    print("EJEMPLO 4: DIRECTORIO PERSONALIZADO")
    print("="*70)

    # Crear instancia con directorio personalizado
    output_dir = "data/weather/chile"
    scraper = WeatherScraper(output_dir=output_dir)

    print(f"\nArchivos se guardarán en: {output_dir}")

    # Ejecutar
    ciudad = "Viña del Mar"
    df = scraper.run(ciudad=ciudad)

    if df is not None:
        print(f"\nDatos guardados en: {output_dir}")


def ejemplo_analisis_datos():
    """
    Ejemplo de análisis básico de los datos extraídos.

    Extrae datos y realiza un análisis simple.
    """
    print("\n" + "="*70)
    print("EJEMPLO 5: ANÁLISIS DE DATOS")
    print("="*70)

    # Crear instancia
    scraper = WeatherScraper()

    # Ejecutar
    ciudad = "Santiago"
    print(f"\nExtrayendo datos de: {ciudad}")

    df = scraper.run(ciudad=ciudad)

    if df is None:
        print("No se pudieron obtener datos.")
        return

    # Análisis básico
    print("\n" + "-"*70)
    print("ANÁLISIS DE DATOS")
    print("-"*70)

    print(f"\nTotal de días en pronóstico: {len(df)}")

    print("\nPrimeros 3 días:")
    print(df.head(3).to_string(index=False))

    print("\nÚltimos 3 días:")
    print(df.tail(3).to_string(index=False))

    # Información de columnas
    print("\nColumnas disponibles:")
    for col in df.columns:
        print(f"  - {col}")

    print("\nInformación del DataFrame:")
    print(df.info())


def ejemplo_manejo_errores():
    """
    Ejemplo de manejo de errores.

    Muestra cómo manejar ciudades no encontradas o errores de conexión.
    """
    print("\n" + "="*70)
    print("EJEMPLO 6: MANEJO DE ERRORES")
    print("="*70)

    # Lista con ciudades válidas e inválidas
    ciudades = [
        "Santiago",           # Válida
        "CiudadInexistente", # Inválida
        "Valparaíso"         # Válida
    ]

    for ciudad in ciudades:
        print(f"\nIntentando extraer datos de: {ciudad}")
        print("-" * 50)

        scraper = WeatherScraper()
        df = scraper.run(ciudad=ciudad)

        if df is not None:
            print(f"✓ Éxito: {len(df)} días de pronóstico")
        else:
            print(f"✗ Error: No se pudieron obtener datos")


def main():
    """
    Función principal que ejecuta todos los ejemplos.

    Comenta los ejemplos que no quieras ejecutar.
    """
    print("\n")
    print("="*70)
    print("EJEMPLOS DE USO - WEATHER SCRAPER")
    print("="*70)
    print("\nNOTA: Estos ejemplos requieren ChromeDriver instalado.")
    print("      Ver README.md para instrucciones de instalación.")
    print("="*70)

    # Descomentar el ejemplo que quieras ejecutar

    # Ejemplo 1: Interactivo
    # ejemplo_interactivo()

    # Ejemplo 2: Programático
    ejemplo_programatico()

    # Ejemplo 3: Múltiples ciudades
    # ADVERTENCIA: Este ejemplo puede tomar varios minutos
    # ejemplo_multiples_ciudades()

    # Ejemplo 4: Directorio personalizado
    # ejemplo_directorio_personalizado()

    # Ejemplo 5: Análisis de datos
    # ejemplo_analisis_datos()

    # Ejemplo 6: Manejo de errores
    # ejemplo_manejo_errores()

    print("\n" + "="*70)
    print("EJEMPLOS COMPLETADOS")
    print("="*70)
    print("\nLos archivos generados están en el directorio 'data/weather/'")


if __name__ == "__main__":
    main()
