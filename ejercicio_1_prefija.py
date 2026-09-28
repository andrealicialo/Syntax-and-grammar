import re


class ParserPrefijo:

    def __init__(self, expresion):
        self.tokens = self.tokenizar(expresion)
        self.posicion = 0

    def tokenizar(self, texto):

        patron = r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[+\-*/()]"

        tokens = re.findall(patron, texto)

        texto_sin_espacios = re.sub(r"\s+", "", texto)

        if "".join(tokens) != texto_sin_espacios:
            raise SyntaxError(
                "La expresión contiene caracteres no reconocidos."
            )

        return tokens

    def actual(self):

        if self.posicion >= len(self.tokens):
            return None

        return self.tokens[self.posicion]

    def consumir(self, esperado=None):

        token = self.actual()

        if token is None:
            raise SyntaxError("Fin inesperado de la expresión.")

        if esperado is not None and token != esperado:

            raise SyntaxError(
                f"Se esperaba '{esperado}' pero apareció '{token}'."
            )

        self.posicion += 1

        return token

    # E -> T E'

    def E(self):

        izquierda = self.T()

        while self.actual() in ("+", "-"):

            operador = self.consumir()

            derecha = self.T()

            izquierda = (
                f"{operador} {izquierda} {derecha}"
            )

        return izquierda

    # T -> F T'

    def T(self):

        izquierda = self.F()

        while self.actual() in ("*", "/"):

            operador = self.consumir()

            derecha = self.F()

            izquierda = (
                f"{operador} {izquierda} {derecha}"
            )

        return izquierda

    # F -> id | num | (E)

    def F(self):

        token = self.actual()

        if token == "(":

            self.consumir("(")

            resultado = self.E()

            self.consumir(")")

            return resultado

        if token is not None and re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?",
            token
        ):

            return self.consumir()

        raise SyntaxError(
            f"Token inesperado: {token}"
        )

    def traducir(self):

        resultado = self.E()

        if self.actual() is not None:

            raise SyntaxError(
                f"Token sobrante: {self.actual()}"
            )

        return resultado


def main():

    expresion = "a/2+10*c"

    print("=" * 60)
    print("EJERCICIO 1 - INFIJA A PREFIJA")
    print("=" * 60)

    print("\nExpresión infija:")
    print(expresion)

    try:

        parser = ParserPrefijo(expresion)

        prefija = parser.traducir()

        print("\nNotación prefija:")
        print(prefija)

    except SyntaxError as error:

        print("\nError:", error)


if __name__ == "__main__":
    main()