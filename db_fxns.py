import streamlit as st
import os
import sqlite3

# Read DB path from secrets
DB_NAME = st.secrets['database']["sqlite_path"]

# Ensure the directory for the DB exists
os.makedirs(os.path.dirname(DB_NAME), exist_ok=True)

# The database Connection
conn = sqlite3.connect(DB_NAME, check_same_thread=False)

#conn = sqlite3.connect('data/data.db',check_same_thread=False)
c = conn.cursor()

# Database
# Table
# Field/Columns
# DataType

# CREATE the database Table and columns
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS taskstable(task TEXT, task_status TEXT, task_due_date DATE)""")

# CREATE/INSERT New Tasks into the database table
def add_data(task,task_status,task_due_date):
    c.execute("""INSERT INTO taskstable(task, task_status, task_due_date) VALUES(?,?,?)""",(task,task_status,task_due_date))
    conn.commit()

# READ/VIEW All Tasks in the database table
def view_all_data():
    c.execute("""SELECT * FROM taskstable""")
    return c.fetchall()

# UPDATE Tasks
# get unique tasks
def view_unique_tasks():
    c.execute("""SELECT DISTINCT task FROM taskstable""")
    return c.fetchall()

# get task by name
def get_task(task):
    c.execute("""SELECT * FROM taskstable WHERE task = ?""", (task,))
    return c.fetchone()

# Changes to the Selected TASK
def update_task(new_task, new_status, new_due_date, original_task):
    c.execute("""
        UPDATE taskstable 
        SET task = ?, task_status = ?, task_due_date = ? 
        WHERE task = ?
    """, (new_task, new_status, new_due_date, original_task))
    conn.commit()

# DELETE Tasks