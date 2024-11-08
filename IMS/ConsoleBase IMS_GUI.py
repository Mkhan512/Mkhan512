import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import csv

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock_quantity": self.stock_quantity
        }

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.products = {}
        self.users = {"admin": {"password": "adminpass", "role": "Admin"},
                      "user": {"password": "userpass", "role": "User"}}
        self.current_user = None

        self.login_window()

    def login_window(self):
        self.clear_window()
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.users.get(username)
        
        if user and user["password"] == password:
            self.current_user = user
            messagebox.showinfo("Login Successful", f"Welcome, {self.current_user['role']}.")
            self.main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Inventory Management System - Main Menu", font=("Arial", 16)).pack(pady=10)

        # Menu options for all users
        tk.Button(self.root, text="View Products", command=self.view_products_window).pack(fill="x")
        tk.Button(self.root, text="Search Product", command=self.search_product_window).pack(fill="x")
        tk.Button(self.root, text="Logout", command=self.logout).pack(fill="x", pady=10)

        # Additional options for Admin users only
        if self.current_user["role"] == "Admin":
            tk.Button(self.root, text="Add Product", command=self.add_product_window).pack(fill="x")
            tk.Button(self.root, text="Delete Product", command=self.delete_product_window).pack(fill="x")
            tk.Button(self.root, text="Export Inventory", command=self.export_inventory).pack(fill="x")
            tk.Button(self.root, text="Import Inventory", command=self.import_inventory).pack(fill="x")

    def add_product_window(self):
        self.clear_window()
        tk.Label(self.root, text="Add Product", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Product ID:").pack()
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.pack()
        tk.Label(self.root, text="Product Name:").pack()
        self.product_name_entry = tk.Entry(self.root)
        self.product_name_entry.pack()
        tk.Label(self.root, text="Category:").pack()
        self.category_entry = tk.Entry(self.root)
        self.category_entry.pack()
        tk.Label(self.root, text="Price:").pack()
        self.price_entry = tk.Entry(self.root)
        self.price_entry.pack()
        tk.Label(self.root, text="Stock Quantity:").pack()
        self.stock_quantity_entry = tk.Entry(self.root)
        self.stock_quantity_entry.pack()
        
        tk.Button(self.root, text="Add Product", command=self.add_product).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack()

    def add_product(self):
        try:
            product_id = self.product_id_entry.get()
            name = self.product_name_entry.get()
            category = self.category_entry.get()
            price = float(self.price_entry.get())
            stock_quantity = int(self.stock_quantity_entry.get())
            if product_id in self.products:
                messagebox.showerror("Error", "Product ID already exists.")
                return
            new_product = Product(product_id, name, category, price, stock_quantity)
            self.products[product_id] = new_product
            messagebox.showinfo("Success", "Product added successfully!")
            self.clear_fields()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for price and stock quantity.")

    def view_products_window(self):
        self.clear_window()
        tk.Label(self.root, text="All Products", font=("Arial", 16)).pack(pady=10)

        # Create table
        columns = ("ID", "Name", "Category", "Price", "Stock")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        for product in self.products.values():
            tree.insert("", "end", values=(product.product_id, product.name, product.category, product.price, product.stock_quantity))

        tree.pack(fill="both", expand=True)
        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)

    def search_product_window(self):
        self.clear_window()
        tk.Label(self.root, text="Search Product", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Enter Product Name or Category:").pack()
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()
        tk.Button(self.root, text="Search", command=self.search_product).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack()

    def search_product(self):
        search_query = self.search_entry.get().lower()
        found_products = [
            (product.product_id, product.name, product.category, product.price, product.stock_quantity)
            for product in self.products.values() if search_query in product.name.lower() or search_query in product.category.lower()
        ]
        if found_products:
            results_window = tk.Toplevel(self.root)
            results_window.title("Search Results")
            columns = ("ID", "Name", "Category", "Price", "Stock")
            tree = ttk.Treeview(results_window, columns=columns, show="headings")
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor="center")

            for product in found_products:
                tree.insert("", "end", values=product)
            tree.pack(fill="both", expand=True)
        else:
            messagebox.showinfo("Search Results", "No matching products found.")

    def export_inventory(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["product_id", "name", "category", "price", "stock_quantity"])
                writer.writeheader()
                for product in self.products.values():
                    writer.writerow(product.to_dict())
            messagebox.showinfo("Export Successful", "Inventory exported successfully.")

    def import_inventory(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product = Product(row["product_id"], row["name"], row["category"], float(row["price"]), int(row["stock_quantity"]))
                    self.products[product.product_id] = product
            messagebox.showinfo("Import Successful", "Inventory imported successfully.")

    def logout(self):
        self.current_user = None
        self.login_window()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = InventoryManagementSystem(root)
    root.mainloop()
