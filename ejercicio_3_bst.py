class Nodo:

    def __init__(self, valor, izquierda=None, derecha=None):

        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


class AtributosBST:

    def __init__(
        self,
        es_bst,
        minimo,
        maximo
    ):

        self.es_bst = es_bst
        self.minimo = minimo
        self.maximo = maximo


def comprobar_bst(nodo):

    # Caso epsilon / nil

    if nodo is None:

        return AtributosBST(
            True,
            float("inf"),
            float("-inf")
        )

    izquierdo = comprobar_bst(
        nodo.izquierda
    )

    derecho = comprobar_bst(
        nodo.derecha
    )

    condicion = (
        izquierdo.es_bst
        and derecho.es_bst
        and izquierdo.maximo < nodo.valor
        and nodo.valor < derecho.minimo
    )

    minimo = min(
        nodo.valor,
        izquierdo.minimo,
        derecho.minimo
    )

    maximo = max(
        nodo.valor,
        izquierdo.maximo,
        derecho.maximo
    )

    return AtributosBST(
        condicion,
        minimo,
        maximo
    )


def main():

    # Árbol válido

    valido = Nodo(
        8,
        Nodo(3),
        Nodo(10)
    )

    # Árbol incorrecto:
    #
    #       8
    #      / \
    #     9   10

    invalido = Nodo(
        8,
        Nodo(9),
        Nodo(10)
    )

    print("=" * 60)
    print("EJERCICIO 3 - ARBOL BINARIO DE BUSQUEDA")
    print("=" * 60)

    resultado1 = comprobar_bst(valido)

    print(
        "\nÁrbol 1:",
        "BST válido"
        if resultado1.es_bst
        else "NO es BST"
    )

    resultado2 = comprobar_bst(invalido)

    print(
        "Árbol 2:",
        "BST válido"
        if resultado2.es_bst
        else "NO es BST"
    )


if __name__ == "__main__":
    main()