class InventarioTienda:

    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []  # Lista vacía de productos

    def agregar_producto(self, nombre, precio, cantidad):
        # Validación de valores positivos
        if precio <= 0 or cantidad <= 0:
            print(
                " Error: El precio y la cantidad deben ser valores mayores a 0."
            )
            return False

        # Comprobar si el producto ya existe para actualizar stock
        for prod in self.productos:
            if prod["nombre"].lower() == nombre.lower():
                prod["cantidad"] += cantidad
                prod["precio"] = precio
                print(
                    f" Stock actualizado para '{prod['nombre']}'. Nueva cantidad: {prod['cantidad']}"
                )
                return True

        # Agregar nuevo producto
        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }
        self.productos.append(nuevo_producto)
        print(f" Producto '{nombre}' agregado exitosamente al inventario.")
        return True

    def vender_producto(self, nombre, cantidad):
        if cantidad <= 0:
            print(" Error: La cantidad a vender debe ser mayor a 0.")
            return False

        for prod in self.productos:
            if prod["nombre"].lower() == nombre.lower():
                if cantidad > prod["cantidad"]:
                    print(
                        f" Error: Stock insuficiente. Solo hay {prod['cantidad']} unidad(es) de '{prod['nombre']}'."
                    )
                    return False

                prod["cantidad"] -= cantidad
                print(
                    f" Venta realizada: {cantidad} unidad(es) de '{prod['nombre']}'."
                )
                print(f" Stock restante: {prod['cantidad']}")
                return True

        print(f" Error: El producto '{nombre}' no existe en el inventario.")
        return False

    def mostrar_inventario(self):
        if not self.productos:
            print("\n El inventario se encuentra actualmente vacío.")
            return

        print(f"\n--- INVENTARIO DE {self.nombre_tienda.upper()} ---")
        for prod in self.productos:
            print(
                f"• Producto: {prod['nombre']} | Precio: ${prod['precio']:.2f} | Cantidad en stock: {prod['cantidad']}"
            )

    def producto_mas_caro(self):
        if not self.productos:
            return None

        mas_caro = max(self.productos, key=lambda p: p["precio"])
        return mas_caro["nombre"], mas_caro["precio"]


def menu():
    nombre = input("Ingrese el nombre de la tienda: ").strip()
    tienda = InventarioTienda(nombre if nombre else "Tienda MiPyME")

    while True:
        print("\n==========================================")
        print(f"   GESTIÓN DE INVENTARIO: {tienda.nombre_tienda}")
        print("==========================================")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Mostrar inventario")
        print("4. Consultar producto más caro")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            nombre_prod = input("Nombre del producto: ").strip()
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad de unidades: "))
                if nombre_prod:
                    tienda.agregar_producto(nombre_prod, precio, cantidad)
                else:
                    print(
                        " Error: El nombre del producto no puede estar vacío."
                    )
            except ValueError:
                print(
                    " Error: Ingrese valores numéricos válidos para precio y cantidad."
                )

        elif opcion == "2":
            nombre_prod = input("Nombre del producto a vender: ").strip()
            try:
                cantidad = int(input("Cantidad a vender: "))
                if nombre_prod:
                    tienda.vender_producto(nombre_prod, cantidad)
                else:
                    print(" Error: Debe ingresar el nombre de un producto.")
            except ValueError:
                print(
                    " Error: Ingrese un número entero válido para la cantidad."
                )

        elif opcion == "3":
            tienda.mostrar_inventario()

        elif opcion == "4":
            resultado = tienda.producto_mas_caro()
            if resultado is None:
                print(
                    " El inventario está vacío. No hay productos para evaluar."
                )
            else:
                nombre_p, precio_p = resultado
                print(
                    f"\n El producto más caro es '{nombre_p}' con un precio de ${precio_p:.2f}"
                )

        elif opcion == "5":
            print("\nSaliendo del sistema de inventario. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()