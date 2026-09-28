ENTERO = "ENTERO"
REAL = "REAL"


def combinar_tipos(tipo1, tipo2):

    if tipo1 == REAL or tipo2 == REAL:
        return REAL

    return ENTERO


def analizar_logico(tipo_inicial, tipos_restantes):

    # atributo sintetizado del primer Termino

    tipo_actual = tipo_inicial

    print(
        "Termino.tipo =",
        tipo_actual
    )

    # MasLogico recibe un atributo heredado.

    for tipo in tipos_restantes:

        heredado = tipo_actual

        print(
            "\nMasLogico.inicial =",
            heredado
        )

        print(
            "Termino.tipo =",
            tipo
        )

        tipo_actual = combinar_tipos(
            heredado,
            tipo
        )

        print(
            "MasLogico.tipo =",
            tipo_actual
        )

    return tipo_actual


def main():

    print("=" * 65)
    print("EJERCICIO 4 - GRAMATICA ATRIBUIDA")
    print("=" * 65)

    print("\nClasificación:")
    print(
        "No es S-atribuida porque utiliza "
        "un atributo heredado."
    )

    print(
        "Puede clasificarse como L-atribuida "
        "si el atributo heredado sólo depende "
        "del padre o de símbolos izquierdos."
    )

    print("\nPRUEBA 1")

    resultado = analizar_logico(
        ENTERO,
        [ENTERO]
    )

    print(
        "Resultado:",
        resultado
    )

    print("\nPRUEBA 2")

    resultado = analizar_logico(
        ENTERO,
        [REAL]
    )

    print(
        "Resultado:",
        resultado
    )


if __name__ == "__main__":
    main()