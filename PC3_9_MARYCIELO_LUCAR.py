import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    libreria_fuentes = figlet.getFonts()

    while True:
        fuente_ingresada = input("Nombre de la fuente a utilizar (Enter para aleatoria): ").strip()

        if fuente_ingresada == "":
            fuente_a_utilizar = random.choice(libreria_fuentes)
            print(f"Se eligió una fuente aleatoria: '{fuente_a_utilizar}'")
        else:
            if fuente_ingresada in libreria_fuentes:
                fuente_a_utilizar = fuente_ingresada
                print(f"Se va a utilizar la fuente: '{fuente_a_utilizar}'")
            else:
                fuente_a_utilizar = random.choice(libreria_fuentes)
                print(f"La fuente ingresada '{fuente_ingresada}' no existe.")
                print(f"Se eligió aleatoriamente: '{fuente_a_utilizar}'")

        texto_a_graficar = input("Texto que deseas imprimir: ")

        figlet.setFont(font=fuente_a_utilizar)
        resultado_texto_graficado = figlet.renderText(texto_a_graficar)
        print(resultado_texto_graficado)

        # Para preguntar si quiere graficar otro texto
        respuesta_usuario = input("¿Quieres graficar otro texto? (SI/NO): ").strip().lower()
        if respuesta_usuario not in ("si", "SI", "sí", "SÍ"):
            print("Gracias! :)")
            break

if __name__ == "__main__":
    main()

