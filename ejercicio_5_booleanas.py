import re


def implicacion(a, b):
    return (not a) or b


def tokenizar(texto):

    texto = texto.upper()

    tokens = re.findall(
        r"TRUE|FALSE|AND|OR|=>",
        texto
    )

    original = re.sub(
        r"\s+",
        "",
        texto
    )

    reconstruido = "".join(tokens)

    if original != reconstruido:

        raise SyntaxError(
            "Expresión booleana no válida."
        )

    return tokens


def evaluar(texto):

    tokens = tokenizar(texto)

    if not tokens:

        raise SyntaxError(
            "Expresión vacía."
        )

    posicion = 0

    def valor():

        nonlocal posicion

        if posicion >= len(tokens):

            raise SyntaxError(
                "Se esperaba TRUE o FALSE."
            )

        token = tokens[posicion]

        if token == "TRUE":

            posicion += 1
            return True

        if token == "FALSE":

            posicion += 1
            return False

        raise SyntaxError(
            f"Se esperaba valor booleano, no {token}."
        )

    # Primer valor

    resultado = valor()

    # Evaluación estrictamente de izquierda a derecha

    while posicion < len(tokens):

        operador = tokens[posicion]
        posicion += 1

        siguiente = valor()

        if operador == "AND":

            resultado = (
                resultado and siguiente
            )

        elif operador == "OR":

            resultado = (
                resultado or siguiente
            )

        elif operador == "=>":

            resultado = implicacion(
                resultado,
                siguiente
            )

        else:

            raise SyntaxError(
                "Operador desconocido."
            )

    return resultado


def main():

    pruebas = [
        "TRUE AND TRUE",
        "TRUE AND FALSE",
        "FALSE OR TRUE",
        "TRUE => FALSE",
        "FALSE => TRUE",
        "TRUE OR FALSE AND FALSE"
    ]

    print("=" * 65)
    print("EJERCICIO 5 - DDS BOOLEANAS")
    print("=" * 65)

    for expresion in pruebas:

        try:

            resultado = evaluar(expresion)

            estado = (
                "ACEPTADA"
                if resultado
                else "RECHAZADA"
            )

            print(
                f"{expresion:<30}"
                f" -> {resultado:<5}"
                f" -> {estado}"
            )

        except SyntaxError as error:

            print(
                expresion,
                "-> ERROR:",
                error
            )


if __name__ == "__main__":
    main()