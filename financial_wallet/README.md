# Financial Wallet - Herramienta de Análisis Financiero

Aplicación Python para análisis y visualización de datos históricos de acciones usando yfinance.

## Descripción

Financial Wallet es una herramienta interactiva que permite descargar, analizar y visualizar datos históricos de acciones de manera sencilla. El proyecto está diseñado para inversores, analistas y cualquier persona interesada en el análisis financiero.

## Características

- **Descarga de datos históricos**: Obtén datos de cualquier ticker disponible en Yahoo Finance
- **Soporte para múltiples tickers**: Analiza una o múltiples acciones simultáneamente
- **Visualización de series temporales**: Gráficos de precios de cierre
- **Comparación de acciones**: Compara el rendimiento de dos o más acciones
- **Análisis de retornos**: Calcula y visualiza la distribución de retornos diarios
- **Análisis de volatilidad**: Calcula la volatilidad anualizada de las acciones
- **Exportación de datos**: Guarda los datos en formato CSV
- **Interfaz interactiva**: Guía paso a paso para el usuario
- **Validación de entradas**: Manejo robusto de errores y entradas incorrectas

## Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

Desde el directorio raíz del proyecto:

```bash
pip install -r requirements.txt
```

O instalación manual de dependencias específicas:

```bash
pip install pandas>=2.0.0 matplotlib>=3.7.0 yfinance>=0.2.0
```

## Uso

### Uso Básico

Desde el directorio raíz del proyecto:

```bash
python -m financial_wallet.wallet
```

O usando Python:

```python
from financial_wallet import FinancialWallet

# Crear instancia
wallet = FinancialWallet()

# Configurar tickers
wallet.set_ticks()

# Configurar fechas
wallet.set_dates()

# Descargar datos
wallet.download_info()

# Mostrar tickers
wallet.show_ticks()
```

### Ejemplos de Uso

#### Análisis de una sola acción

```python
from financial_wallet import FinancialWallet

wallet = FinancialWallet()

# Configuración manual
wallet.ticks = ['AAPL']
wallet.start = '2024-01-01'
wallet.end = '2024-12-31'

# Descargar y analizar
wallet.download_info()
wallet.show_tick('AAPL')
```

#### Comparación de múltiples acciones

```python
from financial_wallet import FinancialWallet

wallet = FinancialWallet()

# Configurar múltiples tickers
wallet.ticks = ['AAPL', 'GOOGL', 'MSFT']
wallet.start = '2024-01-01'
wallet.end = '2024-12-31'

# Descargar datos
wallet.download_info()

# Comparar acciones
wallet.compare_multiple_ticks()
```

#### Análisis de volatilidad

```python
from financial_wallet import FinancialWallet

wallet = FinancialWallet()

# Configurar
wallet.ticks = ['TSLA']
wallet.start = '2024-01-01'
wallet.end = '2024-12-31'

# Descargar y analizar
wallet.download_info()
wallet.analyze_volatility()
```

### Formato de Tickers

- **Acciones individuales**: `AAPL`, `GOOGL`, `MSFT`, `TSLA`
- **Índices**: `DJI` (Dow Jones), `GSPC` (S&P 500), `IXIC` (NASDAQ)
  - Los índices se convierten automáticamente al formato requerido (^DJI, ^GSPC, ^IXIC)

### Formato de Fechas

Las fechas deben ingresarse en formato ISO: `YYYY-MM-DD`

Ejemplo: `2024-01-01`

## Estructura del Módulo

```
financial_wallet/
├── __init__.py           # Inicialización del módulo
├── wallet.py             # Clase principal FinancialWallet
├── examples/             # Ejemplos de uso
│   └── basic_usage.py    # Ejemplo básico
└── README.md             # Esta documentación
```

## Métodos Principales

### `set_ticks()`
Solicita al usuario los tickers de acciones a analizar.

### `set_dates()`
Solicita las fechas de inicio y fin para el análisis.

### `download_info()`
Descarga los datos históricos de Yahoo Finance.

### `show_ticks()`
Muestra los tickers seleccionados.

### `show_tick(tick)`
Visualiza la serie temporal de precios de cierre para un ticker específico.

### `compare_ticks()`
Compara dos tickers (solo si hay exactamente 2 en la lista).

### `compare_multiple_ticks()`
Permite seleccionar pares de tickers para comparar (cuando hay más de 2).

### `returns()`
Calcula y visualiza los retornos diarios de un ticker.

### `analyze_volatility()`
Calcula la volatilidad anualizada de un ticker.

### `export_data()`
Exporta los datos descargados a un archivo CSV.

## Directorio de Salida

Los archivos exportados se guardan en:
```
data/financial/
```

Este directorio se crea automáticamente si no existe.

## Mejoras sobre el Tutorial Original

Basado en el tutorial del canal [Zero2Hero](https://www.youtube.com/watch?v=n3XS3Wrp1bc), se han agregado las siguientes mejoras:

- ✅ Código refactorizado siguiendo PEP 8
- ✅ Documentación completa con docstrings
- ✅ Manejo robusto de errores
- ✅ Uso de rutas relativas para exportación
- ✅ Validación mejorada de entradas
- ✅ Interfaz más amigable
- ✅ Estructura de proyecto profesional
- ✅ Directorio de salida configurable
- ✅ Soporte para índices automático

## Solución de Problemas

### Error al descargar datos

Si obtienes un error al descargar datos:
- Verifica que el ticker sea válido
- Asegúrate de tener conexión a internet
- Verifica que las fechas estén en el rango correcto

### Error de importación

Si obtienes `ModuleNotFoundError`:
```bash
# Asegúrate de estar en el directorio raíz
cd Ideas-Varias

# Instala las dependencias
pip install -r requirements.txt
```

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

## Agradecimientos

- Basado en el tutorial del canal [Zero2Hero](https://www.youtube.com/watch?v=n3XS3Wrp1bc)
- Datos proporcionados por [Yahoo Finance](https://finance.yahoo.com/)
- Biblioteca [yfinance](https://pypi.org/project/yfinance/)
