# Core Package
import streamlit as st
import streamlit.components.v1 as stc

# Import DB Functions from db_fxns
#from db_fxns import *
from db_fxns import create_table,add_data

# Utility package for DateTime
import datetime

# EDA Packages
import pandas as pd

# Import the Functions page db_fxns.app
from db_fxns import *

# Data Viz Pkgs
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">ToDo App (CRUD)</h1>
    <p style="color:white;text-align:center;">Built with Streamlit</p>
    </div>
    """

def main():
    stc.html(HTML_BANNER)

    menu = ["Create","Read","Update","Delete","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    # Create the database Tables
    create_table()

    # CREATE TASK
    if choice == "Create":
        st.subheader("Create New Task")

        # Layout
        col1, col2 = st.columns(2)

        with col1:
            task = st.text_area("Task To Do")

        with col2:
            task_status = st.selectbox("Status", ["To Do", "Ongoing", "Done"])
            task_due_date = st.date_input("Task Due Date", datetime.date.today())

        if st.button("Add Task"):
            add_data(task, task_status, task_due_date)
            st.success("Task Added:{}".format(task))

    # READ/VIEW TASK
    elif choice == "Read":
        st.subheader("View Tasks")
        result = view_all_data()
        #st.write(result)
        with st.expander("View All Tasks"):
            df = pd.DataFrame(result,columns=["Task Name","Task Status","Task Due Date"])
            st.dataframe(df)

        # Add a plot
        with st.expander("Task Status"):
            task_df = df["Task Status"].value_counts().reset_index()
            task_df.columns = ["Task Name", "Count"]
            st.dataframe(task_df)

            p1 = px.pie(task_df, names="Task Name", values="Count", title="Task Distribution")
            st.plotly_chart(p1)

    # UPDATE TASK
    elif choice == "Update":
        st.subheader("Edit/Update Task")
        result = view_all_data()
        # st.write(result)
        df = pd.DataFrame(result, columns=["Task Name", "Task Status", "Task Due Date"])
        with st.expander("View Current Tasks"):
            st.dataframe(df)

        #st.write(view_unique_tasks())
        list_of_task = [i[0] for i in view_unique_tasks()]
        #st.write(list_of_task)
        # Creates a listbox with the unique list of tasks to edit
        selected_task = st.selectbox("Select Task to Edit", list_of_task)

        selected_result = get_task(selected_task)
        #st.write(selected_result)

        if selected_result:
            task = selected_result[0]
            task_status = selected_result[1]
            task_due_date = selected_result[2]

            # Layout
            col1, col2 = st.columns(2)

            with col1:
                new_task = st.text_area("Task To Do",task)

            with col2:
                new_task_status = st.selectbox("Status", ["To Do", "Ongoing", "Done"],index=["To Do", "Ongoing", "Done"].index(task_status))
                new_task_due_date = st.date_input("Due Date",datetime.datetime.strptime(task_due_date, "%Y-%m-%d").date())

            if st.button("Update Task"):
                update_task(new_task, new_task_status, new_task_due_date, task)
                st.success("Task Successfully Updated:: From {} To ::{}".format(task, new_task))
                st.rerun()

            result2 = view_all_data()
            # st.write(result)
            df2 = pd.DataFrame(result2, columns=["Task Name", "Task Status", "Task Due Date"])
            with st.expander("View Updated Tasks"):
                st.dataframe(df2)

    # DELETE TASK
    elif choice == "Delete":
        st.subheader("Delete Task")
        result = view_all_data()
        # st.write(result)
        df = pd.DataFrame(result, columns=["Task Name", "Task Status", "Task Due Date"])
        with st.expander("Current Tasks"):
            st.dataframe(df)

            list_of_task = [i[0] for i in view_unique_tasks()]
            # Creates a listbox with the unique list of tasks to delete
            selected_task = st.selectbox("Select Task to Delete", list_of_task)
            if st.button("Delete Task"):
                delete_task(selected_task)
                st.warning("Task Deleted:{}".format(selected_task))
                st.rerun()

        #delete_task(task)
        #result = view_all_data()
    else:
        st.subheader("About")




if __name__ == '__main__':
    main()
