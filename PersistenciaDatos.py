import sqlite3

class GestionGastos:
    def __init__(self):
        self.conexion = sqlite3.connect("gastos.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla_gastos()

    def crear_tabla_gastos(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS gastos (
                                id INTEGER PRIMARY KEY,
                                categoria TEXT,
                                monto REAL,
                                etiquetas TEXT
                            )''')
        self.conexion.commit()

    def agregar_gasto(self, categoria, monto, etiquetas=None):
        self.cursor.execute('''INSERT INTO gastos (categoria, monto, etiquetas)
                               VALUES (?, ?, ?)''', (categoria, monto, ','.join(etiquetas) if etiquetas else None))
        self.conexion.commit()

    def mostrar_gastos(self):
        self.cursor.execute("SELECT * FROM gastos")
        gastos = self.cursor.fetchall()
        if gastos:
            print("Lista de Gastos:")
            for gasto in gastos:
                print(f"Categoría: {gasto[1]}, Monto: {gasto[2]}, Etiquetas: {gasto[3]}")
        else:
            print("No hay gastos registrados.")

    def cerrar_conexion(self):
        self.conexion.close()

if __name__ == "__main__":
    gestor = GestionGastos()

    while True:
        print("\n1. Agregar gasto")
        print("2. Mostrar gastos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            categoria = input("Ingrese la categoría del gasto: ")
            monto = float(input("Ingrese el monto del gasto: "))
            etiquetas = input("Ingrese las etiquetas del gasto (separadas por coma): ").split(",") if input("¿Desea agregar etiquetas? (s/n): ").lower() == "s" else None
            gestor.agregar_gasto(categoria, monto, etiquetas)
            print("Gasto agregado correctamente.")
        elif opcion == "2":
            gestor.mostrar_gastos()
        elif opcion == "3":
            gestor.cerrar_conexion()
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
