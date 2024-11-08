import tkinter as tk
from tkinter import messagebox
import csv
import os

# File name to store inventory data
inventory_file = "inventory.csv"

# Inventory dictionary
inventory = {}

# Function to load inventory from CSV
def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory[row['item']] = {'quantity': int(row['quantity']), 'price': float(row['price'])}
    display_inventory()

# Function to save inventory to CSV
def save_inventory():
    with open(inventory_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['item', 'quantity', 'price'])
        writer.writeheader()
        for item, details in inventory.items():
            writer.writerow({'item': item, 'quantity': details['quantity'], 'price': details['price']})

# Function to add or update items
def add_or_update_item():
    item = entry_item.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    
    if item and quantity and price:
        if item in inventory:
            inventory[item]['quantity'] += int(quantity)
            inventory[item]['price'] = float(price)
            messagebox.showinfo("Updated", f"{item} updated successfully!")
        else:
            inventory[item] = {'quantity': int(quantity), 'price': float(price)}
            messagebox.showinfo("Added", f"{item} added successfully!")
        
        clear_entries()
        display_inventory()
        save_inventory()  # Save inventory after every change
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Function to remove an item
def remove_item():
    item = entry_item.get()
    if item in inventory:
        del inventory[item]
        messagebox.showinfo("Removed", f"{item} removed successfully!")
        clear_entries()
        display_inventory()
        save_inventory()  # Save inventory after every change
    else:
        messagebox.showwarning("Not Found", f"{item} not found in inventory.")

# Function to search for an item
def search_item():
    item = entry_item.get()
    if item in inventory:
        entry_quantity.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_quantity.insert(0, inventory[item]['quantity'])
        entry_price.insert(0, inventory[item]['price'])
    else:
        messagebox.showwarning("Not Found", f"{item} not found in inventory.")

# Function to clear input entries
def clear_entries():
    entry_item.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)

# Function to display inventory
def display_inventory():
    listbox.delete(0, tk.END)
    listbox.insert(tk.END, f"{'Item':<15}{'Quantity':<10}{'Price':<10}")
    listbox.insert(tk.END, "-"*35)
    for item, details in inventory.items():
        listbox.insert(tk.END, f"{item:<15}{details['quantity']:<10}{details['price']:<10}")

# Create main window
window = tk.Tk()
window.title("Inventory Management System")

# Labels and entries for item details
label_item = tk.Label(window, text="Item Name")
label_item.grid(row=0, column=0, padx=10, pady=10)
entry_item = tk.Entry(window)
entry_item.grid(row=0, column=1, padx=10, pady=10)

label_quantity = tk.Label(window, text="Quantity")
label_quantity.grid(row=1, column=0, padx=10, pady=10)
entry_quantity = tk.Entry(window)
entry_quantity.grid(row=1, column=1, padx=10, pady=10)

label_price = tk.Label(window, text="Price")
label_price.grid(row=2, column=0, padx=10, pady=10)
entry_price = tk.Entry(window)
entry_price.grid(row=2, column=1, padx=10, pady=10)

# Buttons for actions
btn_add_update = tk.Button(window, text="Add/Update Item", command=add_or_update_item)
btn_add_update.grid(row=3, column=0, padx=10, pady=10)

btn_remove = tk.Button(window, text="Remove Item", command=remove_item)
btn_remove.grid(row=3, column=1, padx=10, pady=10)

btn_search = tk.Button(window, text="Search Item", command=search_item)
btn_search.grid(row=4, column=0, padx=10, pady=10)

btn_clear = tk.Button(window, text="Clear Fields", command=clear_entries)
btn_clear.grid(row=4, column=1, padx=10, pady=10)

# Listbox to display inventory
listbox = tk.Listbox(window, width=40, height=10)
listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Load inventory from CSV on startup
load_inventory()

# Start the GUI event loop
window.mainloop()
