"""Aproximacion por Montecarlo de la interseccion elipse-hiperbola."""
import math
import random


def leer_positivo(nombre, entero=False):
    while True:
        try:
            valor = int(input(f"Ingrese {nombre}: ")) if entero else float(input(f"Ingrese {nombre}: "))
            if valor <= 0:
                print("El valor debe ser mayor que cero.")
                continue
            return valor
        except ValueError:
            print("Ingrese un numero valido.")


def estimar_area(a, b, c, d, cantidad, generador=None):
    if min(a, b, c, d, cantidad) <= 0 or int(cantidad) != cantidad:
        raise ValueError("Los parametros deben ser positivos y cantidad entera.")
    generador = generador if generador is not None else random.Random()
    dentro_elipse = 0
    en_interseccion = 0

    for _ in range(int(cantidad)):
        x = generador.uniform(-a, a)
        y = generador.uniform(-b, b)
        elipse = (x ** 2 / a ** 2) + (y ** 2 / b ** 2) <= 1
        hiperbola = (x ** 2 / c ** 2) - (y ** 2 / d ** 2) >= 1
        if elipse:
            dentro_elipse += 1
            if hiperbola:
                en_interseccion += 1

    area_elipse = math.pi * a * b
    area_aprox = area_elipse * en_interseccion / dentro_elipse if dentro_elipse else 0.0
    return dentro_elipse, en_interseccion, area_elipse, area_aprox


def main():
    print("CALCULO DE AREA POR MONTECARLO")
    a = leer_positivo("a (semieje horizontal de la elipse)")
    b = leer_positivo("b (semieje vertical de la elipse)")
    c = leer_positivo("c (hiperbola)")
    d = leer_positivo("d (hiperbola)")
    cantidad = leer_positivo("cantidad de puntos", entero=True)
    dentro, interseccion, area_elipse, area = estimar_area(a, b, c, d, cantidad)
    print("\n--- RESULTADOS ---")
    print(f"Puntos aleatorios generados: {cantidad}")
    print(f"Puntos dentro de la elipse: {dentro}")
    print(f"Puntos en la interseccion: {interseccion}")
    print(f"Area de la elipse: {area_elipse:.6f}")
    print(f"Area aproximada de interseccion: {area:.6f}")
    print("Formula: area_elipse * (puntos_interseccion / puntos_elipse)")


if __name__ == "__main__":
    main()
