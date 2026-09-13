"""
Nombre: Ortega Plaza Diego
Matricula: 2403230009
Asignatura: Ciencia de Datos
Fecha: 12/09/26
"""

import Funciones_auxiliares as calculo

# Diccionarios globales que almacenan los coeficientes de cada ecuacion.
# Estructura: {"x": a, "y": b, "r": c}  ->  a*x + b*y = c
ecuacion_a = {"x": None, "y": None, "r": None}
ecuacion_b = {"x": None, "y": None, "r": None}


def solicitar_float(mensaje):
    """Solicita un numero al usuario y valida que sea convertible a float.

    Args:
        mensaje (str): Texto que se muestra al usuario al solicitar el dato.

    Returns:
        float: El numero ingresado por el usuario.
    """
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Valor invalido. Por favor ingresa un numero.\n")


def capturar_ecuacion(nombre_ecuacion):
    """Captura de forma secuencial los tres coeficientes de una ecuacion.

    Args:
        nombre_ecuacion (str): Etiqueta de la ecuacion ("A" o "B") que
            se muestra en los mensajes de captura.

    Returns:
        dict: Diccionario con los coeficientes capturados, con las
            llaves 'x', 'y' y 'r'.
    """
    print(f"\n--- Captura de la ecuacion {nombre_ecuacion} ---")
    coeficiente_x = solicitar_float("Captura coeficiente de X: ")
    coeficiente_y = solicitar_float("Captura coeficiente de Y: ")
    resultado = solicitar_float("Captura resultado de la ecuacion: ")

    return {"x": coeficiente_x, "y": coeficiente_y, "r": resultado}


def ecuaciones_completas():
    """Verifica que ambas ecuaciones (A y B) hayan sido capturadas.

    Returns:
        bool: True si ninguno de los coeficientes de A ni B es None,
            False en caso contrario.
    """
    valores_a = ecuacion_a.values()
    valores_b = ecuacion_b.values()
    return all(v is not None for v in valores_a) and all(
        v is not None for v in valores_b
    )


def mostrar_soluciones():
    """Calcula y muestra en consola los determinantes y la solucion.

    Valida primero que ambas ecuaciones hayan sido capturadas y que el
    determinante principal sea distinto de cero antes de mostrar los
    valores finales de X e Y.
    """
    if not ecuaciones_completas():
        print("\nDebes capturar primero la ecuacion A y la ecuacion B.\n")
        return

    resultado = calculo.resolver_sistema_cramer(ecuacion_a, ecuacion_b)

    print("\n--- Resultados ---")
    print(f"Delta (determinante principal): {resultado['delta']}")
    print(f"Delta X: {resultado['delta_x']}")
    print(f"Delta Y: {resultado['delta_y']}")

    if resultado["delta"] == 0:
        print(
            "\nEl sistema no tiene solucion unica "
            "(Delta = 0: sistema incompatible o con infinitas soluciones).\n"
        )
    else:
        print(f"X = {resultado['x']}")
        print(f"Y = {resultado['y']}\n")


def mostrar_menu():
    """El menu principal."""
    print("\n----- MENU PRINCIPAL -----")
    print("1. Capturar ecuacion A")
    print("2. Capturar ecuacion B")
    print("3. Mostrar soluciones")
    print("4. Salir")


def ejecutar_programa():
    """Controla el flujo principal del programa."""
    global ecuacion_a, ecuacion_b

    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            ecuacion_a = capturar_ecuacion("A")
        elif opcion == "2":
            ecuacion_b = capturar_ecuacion("B")
        elif opcion == "3":
            mostrar_soluciones()
        elif opcion == "4":
            print("\nFinalizando el programa.")
        else:
            print("\nOpcion invalida. Intenta de nuevo.\n")


if __name__ == "__main__":
    ejecutar_programa()