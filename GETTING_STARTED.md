# Guía de Inicio Rápido

Esta guía te ayudará a comenzar a usar los proyectos en este repositorio en pocos minutos.

## Instalación Rápida

### 1. Clonar el repositorio

```bash
git clone https://github.com/Gustavo-Campos-Luna/Ideas-Varias.git
cd Ideas-Varias
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso Rápido

### Financial Wallet

Analiza acciones de manera interactiva:

```bash
python -m financial_wallet.wallet
```

O ejecuta el ejemplo:

```bash
python financial_wallet/examples/basic_usage.py
```

### Weather Scraper

**Primero**: Instala ChromeDriver (ver sección de ChromeDriver abajo)

Extrae datos meteorológicos:

```bash
python -m weather_scraper.scraper
```

O ejecuta el ejemplo:

```bash
python weather_scraper/examples/basic_usage.py
```

## Instalación de ChromeDriver (solo para Weather Scraper)

### Opción 1: Instalación Rápida (Linux/macOS)

```bash
# Linux
sudo apt-get install chromium-chromedriver

# macOS
brew install chromedriver
```

### Opción 2: Instalación Manual

1. **Verifica tu versión de Chrome**:
   - Abre Chrome → Menú → Ayuda → Información de Google Chrome

2. **Descarga ChromeDriver**:
   - Visita: https://chromedriver.chromium.org/downloads
   - Descarga la versión compatible con tu Chrome

3. **Instala ChromeDriver**:

   **Windows**:
   ```cmd
   # Coloca chromedriver.exe en:
   C:\chromedriver\chromedriver.exe
   ```

   **Linux**:
   ```bash
   sudo mv chromedriver /usr/local/bin/
   sudo chmod +x /usr/local/bin/chromedriver
   ```

   **macOS**:
   ```bash
   mv chromedriver /usr/local/bin/
   chmod +x /usr/local/bin/chromedriver
   ```

## Estructura del Proyecto

```
Ideas-Varias/
├── financial_wallet/     # Análisis financiero
├── weather_scraper/      # Scraping meteorológico
├── data/                 # Archivos generados
├── requirements.txt      # Dependencias
└── README.md            # Documentación principal
```

## Ejemplos Rápidos

### Financial Wallet - Uso Programático

```python
from financial_wallet import FinancialWallet

# Crear instancia
wallet = FinancialWallet()

# Configurar
wallet.ticks = ['AAPL', 'GOOGL']
wallet.start = '2024-01-01'
wallet.end = '2024-12-31'

# Descargar y analizar
wallet.download_info()
wallet.compare_ticks()
```

### Weather Scraper - Uso Programático

```python
from weather_scraper import WeatherScraper

# Crear instancia
scraper = WeatherScraper()

# Ejecutar
df = scraper.run(ciudad="Santiago")
print(df)
```

## Solución de Problemas Comunes

### Error: ModuleNotFoundError

```bash
# Asegúrate de estar en el directorio correcto
cd Ideas-Varias

# Reinstala las dependencias
pip install -r requirements.txt
```

### Error: ChromeDriver no encontrado

```bash
# Verifica la instalación
which chromedriver  # Linux/macOS
where chromedriver  # Windows

# Si no está instalado, sigue las instrucciones de instalación arriba
```

### Error: No module named 'financial_wallet'

```bash
# Ejecuta desde el directorio raíz
cd Ideas-Varias
python -m financial_wallet.wallet
```

## Próximos Pasos

1. **Lee la documentación completa**: [README.md](./README.md)
2. **Explora los ejemplos**:
   - `financial_wallet/examples/basic_usage.py`
   - `weather_scraper/examples/basic_usage.py`
3. **Lee las guías específicas**:
   - [Financial Wallet README](./financial_wallet/README.md)
   - [Weather Scraper README](./weather_scraper/README.md)

## Obtener Ayuda

Si tienes problemas:

1. Revisa la documentación en los README de cada proyecto
2. Verifica que todas las dependencias están instaladas
3. Asegúrate de estar usando Python 3.8 o superior
4. Para Weather Scraper, verifica que ChromeDriver esté correctamente instalado

## Recursos Adicionales

- **Financial Wallet**: Basado en [tutorial de Zero2Hero](https://www.youtube.com/watch?v=n3XS3Wrp1bc)
- **Documentación de yfinance**: https://pypi.org/project/yfinance/
- **Documentación de Selenium**: https://www.selenium.dev/documentation/
- **ChromeDriver**: https://chromedriver.chromium.org/

---

¡Listo! Ahora estás preparado para usar ambos proyectos. 🚀
