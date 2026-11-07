import json
import os


class StockInvalidoError(Exception):
    pass


class DispositivoEcologico:

    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

        self.__stock = 0
        self.asignar_stock(stock)

    def asignar_stock(self, nuevo_stock: int) -> None:
        if nuevo_stock < 0:
            raise StockInvalidoError("El stock no puede ser negativo")

        self.__stock = nuevo_stock

    def obtener_stock(self) -> int:
        return self.__stock

    def mostrar_ficha_tecnica(self) -> str:
        return (
            f"Codigo: {self.codigo}, "
            f"Nombre: {self.nombre}, "
            f"Precio: ${self.precio}, "
            f"Stock: {self.obtener_stock()}"
        )

    def a_diccionario(self) -> dict:
        """Convierte los datos básicos del dispositivo en un diccionario."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.obtener_stock()
        }


class PanelSolar(DispositivoEcologico):

    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        stock: int,
        potencia_kw: float,
        eficiencia: float
    ):
        super().__init__(codigo, nombre, precio, stock)

        self.potencia_kw = potencia_kw
        self.eficiencia = eficiencia

    def mostrar_ficha_tecnica(self) -> str:
        return (
            f"Codigo: {self.codigo}, "
            f"Nombre: {self.nombre}, "
            f"Precio: ${self.precio}, "
            f"Stock: {self.obtener_stock()}, "
            f"Potencia: {self.potencia_kw} KW, "
            f"Eficiencia: {self.eficiencia}%"
        )

    def a_diccionario(self) -> dict:
        """Extiende el diccionario del padre sumando los atributos propios del panel."""
        producto = super().a_diccionario()
        producto["potencia_kw"] = self.potencia_kw
        producto["eficiencia"] = self.eficiencia
        return producto


class GestorInventario:

    def guardar_catalogo_json(self, lista_dispositivos: list, ruta_archivo: str) -> None:
        catalogo = []

        # Gracias al polimorfismo, cada objeto sabe cómo convertirse a diccionario
        for dispositivo in lista_dispositivos:
            catalogo.append(dispositivo.a_diccionario())

        ruta = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            ruta_archivo
        )

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, indent=4, ensure_ascii=False)

        print(f"\nCatalogo guardado con exito en: {ruta}")


# --- Instancio los objetos ---

panel1 = PanelSolar(
    "PS001",
    "Panel Solar Hogar",
    500,
    10,
    5,
    21.5
)

panel2 = PanelSolar(
    "PS002",
    "Panel Solar Industrial",
    1500,
    20,
    10,
    20
)

equipo1 = DispositivoEcologico(
    "DE001",
    "Controlador de Energia",
    800,
    15
)


# --- Prueba de stock invalido ---
try:
    panel_erroneo = PanelSolar(
        "PS003",
        "Panel Solar Prueba",
        600,
        -10,
        5,
        20
    )

except StockInvalidoError as error:
    print(f"Error controlado: {error}")


# Productos validos
productos = [panel1, panel2, equipo1]


# --- Mostrar fichas tecnicas ---
print("\n--- CATALOGO ECOTECH ---")

for producto in productos:
    print(producto.mostrar_ficha_tecnica())


# --- Guardar catalogo ---
gestor = GestorInventario()
gestor.guardar_catalogo_json(
    productos,
    "catalogo_ecotech.json"
)