from tkinter import *
from tkinter import messagebox 
import mysql.connector

def insert_data():
    name = e1.get()
    email = e2.get()

    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Sneha"
        )

        cursor = connection.cursor()
        query = "INSERT INTO login (user, email) values (%s, %s)"
        values = (name, email)

        cursor.execute(query, values)
        connection.commit()

        messagebox.showinfo("Success", "Data inserted successfully")

        # e1.delete(0, END)
        # e2.delete(0, END)

    except mysql.connector.Error as err:
        print(f"error: '{err}'")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

root = Tk()
root.title("Data Insertion GUI")
root.geometry('500x500')

# Create labels and entry fields
l1 = Label(root, text="User Name").grid(row=0, column=0, padx=10, pady=5)
l2 = Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)

e1 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)

e2 = Entry(root)
e2.grid(row=1, column=1, padx=10, pady=5)

# Create a button to insert data
btn = Button(root, text="Insert Data", command=insert_data)
btn.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
