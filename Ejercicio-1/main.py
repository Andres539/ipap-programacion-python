"""
Puntos pendientes
2 Comentarios de funciones


"""
from typing import TypedDict, Optional, List, Tuple


class RegistroSensor(TypedDict):
    sensor_id: str
    temperatura: str
    ubicacion: Optional[str]

def get_sensor_id(registro: RegistroSensor) -> str:
    if registro.get("sensor_id") is None:
        raise KeyError("El sensor_id no existe")
    return registro["sensor_id"].strip()

def get_temperatura(registro: RegistroSensor) -> str:
    if registro.get("temperatura") is None:
        return KeyError("La temperatura no existe")
    return registro["temperatura"].strip().replace("°C", "").replace("C", "")

def get_ubicacion(registro: RegistroSensor) -> str:
    
    if registro.get("ubicacion") is None:
        return "Ubicación desconocida"
    return registro["ubicacion"].strip()


class Sensor(TypedDict):
    sensor_id: str
    temperatura: float
    ubicacion: str

def limpiar_registro_sensor(registro_raw: RegistroSensor) -> Sensor:
    """
    Raises:
        KeyError: El sensor_id no existe en el registro_raw
        KeyError: La temperatura no existe en el registro_raw
    """
    sensor_id = get_sensor_id(registro_raw)
    otuputTemperatura = float(get_temperatura(registro_raw))
    ubicacion = get_ubicacion(registro_raw)

    return {
        "sensor_id": sensor_id,
        "temperatura": otuputTemperatura,
        "ubicacion": ubicacion
    }

def generar_resumen_sensores(
        lista_sensores_limpios: Sensor, 
        umbral_temperatura: float) -> Tuple[List[str], float]:
    sensores_alerta = []
    suma_temperaturas = 0

    for sensor in lista_sensores_limpios:
        suma_temperaturas += sensor["temperatura"]

        if sensor["temperatura"] > umbral_temperatura:
            sensores_alerta.append(sensor["sensor_id"])

    if len(lista_sensores_limpios) > 0:
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    else:
        promedio_temperatura = 0.0

    return sensores_alerta, promedio_temperatura


if __name__ == "__main__":
    # Datos de trabajo
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-002", "temperatura": "31.2°C", "ubicacion": " Planta Sur "},
        {"sensor_id": "SENSOR-003 ", "temperatura": "28.7C"},
        {"sensor_id": " SENSOR-004 ", "temperatura": "33.4C", "ubicacion": "Depósito"}
    ]

    sensores_limpios = []

    for registro in registros_crudos:
        sensores_limpios.append(limpiar_registro_sensor(registro))

    umbral = float(input("Ingrese el umbral de temperatura a controlar: "))

    sensores_alerta, promedio = generar_resumen_sensores(
        sensores_limpios,
        umbral
    )

    print("\n--- REPORTE DE SENSORES ---")
    print(f"Umbral: {umbral:.2f} °C")
    print(f"Temperatura promedio: {promedio:.2f} °C")

    print("Sensores en alerta:")

    if sensores_alerta:
        for sensor_id in sensores_alerta:
            print(sensor_id)
    else:
        print("Ningún sensor supera el umbral ingresado.")
