def solicitar_fraccion():
    fraccion_ingresada = input("Ingrese fracción en formato X/Y: ").strip()
    if "/" not in fraccion_ingresada:
        raise ValueError("Formato inválido, debe contener '/'.")

    x_fraccion, y_fraccion = fraccion_ingresada.split("/", 1)
    x_fraccion, y_fraccion = x_fraccion.strip(), y_fraccion.strip()

    try:
        x = int(x_fraccion)
        y = int(y_fraccion)
    except ValueError:
        raise ValueError("X y Y deben ser enteros.")

    if y == 0:
        raise ZeroDivisionError("Y no puede ser 0.")

    if x > y:
        raise ValueError("X debe ser menor o igual a Y.")

    if x < 0 or y < 0:
        raise ValueError("X y Y deben ser enteros no negativos.")

    return x, y


def nivel_combustible(x, y):
    ratio_combustible = x / y
    if ratio_combustible < 0.01:
        return "E"
    if ratio_combustible > 0.99:
        return "F"
    return f"{round(ratio_combustible * 100)}%"


def main():
    while True:
        try:
            x, y = solicitar_fraccion()
            resultado_fraccion = nivel_combustible(x, y)
            print(resultado_fraccion)
            break
        except ZeroDivisionError:
            print("Error: Y no puede ser 0. Digite nuevamente la fracción.")
        except ValueError as e:
            print(f"Error: {e} Digite nuevamente la fracción.")


if __name__ == "__main__":
    main()