"""
Archivo de configuración para Weather Scraper.

Configuración de rutas, opciones del navegador y parámetros generales.
"""

import os
import platform


# Directorio de salida para datos
OUTPUT_DIR = 'data/weather'

# URL del sitio meteorológico
WEATHER_URL = 'https://www.meteored.cl/'

# Timeout para esperas del navegador (en segundos)
WAIT_TIMEOUT = 10

# Opciones del navegador Chrome
CHROME_OPTIONS = [
    '--start-maximized',
    '--incognito',
    # Descomentar la siguiente línea para modo headless (sin ventana)
    # '--headless',
]


def get_chromedriver_path():
    """
    Obtiene la ruta del ChromeDriver según el sistema operativo.

    Esta función intenta detectar automáticamente la ubicación del ChromeDriver.
    Si no lo encuentra, devuelve None y el usuario debe configurarlo manualmente.

    Returns:
        str or None: Ruta al ejecutable de ChromeDriver o None si no se encuentra.
    """
    system = platform.system()

    # Intentar encontrar ChromeDriver en PATH
    chromedriver_name = 'chromedriver.exe' if system == 'Windows' else 'chromedriver'

    # Buscar en PATH
    for path in os.environ.get('PATH', '').split(os.pathsep):
        chromedriver_path = os.path.join(path, chromedriver_name)
        if os.path.isfile(chromedriver_path) and os.access(chromedriver_path, os.X_OK):
            return chromedriver_path

    # Rutas comunes según el sistema operativo
    common_paths = {
        'Windows': [
            r'C:\chromedriver\chromedriver.exe',
            os.path.expanduser(r'~\chromedriver\chromedriver.exe'),
        ],
        'Linux': [
            '/usr/local/bin/chromedriver',
            '/usr/bin/chromedriver',
            os.path.expanduser('~/chromedriver/chromedriver'),
        ],
        'Darwin': [  # macOS
            '/usr/local/bin/chromedriver',
            '/opt/homebrew/bin/chromedriver',
            os.path.expanduser('~/chromedriver/chromedriver'),
        ]
    }

    # Buscar en rutas comunes
    for path in common_paths.get(system, []):
        if os.path.isfile(path):
            return path

    # Si no se encuentra, devolver None
    return None


def ensure_output_dir():
    """Crea el directorio de salida si no existe."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


# Crear directorio de salida al importar el módulo
ensure_output_dir()
