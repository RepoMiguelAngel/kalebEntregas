"""Registro sencillo de gastos personales desde la terminal."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


@dataclass(frozen=True)
class Gasto:
    descripcion: str
    monto: Decimal


def convertir_monto(valor: str) -> Decimal:
    """Convierte texto a un monto decimal positivo."""
    try:
        monto = Decimal(valor)
    except InvalidOperation as error:
        raise ValueError("El monto debe ser un número válido.") from error

    if not monto.is_finite() or monto <= 0:
        raise ValueError("El monto debe ser un número mayor que cero.")
    return monto


def agregar_gasto(gastos: list[Gasto], descripcion: str, monto: Decimal) -> Gasto:
    """Valida y agrega un gasto a la lista."""
    descripcion = descripcion.strip()
    if not descripcion:
        raise ValueError("La descripción no puede estar vacía.")
    if not monto.is_finite() or monto <= 0:
        raise ValueError("El monto debe ser un número mayor que cero.")

    gasto = Gasto(descripcion=descripcion, monto=monto)
    gastos.append(gasto)
    return gasto


def calcular_total(gastos: list[Gasto]) -> Decimal:
    """Calcula el total de los gastos registrados."""
    return sum((gasto.monto for gasto in gastos), start=Decimal("0"))


def main() -> None:
    gastos: list[Gasto] = []
    print("Control de gastos personales")
    print("Ingresa una descripción vacía para terminar.\n")

    while True:
        descripcion = input("Descripción del gasto: ").strip()
        if not descripcion:
            break

        try:
            monto = convertir_monto(input("Monto: "))
            agregar_gasto(gastos, descripcion, monto)
        except ValueError as error:
            print(f"Error: {error}\n")
            continue

        print("Gasto registrado.\n")

    if gastos:
        print("\nGastos registrados:")
        for gasto in gastos:
            print(f"- {gasto.descripcion}: ${gasto.monto:.2f}")
    else:
        print("\nNo se registraron gastos.")

    print(f"Total: ${calcular_total(gastos):.2f}")


if __name__ == "__main__":
    main()
