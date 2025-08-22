# students = []

def get_students(students):
    return students

def input_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the grade for {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def add_students(students):
    try:
        n = int(input("How many students do you want to add? "))
    except ValueError:
        print("Invalid number.")
        return
    for _ in range(n):
        name = input("Full name of the student: ")
        section = input("Section (e.g., 11B): ")
        spanish = input_grade("Spanish")
        english = input_grade("English")
        social_studies = input_grade("Social Studies")
        science = input_grade("Science")
        student = {
            "name": name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "social": social_studies,
            "science": science
        }
        students.append(student)
        print(f"Student '{name}' added successfully.")

def show_students(students):
    if not students:
        print("No students registered.")
        return
    print("\n--- Student List ---")
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} - Section: {s['section']} - "
            f"Grades: Spanish={s['spanish']}, English={s['english']}, "
            f"Social Studies={s['social']}, Science={s['science']}")

def student_average(s):
    return (s['spanish'] + s['english'] + s['social'] + s['science']) / 4

def show_top_3(students):
    if not students:
        print("No students registered.")
        return

    top_3 = []

    for s in students:
        avg = student_average(s)
        if len(top_3) < 3:
            top_3.append((s, avg))
        else:
            min_index = 0
            for i in range(1, 3):
                if top_3[i][1] < top_3[min_index][1]:
                    min_index = i
            if avg > top_3[min_index][1]:
                top_3[min_index] = (s, avg)

    # Manual sort of top 3
    for i in range(len(top_3)):
        for j in range(i + 1, len(top_3)):
            if top_3[j][1] > top_3[i][1]:
                top_3[i], top_3[j] = top_3[j], top_3[i]

    print("\n--- Top 3 Students by Average ---")
    for i, (s, avg) in enumerate(top_3, start=1):
        print(f"{i}. {s['name']} - Average: {avg:.2f}")

def show_average(students):
    if not students:
        print("No students registered.")
        return
    total = 0
    for s in students:
        total += student_average(s)
    overall_avg = total / len(students)
    print(f"\nOverall student average: {overall_avg:.2f}")