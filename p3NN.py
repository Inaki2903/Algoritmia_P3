def fib(n: int) -> int:
    """
    Calcula el n-ésimo número de Fibonacci usando programación dinámica.
    
    Argumentos:
        n (int): Posición en la secuencia de Fibonacci (n >= 0).
    
    Retorna:
        int: Valor de Fibonacci en la posición n.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Programación dinámica bottom-up
    prev2 = 0
    prev1 = 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


def knapsack(W: int, weights: list[int], values: list[int]) -> int:
    """
    Resuelve el problema de la mochila 0/1 usando programación dinámica.
    
    Argumentos:
        W (int): Capacidad máxima de la mochila.
        weights (list[int]): Lista con los pesos de los objetos.
        values (list[int]): Lista con los valores de los objetos (misma longitud que weights).
    
    Retorna:
        int: Valor máximo que se puede obtener sin superar la capacidad W.
    """
    n = len(weights)
    
    # dp[i][w] = valor máximo usando los primeros i objetos con capacidad w
    # Optimización: solo necesitamos la fila anterior
    dp = [0] * (W + 1)
    
    for i in range(n):
        # Iteramos hacia atrás para evitar usar valores ya actualizados
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[W]


def lcs(X: str, Y: str) -> int:
    """
    Calcula la longitud de la subsecuencia común más larga entre dos cadenas.
    
    Argumentos:
        X (str): Primera cadena.
        Y (str): Segunda cadena.
    
    Retorna:
        int: Longitud de la subsecuencia común más larga.
    """
    m = len(X)
    n = len(Y)
    
    # dp[i][j] = longitud de LCS de X[0:i] y Y[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def coin_change(coins: list[int], amount: int) -> int:
    """
    Calcula el mínimo número de monedas necesarias para alcanzar una cantidad dada.
    
    Argumentos:
        coins (list[int]): Lista con los valores de las monedas disponibles.
        amount (int): Cantidad objetivo.
    
    Retorna:
        int: Número mínimo de monedas necesarias. Si no es posible, retorna -1.
    """
    # dp[i] = mínimo número de monedas para alcanzar la cantidad i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def unique_paths(m: int, n: int) -> int:
    """
    Calcula el número de caminos únicos en una cuadrícula de m filas y n columnas.
    
    Argumentos:
        m (int): Número de filas.
        n (int): Número de columnas.
    
    Retorna:
        int: Número total de caminos únicos desde la esquina superior izquierda a la inferior derecha.
    """
    # dp[i][j] = número de caminos únicos para llegar a la posición (i, j)
    # Optimización: solo necesitamos la fila anterior
    dp = [1] * n
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]
    
    return dp[n - 1]

