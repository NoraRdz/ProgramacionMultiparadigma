from functools import reduce

# --- Datos de prueba ---
ventas_ejemplo = [ 
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80},
    {'id': 5, 'monto': 300},
]


def es_venta_mayor_a_100(venta):
    return venta['monto'] > 100

def calcular_impuesto_y_formatear(venta):
    monto_con_impuesto = venta['monto'] * 1.15
    return {
        'id': venta['id'],
        'monto_original': venta['monto'],
        'monto_final': monto_con_impuesto
    }

def sumar_totales(acumulador, venta_procesada):
    return acumulador + venta_procesada['monto_final']


def procesar_ventas_funcional(ventas):
    ventas_filtradas = list(filter(es_venta_mayor_a_100, ventas))
    resultado = list(map(calcular_impuesto_y_formatear, ventas_filtradas))
    total = reduce(sumar_totales, resultado, 0)
    
    return resultado, total


if __name__ == "__main__":
    lista_final, gran_total = procesar_ventas_funcional(ventas_ejemplo)
    
    print("=== Resultado del procesamiento funcional ===")
    print(f"Total acumulado: {gran_total}")
    print("Lista de ventas procesadas:")
    for v in lista_final:
        print(v)