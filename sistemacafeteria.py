#Pruebas Sistema de Gestión de Cafetería
#Augusto Gómez Maxil | A01736346  

#El código ofrece un conjunto de funciones para validar registros de productos, donde cada registro consta de un nombre de producto seguido de una lista de tamaños. La función "validar_y_transformar_tamanos" se encarga de verificar que los tamaños proporcionados sean números enteros dentro del rango de 1 a 48, sin duplicados y en orden ascendente. Por otro lado, la función "validar_producto" verifica que el nombre del producto esté compuesto únicamente por letras, tenga una longitud entre 2 y 15 caracteres, y que la cantidad de tamaños esté entre 1 y 5. Además, utiliza la función de validación de tamaños para garantizar la integridad de la información. En conjunto, estas funciones aseguran que los registros de productos estén en el formato correcto y que los tamaños sean válidos y estén ordenados adecuadamente antes de ser procesados.

def validar_y_transformar_tamanos(tamanos_str):
    """
    Valida y transforma los tamaños proporcionados como cadenas de texto en enteros.

    Args:
    tamanos_str (lista de str): Lista de cadenas de texto representando los tamaños.

    Returns:
    tuple: Una tupla que contiene un booleano indicando si los tamaños son válidos,
           y ya sea una lista de enteros (tamaños válidos) o un mensaje de error (si no son válidos).
    """
    tamanos_int = []
    tamanos_set = set()  # Para verificar duplicados

    for tamano_str in tamanos_str:
        tamano_str = tamano_str.strip()

        # Verificar si los valores son enteros
        if not tamano_str.lstrip("-").isdigit():
            return False, "Los tamaños deben ser valores enteros."
        tamano_int = int(tamano_str)

        # Verificar si los tamaños están dentro del rango de 1 a 48
        if not 1 <= tamano_int <= 48:
            return False, "Los tamaños deben estar en el rango de 1 a 48."

        # Verificar que no haya valores duplicados
        if tamano_int in tamanos_set:
            return False, "Los tamaños no pueden repetir valores."
        tamanos_int.append(tamano_int)
        tamanos_set.add(tamano_int)

    # Verificar si los valores están en orden ascendente
    if tamanos_int != sorted(tamanos_int):
        return False, "Los tamaños no están en orden ascendente."

    return True, tamanos_int


def validar_producto(registro_str):
    """
    Validar el formato de un registro de producto.

    Args:
    registro_str (str): Cadena de texto que representa el registro del producto en el formato 'nombre, tamaño1, tamaño2, ..., tamañoN'.

    Returns:
    tuple: Una tupla que contiene un booleano indicando si el registro es válido,
           y ya sea True (si es válido) o un mensaje de error (si no es válido).
    """
    # Eliminar espacios en blanco
    registro_str = registro_str.replace(" ", "")
    registro_separado = registro_str.split(",")
    # Obtener el primer valor que es el nombre del producto
    nombre_producto = registro_separado[0]
    # Obtener los siguientes valores que son los tamaños
    tamanos_str = registro_separado[1:]

    # Validar que el nombre del producto sea alfabético
    if not nombre_producto.isalpha():
        return False, "El nombre del producto debe contener solo letras."

    # Validar que el nombre del producto tenga una longitud entre 2 y 15 caracteres
    if len(nombre_producto) < 2 or len(nombre_producto) > 15:
        return False, "El nombre del producto debe tener entre 2 y 15 caracteres."

    # Validar que la cantidad de tamaños esté entre 1 y 5
    if not 1 <= len(tamanos_str) <= 5:
        return False, "La cantidad de tamaños debe estar entre 1 y 5."

    # Utilizar la función auxiliar para validar y transformar tamaños
    valido, resultado = validar_y_transformar_tamanos(tamanos_str)
    if not valido:
        return False, resultado

    return True


def test_bebida():
    #1 a 48
     #  Se coloca el límite inferior (válido)
  assert validar_producto("Capuccino,1,2,3,4") == True
  # Se coloca el límite superior (válido)
  assert validar_producto("Espresso,41,48") == True
  # Se colocan valores menores que el rango (0)
  assert validar_producto("Espresso,0,2,3,4") == (False, "Los tamaños deben estar en el rango de 1 a 48.")
  
  
  #2 caracteres
  assert validar_producto("ab,1,2,3,4") == True
  
  #Espacios en blanco
  assert validar_producto("Caramel Latte, 12, 16, 20") == True
  assert validar_producto("   Green Tea  ,  8, 12  ") == True
  
  #comas separadas
  assert validar_producto("Mocha,10,20,30") == True
  
  #nombre primero
  assert validar_producto("Cappuccino, 10, 15") == True
  
  #tamaño 1 a 5
  assert validar_producto("Iced Coffee, 8") == True
  
  #orden ascendente
  assert validar_producto("Tea, 5, 10, 15, 20") == True
  
  #tamaño entero
  assert validar_producto("Espresso, 10, 20, 25") == True
  # Un tamaño es un número decimal
  assert validar_producto("Mocha,1.5,2,3,4") == (False, 'Los tamaños deben ser valores enteros.')
  
  
  #tamaño rango
  assert validar_producto("Latte, 12, 16, 20") == True
  
  #2 a 15 caracteres
  assert validar_producto("Smoothie, 20, 30") == True
  
  #nombre akfabetici
  assert validar_producto("Coffee, 8, 12, 16") == True
  



#Testeo
#UniTest replit

