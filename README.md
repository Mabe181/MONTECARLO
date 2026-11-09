# Método de Montecarlo: elipse e hipérbola

Programa en Python que aproxima el área de intersección entre la elipse `x²/a² + y²/b² <= 1` y la región `x²/c² - y²/d² >= 1`.

## Ejecución

```bash
python montecarlo.py
```

Ingresar los parámetros a, b, c, d y la cantidad de puntos solicitada.

## Resultados de las pruebas

| Prueba | a | b | c | d | Puntos generados | Dentro de elipse | Intersección | Área aproximada |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 10 | 5 | 4 | 4 | 1000 | 796 | 325 | 64.134272 |
| 2 | 12 | 7 | 5 | 4 | 10000 | 7830 | 2888 | 97.334003 |
| 3 | 10 | 5 | 4 | 4 | 100000 | 78563 | 33661 | 67.302134 |

La fórmula usada es `πab × (puntos_intersección / puntos_elipse)`. Como se emplean muestras aleatorias, los resultados varían entre ejecuciones.
