import requests

def problema8():
    datos_problema8 = []

    for mes in range(1, 13):
        url_bbdd = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year=2025"
        try:
            respuesta_bbdd = requests.get(url_bbdd)
            if respuesta_bbdd.status_code == 200:
                datos_mes = respuesta_bbdd.json()   # lista de dicts con fecha, compra, venta
                datos_problema8.extend(datos_mes)
            else:
                print(f"Error en mes {mes}, código {respuesta_bbdd.status_code}")
        except requests.RequestException:
            print(f"No se pudo conectar al API en el mes {mes}")

    if not datos_problema8:
        print("No se obtuvieron datos")
        return
    
    # Obtener las fechas donde el valor de compra del dólar sea el mínimo.
    minimo_compra = min(datos_problema8, key=lambda x: x["compra"])
    print(f"Mínimo valor de compra: {minimo_compra['compra']} realizada en {minimo_compra['fecha']}")

    # Obtener las fechas donde el valor de venta del dólar sea máximo.
    maximo_venta = max(datos_problema8, key=lambda x: x["venta"])
    print(f"Máximo valor de venta: {maximo_venta['venta']} realizada en {maximo_venta['fecha']}")

    # Obtener aquellas fechas donde el valor de la diferencia de compraventa sea máxima.
    max_dif = max(datos_problema8, key=lambda x: x["venta"] - x["compra"])
    diferencia = round(max_dif["venta"] - max_dif["compra"], 3)
    print(f"Mayor diferencia: {diferencia} realizada en {max_dif['fecha']}")

problema8()