from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
	def __init__(self, nombre:str, cantidad_satelites:int, masa:float, volomen:float, diametro: int, distancia_sol:int, tipo:TipoPlaneta, es_observable:bool, periodo_orbital:float, peroido_rotacional:float):
		self.nombre = nombre
		self.cantidad_satelites = cantidad_satelites
		self.masa = masa
		self.volumen = volomen
		self.diametro = diametro
		self.distancia_sol = distancia_sol
		self.tipo = tipo
		self.es_observable = es_observable
		self.periodo_orbital = periodo_orbital
		self.periodo_rotacional = peroido_rotacional

	def nuevo_planeta():
		try:
			nombre = input("Ingrese el nombre del planeta: ")
		except Exception as e:
			while True:
				print("Error al ingresar el nombre del planeta. Intente nuevamente.")
				nombre = input("Ingrese el nombre del planeta: ")
				if nombre == "" or nombre.isspace():
					print("El nombre del planeta no puede estar vacío. Intente nuevamente.")
					pass
				if nombre:
					break
			return None
		try:
			cantidad_satelites = int(input("Ingrese la cantidad de satelites: "))
		except Exception as e:
			while True:
				print("Error al ingresar la cantidad de satelites. Intente nuevamente.")
				cantidad_satelites = input("Ingrese la cantidad de satelites: ")
				if cantidad_satelites.isdigit():
					cantidad_satelites = int(cantidad_satelites)
					break
			return None
		try:
			masa = float(input("Ingrese la masa del planeta en kg: "))
		except Exception as e:
			while True:
				print("Error al ingresar la masa del planeta. Intente nuevamente.")
				masa = input("Ingrese la masa del planeta en kg: ")
				try:
					masa = float(masa)
					break
				except ValueError:
					print("La masa debe ser un número válido. Intente nuevamente.")
			return None
		try:
			volumen = float(input("Ingrese el volumen del planeta en km³: "))
		except Exception as e:
			while True:
				print("Error al ingresar el volumen del planeta. Intente nuevamente.")
				volumen = input("Ingrese el volumen del planeta en km³: ")
				try:	
					volumen = float(volumen)
					break
				except ValueError:
					print("El volumen debe ser un número válido. Intente nuevamente.")
			return None
		try:			diametro = int(input("Ingrese el diametro del planeta en km: "))
		except Exception as e:
			while True:
				print("Error al ingresar el diametro del planeta. Intente nuevamente.")
				diametro = input("Ingrese el diametro del planeta en km: ")
				if diametro.isdigit():
					diametro = int(diametro)
					break
			return None
		try:
			distancia_sol = int(input("Ingrese la distancia al sol en km: "))
		except Exception as e:
			while True:
				print("Error al ingresar la distancia al sol. Intente nuevamente.")
				distancia_sol = input("Ingrese la distancia al sol en km: ")
				if distancia_sol.isdigit():
					distancia_sol = int(distancia_sol)
					break
			return None
		try:
			tipo = input("Ingrese el tipo de planeta (TERRESTRE/GASEOSO/ENANO): ")
		except Exception as e:
			while True:
				print("Error al ingresar el tipo de planeta. Intente nuevamente.")
				tipo = input("Ingrese el tipo de planeta (TERRESTRE/GASEOSO/ENANO): ")
				if tipo.upper() in ["TERRESTRE", "GASEOSO", "ENANO"]:
					tipo = TipoPlaneta(tipo.upper())
					break
			return None
		try:
			es_observable = input("¿Es observable? (S/N): ")
		except Exception as e:
			while True:
				print("Error al ingresar si el planeta es observable. Intente nuevamente.")
				es_observable = input("¿Es observable? (S/N): ")
				if es_observable.upper() in ["S", "N"]:
					if es_observable.upper() == "S":
						es_observable = True
					else:
						es_observable = False
					break
			return None
		try:
			periodo_orbital = float(input("Ingrese el periodo orbital en años: "))
		except Exception as e:
			while True:
				print("Error al ingresar el periodo orbital. Intente nuevamente.")
				periodo_orbital = input("Ingrese el periodo orbital en años: ")
				try:
					periodo_orbital = float(periodo_orbital)
					break
				except ValueError:
					print("El periodo orbital debe ser un número válido. Intente nuevamente.")
			return None
		try:
			periodo_rotacional = float(input("Ingrese el periodo rotacional en días: "))
		except Exception as e:
			while True:
				print("Error al ingresar el periodo rotacional. Intente nuevamente.")
				periodo_rotacional = input("Ingrese el periodo rotacional en días: ")
				try:
					periodo_rotacional = float(periodo_rotacional)
					break
				except ValueError:
					print("El periodo rotacional debe ser un número válido. Intente nuevamente.")
			return None
		return Planeta(nombre, cantidad_satelites, masa, volumen, diametro, distancia_sol, tipo, es_observable, periodo_orbital, periodo_rotacional)

	def imprimir(self):
		print(f"Nombre del planeta = {self.nombre}\nCantidad de satelites = {self.cantidad_satelites}\nMasa del planeta = {self.masa} kg\nVolumen del planeta = {self.volumen} km³\nDiametro del planeta = {self.diametro} km\nDistancia al sol = {self.distancia_sol} km\nTipo de planeta = {self.tipo}\nEs observable = {self.es_observable}\nDensidad del planeta = {self.calcular_densidad()} kg/km³\n¿Es un planeta exterior? = {self.planeta_exterior()}\nPeriodo orbital = {self.periodo_orbital} años\nPeriodo rotacional = {self.periodo_rotacional} días")
	
	def calcular_densidad(self):
		densidad = self.masa / self.volumen
		return densidad
	
	def planeta_exterior(self):
		limite = 508632758.0
		return self.distancia_sol > limite

if __name__ == "__main__":
	planetas = []
	planetas.append(Planeta("Tierra", 1, 5.972e24, 1.08321e12, 12742, 149597870, "TERRESTRE", True, 1, 0.997))
	planetas.append(Planeta("Jupiter", 79, 1.898e27, 1.43128e15, 139820, 778547200, "GASEOSO", True, 11.86, 0.413))
	planetas.append(Planeta("Neptuno", 14, 1.024e26, 6.254e13, 49244, 4498396441, "GASEOSO", True, 164.8, 0.67))

	for planeta in planetas:
		print("\n-----------------------------")
		planeta.imprimir()
	
	print("-----------------------------\nIngresar más Planetas\n-----------------------------")

	try:
		N = int(input("Ingrese el número de planetas a ingresar: "))
	except ValueError:
		print("Error: Saliendo del programa...")
		exit()
	
	for i in range(N):
		print(f"\n-----------------------------")
		print(f"Ingrese los datos del planeta {i+1}:\n")
		p = Planeta.nuevo_planeta()
		planetas.append(p)