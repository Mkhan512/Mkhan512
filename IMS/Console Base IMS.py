# Inventory Management System (IMS)

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.product_id} - {self.name} ({self.category}) - ${self.price} - Stock: {self.stock_quantity}"


class InventoryManagementSystem:
    def __init__(self):
        self.products = {}  # Dictionary to store products with product_id as key
        self.users = {"admin": {"password": "adminpass", "role": "Admin"},
                      "user": {"password": "userpass", "role": "User"}}  # Sample users
        self.current_user = None

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.users.get(username)
        if user and user["password"] == password:
            self.current_user = user
            print(f"Login successful! Welcome, {self.current_user['role']}.")
            return True
        else:
            print("Invalid username or password.")
            return False

    def add_product(self):
        if self.current_user["role"] != "Admin":
            print("Permission denied. Only Admins can add products.")
            return

        try:
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = float(input("Enter Product Price: "))
            stock_quantity = int(input("Enter Stock Quantity: "))

            if product_id in self.products:
                print("Product ID already exists. Use a unique Product ID.")
                return

            new_product = Product(product_id, name, category, price, stock_quantity)
            self.products[product_id] = new_product
            print("Product added successfully!")
        except ValueError:
            print("Invalid input for price or stock quantity. Please enter numbers only.")

    def edit_product(self):
        if self.current_user["role"] != "Admin":
            print("Permission denied. Only Admins can edit products.")
            return

        product_id = input("Enter Product ID to edit: ")
        product = self.products.get(product_id)
        if product:
            try:
                product.name = input(f"Enter new name ({product.name}): ") or product.name
                product.category = input(f"Enter new category ({product.category}): ") or product.category
                product.price = float(input(f"Enter new price ({product.price}): ") or product.price)
                product.stock_quantity = int(input(f"Enter new stock quantity ({product.stock_quantity}): ") or product.stock_quantity)
                print("Product updated successfully!")
            except ValueError:
                print("Invalid input. Please enter numbers for price and stock quantity.")
        else:
            print("Product not found.")

    def delete_product(self):
        if self.current_user["role"] != "Admin":
            print("Permission denied. Only Admins can delete products.")
            return

        product_id = input("Enter Product ID to delete: ")
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully!")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products.values():
                print(product)
            print("End of product list.")

    def search_product(self):
        search_name = input("Enter product name or category to search: ").lower()
        found = False
        for product in self.products.values():
            if search_name in product.name.lower() or search_name in product.category.lower():
                print(product)
                found = True
        if not found:
            print("No products found with that name or category.")

    def adjust_stock(self):
        if self.current_user["role"] != "Admin":
            print("Permission denied. Only Admins can adjust stock.")
            return

        product_id = input("Enter Product ID to adjust stock: ")
        product = self.products.get(product_id)
        if product:
            try:
                adjustment = int(input("Enter stock adjustment (positive to restock, negative to reduce): "))
                product.stock_quantity += adjustment
                print(f"Stock adjusted. New stock quantity for {product.name}: {product.stock_quantity}")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        else:
            print("Product not found.")

    def run(self):
        if not self.login():
            return

        while True:
            print("\nInventory Management System - Menu")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. View Products")
            print("5. Search Product")
            print("6. Adjust Stock")
            print("7. Logout")
            choice = input("Select an option (1-7): ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.edit_product()
            elif choice == "3":
                self.delete_product()
            elif choice == "4":
                self.view_products()
            elif choice == "5":
                self.search_product()
            elif choice == "6":
                self.adjust_stock()
            elif choice == "7":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please select an option between 1 and 7.")


# Main Execution
if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.run()
