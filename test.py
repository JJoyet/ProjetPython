def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro")
    return x / y

print(divide(10, 0))