import re


ENTERO = "ENTERO"
REAL = "REAL"


class Resultado:

    def __init__(self, tipo, valor):

        self.tipo = tipo
        self.valor = valor


class Parser:

    def __init__(self, texto):

        self.tokens = re.findall(
            r"[A-Za-z_][A-Za-z0-9_]*"
            r"|\d+\.\d+"
            r"|\d+"
            r"|[+\-*/=()]",
            texto
        )

        texto_limpio = re.sub(
            r"\s+",
            "",
            texto
        )

        if "".join(self.tokens) != texto_limpio:

            raise SyntaxError(
                "Existen caracteres no válidos."
            )

        self.pos = 0

    def actual(self):

        if self.pos >= len(self.tokens):
            return None

        return self.tokens[self.pos]

    def consumir(self, esperado=None):

        token = self.actual()

        if token is None:

            raise SyntaxError(
                "Fin inesperado."
            )

        if esperado is not None and token != esperado:

            raise SyntaxError(
                f"Se esperaba {esperado}, "
                f"pero apareció {token}."
            )

        self.pos += 1

        return token

    def combinar_tipo(self, a, b, operador):

        if operador == "/":
            return REAL

        if a == REAL or b == REAL:
            return REAL

        return ENTERO

    # fact -> entero | real | (exp)

    def fact(self):

        token = self.actual()

        if token == "(":

            self.consumir("(")

            resultado = self.exp()

            self.consumir(")")

            return resultado

        if token is not None and re.fullmatch(
            r"\d+\.\d+",
            token
        ):

            self.consumir()

            return Resultado(
                REAL,
                float(token)
            )

        if token is not None and token.isdigit():

            self.consumir()

            return Resultado(
                ENTERO,
                int(token)
            )

        raise SyntaxError(
            f"Factor inválido: {token}"
        )

    # term -> fact masFact

    def term(self):

        izquierda = self.fact()

        while self.actual() in ("*", "/"):

            operador = self.consumir()

            derecha = self.fact()

            tipo = self.combinar_tipo(
                izquierda.tipo,
                derecha.tipo,
                operador
            )

            if operador == "*":

                valor = (
                    izquierda.valor
                    * derecha.valor
                )

            else:

                if derecha.valor == 0:

                    raise ZeroDivisionError(
                        "División entre cero."
                    )

                valor = (
                    izquierda.valor
                    / derecha.valor
                )

            izquierda = Resultado(
                tipo,
                valor
            )

        return izquierda

    # exp -> term masTerm

    def exp(self):

        izquierda = self.term()

        while self.actual() in ("+", "-"):

            operador = self.consumir()

            derecha = self.term()

            tipo = self.combinar_tipo(
                izquierda.tipo,
                derecha.tipo,
                operador
            )

            if operador == "+":

                valor = (
                    izquierda.valor
                    + derecha.valor
                )

            else:

                valor = (
                    izquierda.valor
                    - derecha.valor
                )

            izquierda = Resultado(
                tipo,
                valor
            )

        return izquierda

    # S -> var = exp

    def asignacion(self):

        identificador = self.actual()

        if identificador is None or not re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_]*",
            identificador
        ):

            raise SyntaxError(
                "Se esperaba un identificador."
            )

        self.consumir()

        self.consumir("=")

        resultado = self.exp()

        if self.actual() is not None:

            raise SyntaxError(
                f"Token sobrante: {self.actual()}"
            )

        return (
            identificador,
            resultado
        )


def main():

    pruebas = [

        "x = 2 + 3 * 4",
        "resultado = 2 + 3 * 4.5",
        "promedio = (10 + 5) / 2",
        "valor = 20 - 3 * 2"
    ]

    print("=" * 70)
    print("EJERCICIO 7 - INFERENCIA DE TIPO Y EVALUACION")
    print("=" * 70)

    for expresion in pruebas:

        print(
            "\nExpresión:",
            expresion
        )

        try:

            parser = Parser(expresion)

            variable, resultado = parser.asignacion()

            print(
                f"{variable}.tipo  =",
                resultado.tipo
            )

            print(
                f"{variable}.valor =",
                resultado.valor
            )

        except Exception as error:

            print(
                "ERROR:",
                error
            )


if __name__ == "__main__":
    main()