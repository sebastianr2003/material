def area_rectangular(a, b):#def es una funcion (a,b)datos
    result = a * b
    return result # return devuelve el resultado de la funcion
if __name__== "__main__":#Llamada al metodo add_numbers()
#__name__ es una variable especial en Python que se establece automáticamente.
#Ejecución directa: Si ejecutas el script directamente, `__name__` será `"__main__"`, por lo que el código dentro del bloque `if` se ejecutará. 
    number = area_rectangular(20,2)
    print(number)
#----------------------
def multiplicador_numbers(a, b):
#Sumar dos números. Parámetros:
#a (int o float):El primer número que se sumará. 
#b (int o float):El segundo número que se sumará.
#Devuelve: int o float:La suma de los dos valores de entrada 
    result = a * b
    return result
#----------------------
""" Liberia time forma de importar una liberia """
import time # importa la libreria time
class Timer:
    def __enter__(self):# instancia del objeto
        self.start_time = time.time()
        return self# returna el objeto
    def __exit__(self, exc_type, exc_val, exc_tb):
    #exc_type exception exc_val error asociado con la excepcion exc_tb donde ocurrio la exception
        end_time = time.time()# tiempo de finalizacion
        print(f"tiempo de ejecucion {end_time - self.start_time} segundos")# timepo de finalizacion menos timepo de inicio
with Timer():# codigo cuyo tiempo que queremos medir
   pass# simulacion de una operacion
#----------------------
def es_par(x):#define una funcion y entra un dato
    if x % 2 == 0:
     # si es par
        return (f"es un numero par:, {x}")# f"" entra una variable en una cadena de texto
    else:
     # si es impar
        return (f"es un numero impar:, {x}")
#llama al metodo greet
if __name__ == "__main__":
    dato = input("introducir numero: ")# entra un dato por teclado input
    resultado = es_par(dato)# funcion en resultado
    print(resultado)# imprime