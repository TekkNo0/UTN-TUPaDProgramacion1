while True:
    num1 = int(input("Ingrese el primer número (distinto de 0): "))
    num2 = int(input("Ingrese el segundo número (distinto de 0): "))

    if num1 != 0 and num2 != 0:
        break
    else:
        print("Intente de nuevo.")

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)