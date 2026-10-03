import sqlite3
from datetime import datetime
from pathlib import Path

# Goal with this file
#    Add expenses
#    Show all expenses
#    Monthly summary
#    Category summary
#    Delete by ID

DATABASE_PATH = Path(__file__).resolve().parent / "expenses.db"


def initialize_database():
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                note TEXT,
                date TEXT NOT NULL
            )
        """)



def add_expenses():
    amount = float(input("Amount: "))
    category = input("Category: ").upper()
    note = input("Note: ")
    date = datetime.now().strftime("%d-%m-%Y")

    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
        (amount, category, note, date)
    )

    conn.commit()
    conn.close()

    print("Expense saved!")



def show_expenses():
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    cur.execute(
        "SELECT id, amount, category, note, date FROM expenses ORDER BY date DESC"
    )

    rows = cur.fetchall()
    conn.close()

    print("\n === Expenses === ")

    if not rows:
        print("No expenses")
        return

    for row in rows:
        # id (0), date (4), amount (1), category (2), note (3)
        print(f"{row[0]}. {row[4]} | {row[1]} | {row[2]} | {row[3]} ")



def delete():
    show_expenses()
    deleted_id = input("Enter ID to delete: ")

    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    cur.execute("DELETE FROM expenses WHERE id = ?", (deleted_id))

    conn.commit()
    conn.close()

    print("Deleted!")



def monthly_summary():
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT SUBSTR(date, 1, 7) AS month, SUM(amount) AS total
        FROM expenses
        GROUP BY month
        ORDER BY month DESC
        """)

    rows = cur.fetchall()
    conn.close()

    print("\n === Monthly Summary ===")

    if not rows:
        print("No expenses")
        return

    for row in rows:
        print(f"{row[0]} : {row[1]}")



def category_summary():

    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    cur.execute(""" 
        SELECT category, SUM(amount) as total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
    """)

    rows = cur.fetchall()
    conn.close()

    print("\n === Category Summary ==== ")

    if not rows:
        print("No data.")
        return

    for row in rows:
        print(f"{row[0]} : {row[1]}")



def main():
    initialize_database()

    print(" === Expense tracker === ")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Monthly summary")
    print("4. Category summary")
    print("5. Delete by ID")
    print("6. Exit")

    inp = int(input("Select option: "))

    match (inp):
        case 1: add_expenses()
        case 2: show_expenses()
        case 3: monthly_summary()
        case 4: category_summary()
        case 5: delete()
        case 6: quit()
        case _: print("Unknown command")


if __name__ == "__main__":
    main()