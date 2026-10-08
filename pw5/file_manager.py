import os
import zipfile
from domains.student import Student
from domains.course import Course

TXT_FILES = ["students.txt", "courses.txt", "marks.txt"]

def save_students_txt(students):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")

def save_courses_txt(courses):
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

def save_marks_txt(marks):
    with open("marks.txt", "w", encoding="utf-8") as f:
        for (cid, sid), mark in marks.items():
            f.write(f"{cid},{sid},{mark}\n")

def compress_to_dat():
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_name in TXT_FILES:
            if os.path.exists(file_name):
                zipf.write(file_name)
    for file_name in TXT_FILES:
        if os.path.exists(file_name):
            os.remove(file_name)

def decompress_and_load():
    students = []
    courses = []
    marks = {}

    if not os.path.exists("students.dat"):
        return students, courses, marks
    with zipfile.ZipFile("students.dat", "r") as zipf:
        zipf.extractall()
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    students.append(Student(parts[0], parts[1], parts[2]))
    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], int(parts[2])))
    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    marks[(parts[0], parts[1])] = float(parts[2])
    for file_name in TXT_FILES:
        if os.path.exists(file_name):
            os.remove(file_name)

    return students, courses, marks