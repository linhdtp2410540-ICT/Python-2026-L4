import curses
import file_manager
import input
import output
import pandas_manager


def handle_query_ui(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== PANDAS QUERY ON STUDENTS DATAFRAME ===")
    stdscr.addstr(
        1,
        0,
        "Enter condition (e.g. name == 'Mr. Volunteers' or id == 'S1'):",
    )
    stdscr.refresh()

    curses.echo()
    condition_bytes = stdscr.getstr(3, 0)
    curses.noecho()

    condition_str = condition_bytes.decode("utf-8").strip()

    stdscr.clear()
    if condition_str:
        result = pandas_manager.query_students(condition_str)
        stdscr.addstr(0, 0, f"Query result for [{condition_str}]:\n\n")
        stdscr.addstr(2, 0, str(result))
    else:
        stdscr.addstr(0, 0, "No query condition entered!")

    stdscr.addstr(12, 0, "\nPress any key to return to menu...")
    stdscr.refresh()
    stdscr.getch()


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
        elif choice == "7":
            pandas_manager.export_to_csv(students, courses, marks)
            stdscr.clear()
            stdscr.addstr(
                0,
                0,
            )
            stdscr.addstr(2, 0, "Press any key to continue...")
            stdscr.getch()
        elif choice == "8":
            handle_query_ui(stdscr)
        elif choice == "0":
            file_manager.save_and_compress(students, courses, marks)
            break


if __name__ == "__main__":
    curses.wrapper(main)