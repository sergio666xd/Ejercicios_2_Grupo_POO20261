class Persona:
    def __init__(self, nombre:str, apellidos:str, documento:str, genero:str, pais_nacimiento:str, año_nacimiento:int):
        self.nombre = nombre
        self.apellidos = apellidos
        self.documento = documento
        self.genero = genero.upper()
        self.pais_nacimiento = pais_nacimiento
        self.año_nacimiento = año_nacimiento

    def imprimir(self):
        if self.genero == "H":
            self.genero = "Hombre"
        elif self.genero == "M":
            self.genero = "Mujer"
        print(f"Nombre = {self.nombre}\nApellidos = {self.apellidos}\nGenero = {self.genero}\nDocumento de Identidad = {self.documento}\nPais de nacimiento = {self.pais_nacimiento}\nAño de nacimiento = {self.año_nacimiento}")

    def nueva_persona():
        try:
            nombre = input("Ingrese el nombre: ")
        except Exception as e:
            while True:
                print("Error al ingresar el nombre. Intente nuevamente.")
                nombre = input("Ingrese el nombre: ")
                if nombre == "" or nombre.isspace():
                    print("El nombre no puede estar vacío. Intente nuevamente.")
                    pass
                if nombre:
                    break
            return None
        try:
            apellidos = input("Ingrese los apellidos: ")
        except Exception as e:
            while True:
                print("Error al ingresar los apellidos. Intente nuevamente.")
                apellidos = input("Ingrese los apellidos: ")
                if apellidos == "" or apellidos.isspace():
                    print("Los apellidos no pueden estar vacíos. Intente nuevamente.")
                    pass
                if apellidos:
                    break
            return None
        try:
            documento = input("Ingrese el documento de identidad: ")
        except Exception as e:
            while True:
                print("Error al ingresar el documento de identidad. Intente nuevamente.")
                documento = input("Ingrese el documento de identidad: ")
                if documento:
                    break
            return None
        try:
            genero = input("Ingrese el género (H/M): ")
        except Exception as e:
            while True:
                print("Error al ingresar el género. Intente nuevamente.")
                genero = input("Ingrese el género (H/M): ")
                if genero.upper() in ["H", "M"]:
                    break
            return None
        try:
            pais_nacimiento = input("Ingrese el país de nacimiento: ")
        except Exception as e:
            while True:
                print("Error al ingresar el país de nacimiento. Intente nuevamente.")
                pais_nacimiento = input("Ingrese el país de nacimiento: ")
                if pais_nacimiento:
                    break
            return None
        
        try:
            año_nacimiento = int(input("Ingrese el año de nacimiento: "))
        except ValueError:
            while True:
                print("Error: El año de nacimiento debe ser un número entero.")
                try:
                    año_nacimiento = int(input("Ingrese el año de nacimiento: "))
                    break
                except ValueError:
                    continue
        return Persona(nombre, apellidos, documento, genero, pais_nacimiento, año_nacimiento)


if __name__ == "__main__":
    personas = []
    personas.append(Persona("Juan", "Pérez", "12345678", "H", "Argentina", 1990))
    personas.append(Persona("María", "Gómez", "87654321", "M", "España", 1985))

    for i, p in enumerate(personas):
        print(f"Persona {i+1}:")
        p.imprimir()
        if i < len(personas) - 1:
            print("-----------------------------")

    print("-----------------------------\nIngresar más Personas\n-----------------------------")
    try:
        N = int(input("Ingrese el número de personas a ingresar: "))
    except ValueError:
        print("Error: Saliendo del programa...")
        exit()
    for i in range(N):
        print(f"\n-----------------------------")
        print(f"Ingrese los datos de la persona {i+1}:\n")
        p = Persona.nueva_persona()
        personas.append(p)

    print("\n-----------------------------")
    
    for i, p in enumerate(personas):
        print(f"Persona {i+1}:")
        p.imprimir()
        if i < len(personas) - 1:
            print("-----------------------------")