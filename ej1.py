# Ejercicio 1: Fibonacci con Programación Dinámica 

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

    dp = [0] * (n + 1)

    dp[0]=0

    dp[1] =1  

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
