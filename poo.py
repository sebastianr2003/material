class Automovil: #creando clase
    def __init__(self,marca,modelo,año,color,encendido=False): #constructor      
        #atributos de la clase o caracteristicas
        '''
            'SELF. permite a cada objeto mantener su propio estado y comportamiento'
        '''
        self._marca = marca #`_` se usa deltante del atributo para saber que es protegido
        self._modelo = modelo 
        self._año = año
        self._color = color 
        self._velocidad = 0
        self._encedido = False
        self._kilometraje = 0
        self._nivel_combustible = 100
        self._presion_neumaticos = 32
        #Metodos 
    '''
            @property,@marca.setter -> se usa para tener un codigo mas legible y ordenado () tambien para encapsular permite validacion
            -> sin encapsular autito.marca= 30 # suelta error sin validacion
            -> con encapsular autito.marca= 30 # ahora lo valida y puede solar un valueerror
        isinstance -> comprueba se un objeto es una instancia (instancia de clase, tipo de dato)
        str es la clase string 
        .strip() es un metodo de string que elimina epsacios en blanco en el inicio ->si esta vacia devuelve false o vacio
    '''
    @property
    def marca(self):
        return self._marca        
    
    @marca.setter
    def marca(self, nueva_marca):
        if isinstance(nueva_marca, str) and nueva_marca.strip():
            self._marca = nueva_marca.strip()
        else:
            raise ValueError("la marca debe ser un texto no vacio")    
        
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self,nuevo_modelo):
        if isinstance(nuevo_modelo, str) and nuevo_modelo.strip():
            self._marca = nuevo_modelo.strip()
        else:
            raise ValueError("la modelo debe ser un texto no vacio")    
        
    @property
    def año(self):
        return self._año
    
    @año.setter
    def año(self, nuevo_año):
        if isinstance(nuevo_año, str) and nuevo_año.strip():
            self._marca = nuevo_año.strip()
        else:
            raise ValueError("la modelo debe ser un texto no vacio") 
          
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,nuevo_color):
        if isinstance(nuevo_color, str) and nuevo_color.strip():
            self._marca = nuevo_color.strip()
        else:
            raise ValueError("la modelo debe ser un texto no vacio")
    
    @property
    def velocidad(self):
        return self._velocidad
    
    @property
    def encendido(self):
        return self.encendido
    
    @property
    def encender(self):
        if not self._encedido:
            if self._nivel_combustible > 0:
                self._encedido = True
                print("el automovil esta encendido")
            else:
                print("no se enciende, sin combustible")
        else:
            print("el automovil esta encendido")
            
    @property
    def apagar(self):
        if self._encendido:
            self._encendido = False
            self._velocidad= 0
            print("el automovil se apagado")
        else:
            print("el automovil esta apagado")
            
    @property
    def estado(self):
        if self._encendido:
            print(f"el automovil esta encendido a {self._velocidad}km/h")
        else:
            print("el automovil esta apagado")
        
    @property
    def kilometraje(self):
        return self.kilometraje
    
    @kilometraje.setter
    def kilometraje(self, nuevo_kilometraje):
        if isinstance(nuevo_kilometraje,(int, float)) and nuevo_kilometraje>=0:# integer y float()
            self._kilometraje = nuevo_kilometraje
        else:
            raise ValueError("kilometraje debe ser positivo")
    
    @property
    def nivel_combustible(self):
        return self._nivel_combustible
    @nivel_combustible.setter
    def nivel_combustible(self, nuevo_nivel_combustible):
        if isinstance(nuevo_nivel_combustible,(int, float)) and 0 <= nuevo_nivel_combustible <= 100:
            self._nivel_combustible = nuevo_nivel_combustible
        else:
            raise ValueError("nivel de combustible debe ser entre 0 y 100")
    @property
    def presion_neumatico(self):
        return self._presion_neumaticos  
    
    #metodos de mantenimiento  
    def llenar_tanque(self):
        self._nivel_combustible = 100
    
    def inflar_neumatico(self,presion):
        if 28 <= presion <= 40:
            self._presion_neumaticos = presion
            print(f"neumatico inflado a {presion}")
        else:
            print(f"presion fuera de rango valido (recomendada 28-40)")
            
    #metodo especial
    def __str__(self):
        return (f"Atributos={self._marca}_{self._modelo}_{self._año}_{self._color}_kilometraje={self._kilometraje}_"
                f"velocidad={self._velocidad}km/h_combustible={self._nivel_combustible}%_{self._presion_neumaticos}presion de llanta")

#ejemplo de uso
mi_car = Automovil("toyota","corolla",2020,"rojo",False)
print(mi_car)
mi_car.nivel_combustible = 50  
print(mi_car)
