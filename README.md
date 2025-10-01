# ☕ Cafe Management System

A simple and user-friendly system developed to manage cafe operations like **order processing, bill calculations, and record keeping**.  
The project uses **Python (Tkinter)** for the graphical interface and **SQLite3** for backend storage, making it lightweight, efficient, and easy to use.

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Future Enhancements](#-future-enhancements)
- [Contributors](#-contributors)
- [License](#-license)

---

## 💡 About the Project

In today’s food industry, managing daily operations manually can be time-consuming and error-prone.  
This **Cafe Management System** was designed to provide a **digital solution** for small to medium-sized cafes.  

It allows staff to take orders, calculate totals (with tax), and store transaction details in a database. The system eliminates manual billing errors and saves time during peak hours.

This project was developed as part of the **B.Tech CSE AIML (3rd Semester, 2025–2026)** coursework at Rai Technology University.

---

## ✨ Key Features
- **Order Processing**: Add menu items and quantities through a GUI.
- **Automated Billing**: Calculates subtotal, applies 5% tax, and generates a final total.
- **Database Integration**: Every order is stored in a local SQLite database with timestamp.
- **Error Handling**: Warns users if no items are selected.
- **Clear & Simple UI**: Built with Tkinter for cross-platform support.

---

## ⚙️ How It Works
The system follows a simple workflow:

1. Launch the application.
2. Select menu items and enter quantities.
3. The system calculates totals and applies tax.
4. A detailed bill is displayed in a message box.
5. All orders are saved in the **SQLite database**.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Tkinter (comes pre-installed with Python)
- SQLite3 (bundled with Python)

### Installation
cd cafe-management-system

Run the program:
python cafe.py

🖥️ Usage
Enter quantities for menu items.
Click Calculate Bill to generate the bill.
Use Clear to reset inputs.
Use Exit to close the program.

📂 Project Structure
Cafe-Management-System/
│── CAFE MANAGEMENT SYSTEM.py         # Main application code
│── cafe.db         # SQLite database (auto-created on first run)
│── README.md       # Project documentation
🔮 Future Enhancements
User authentication and login

Printable receipts

Inventory management

Advanced reporting (daily/monthly sales)

👨‍💻 Contributors
Rakesh C (RTU24101CS014)

Darshan D (RTU24101CS015)

Manish M (RTU24101CS021)

G Roshan Zameer (RTU24101CS035)

📜 License
This project is for educational purposes. Free to use and modify.
