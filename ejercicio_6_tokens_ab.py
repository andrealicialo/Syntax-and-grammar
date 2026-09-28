class Atributos:

    def __init__(self):

        self.a = 0
        self.b = 0


def analizar(cadena):

    atributos = Atributos()

    for token in cadena.upper():

        if token.isspace():
            continue

        if token == "A":

            atributos.a += 1

        elif token == "B":

            atributos.b += 1

        else:

            raise SyntaxError(
                f"Token no permitido: {token}"
            )

    acepta = (
        atributos.a
        == atributos.b
    )

    return (
        atributos.a,
        atributos.b,
        acepta
    )


def main():

    pruebas = [
        "AB",
        "AABB",
        "ABAB",
        "BBAA",
        "AAABB",
        "AAB",
        ""
    ]

    print("=" * 65)
    print("EJERCICIO 6 - IGUAL NUMERO DE A Y B")
    print("=" * 65)

    for cadena in pruebas:

        try:

            a, b, acepta = analizar(cadena)

            resultado = (
                "ACEPTADA"
                if acepta
                else "RECHAZADA"
            )

            print(
                f"{cadena or 'epsilon':<10}"
                f" A={a} B={b}"
                f" -> {resultado}"
            )

        except SyntaxError as error:

            print(error)


if __name__ == "__main__":
    main()