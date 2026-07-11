
# Datos iniciales a modo de ejemplo y pruebas
# ==========================================

d_prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
}

d_bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],
}

# Funciones de validación
# ==========================================

def validar_texto(texto):
    return texto.strip() != ""


def validar_mayor_a_cero(valor):
    try:
        return int(valor) > 0
    except ValueError:
        return False


def validar_mayor_igual_a_cero(valor):
    try:
        return int(valor) >= 0
    except ValueError:
        return False


def validar_si_o_no(valor):
    return valor.lower() in ("s", "n")


def convertir_a_booleano(valor):
    return valor.strip().lower() == "s"

# Funciones principales
# ==========================================

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de Prendas por rango de precio")
    print("3. Actualizar precio de Prenda")
    print("4. Agregar Prenda")
    print("5. Eliminar Prenda")
    print("6. Salir")
    print("====================================")


def leer_opcion():

    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe ingresar una opción entre 1 y 6.")
        except ValueError:
            print("Debe seleccionar una opción válida.")

def buscar_codigo(diccionario, codigo):

    codigo = codigo.upper()
    for clave in diccionario:
        if clave.upper() == codigo:
            return True
    return False

def unidades_categoria(d_prendas, d_bodega, categoria):

    total = 0
    for codigo in d_prendas:
        if d_prendas[codigo][1].lower() == categoria.lower():
            total += d_bodega[codigo][1]
    print(f"Total de unidades: {total}")


def busqueda_precio(d_prendas, d_bodega, p_minimo, p_maximo):

    resultados = []
    for codigo in d_bodega:
        precio = d_bodega[codigo][0]
        stock = d_bodega[codigo][1]
        if p_minimo <= precio <= p_maximo and stock > 0:
            nombre = d_prendas[codigo][0]
            resultados.append(f"{nombre} - {codigo} - ${precio}")
    resultados.sort()
    return resultados


def actualizar_precio(d_bodega, codigo, nuevo_precio):

    codigo = codigo.upper()
    if buscar_codigo(d_bodega, codigo):
        d_bodega[codigo][0] = nuevo_precio
        return True
    return False

def agregar_prenda(d_prendas,
                d_bodega,
                codigo,
                nombre,
                categoria,
                talla,
                color,
                material,
                es_unisex,
                precio,
                unidades):

    codigo = codigo.upper()

    if buscar_codigo(d_prendas, codigo):
        return False

    d_prendas[codigo] = [
        nombre,
        categoria,
        talla,
        color,
        material,
        es_unisex
    ]

    d_bodega[codigo] = [
        precio,
        unidades
    ]
    return True

def eliminar_prenda(d_prendas, d_bodega, codigo):

    codigo = codigo.upper()
    if not buscar_codigo(d_prendas, codigo):
        return False
    del d_prendas[codigo]
    del d_bodega[codigo]
    return True

# Programa principal
# ==========================================

def programa_principal():

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            categoria = input("Ingrese la categoría: ").strip()
            while not validar_texto(categoria):
                categoria = input("Ingrese la categoría: ").strip()
            unidades_categoria(d_prendas, d_bodega, categoria)

        elif opcion == 2:
            while True:
                try:
                    p_minimo = int(input("Precio mínimo: "))
                    p_maximo = int(input("Precio máximo: "))
                    if p_minimo <= p_maximo:
                        break
                    print("El mínimo no puede ser mayor que el máximo.")
                except ValueError:
                    print("Debe ingresar valores enteros.")
            lista = busqueda_precio(d_prendas, d_bodega, p_minimo, p_maximo)
            if len(lista) == 0:
                print("No existen prendas en ese rango.")
            else:
                print("\nPrendas encontradas:")
                for prenda in lista:
                    print(prenda)

        elif opcion == 3:
            while True:

                codigo = input("Ingrese el Código: ").strip().upper()
                while True:
                    precio = input("Ingrese el Nuevo precio: ")
                    if validar_mayor_a_cero(precio):
                        precio = int(precio)
                        break
                    print("Debe ingresar un entero mayor que cero.")
                if actualizar_precio(d_bodega, codigo, precio):
                    print("Precio actualizado correctamente.")
                else:
                    print("Código no encontrado.")
                while True:
                    respuesta = input("¿Desea actualizar otro precio? (S/N): ").strip().upper()
                    if respuesta == "S":
                        break
                    elif respuesta == "N":
                        break
                    else:
                        print("Debe ingresar S o N.")
                if respuesta == "N":
                    break

        elif opcion == 4:

            while True:
                codigo = input("Ingrese el Código: ").strip().upper()
                if validar_texto(codigo) and not buscar_codigo(d_prendas, codigo):
                    break
                print("Código inválido o existente.")
            while True:
                nombre = input("Ingrese el Nombre: ").strip()
                if validar_texto(nombre):
                    break
            while True:
                categoria = input("Ingrese la Categoría: ").strip()
                if validar_texto(categoria):
                    break
            while True:
                talla = input("Ingrese la Talla: ").strip()
                if validar_texto(talla):
                    break
            while True:
                color = input("Ingrese el Color: ").strip()
                if validar_texto(color):
                    break
            while True:
                material = input("Ingrese el Material: ").strip()
                if validar_texto(material):
                    break
            while True:
                es_unisex = input("¿La prenda es unisex? (s/n): ").lower()
                if validar_si_o_no(es_unisex):
                    es_unisex = convertir_a_booleano(es_unisex)
                    break
            while True:
                precio = input("Ingrese el Precio: ")
                if validar_mayor_a_cero(precio):
                    precio = int(precio)
                    break
                print("Debe ingresar un entero mayor que cero.")
            while True:
                unidades = input("Ingrese las Unidades: ")
                if validar_mayor_igual_a_cero(unidades):
                    unidades = int(unidades)
                    break
                print("Debe ingresar un entero mayor que cero.")
                
            if agregar_prenda(
                d_prendas,
                d_bodega,
                codigo,
                nombre,
                categoria,
                talla,
                color,
                material,
                es_unisex,
                precio,
                unidades
            ):
                print("Prenda agregada correctamente.")
            else:
                print("No fue posible agregar la prenda.")

        elif opcion == 5:
            codigo = input("Ingrese el Código: ")
            if eliminar_prenda(d_prendas, d_bodega, codigo):
                print("Prenda eliminada.")
            else:
                print("El Código no existe.")
        else:
            print("Programa finalizado.")
            break

programa_principal()