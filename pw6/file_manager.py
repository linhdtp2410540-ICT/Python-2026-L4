import os
import pickle
import zipfile

DATA_FILE = "data.pkl"
ZIP_FILE = "students.dat"


def save_and_compress(students, courses, marks):
    data = {"students": students, "courses": courses, "marks": marks}

    with open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)
    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(DATA_FILE)
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)


def decompress_and_load():
    students = []
    courses = []
    marks = {}

    if not os.path.exists(ZIP_FILE):
        return students, courses, marks
    with zipfile.ZipFile(ZIP_FILE, "r") as zipf:
        zipf.extractall()
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            data = pickle.load(f)
            students = data.get("students", [])
            courses = data.get("courses", [])
            marks = data.get("marks", {})
        os.remove(DATA_FILE)

    return students, courses, marks