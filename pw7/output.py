import numpy as np
import curses

def calculate_gpa(students, courses, marks):
    for s in students:
        marks_list = []
        credits_list = []

        for c in courses:
            key = (c.get_id(), s.get_id())
            if key in marks:
                marks_list.append(marks[key])
                credits_list.append(c.get_credits())

        if credits_list and sum(credits_list) > 0:
            np_marks = np.array(marks_list)
            np_credits = np.array(credits_list)
            gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
            s.set_gpa(round(gpa, 2))
        else:
            s.set_gpa(0.0)

def sort_students_by_gpa(students, courses, marks):
    calculate_gpa(students, courses, marks)
    students.sort(key=lambda s: s.get_gpa(), reverse=True)

def list_students(stdscr, students, courses, marks):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENT LIST (SORTED BY GPA DESCENDING) ===")

    if not students:
        stdscr.addstr(2, 0, "No students found!")
    else:
        sort_students_by_gpa(students, courses, marks)
        line = 2
        for s in students:
            stdscr.addstr(
                line, 0, 
                f"ID: {s.get_id()} | Name: {s.get_name()} | DoB: {s.get_dob()} | GPA: {s.get_gpa():.2f}"
            )
            line += 1

    stdscr.addstr(line + 1, 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

def list_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== COURSE LIST ===")

    if not courses:
        stdscr.addstr(2, 0, "No courses found!")
    else:
        line = 2
        for c in courses:
            stdscr.addstr(
                line, 0, 
                f"ID: {c.get_id()} | Name: {c.get_name()} | Credits: {c.get_credits()}"
            )
            line += 1

    stdscr.addstr(line + 1, 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

def show_marks(stdscr, students, courses, marks):
    if not courses or not students:
        stdscr.clear()
        stdscr.addstr(0, 0, "No data available! Press any key...")
        stdscr.getch()
        return

    from input import get_input_str
    cid = get_input_str(stdscr, "Enter course ID to view marks: ")
    stdscr.clear()
    stdscr.addstr(0, 0, f"=== MARKS FOR COURSE [{cid}] ===")

    line = 2
    has_marks = False
    for s in students:
        key = (cid, s.get_id())
        if key in marks:
            stdscr.addstr(
                line, 0, 
                f"Student: {s.get_name()} (ID: {s.get_id()}) -> Mark: {marks[key]}"
            )
            line += 1
            has_marks = True

    if not has_marks:
        stdscr.addstr(line, 0, "No marks recorded for this course!")
        line += 1

    stdscr.addstr(line + 1, 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

def display_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENT MANAGEMENT SYSTEM (PANDAS EXTRA) ===")
    stdscr.addstr(1, 0, "1. Input Students")
    stdscr.addstr(2, 0, "2. Input Courses")
    stdscr.addstr(3, 0, "3. Input Marks")
    stdscr.addstr(4, 0, "4. List Students")
    stdscr.addstr(5, 0, "5. List Courses")
    stdscr.addstr(6, 0, "6. Show Marks")
    stdscr.addstr(7, 0, "7. Export Info to CSV Files")
    stdscr.addstr(8, 0, "8. Query Students DataFrame (Pandas)")
    stdscr.addstr(9, 0, "0. Exit")
    stdscr.addstr(11, 0, "Select an option: ")
    stdscr.refresh()