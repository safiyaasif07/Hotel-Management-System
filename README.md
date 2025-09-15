# 🏨 Hotel Management System

The _Hotel Management System_ is a lightweight _web-based application_ built using _Flask (Python)_ and _SQLite_ to manage hotel room bookings efficiently.  
It provides full _CRUD (Create, Read, Update, Delete)_ functionality, ensuring an easy way to handle guest reservations and maintain hotel records.

---

## 🔑 Features

- ➕ _Add Bookings_ – Register new customer reservations with room details.
- ✏ _Edit Bookings_ – Update existing bookings with new dates, status, or payment info.
- ❌ _Delete Bookings_ – Remove bookings from the system.
- 📋 _View Bookings_ – Display all reservations in a tabular format.
- 🔢 _Continuous Booking IDs_ – Reuses deleted IDs so booking numbers remain sequential.
- ✅ _Validation_ – Ensures check-out date is always after check-in date.
- ⚡ _Flash Messages_ – Success/error notifications for user actions.
- 🎨 _Responsive UI_ – Clean and simple HTML/CSS design.

---

## 🛠 Tech Stack

- _Backend:_ Python, Flask
- _Database:_ SQLite
- _Frontend:_ HTML, CSS (Jinja2 templates)
- _Version Control:_ Git & GitHub

---

## 📂 Project Structure

SAFF/
├── templates/
│ └── base.html # HTML template used by Flask to render pages
├── app.py # Main Flask application code
├── hotel.db # SQLite database file to store booking data
└── README.md # Documentation file for project information

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/hotel-management-system.git
cd hotel-management-system

2. Create a virtual environment

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3.Install Dependencies

pip install flask

4.Run the application

python app.py

5.Open in browser

Go to 👉 http://127.0.0.1:5000/

```

Example Input and Output

Example 1 – Adding a Booking

Input (via Add Booking Form):

Customer Name: John Doe
Room Number: 101
Check-In: 2025-09-15
Check-Out: 2025-09-20
Payment Status: Paid
Special Request: Extra bed
Status: Active

Output (Displayed in Table):

ID Customer Room Check-In Check-Out Payment Request Status

1 John Doe 101 2025-09-15 2025-09-20 Paid Extra bed Active


License

This project is licensed under the MIT License – see the LICENSE file for details.

Output of the program:

<img width="1872" height="841" alt="image" src="https://github.com/user-attachments/assets/9abbb6c6-fa84-4c8d-8b94-151b32db9702" />
