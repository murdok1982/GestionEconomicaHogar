import PersistenciaDatos
import tkinter as tk

class GestionGastosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Gastos")
        
        # Crear widgets
        self.label = tk.Label(root, text="Ingrese su gasto:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.label_category = tk.Label(root, text="Ingrese la categoría del gasto:")
        self.label_category.pack()
        
        self.entry_category = tk.Entry(root)
        self.entry_category.pack()
        
        self.add_button = tk.Button(root, text="Agregar Gasto", command=self.agregar_gasto)
        self.add_button.pack()
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack()
        
        self.show_button = tk.Button(root, text="Mostrar Gastos", command=self.mostrar_gastos)
        self.show_button.pack()
        
        self.label_categories = tk.Label(root, text="Categorías de Gastos:")
        self.label_categories.pack()
        
        self.categories_listbox = tk.Listbox(root)
        self.categories_listbox.pack()
        
    def agregar_gasto(self):
        gasto = self.entry.get()
        categoria = self.entry_category.get()
        if gasto and categoria:
            self.listbox.insert(tk.END, f"Gasto: {gasto}, Categoría: {categoria}")
            self.entry.delete(0, tk.END)
            self.entry_category.delete(0, tk.END)
            if categoria not in self.categories_listbox.get(0, tk.END):
                self.categories_listbox.insert(tk.END, categoria)
        else:
            messagebox.showwarning("Error", "Ingrese un gasto y una categoría válidos.")
            
    def mostrar_gastos(self):
        if self.listbox.size() == 0:
            messagebox.showinfo("Gastos", "No hay gastos registrados.")
        else:
            gastos = "\n".join(self.listbox.get(0, tk.END))
            messagebox.showinfo("Gastos", gastos)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionGastosApp(root)
    root.mainloop()


class GestionGastos:
    def __init__(self):
        self.gastos = {}
        self.categorias = set()

    def agregar_gasto(self, categoria, monto, etiquetas=None):
        if categoria in self.gastos:
            self.gastos[categoria]["monto"] += monto
            if etiquetas:
                self.gastos[categoria]["etiquetas"].extend(etiquetas)
        else:
            self.gastos[categoria] = {"monto": monto, "etiquetas": etiquetas or []}
            self.categorias.add(categoria)

    def mostrar_gastos(self):
        if self.gastos:
            print("Gastos por categoría:")
            for categoria, info in self.gastos.items():
                monto = info["monto"]
                etiquetas = ", ".join(info["etiquetas"])
                print(f"{categoria}: ${monto} (Etiquetas: {etiquetas})")
        else:
            print("No hay gastos registrados.")

    def mostrar_categorias(self):
        if self.categorias:
            print("Categorías disponibles:")
            for categoria in self.categorias:
                print(categoria)
        else:
            print("No hay categorías registradas.")

if __name__ == "__main__":
    gestor = GestionGastos()

    while True:
        print("\n1. Agregar gasto")
        print("2. Mostrar gastos")
        print("3. Mostrar categorías")
        print("4. Salir")
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
            gestor.mostrar_categorias()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
