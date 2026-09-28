class AtributosNumero:

    def __init__(self, valor, longitud):
        self.valor = valor
        self.longitud = longitud


def calcular_numero(digitos):

    valor = 0

    for digito in digitos:

        valor = (
            valor * 10
            + int(digito)
        )

    return AtributosNumero(
        valor,
        len(digitos)
    )


def evaluar_real(cadena):

    if cadena.count(".") != 1:

        raise ValueError(
            "Debe existir exactamente un punto decimal."
        )

    parte_entera, parte_decimal = cadena.split(".")

    if (
        not parte_entera
        or not parte_decimal
        or not parte_entera.isdigit()
        or not parte_decimal.isdigit()
    ):

        raise ValueError(
            "Formato de número real incorrecto."
        )

    entero = calcular_numero(
        parte_entera
    )

    decimal = calcular_numero(
        parte_decimal
    )

    valor = (
        entero.valor
        +
        decimal.valor
        / (10 ** decimal.longitud)
    )

    return valor


def main():

    pruebas = [
        "123.456",
        "25.75",
        "7.05",
        "100.001"
    ]

    print("=" * 60)
    print("EJERCICIO 2 - CALCULO DE NUMEROS REALES")
    print("=" * 60)

    for cadena in pruebas:

        try:

            resultado = evaluar_real(cadena)

            print(
                f"{cadena:<12} -> {resultado}"
            )

        except ValueError as error:

            print(
                f"{cadena:<12} -> ERROR: {error}"
            )


if __name__ == "__main__":
    main()