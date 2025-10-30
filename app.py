from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

DB_NAME = "hotel.db"

# -------- DATABASE SETUP --------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Remove AUTOINCREMENT to allow reuse of deleted IDs
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY,
                        customer TEXT NOT NULL,
                        room INTEGER NOT NULL,
                        check_in DATE NOT NULL,
                        check_out DATE NOT NULL,
                        payment_status TEXT DEFAULT 'Pending',
                        special_request TEXT DEFAULT 'None',
                        status TEXT DEFAULT 'Active'
                    )''')
    conn.commit()
    conn.close()

init_db()

# -------- ROUTES --------
@app.route("/")
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings ORDER BY id ASC")
    bookings = cursor.fetchall()
    conn.close()
    return render_template("base.html", bookings=bookings)

@app.route("/add", methods=["GET", "POST"])
def add_booking():
    if request.method == "POST":
        customer = request.form["customer"]
        room = request.form["room"]
        check_in = request.form["check_in"]
        check_out = request.form["check_out"]
        payment_status = request.form["payment_status"]
        special_request = request.form.get("special_request", "None")
        status = request.form["status"]

        # Validate dates
        if datetime.strptime(check_out, "%Y-%m-%d") <= datetime.strptime(check_in, "%Y-%m-%d"):
            flash("Check-out date must be after check-in date!", "error")
            return redirect(request.url)

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Calculate next available ID (reuse deleted IDs)
        cursor.execute("SELECT MIN(id + 1) FROM bookings WHERE (id + 1) NOT IN (SELECT id FROM bookings)")
        next_id = cursor.fetchone()[0]
        if next_id is None:
            next_id = 1  # Table is empty

        cursor.execute("""
            INSERT INTO bookings (id, customer, room, check_in, check_out, payment_status, special_request, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (next_id, customer, room, check_in, check_out, payment_status, special_request, status))

        conn.commit()
        conn.close()
        flash("Booking added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_booking(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if request.method == "POST":
        customer = request.form["customer"]
        room = request.form["room"]
        check_in = request.form["check_in"]
        check_out = request.form["check_out"]
        payment_status = request.form["payment_status"]
        special_request = request.form.get("special_request", "None")
        status = request.form["status"]

        # Validate dates
        if datetime.strptime(check_out, "%Y-%m-%d") <= datetime.strptime(check_in, "%Y-%m-%d"):
            flash("Check-out date must be after check-in date!", "error")
            return redirect(request.url)

        cursor.execute("""
            UPDATE bookings SET
            customer = ?, room = ?, check_in = ?, check_out = ?, payment_status = ?, special_request = ?, status = ?
            WHERE id = ?
        """, (customer, room, check_in, check_out, payment_status, special_request, status, id))
        conn.commit()
        conn.close()
        flash("Booking updated successfully!", "success")
        return redirect(url_for("index"))

    cursor.execute("SELECT * FROM bookings WHERE id = ?", (id,))
    booking = cursor.fetchone()
    conn.close()
    return render_template("add.html", booking=booking, edit=True)

@app.route("/delete/<int:id>")
def delete_booking(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bookings WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    flash("Booking deleted successfully!", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)