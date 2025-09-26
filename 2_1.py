def check_reflexive(edges, vertices):
    for v in range(1, vertices + 1):
        if (v, v) not in edges:
            return False
    return True


def check_symmetric(edges):
    for a, b in edges:
        if (b, a) not in edges:
            return False
    return True


def check_antisymmetric(edges):
    for a, b in edges:
        if a != b and (b, a) in edges:
            return False
    return True


def check_transitive(edges):
    for a, b in edges:
        for c, d in edges:
            if b == c and (a, d) not in edges:
                return False
    return True


def main():
    n, m = map(int, input("Введите число ребер и число вершин: ").split())
    edges = []

    for i in range(n):
        a, b = map(int, input(f"Введите ребро №{i + 1}: ").split())
        edges.append((a, b))

    reflexive = check_reflexive(edges, m)
    symmetric = check_symmetric(edges)
    antisymmetric = check_antisymmetric(edges)
    transitive = check_transitive(edges)

    print()
    results = [
        "Рефлексивное" if reflexive else "Нерефлексивное",
        "Транзитивное" if transitive else "Нетранзитивное",
        "Симметричное" if symmetric else "Антисимметричное" if antisymmetric else "Несимметричное"
    ]

    print("\n".join(results))


main()
