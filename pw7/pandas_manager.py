import os
import pandas as pd

STUDENTS_CSV = "students.csv"
COURSES_CSV = "courses.csv"
MARKS_CSV = "marks.csv"


def export_to_csv(students, courses, marks):
    students_data = [
        {"id": s.get_id(), "name": s.get_name(), "dob": s.get_dob()}
        for s in students
    ]
    df_students = pd.DataFrame(students_data)
    df_students.to_csv(STUDENTS_CSV, index=False)

    courses_data = [
        {"id": c.get_id(), "name": c.get_name(), "credits": c.get_credits()}
        for c in courses
    ]
    df_courses = pd.DataFrame(courses_data)
    df_courses.to_csv(COURSES_CSV, index=False)

    marks_data = [
        {"course_id": cid, "student_id": sid, "mark": mark}
        for (cid, sid), mark in marks.items()
    ]
    df_marks = pd.DataFrame(marks_data)
    df_marks.to_csv(MARKS_CSV, index=False)


def load_csv_dataframes():
    df_students = (
        pd.read_csv(STUDENTS_CSV)
        if os.path.exists(STUDENTS_CSV)
        else pd.DataFrame()
    )
    df_courses = (
        pd.read_csv(COURSES_CSV)
        if os.path.exists(COURSES_CSV)
        else pd.DataFrame()
    )
    df_marks = (
        pd.read_csv(MARKS_CSV) if os.path.exists(MARKS_CSV) else pd.DataFrame()
    )

    return df_students, df_courses, df_marks


def query_students(condition_str):
    df_students, _, _ = load_csv_dataframes()

    if df_students.empty:
        return 

    try:
        result_df = df_students.query(condition_str)
        return result_df
    except Exception as e:
        return f"Query Syntax Error: {e}"