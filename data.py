import csv
from actions import get_students

def export_to_csv():
    students = get_students()
    if not students:
        print("No data to export.")
        return
    with open("students.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "section", "spanish", "english", "social", "science"])
        writer.writeheader()
        writer.writerows(students)
    print("Data exported successfully to 'students.csv'.")

def import_from_csv():
    from actions import get_students  # avoid circular import
    students = get_students()
    try:
        with open("students.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader:
                try:
                    student = {
                        "name": row["name"],
                        "section": row["section"],
                        "spanish": float(row["spanish"]),
                        "english": float(row["english"]),
                        "social": float(row["social"]),
                        "science": float(row["science"])
                    }
                    students.append(student)
                    count += 1
                except Exception as e:
                    print(f"Error importing a row: {e}")
            print(f"{count} students imported from 'students.csv'.")
    except FileNotFoundError:
        print("No 'students.csv' file found to import.")