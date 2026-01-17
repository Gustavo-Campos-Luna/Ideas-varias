# Weather Scraper - Extractor de Datos Meteorológicos

Herramienta automatizada para extraer datos meteorológicos del sitio web Meteored usando Selenium.

## Descripción

Weather Scraper es una aplicación Python que utiliza Selenium WebDriver para extraer automáticamente información meteorológica de diferentes ciudades desde [Meteored](https://www.meteored.cl/). Los datos extraídos se pueden guardar en formatos CSV y Excel para análisis posterior.

## Características

- **Scraping automatizado**: Extrae datos meteorológicos de manera automática
- **Búsqueda dinámica de ciudades**: Busca cualquier ciudad disponible en Meteored
- **Múltiples formatos de salida**: Guarda los datos en CSV y Excel
- **Configuración flexible**: ChromeDriver con detección automática de rutas
- **Manejo robusto de errores**: Mensajes claros y manejo de excepciones
- **Modo incógnito**: Navegación privada por defecto
- **Fácil configuración**: Archivo de configuración centralizado

## Instalación

### Requisitos Previos

1. **Python 3.8 o superior**
2. **Google Chrome** instalado
3. **ChromeDriver** compatible con tu versión de Chrome

### Instalación de Dependencias

Desde el directorio raíz del proyecto:

```bash
pip install -r requirements.txt
```

O instalación manual de dependencias específicas:

```bash
pip install pandas>=2.0.0 selenium>=4.0.0 openpyxl>=3.1.0
```

### Configuración de ChromeDriver

#### Opción 1: Instalación Automática (Recomendada)

El scraper intentará detectar automáticamente ChromeDriver en tu sistema.

#### Opción 2: Instalación Manual

1. **Descarga ChromeDriver**:
   - Visita: https://chromedriver.chromium.org/downloads
   - Descarga la versión compatible con tu Chrome

2. **Verifica tu versión de Chrome**:
   - Chrome → Ayuda → Información de Google Chrome

3. **Coloca ChromeDriver en una ubicación accesible**:

   **Windows**:
   ```
   C:\chromedriver\chromedriver.exe
   ```

   **Linux**:
   ```
   /usr/local/bin/chromedriver
   /usr/bin/chromedriver
   ```

   **macOS**:
   ```
   /usr/local/bin/chromedriver
   /opt/homebrew/bin/chromedriver
   ```

4. **Alternativamente, agrega ChromeDriver al PATH**:
   - Windows: Variables de entorno → PATH
   - Linux/macOS: Agrega a ~/.bashrc o ~/.zshrc

## Uso

### Uso Básico

Desde el directorio raíz del proyecto:

```bash
python -m weather_scraper.scraper
```

El programa te pedirá ingresar el nombre de la ciudad:

```
Ingresa el nombre de la ciudad a buscar: Santiago
```

### Uso Programático

```python
from weather_scraper import WeatherScraper

# Crear instancia
scraper = WeatherScraper()

# Ejecutar scraper (solicita ciudad interactivamente)
scraper.run()
```

### Uso con Ciudad Específica

```python
from weather_scraper import WeatherScraper

# Crear instancia
scraper = WeatherScraper()

# Ejecutar con ciudad específica
df = scraper.run(ciudad="Santiago")

# El DataFrame contiene los datos extraídos
print(df)
```

### Personalizar Directorio de Salida

```python
from weather_scraper import WeatherScraper

# Crear instancia con directorio personalizado
scraper = WeatherScraper(output_dir="mis_datos/clima")

# Ejecutar scraper
scraper.run(ciudad="Valparaíso")
```

## Estructura del Módulo

```
weather_scraper/
├── __init__.py           # Inicialización del módulo
├── scraper.py            # Clase principal WeatherScraper
├── config.py             # Configuración y parámetros
├── examples/             # Ejemplos de uso
│   └── basic_usage.py    # Ejemplo básico
└── README.md             # Esta documentación
```

## Configuración

El archivo `config.py` contiene todos los parámetros configurables:

```python
# Directorio de salida para datos
OUTPUT_DIR = 'data/weather'

# URL del sitio meteorológico
WEATHER_URL = 'https://www.meteored.cl/'

# Timeout para esperas del navegador (segundos)
WAIT_TIMEOUT = 10

# Opciones del navegador Chrome
CHROME_OPTIONS = [
    '--start-maximized',
    '--incognito',
    # '--headless',  # Descomentar para modo sin ventana
]
```

### Modo Headless

Para ejecutar sin abrir ventana del navegador, descomentar en `config.py`:

```python
CHROME_OPTIONS = [
    '--start-maximized',
    '--incognito',
    '--headless',  # Activar modo sin ventana
]
```

## Datos Extraídos

El scraper extrae la siguiente información:

| Campo | Descripción |
|-------|-------------|
| **Día** | Día de la semana |
| **Fecha** | Fecha del pronóstico |
| **Temperatura** | Temperatura máxima/mínima |
| **Viento** | Velocidad y dirección del viento |

### Ejemplo de Salida

```
     Día      Fecha  Temperatura        Viento
0    Lun  18 Ene      23° / 14°      15 km/h N
1    Mar  19 Ene      25° / 16°      12 km/h NE
2    Mié  20 Ene      22° / 15°      18 km/h E
```

## Directorio de Salida

Los archivos se guardan en:
```
data/weather/
├── resultados_santiago.csv
├── resultados_santiago.xlsx
├── resultados_valparaiso.csv
└── resultados_valparaiso.xlsx
```

Este directorio se crea automáticamente si no existe.

## Métodos Principales

### `run(ciudad=None)`
Ejecuta el flujo completo del scraper.
- **Parámetros**:
  - `ciudad` (str, opcional): Ciudad a buscar. Si es None, solicita al usuario.
- **Retorna**: DataFrame con los datos extraídos, o None si hay error.

### Métodos Internos

- `_configurar_driver()`: Configura el WebDriver de Chrome
- `_buscar_ciudad(ciudad)`: Busca una ciudad en el sitio web
- `_extraer_informacion()`: Extrae los datos meteorológicos
- `_guardar_datos(df, ciudad)`: Guarda los datos en CSV y Excel

## Solución de Problemas

### Error: "No se pudo inicializar ChromeDriver"

**Causas comunes**:
- ChromeDriver no está instalado
- ChromeDriver no es compatible con tu versión de Chrome
- ChromeDriver no está en el PATH

**Soluciones**:
1. Descarga ChromeDriver desde: https://chromedriver.chromium.org/
2. Verifica compatibilidad con tu versión de Chrome
3. Coloca ChromeDriver en una ubicación del PATH
4. O especifica la ruta en `config.py`

### Error: "No se pudo encontrar el cuadro de búsqueda"

**Causas comunes**:
- Conexión a internet inestable
- El sitio web cambió su estructura
- Timeout muy corto

**Soluciones**:
1. Verifica tu conexión a internet
2. Aumenta `WAIT_TIMEOUT` en `config.py`
3. Verifica que el sitio esté disponible

### Error: "No se pudo extraer la información"

**Causas comunes**:
- Ciudad no disponible en el sitio
- Formato de página cambió
- Error de conexión

**Soluciones**:
1. Verifica el nombre de la ciudad
2. Prueba con otra ciudad conocida
3. Revisa la estructura del sitio web

### Problemas de importación

```bash
# Asegúrate de estar en el directorio raíz
cd Ideas-Varias

# Reinstala las dependencias
pip install -r requirements.txt
```

## Mejoras Implementadas

Mejoras sobre el código original:

- ✅ Código refactorizado siguiendo PEP 8
- ✅ Documentación completa con docstrings
- ✅ Detección automática de ChromeDriver
- ✅ Archivo de configuración centralizado
- ✅ Manejo robusto de errores y excepciones
- ✅ Uso de rutas relativas
- ✅ Mensajes de error informativos
- ✅ Estructura de proyecto profesional
- ✅ Directorio de salida configurable
- ✅ Soporte multiplataforma (Windows, Linux, macOS)

## Notas Importantes

1. **Uso Responsable**: Este scraper está diseñado para uso educacional y personal. Respeta los términos de servicio del sitio web.

2. **Rate Limiting**: No hagas requests excesivos al sitio. El scraper incluye delays apropiados.

3. **Mantenimiento**: Los sitios web pueden cambiar su estructura. Si el scraper deja de funcionar, puede requerir actualizaciones.

## Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature
3. Haz commit de tus cambios
4. Push a la rama
5. Abre un Pull Request

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Autor

Gustavo Campos Luna

## Recursos

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
- [Meteored](https://www.meteored.cl/)
