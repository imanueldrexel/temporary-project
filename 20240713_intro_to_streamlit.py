import streamlit as st
import sqlite3
import datetime

# Database connection
def create_connection():
    conn = sqlite3.connect('streamlit_db_example.db')
    return conn

def create_table(conn):
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            date_of_birth DATE NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')

def insert_data(conn, name, age, date_of_birth):
    with conn:
        conn.execute('''
        INSERT INTO user_data (name, age, date_of_birth) 
        VALUES (?, ?, ?)
        ''', (name, age, date_of_birth))

def fetch_data(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_data')
    return cursor.fetchall()

def main():
    st.title("User Data Input")

    # Input Widgets
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=120, value=0)
    date_of_birth = st.date_input("Enter your date of birth", datetime.date(2000, 1, 1))

    if st.button("Submit"):
        conn = create_connection()
        create_table(conn)  # Ensure the table is created before inserting data
        insert_data(conn, name, age, date_of_birth)
        st.success("Data submitted successfully!")

    # Show the data stored in the database
    conn = create_connection()
    create_table(conn)  # Ensure the table is created before fetching data
    data = fetch_data(conn)
    st.write("Stored Data:")
    for row in data:
        st.write(row)

if __name__ == "__main__":
    main()
