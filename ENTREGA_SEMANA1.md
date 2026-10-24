# Entrega 1: Preparación del entorno para desarrollo e integración continua

> Completa los campos entre corchetes y sustituye cada indicación de captura por una imagen tomada de tu propio repositorio. No presentes como evidencia una ejecución que no hayas realizado.

## Portada

- **Alumno:** [Nombre completo]
- **Materia:** [Nombre de la materia]
- **Grupo:** [Grupo]
- **Fecha:** [Fecha de entrega]
- **Proyecto:** Control de gastos personales

## Descripción y objetivo

El proyecto es una aplicación de consola que permite registrar gastos, validar que cada monto sea positivo y calcular la suma de los gastos capturados. El objetivo de la práctica es organizar el código, registrar cambios con Git y ejecutar pruebas automáticamente con GitHub Actions.

## Herramientas y versiones

Completa las versiones con las que trabajaste:

| Herramienta | Versión utilizada |
|---|---|
| Python | [Ejecuta `python --version`] |
| Git | [Ejecuta `git --version`] |
| GitHub Actions | Flujo definido en `.github/workflows/ci.yml` |
| `unittest` | Biblioteca estándar de Python |

## Estructura del proyecto

```text
.
├── .github/workflows/ci.yml
├── tests/test_control_gastos.py
├── .gitignore
├── control_gastos.py
├── ENTREGA_SEMANA1.md
└── README.md
```

La aplicación se ejecuta con `python control_gastos.py`; las pruebas, con `python -m unittest discover -s tests -v`.

## Repositorio de GitHub

- **URL:** [Pega aquí el enlace a tu repositorio]

## Evidencias

Inserta capturas reales de tu proyecto y agrega una breve explicación a cada una.

1. **Commits:** captura la salida de `git --no-pager log --oneline` donde se observen al menos cinco commits significativos.
2. **Flujo de CI:** captura el archivo `.github/workflows/ci.yml` en tu repositorio.
3. **Ejecución exitosa:** en GitHub, abre la pestaña **Actions**, selecciona una ejecución finalizada correctamente y captura el resultado.
4. **Error controlado:** modifica temporalmente una expectativa en `tests/test_control_gastos.py` para que sea incorrecta, ejecuta las pruebas y sube el cambio. Captura el resultado fallido en Actions.
5. **Corrección:** restaura la expectativa correcta, ejecuta las pruebas, sube la corrección y captura la ejecución exitosa posterior.

No dejes el error intencional en la versión final. Conserva la captura del fallo antes de corregirlo.

## Conclusión personal

[Explica con tus palabras cómo Git te ayudó a conservar el historial de cambios y cómo la integración continua permitió detectar el error antes de dar el trabajo por terminado. Menciona qué aprendiste al revisar el resultado de las pruebas.]

## Exportar a PDF

Completa la portada, pega las evidencias y escribe la conclusión. Después abre este archivo en VS Code o en un editor Markdown y usa **Imprimir > Guardar como PDF**. Revisa que las capturas y el enlace sean legibles antes de entregar.
