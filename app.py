import streamlit as st

import pandas as pd
# MySQL Database library :- mysql-connector
st.title("Streamlit with SQLite Database")

# Web :- M(Model Database Table) V(Logic) T(Template UI), MVC
# Mobile :- MVVM

st.divider()

menu = [
    "Add Student",
    "View Students",
    "Update Student",
    "Delete Student"
]

# Widgets
choice = st.sidebar.selectbox("Choose Action", menu)

# Add Student UI
if choice == "Add Student":
    st.header("Add the Student Details")
    student_name = st.text_input("Enter Student Name")
    student_age = st.number_input("Enter Age", min_value=10,max_value=50)
    student_course = st.text_input("Enter Student Course")
    
    if st.button("Submit", type="primary"): # True
        result = add_student(student_name, student_age, student_course)
        if result: # True
            st.success("Student added successfully!")
        else:
            st.error("Failed to add student.")

elif choice == "View Students":
    st.subheader("All Students Data")
    studentsData = view_students_details()
    st.write(studentsData)
    column_names = ["ID","Name","Age","Course"]
    df = pd.DataFrame(studentsData, columns=column_names)
    st.write(df)

    # Streamlit
    st.dataframe(df)

elif choice == "Update Student":
    st.subheader("Update Student Details")

    # Firstly get all the students data
    fecthStudentsData = view_students_details()

    # Get the Ids
    """
    ids = []
    for i in fecthStudentsData:
        ids.append(i[0])
    
    st.write(ids)
    """
    ids = [i[0] for i in fecthStudentsData] # List Comprehension

    # Select Id to update the data
    student_id = st.selectbox("Select Student Id", ids)
    st.write(student_id)

    # Showing the previous added data in the columns
    selected = None
    for student in fecthStudentsData:
        if student[0] == student_id:
            selected = student

    student_name = st.text_input("Enter Student Name", selected[1])
    student_age = st.number_input("Enter Age", min_value=10,max_value=50, value=selected[2])
    student_course = st.text_input("Enter Student Course", selected[3])

    if st.button("Update", type="primary"): # True
        result = update_student(student_name, student_age, student_course, student_id)
        if result: # True
            st.success("Student updated successfully!")
        else:
            st.error("Failed to update student data.")


