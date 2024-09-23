from abc import ABC, abstractmethod

class VehiculoBase(ABC):
    def __init__(self, marca, modelo, año, capacidad, tipo_combustible):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad = capacidad
        self.tipo_combustible = tipo_combustible
        self.disponible = True
        self.conductor_asignado = None

    @abstractmethod
    def asignar_conductor(self, conductor):
        pass

    @abstractmethod
    def liberar_vehiculo(self):
        pass

    def __str__(self):
        estado = "Disponible" if self.disponible else f"No Disponible (Conductor: {self.conductor_asignado.nombre})"
        return f"{self.marca} {self.modelo} ({self.año}) - {self.capacidad} pasajeros - {self.tipo_combustible} - {estado}"


class Vehiculo(VehiculoBase):
    def asignar_conductor(self, conductor):
        if self.disponible:
            self.conductor_asignado = conductor
            self.disponible = False
            print(f"Conductor {conductor.nombre} asignado al vehículo {self.marca} {self.modelo}.")
        else:
            print(f"El vehículo {self.marca} {self.modelo} no está disponible.")

    def liberar_vehiculo(self):
        if not self.disponible and self.conductor_asignado:
            print(f"Vehículo {self.marca} {self.modelo} liberado de {self.conductor_asignado.nombre}.")
            self.conductor_asignado = None
            self.disponible = True
        else:
            print(f"El vehículo {self.marca} {self.modelo} ya está disponible.")


class Conductor:
    def __init__(self, nombre, fecha_nacimiento, licencia):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.licencia = licencia

    def __str__(self):
        return f"{self.nombre} - Licencia: {self.licencia} - Fecha de Nacimiento: {self.fecha_nacimiento}"


class Servicio:
    def __init__(self, tipo, descripcion):
        self.tipo = tipo
        self.descripcion = descripcion

    def realizar_servicio(self, vehiculo):
        print(f"Realizando servicio de {self.tipo} en el vehículo {vehiculo.marca} {vehiculo.modelo}.")
        vehiculo.liberar_vehiculo()

    def __str__(self):
        return f"Servicio: {self.tipo} - Descripción: {self.descripcion}"


class Gestion:
    def __init__(self):
        self.vehiculos = []
        self.conductores = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.marca} {vehiculo.modelo} agregado al sistema.")

    def agregar_conductor(self, conductor):
        self.conductores.append(conductor)
        print(f"Conductor {conductor.nombre} agregado al sistema.")

    def mostrar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos en el sistema.")
        else:
            print("Vehículos en el sistema:")
            for vehiculo in self.vehiculos:
                print(vehiculo)

    def mostrar_conductores(self):
        if not self.conductores:
            print("No hay conductores en el sistema.")
        else:
            print("Conductores en el sistema:")
            for conductor in self.conductores:
                print(conductor)

    def asignar_conductor_a_vehiculo(self):
        self.mostrar_vehiculos()
        vehiculo_idx = int(input("Selecciona el número del vehículo: ")) - 1
        self.mostrar_conductores()
        conductor_idx = int(input("Selecciona el número del conductor: ")) - 1
        self.vehiculos[vehiculo_idx].asignar_conductor(self.conductores[conductor_idx])

    def realizar_servicio_a_vehiculo(self):
        self.mostrar_vehiculos()
        vehiculo_idx = int(input("Selecciona el número del vehículo: ")) - 1
        servicio_tipo = input("Tipo de servicio (Mantenimiento/Combustible): ")
        descripcion = input("Descripción del servicio: ")
        servicio = Servicio(servicio_tipo, descripcion)
        servicio.realizar_servicio(self.vehiculos[vehiculo_idx])


def main():
    gestion = Gestion()

    while True:
        print("\n===== Sistema de Gestión de Vehículos =====")
        print("1. Agregar Vehículo")
        print("2. Agregar Conductor")
        print("3. Mostrar Vehículos")
        print("4. Mostrar Conductores")
        print("5. Asignar Conductor a Vehículo")
        print("6. Realizar Servicio a Vehículo")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            marca = input("Marca del vehículo: ")
            modelo = input("Modelo del vehículo: ")
            año = int(input("Año del vehículo: "))
            capacidad = int(input("Capacidad de pasajeros: "))
            tipo_combustible = input("Tipo de combustible: ")
            vehiculo = Vehiculo(marca, modelo, año, capacidad, tipo_combustible)
            gestion.agregar_vehiculo(vehiculo)

        elif opcion == "2":
            nombre = input("Nombre del conductor: ")
            fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
            licencia = input("Número de licencia de conducir: ")
            conductor = Conductor(nombre, fecha_nacimiento, licencia)
            gestion.agregar_conductor(conductor)

        elif opcion == "3":
            gestion.mostrar_vehiculos()

        elif opcion == "4":
            gestion.mostrar_conductores()

        elif opcion == "5":
            gestion.asignar_conductor_a_vehiculo()

        elif opcion == "6":
            gestion.realizar_servicio_a_vehiculo()

        elif opcion == "7":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 7.")

if __name__ == "__main__":
    main()
