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

Inicializa Git en la carpeta del proyecto (no en una carpeta superior):

```bash
git init
git add .
git commit -m "Crear aplicación de control de gastos"
```

Para publicar el proyecto, crea un repositorio vacío en tu cuenta de GitHub y conecta la URL que GitHub te proporcione:

```bash
git branch -M main
git remote add origin https://github.com/TU-USUARIO/control-gastos.git
git push -u origin main
```

Continúa registrando cambios con mensajes que expliquen el propósito real de cada cambio. La guía de la entrega y las evidencias que debes capturar están en `ENTREGA_SEMANA1.md`.
