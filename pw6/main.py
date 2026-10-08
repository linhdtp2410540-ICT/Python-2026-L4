import curses
import file_manager
import input
import output


def main(stdscr):
    curses.curs_set(0)

    students, courses, marks = file_manager.decompress_and_load()

    while True:
        output.display_menu(stdscr)
        choice = stdscr.getkey()

        if choice == "1":
            input.input_students(stdscr, students, courses, marks)
        elif choice == "2":
            input.input_courses(stdscr, students, courses, marks)
        elif choice == "3":
            input.input_marks(stdscr, students, courses, marks)
        elif choice == "4":
            output.list_students(stdscr, students, courses, marks)
        elif choice == "5":
            output.list_courses(stdscr, courses)
        elif choice == "6":
            output.show_marks(stdscr, students, courses, marks)
        elif choice == "0":
            file_manager.save_and_compress(students, courses, marks)
            break


if __name__ == "__main__":
    curses.wrapper(main)