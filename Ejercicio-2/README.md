# Sistema de Gestión Ecotech - Trabajo Práctico Final

Desarrollo para administrar el inventario y catálogo de dispositivos ecológicos de la empresa Ecotech.

---

## Características del Proyecto

* **Programación Orientada a Objetos (POO):** Uso de herencia, encapsulamiento, polimorfismo y manejo de excepciones personalizadas.
* **Validación de Datos:** Control de errores de negocio (por ejemplo, prohibición de stock negativo mediante excepciones personalizadas).
* **Polimorfismo:** Implementación del método `a_diccionario()` en las clases para delegar la serialización sin usar condiciones de tipo (`isinstance`).
* **Persistencia de Datos:** Exportación automática del catálogo completo a un archivo formato `JSON` estructurado con codificación UTF-8.

---

## Estructura del Código

1. **`StockInvalidoError`**: Excepción personalizada para manejar errores cuando se intenta asignar un stock menor a cero.
2. **`DispositivoEcologico`**: Clase base (padre) que define los atributos comunes de cualquier equipo (código, nombre, precio, stock encapsulado) y su conversión a diccionario.
3. **`PanelSolar`**: Clase derivada (hija) que hereda de `DispositivoEcologico`, agregando atributos específicos (`potencia_kw`, `eficiencia`) y adaptando su ficha técnica y serialización (polimorfismo).
4. **`GestorInventario`**: Clase encargada de recolectar los productos y generar el archivo JSON en el directorio de ejecución de forma segura usando rutas absolutas (`os` + `json`).

---
