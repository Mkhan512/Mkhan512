import tkinter as tk
from tkinter import ttk, messagebox

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1000x600")

        # Sidebar Menu
        self.sidebar = tk.Frame(self.root, bg="#f5f5f5", width=200)
        self.sidebar.pack(side="left", fill="y")

        self.create_sidebar_button("Inventory", self.show_inventory)
        self.create_sidebar_button("Orders", lambda: messagebox.showinfo("Orders", "Orders View"))
        self.create_sidebar_button("Order History", lambda: messagebox.showinfo("Order History", "Order History View"))
        self.create_sidebar_button("Issued Items", lambda: messagebox.showinfo("Issued Items", "Issued Items View"))
        self.create_sidebar_button("Users", lambda: messagebox.showinfo("Users", "Users Management"))
        self.create_sidebar_button("Admin Actions", lambda: messagebox.showinfo("Admin Actions", "Admin Actions"))

        # Main Content Area
        self.main_frame = tk.Frame(self.root, bg="#ffffff")
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.create_inventory_table()
        self.create_inventory_controls()

    def create_sidebar_button(self, text, command):
        button = tk.Button(
            self.sidebar, text=text, command=command, bg="#f5f5f5", fg="#333333",
            font=("Arial", 12), anchor="w"
        )
        button.pack(fill="x", padx=10, pady=5)

    def create_inventory_table(self):
        tk.Label(self.main_frame, text="Inventory", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)

        # Search bar and Add Items button
        search_frame = tk.Frame(self.main_frame, bg="#ffffff")
        search_frame.pack(pady=10)

        tk.Entry(search_frame, width=30, font=("Arial", 12)).pack(side="left", padx=5)
        tk.Button(search_frame, text="Search", bg="#007bff", fg="#ffffff", font=("Arial", 12)).pack(side="left", padx=5)
        tk.Button(search_frame, text="All Items", bg="#28a745", fg="#ffffff", font=("Arial", 12)).pack(side="left", padx=5)
        tk.Button(search_frame, text="Add Items", bg="#28a745", fg="#ffffff", font=("Arial", 12), command=self.add_item).pack(side="left", padx=5)

        # Inventory table
        columns = ("Sno", "Item Name", "Item Cost", "Description", "Quantity", "Available", "Actions")
        self.tree = ttk.Treeview(self.main_frame, columns=columns, show="headings", height=15)
        
        # Define column headings and column width
        self.tree.heading("Sno", text="Sno")
        self.tree.heading("Item Name", text="Item Name")
        self.tree.heading("Item Cost", text="Item Cost")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Available", text="Available")
        self.tree.heading("Actions", text="Actions")

        self.tree.column("Sno", width=50)
        self.tree.column("Item Name", width=150)
        self.tree.column("Item Cost", width=100)
        self.tree.column("Description", width=200)
        self.tree.column("Quantity", width=80)
        self.tree.column("Available", width=80)
        self.tree.column("Actions", width=100)

        # Add sample data
        sample_data = [
            (1, "Mouse", "500", "Hp", 10, 9),
            (2, "Bats", "1000", "Mrf", 10, 10),
            (3, "Printer", "5000", "Hp Printer", 4, 3),
            (4, "Football", "2000", "Nivia", 10, 10),
            (5, "Dell Desktop", "28895", "Dell Inspiron 3043", 2, 2)
        ]
        
        for item in sample_data:
            self.tree.insert("", "end", values=item)

        self.tree.pack(pady=10)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def create_inventory_controls(self):
        # Action buttons for issuing and receiving items
        control_frame = tk.Frame(self.main_frame, bg="#ffffff")
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Issue Item", bg="#17a2b8", fg="#ffffff", font=("Arial", 12), command=self.issue_item).pack(side="left", padx=10)
        tk.Button(control_frame, text="Receive Item", bg="#ffc107", fg="#ffffff", font=("Arial", 12), command=self.receive_item).pack(side="left", padx=10)

    def add_item(self):
        messagebox.showinfo("Add Item", "Add Item functionality")

    def issue_item(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item)["values"]
            messagebox.showinfo("Issue Item", f"Issued: {item_data[1]}")
        else:
            messagebox.showerror("Error", "No item selected")

    def receive_item(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tre
