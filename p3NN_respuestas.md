# AEDATA 2025-26, Práctica 3 - Respuestas Teóricas

## Ejercicio 1: Fibonacci con Programación Dinámica

### Pregunta: ¿Cuál es la complejidad del algoritmo frente a la versión recursiva simple?

**Respuesta:**

- **Versión recursiva simple**: Tiene complejidad temporal O(2^n) y complejidad espacial O(n) debido a la profundidad de la pila de llamadas recursivas. Esto se debe a que cada llamada a `fib(n)` genera dos llamadas recursivas (`fib(n-1)` y `fib(n-2)`), y muchas de estas llamadas se repiten múltiples veces (subproblemas superpuestos).

- **Versión con programación dinámica (bottom-up)**: Tiene complejidad temporal O(n) y complejidad espacial O(1) con la optimización utilizada (solo guardamos los dos valores anteriores). El algoritmo itera desde 2 hasta n una sola vez, calculando cada valor de Fibonacci exactamente una vez.

La mejora es significativa: de exponencial a lineal en tiempo, y de lineal a constante en espacio.

---

## Ejercicio 2: Problema de la Mochila 0/1

### Pregunta: ¿Cuál es la complejidad del algoritmo?

**Respuesta:**

- **Complejidad temporal**: O(n × W), donde n es el número de objetos y W es la capacidad máxima de la mochila. Esto se debe a que para cada uno de los n objetos, iteramos sobre todas las capacidades posibles desde W hasta el peso del objeto.

- **Complejidad espacial**: O(W) con la optimización utilizada (solo guardamos una fila de la tabla DP en lugar de toda la tabla n × W). Sin optimización sería O(n × W).

El algoritmo utiliza programación dinámica bottom-up, evitando recalcular subproblemas que ya han sido resueltos.

---

## Ejercicio 3: Longest Common Subsequence (LCS)

### Pregunta 1: ¿Cuál es la complejidad del algoritmo?

**Respuesta:**

- **Complejidad temporal**: O(m × n), donde m es la longitud de la cadena X y n es la longitud de la cadena Y. El algoritmo llena una tabla de tamaño (m+1) × (n+1), y cada celda se calcula en tiempo constante.

- **Complejidad espacial**: O(m × n) para almacenar la tabla DP. Con optimización se podría reducir a O(min(m, n)) si solo guardamos las dos últimas filas.

### Pregunta 2: ¿Cómo se modifica si solo queremos saber si existe una subsecuencia de longitud k?

**Respuesta:**

Para verificar si existe una subsecuencia común de longitud exactamente k, podemos modificar el algoritmo de dos formas:

1. **Modificación directa**: Después de calcular la tabla DP completa, simplemente verificamos si `dp[m][n] >= k`. Esto mantiene la complejidad O(m × n).

2. **Optimización temprana**: Podemos detener el algoritmo tan pronto como encontremos que `dp[i][j] >= k` en cualquier punto, aunque esto no mejora la complejidad en el peor caso.

3. **Enfoque alternativo**: Si solo necesitamos verificar existencia (no la longitud exacta), podemos usar un enfoque de "early termination" que se detiene cuando `dp[i][j] == k` y verifica si podemos extenderlo hasta el final. Sin embargo, la complejidad sigue siendo O(m × n) en el peor caso.

La complejidad temporal sigue siendo O(m × n) en todos los casos, ya que en el peor caso necesitamos llenar toda la tabla para estar seguros.

---

## Ejercicio 4: Cambio de Monedas

### Pregunta 1: ¿Cuál es la complejidad del algoritmo?

**Respuesta:**

- **Complejidad temporal**: O(amount × |coins|), donde `amount` es la cantidad objetivo y `|coins|` es el número de tipos de monedas diferentes. Para cada moneda, iteramos sobre todas las cantidades desde el valor de la moneda hasta `amount`.

- **Complejidad espacial**: O(amount) para almacenar el array DP que guarda el mínimo número de monedas para cada cantidad desde 0 hasta `amount`.

### Pregunta 2: ¿Qué ocurre si añadimos una restricción de número máximo de monedas por tipo?

**Respuesta:**

Si añadimos una restricción de que cada tipo de moneda solo se puede usar un número máximo de veces (por ejemplo, máximo `limit[i]` monedas del tipo `i`), el problema se vuelve más complejo:

1. **Modificación del algoritmo**: Necesitamos modificar la tabla DP para llevar cuenta de cuántas monedas de cada tipo hemos usado. Esto podría requerir una tabla tridimensional `dp[i][j][k]` donde `i` es la cantidad, `j` es el tipo de moneda, y `k` es el número de monedas de ese tipo usadas, o usar un enfoque diferente.

2. **Complejidad**: La complejidad temporal aumentaría significativamente. Si cada moneda tiene un límite `limit[i]`, la complejidad podría ser O(amount × |coins| × max(limits)), lo cual puede ser mucho mayor.

3. **Enfoque alternativo**: Podríamos modelar esto como un problema de mochila con múltiples copias limitadas de cada objeto, o usar programación dinámica con estados que incluyan el número de monedas usadas de cada tipo.

4. **Caso especial**: Si todos los límites son 1, volvemos al problema de mochila 0/1. Si los límites son infinitos, volvemos al problema original de cambio de monedas sin restricciones.

---

## Ejercicio 5: Caminos en una Cuadrícula

### Pregunta: ¿Cuál es la complejidad del enfoque dinámico?

**Respuesta:**

- **Complejidad temporal**: O(m × n), donde m es el número de filas y n es el número de columnas. El algoritmo itera sobre cada celda de la cuadrícula exactamente una vez (excepto la primera fila y columna que se inicializan a 1).

- **Complejidad espacial**: O(n) con la optimización utilizada, donde solo guardamos una fila de la tabla DP en lugar de toda la tabla m × n. Sin optimización sería O(m × n).

**Nota**: El número total de caminos únicos en una cuadrícula m × n es igual al coeficiente binomial C(m+n-2, m-1) o C(m+n-2, n-1), que se puede calcular directamente en O(min(m, n)) tiempo y O(1) espacio, pero el enfoque de programación dinámica es más intuitivo y fácil de entender.

---

## Resumen de Complejidades

| Ejercicio | Complejidad Temporal | Complejidad Espacial |
|-----------|----------------------|---------------------|
| Fibonacci | O(n) | O(1) |
| Mochila 0/1 | O(n × W) | O(W) |
| LCS | O(m × n) | O(m × n) |
| Cambio de Monedas | O(amount × \|coins\|) | O(amount) |
| Caminos en Cuadrícula | O(m × n) | O(n) |

