import GestorGastos 
import tkinter as tk
from tkinter import messagebox

class GestionGastosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Gastos")
        
        # Crear widgets
        self.label = tk.Label(root, text="Ingrese su gasto:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.add_button = tk.Button(root, text="Agregar Gasto", command=self.agregar_gasto)
        self.add_button.pack()
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack()
        
        self.show_button = tk.Button(root, text="Mostrar Gastos", command=self.mostrar_gastos)
        self.show_button.pack()
        
    def agregar_gasto(self):
        gasto = self.entry.get()
        if gasto:
            self.listbox.insert(tk.END, gasto)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Ingrese un gasto válido.")
            
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
