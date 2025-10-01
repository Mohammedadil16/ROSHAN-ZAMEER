import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect("cafe.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT,
    quantity INTEGER,
    total_price REAL,
    order_time TEXT
)
""")
conn.commit()

# Menu items with prices
menu = {
    "coffee": 50,
    "Tea": 30,
    "Sandwich": 80,
    "Burger": 100,
    "Pastry": 60
}

# Create main application window
root = tk.Tk()
root.title("Cafe Management System")
root.geometry("500x600")

# Store quantity input widgets
qty_vars = {}

def calculate_bill():
    total = 0
    order_summary = ""

    for item, price in menu.items():
        qty = qty_vars[item].get()
        if qty.isdigit() and int(qty) > 0:
            item_total = int(qty) * price
            total += item_total
            order_summary += f"{item} x {qty} = ₹{item_total}\n"

            # Store in database
            cursor.execute("INSERT INTO orders (item, quantity, total_price, order_time) VALUES (?, ?, ?, ?)",
                           (item, int(qty), item_total, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()

    if total == 0:
        messagebox.showwarning("No Order", "Please select at least one item.")
        return

    tax = total * 0.05
    grand_total = total + tax
    order_summary += f"\nSubtotal: ₹{total:.2f}\nTax (5%): ₹{tax:.2f}\nTotal: ₹{grand_total:.2f}"

    messagebox.showinfo("Bill", order_summary)

def clear_fields():
    for var in qty_vars.values():
        var.set("0")

# UI Layout
tk.Label(root, text="Cafe Menu", font=("Helvetica", 16, "bold")).pack(pady=10)

menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

# Generate menu rows
for i, (item, price) in enumerate(menu.items()):
    tk.Label(menu_frame, text=f"{item} (₹{price})", font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5, sticky='w')
    qty_var = tk.StringVar(value="0")
    qty_vars[item] = qty_var
    tk.Entry(menu_frame, textvariable=qty_var, width=5).grid(row=i, column=1)

# Buttons
tk.Button(root, text="Calculate Bill", command=calculate_bill, bg="green", fg="white", font=("Helvetica", 12)).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields, bg="orange", fg="white", font=("Helvetica", 12)).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", font=("Helvetica", 12)).pack(pady=10)

root.mainloop()
