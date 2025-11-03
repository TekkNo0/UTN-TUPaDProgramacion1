nombre_archivo = "productos.txt"
productos = []

print("--- Cargando Productos ---")

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    next(archivo, None)
    for linea in archivo:
        linea_limpia = linea.strip()
        
        if linea_limpia:
            partes = linea_limpia.split(",")
            
            producto = {
                'nombre': partes[0],
                'precio': float(partes[1]),
                'cantidad': int(partes[2])
            }
            productos.append(producto)

print("Productos cargados en la lista de diccionarios:")
print(productos)
print("---------------------------------")


print("\n--- Buscar Producto ---")
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for producto in productos:
    if producto['nombre'].lower() == nombre_buscar.lower():
        print("\n¡Producto encontrado!")
        print(f"  Nombre:   {producto['nombre']}")
        print(f"  Precio:   ${producto['precio']}")
        print(f"  Cantidad: {producto['cantidad']}")
        encontrado = True
        break 

if not encontrado:
    print(f"\nError: El producto '{nombre_buscar}' no se encuentra en la lista.")


print("\n--- Agregar Nuevo Producto ---")
nuevo_nombre = input("Ingrese el nombre del producto: ")
nuevo_precio = input("Ingrese el precio: ")
nueva_cantidad = input("Ingrese la cantidad: ")

nuevo_producto_dict = {
    'nombre': nuevo_nombre,
    'precio': float(nuevo_precio),
    'cantidad': int(nueva_cantidad)
}
productos.append(nuevo_producto_dict)

print(f"\n¡Producto '{nuevo_nombre}' agregado a la lista!")

print("\nLista actualizada (antes de guardar):")
print(productos)
print("---------------------------------")


print("\n--- Guardando Lista Actualizada en Archivo ---")

with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    for producto in productos:
        nombre = producto['nombre']
        precio = producto['precio']
        cantidad = producto['cantidad']
        linea_para_guardar = f"{nombre},{precio},{cantidad}\n"
        
        archivo.write(linea_para_guardar)

print(f"¡Archivo '{nombre_archivo}' sobrescrito con éxito con la lista actualizada!")