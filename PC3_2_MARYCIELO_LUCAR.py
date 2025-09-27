def menu():
    while True:
        print("\nMENÚ DE OPCIONES")
        print("3. Problema 3 - Cargar alumnos")
        print("4. Problema 4 - Rectángulo y Cuadrado")
        print("5. Problema 5 - Aprobados y desaprobados")
        print("6. Problema 6 - Promedio del curso")
        print("7. Problema 7 - Mayor y menor promedio")
        print("8. Problema 8 - Buscar alumno por nombre")
        print("0. Salir")
        
        try:
            opcion = int(input("Seleccione opción: "))
            if  opcion == 3:
                problema3()
            elif opcion == 4:
                problema4()
            elif opcion == 5:
                problema5()
            elif opcion == 6:
                problema6()
            elif opcion == 7:
                problema7()
            elif opcion == 8:
                problema8()
            elif opcion == 0:
                 print("Gracias! :)")
                 break
            else:
                print("Opción no válida, intente de nuevo.")
        except ValueError:
            print("Debe ingresar un número entero.")


# PROBLEMA 3: Cargar n alumnos 
base_alumnos = []

def problema3():
    print("\n Cargar alumnos")
    try:
        cant_alumnos = int(input("¿Cuántos alumnos desea ingresar? "))
        if cant_alumnos <= 0:
            print("El número de alumnos debe ser >= 1")
            return
    except ValueError:
        print("Ingrese un número entero.")
        return

    for i in range(1, cant_alumnos+1):
        nombre_alumno = input(f"Nombre del alumno {i}: ").strip()
        notas_alumno = []
        for j in range(1, 4):
            while True:
                try:
                    nota_ingresada = float(input(f"Nota {j} (0-10): "))
                    if 0 <= nota_ingresada <= 10:
                        notas_alumno.append(nota_ingresada)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10")
                except ValueError:
                    print("Ingrese número válido")
        base_alumnos.append({"Nombre": nombre_alumno, "Notas": notas_alumno})
    print("\nListado de alumnos cargados:")
    for alumno in base_alumnos:
        notas_txt = ", ".join(str(n) for n in alumno["Notas"])
        print(f"- {alumno['Nombre']} | Notas: [{notas_txt}]")

# PROBLEMA 4: RECTÁNGULO - CUADRADO 
class RECTANGULO:
    def __init__(self, largo_rect, ancho_rect):
        if largo_rect <= 0 or ancho_rect <= 0:
            raise ValueError("Dimensiones > 0.")
        self.largo = largo_rect
        self.ancho = ancho_rect

    def area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado_cuadrado):
        super().__init__(lado_cuadrado, lado_cuadrado)

def problema4():
    print("\nÁrea del rectángulo y cuadrado")
    try:
        largo_a_evaluar = float(input("Largo del rectángulo: "))
        ancho_a_evaluar = float(input("Ancho del rectángulo: "))
        rect = RECTANGULO(largo_a_evaluar, ancho_a_evaluar)
        print(f"Área del rectángulo = {rect.area():.2f}")

        lado_cuadrado = float(input("Lado del cuadrado: "))
        cuad = CUADRADO(lado_cuadrado)
        print(f"Área del cuadrado = {cuad.area():.2f}")
    except ValueError as e:
        print(f"Error: {e}")


# PROBLEMA 5: Alumnos aprobados y desaprobados
def problema5():
    print("\nAprobados y desaprobados")
    if not base_alumnos:
        print("Primero debe cargar información de alumnos, elija opción 3")
        return
    alum_aprob = 0
    for a in base_alumnos:
        prom = sum(a["Notas"]) / 3   # calcular al vuelo
        if prom >= 4:
            alum_aprob += 1
    alum_desap = len(base_alumnos) - alum_aprob
    print(f"Aprobados: {alum_aprob} | Desaprobados: {alum_desap}")


# PROBLEMA 6: Alumnos aprobados y desaprobados
def problema6():
    if not base_alumnos:
        print("Primero debe cargar información de alumnos, elija opción 3")
        return
    promedio_total = sum(sum(a["Notas"]) / 3 for a in base_alumnos) / len(base_alumnos)
    print(f"Promedio del curso = {promedio_total:.2f}")


# PROBLEMA 7: Mayor y menos promedio
def problema7():
    print("\nMayor y menor promedio")
    if not base_alumnos:
        print("Primero debe cargar información de alumnos, elija opción 3")
        return

    # función helper para el promedio
    def prom(a): 
        return sum(a["Notas"]) / 3

    mayor = max(base_alumnos, key=prom)
    menor = min(base_alumnos, key=prom)
    print(f"Mayor promedio: {mayor['Nombre']} ({prom(mayor):.2f})")
    print(f"Menor promedio: {menor['Nombre']} ({prom(menor):.2f})")


# PROBLEMA 8: Buscar alumno por nombre
def problema8():
    print("\nBuscar alumno por nombre")
    if not base_alumnos:
        print("Primero debe cargar información de alumnos, elija opción 3")
        return
    
    term = input("Nombre (o parte de él): ").strip().lower()
    resultados_busqueda = [a for a in base_alumnos if term in a["Nombre"].lower()]
    
    if not resultados_busqueda:
        print("No se encontraron coincidencias.")
        return []

    print("\nCoincidencias encontradas:")
    for a in resultados_busqueda:
        notas_txt = ", ".join(f"{n:.1f}" for n in a["Notas"])
        prom = sum(a["Notas"]) / 3    # calcular al vuelo
        print(f"- {a['Nombre']} | Notas: [{notas_txt}] | Promedio: {prom:.2f}")
    return resultados_busqueda

if __name__ == "__main__":
    menu()