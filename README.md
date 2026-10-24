# Control de gastos personales

## Objetivo

Aplicación de consola para registrar gastos personales, validar montos positivos y calcular el total. El proyecto sirve para practicar control de versiones, pruebas automatizadas e integración continua.

## Herramientas

- Python 3.12 o posterior
- Git
- GitHub
- GitHub Actions
- Pruebas con `unittest` (incluido en Python)

## Estructura

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_control_gastos.py
├── .gitignore
├── control_gastos.py
├── ENTREGA_SEMANA1.md
└── README.md
```

## Ejecutar el programa

Desde esta carpeta, ejecuta:

```bash
python control_gastos.py
```

Escribe la descripción y el monto de cada gasto. Para terminar, deja vacía la descripción. El programa muestra los gastos registrados y su total.

## Ejecutar las pruebas

```bash
python -m unittest discover -s tests -v
```

## Integración continua

El flujo de GitHub Actions está en `.github/workflows/ci.yml`. Se ejecuta en cada `push` y en cada `pull_request`; prepara Python 3.12 y corre las pruebas de `unittest`. Un resultado exitoso significa que todas las pruebas terminaron sin errores.

## Git y GitHub

El proyecto está publicado en [github.com/RepoMiguelAngel/kalebEntregas](https://github.com/RepoMiguelAngel/kalebEntregas). Para obtener una copia:

```bash
git clone https://github.com/RepoMiguelAngel/kalebEntregas.git
```

Los cambios se registran con commits descriptivos y se publican con `git push`. La guía de la entrega y las evidencias que debes capturar están en `ENTREGA_SEMANA1.md`.
