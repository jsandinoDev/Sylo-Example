from actions import get_students, add_students, show_students, show_top_3, show_average
from data import export_to_csv, import_from_csv

def show_menu():
    students = []
    while True:
        print("\n=== Student Menu ===")
        print("1. Enter student info")
        print("2. List all students")
        print("3. Top 3 students")
        print("4. Overall average")
        print("5. Export to CSV")
        print("6. Import from CSV")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_students(students)
        elif choice == "2":
            get_students(students)
        elif choice == "3":
            show_top_3(students)
        elif choice == "4":
            show_average(students)
        elif choice == "5":
            export_to_csv(students)
        elif choice == "6":
            import_from_csv()
        elif choice == "0":
            print("👋 Goodbye.")
            break
        else:
            print("❌ Invalid option – please try again.")
