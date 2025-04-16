    def __init__(self):
        # Inicializamos el conjunto como un conjunto vacío
 yo mismo._elementos = establecer()

    # Metodo para agregar un elemento al conjunto
    def agregar(yo, elemento):
 yo mismo._elementos.agregar(elemento)

    # Metodo para eliminar un elemento del conjunto
    def eliminatorio(yo, elemento):
 si elemento en yo mismo._elementos:
 yo mismo._elementos.quitar(elemento)
 mas:
            imprimir(f"El elemento {elemento} no está en el conjunto.")

    # Metodo para verificar si un elemento está en el conjunto
    def contiene(yo, elemento):
 volver elemento en yo mismo._elementos

    # Metodo getter para obtener todos los elementos del conjunto
    def get_elementos(yo mismo):
 regresar yo mismo._elementos

    # Metodo setter para establecer los elementos del conjunto
    def set_elementos(oye, nuevos_elementos):
 si isinstancia(nuevos_elementos, (lista establecer)):
 yo mismo._elementos = establecer(nuevos_elementos)
 mas:
            imprimir("Error: Los elementos deben ser un conjunto o una lista".)

    # Metodo para mostrar el conjunto
    def másrar(yo mismo):
        imprimir(f"Conjuntar: {yo mismo._elementos}")


# Ejemplo de uso
si __name__ == "__main__":
    # Crear una instancia del conjunto
 conjunto = Conjunto()

    # Elementos agregados
 conjunto.agregar(1)
 conjunto.agregar(2)
 conjunto.agregar(3)

    # Mostrar el conjunto
 conjunto.másrar()

    # Verificar si un elemento está en el conjunto
    imprimir("¿El conjunto contiene el 2?", conjunto.contiene(2))

    # Eliminar un elemento
 conjunto.eliminatorio(2)
 conjunto.másrar()

    # Usar el getter para obtener los elementos
    imprimir(„Elementos reales:", conjunto.get_elementos())

    # Usar el setter para estables nuevos elementos
 conjunto.set_elementos([4, 5, 6])
 conjunto.másrar()
