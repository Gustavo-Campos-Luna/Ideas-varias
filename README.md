# Ideas Varias - Proyectos Python

Colección de proyectos Python profesionales para análisis financiero y automatización de datos.

## Descripción

Este repositorio contiene dos proyectos principales desarrollados en Python:

1. **Financial Wallet**: Herramienta de análisis financiero para visualizar y comparar el rendimiento de acciones
2. **Weather Scraper**: Scraper automatizado de datos meteorológicos usando Selenium

## Estructura del Proyecto

```
Ideas-Varias/
├── financial_wallet/         # Proyecto de análisis financiero
│   ├── wallet.py             # Módulo principal
│   ├── examples/             # Ejemplos de uso
│   └── README.md             # Documentación específica
├── weather_scraper/          # Proyecto de scraping meteorológico
│   ├── scraper.py            # Módulo principal
│   ├── config.py             # Configuración
│   ├── examples/             # Ejemplos de uso
│   └── README.md             # Documentación específica
├── data/                     # Directorio para datos generados
│   ├── financial/            # Exportaciones financieras
│   └── weather/              # Exportaciones meteorológicas
└── requirements.txt          # Dependencias del proyecto
```

## Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Chrome browser (para Weather Scraper)
- ChromeDriver (para Weather Scraper)

### Instalación de Dependencias

1. Clona este repositorio:
```bash
git clone https://github.com/Gustavo-Campos-Luna/Ideas-Varias.git
cd Ideas-Varias
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Configuración de ChromeDriver (solo para Weather Scraper)

1. Descarga ChromeDriver desde: https://chromedriver.chromium.org/
2. Extrae el ejecutable
3. Configura la ruta en `weather_scraper/config.py`

## Uso Rápido

### Financial Wallet

```python
from financial_wallet.wallet import FinancialWallet

# Crear instancia
wallet = FinancialWallet()

# Configurar y analizar
wallet.set_ticks()
wallet.set_dates()
wallet.download_info()
wallet.show_ticks()
```

Ver más ejemplos en: `financial_wallet/examples/`

### Weather Scraper

```python
from weather_scraper.scraper import WeatherScraper

# Ejecutar scraper
scraper = WeatherScraper()
scraper.run()
```

Ver más ejemplos en: `weather_scraper/examples/`

## Características Principales

### Financial Wallet
- Descarga de datos históricos de acciones
- Visualización de series temporales
- Comparación entre múltiples tickers
- Análisis de retornos y volatilidad
- Exportación de datos a CSV

### Weather Scraper
- Extracción automatizada de datos meteorológicos
- Búsqueda dinámica de ciudades
- Guardado en múltiples formatos (CSV, Excel)
- Configuración personalizable del navegador

## Proyectos

Cada proyecto tiene su propia documentación detallada:

- [Financial Wallet](./financial_wallet/README.md)
- [Weather Scraper](./weather_scraper/README.md)

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Autor

Gustavo Campos Luna

## Agradecimientos

- **Financial Wallet**: Basado en el tutorial del canal [Zero2Hero](https://www.youtube.com/watch?v=n3XS3Wrp1bc&list=PL3lna2aeKsUd5GALdbjTTpEIvCdU-bz9K&index=6&ab_channel=Zero2Hero)
- **Weather Scraper**: Desarrollado usando Selenium y datos de [Meteored](https://www.meteored.cl/)

## Soporte

Si encuentras algún problema o tienes sugerencias, por favor abre un issue en GitHub.
