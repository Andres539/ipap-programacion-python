from django.shortcuts import render

# 1. Lógica de cálculo (Punto A)
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return consumo_kwh * factor_emision

# 2. Procesamiento de métricas (Punto B - Parte 1)
def obtener_metricas_consumo(registros):
    if not registros:
        return {
            "total_emisiones": 0.0,
            "planta_mayor_consumo": None,
            "detalle_plantas": []
        }

    total_emisiones = 0.0
    planta_mayor_consumo = None
    max_consumo = -1.0
    detalle_plantas = []

    for reg in registros:
        nombre = reg.get("planta")
        consumo = reg.get("consumo_kwh", 0)
        
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones
        
        if consumo > max_consumo:
            max_consumo = consumo
            planta_mayor_consumo = nombre

        detalle_plantas.append({
            "planta": nombre,
            "consumo_kwh": consumo,
            "emisiones": emisiones
        })

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "detalle_plantas": detalle_plantas
    }

# 3. Vista de Django (Punto B - Parte 2)
def vista_panel_sustentabilidad(request):
    # Datos simulados de plantas industriales
    registros_plantas = [
        {"planta": "Planta Norte", "consumo_kwh": 2500},
        {"planta": "Planta Sur", "consumo_kwh": 4100},
        {"planta": "Planta Este", "consumo_kwh": 1300},
    ]

    metricas = obtener_metricas_consumo(registros_plantas)

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "detalle_plantas": metricas["detalle_plantas"],
    }

    return render(request, "sustentabilidad/panel.html", contexto)
