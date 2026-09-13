"""
Nombre: Ortega Plaza Diego
Matricula: 2403230009
Asignatura: Ciencia de Datos
Fecha: 12/09/26
"""


def calcular_determinante(a1, b1, a2, b2):
    """Calcula el determinante de una matriz 2x2.

    La matriz tiene la forma:
    | a1  b1 |
    | a2  b2 |

    Args:
        a1 (float): Elemento superior izquierdo.
        b1 (float): Elemento superior derecho.
        a2 (float): Elemento inferior izquierdo.
        b2 (float): Elemento inferior derecho.

    Returns:
        float: El valor del determinante (a1*b2 - a2*b1).
    """
    return (a1 * b2) - (a2 * b1)


def calcular_determinante_principal(coeficientes_a, coeficientes_b):
    """Calcula el determinante principal (Delta) del sistema.

    Args:
        coeficientes_a (dict): Diccionario con 'x', 'y', 'r' de la
            ecuacion A (a1, b1, c1).
        coeficientes_b (dict): Diccionario con 'x', 'y', 'r' de la
            ecuacion B (a2, b2, c2).

    Returns:
        float: Valor de Delta = a1*b2 - a2*b1.
    """
    a1, b1 = coeficientes_a["x"], coeficientes_a["y"]
    a2, b2 = coeficientes_b["x"], coeficientes_b["y"]
    return calcular_determinante(a1, b1, a2, b2)


def calcular_determinante_x(coeficientes_a, coeficientes_b):
    """Calcula el determinante de X (Delta_x).

    Args:
        coeficientes_a (dict): Diccionario con 'x', 'y', 'r' de la
            ecuacion A (a1, b1, c1).
        coeficientes_b (dict): Diccionario con 'x', 'y', 'r' de la
            ecuacion B (a2, b2, c2).

    Returns:
        float: Valor de Delta_x = c1*b2 - c2*b1.
    """
    c1, b1 = coeficientes_a["r"], coeficientes_a["y"]
    c2, b2 = coeficientes_b["r"], coeficientes_b["y"]
    return calcular_determinante(c1, b1, c2, b2)


def calcular_determinante_y(coeficientes_a, coeficientes_b):
    """Calcula el determinante de Y (Delta_y).

    Args:
        coeficientes_a (dict): Diccionario con 'x', 'y', 'r' de la
            ecuacion A (a1, b1, c1).
        coeficientes_b (dict): Diccionario con 'x', 'y', 'r' de la
            ecuacion B (a2, b2, c2).

    Returns:
        float: Valor de Delta_y = a1*c2 - a2*c1.
    """
    a1, c1 = coeficientes_a["x"], coeficientes_a["r"]
    a2, c2 = coeficientes_b["x"], coeficientes_b["r"]
    return calcular_determinante(a1, c1, a2, c2)


def calcular_valor_x(delta_x, delta):
    """Calcula el valor de la incognita X.

    Args:
        delta_x (float): Determinante de X.
        delta (float): Determinante principal del sistema.

    Returns:
        float: Valor de X (delta_x / delta).

    Raises:
        ZeroDivisionError: Si delta es igual a 0.
    """
    if delta == 0:
        raise ZeroDivisionError("El determinante principal es 0.")
    return delta_x / delta


def calcular_valor_y(delta_y, delta):
    """Calcula el valor de la incognita Y.

    Args:
        delta_y (float): Determinante de Y.
        delta (float): Determinante principal del sistema.

    Returns:
        float: Valor de Y (delta_y / delta).

    Raises:
        ZeroDivisionError: Si delta es igual a 0.
    """
    if delta == 0:
        raise ZeroDivisionError("El determinante principal es 0.")
    return delta_y / delta


def resolver_sistema_cramer(coeficientes_a, coeficientes_b):
    """Aqui se aplica la Regla de Cramer.

    Args:
        coeficientes_a (dict): Diccionario con 'x', 'y', 'r' de la
            ecuacion A (a1, b1, c1).
        coeficientes_b (dict): Diccionario con 'x', 'y', 'r' de la
            ecuacion B (a2, b2, c2).

    Returns:
        dict: Diccionario con las llaves 'delta', 'delta_x', 'delta_y',
            'x' e 'y'. Si 'delta' es 0, 'x' e 'y' seran None.
    """
    delta = calcular_determinante_principal(coeficientes_a, coeficientes_b)
    delta_x = calcular_determinante_x(coeficientes_a, coeficientes_b)
    delta_y = calcular_determinante_y(coeficientes_a, coeficientes_b)

    resultado = {
        "delta": delta,
        "delta_x": delta_x,
        "delta_y": delta_y,
        "x": None,
        "y": None,
    }

    if delta != 0:
        resultado["x"] = calcular_valor_x(delta_x, delta)
        resultado["y"] = calcular_valor_y(delta_y, delta)

    return resultado