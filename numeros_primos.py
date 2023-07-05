def calcular_primos(N):
    primos = []
    for num in range(2, N + 1):
        ok_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                ok_primo = False
                break

        if ok_primo:
            primos.append(num)

    return primos


N = 5
resultado = calcular_primos(N)
print(resultado)
