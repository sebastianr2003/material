    def __init__(self):
        # Inicializamos el conjunto como un conjunto vacío
        self._elementos = set()

    # Método para agregar un elemento al conjunto
    def agregar(self, elemento):
        self._elementos.add(elemento)

    # Método para eliminar un elemento del conjunto
    def eliminar(self, elemento):
        if elemento in self._elementos:
            self._elementos.remove(elemento)
        else:
            print(f"El elemento {elemento} no está en el conjunto.")

    # Método para verificar si un elemento está en el conjunto
    def contiene(self, elemento):
        return elemento in self._elementos

    # Método getter para obtener todos los elementos del conjunto
    def get_elementos(self):
        return self._elementos

    # Método setter para establecer los elementos del conjunto
    def set_elementos(self, nuevos_elementos):
        if isinstance(nuevos_elementos, (set, list)):
            self._elementos = set(nuevos_elementos)
        else:
            print("Error: Los elementos deben ser un conjunto o una lista.")

    # Método para mostrar el conjunto
    def mostrar(self):
        print(f"Conjunto: {self._elementos}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia del conjunto
    conjunto = Conjunto()

    # Agregar elementos
    conjunto.agregar(1)
    conjunto.agregar(2)
    conjunto.agregar(3)

    # Mostrar el conjunto
    conjunto.mostrar()

    # Verificar si un elemento está en el conjunto
    print("¿El conjunto contiene el 2?", conjunto.contiene(2))

    # Eliminar un elemento
    conjunto.eliminar(2)
    conjunto.mostrar()

    # Usar el getter para obtener los elementos
    print("Elementos actuales:", conjunto.get_elementos())

    # Usar el setter para establecer nuevos elementos
    conjunto.set_elementos([4, 5, 6])
    conjunto.mostrar()
