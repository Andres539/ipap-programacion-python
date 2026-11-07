
# Consigna

Ejercicio 1 -
Sanitización y Análisis Estadístico de Sensores (20 puntos)

Los microcontroladores de EcoTech Solutions transmiten lecturas térmicas en formato heterogéneo con espacios indeseados, textos mezclados con unidades de medida y atributos incompletos. Se necesita un componente que normalice estos registros individuales y genere un reporte consolidado para la toma de decisiones.

Punto A: Normalización de Lecturas ( limpiar_registro_sensor ): Diseña la función limpiar_registro_sensor(registro_raw) encargada de procesar un diccionario con datos crudos de un sensor (por ejemplo: {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}). La función debe transformar la información para retornar un nuevo diccionario estandarizado, garantizando que el identificador quede sin espacios sobrantes, la temperatura sea un valor numérico de tipo float sin sufijos de unidad, y la ubicación posea un valor por defecto seguro en caso de no haberse registrado.

Punto B: Monitoreo y Mapeo Estadístico ( generar_resumen_sensores ): Desarrolla la función generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura) que tome una colección de registros sanitizados previamente con la función del Punto A y un valor límite. Debe retornar una tupla (lista_sensores_alerta, promedio_temperatura) conteniendo los IDs de los dispositivos que superan el umbral estipulado y el promedio térmico global de la planta. Incluye un bloque de ejecución que demuestre el flujo completo desde la limpieza de registros crudos hasta la impresión formateada del reporte final.

# Gestión de Equipos Energéticos

Proyecto desarrollado en Python para representar y administrar equipos energéticos.

## Descripción

El programa utiliza Programación Orientada a Objetos (POO) para modelar distintos equipos energéticos y controlar atributos como:

- Código del equipo
- Nombre
- Precio
- Stock disponible

También se define una excepción personalizada para controlar valores de stock inválidos.

## Estructura del programa

### Clase `StockInvalidoError`

Excepción personalizada que permitirá controlar errores relacionados con valores de stock no válidos.

```python
class StockInvalidoError(Exception):
    pass
```

### Clase `EquipoEnergetico`

Representa un equipo energético genérico.

El constructor recibe:

- `codigo`: identificador del equipo.
- `nombre`: nombre del equipo.
- `precio`: precio del equipo.
- `stock`: cantidad disponible.

Ejemplo:

```python
equipo = EquipoEnergetico(
    "EQ-001",
    "Equipo Solar",
    1500.0,
    10
)
```

El stock se almacena como un atributo privado:

```python
self.__stock
```

y se modifica mediante el método:

```python
asignar_stock()
```

Esto permite validar el valor antes de modificar el stock.

### Clase `PanelFotovoltaico`

Hereda de la clase `EquipoEnergetico`.

```python
class PanelFotovoltaico(EquipoEnergetico):
    pass
```

De esta manera, un panel fotovoltaico podrá reutilizar los atributos y métodos definidos para los equipos energéticos.

### Clase `AdministradorCatalogo`

Clase destinada a administrar el catálogo de equipos.

```python
class AdministradorCatalogo():
    pass
```

Actualmente su implementación se encuentra pendiente.

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Herencia
- Encapsulamiento
- Excepciones personalizadas

También se importa el módulo estándar:

```python
import json
```

que podrá utilizarse para trabajar con información en formato JSON.

## Estado del proyecto

El programa se encuentra en desarrollo.

Actualmente están definidas las estructuras principales:

1. `StockInvalidoError`
2. `EquipoEnergetico`
3. `PanelFotovoltaico`
4. `AdministradorCatalogo`

Queda pendiente completar las validaciones y funcionalidades de administración del catálogo.

## Ejecución

Para ejecutar el programa:

```bash
python main.py
```

Se requiere Python 3 instalado en el equipo.
