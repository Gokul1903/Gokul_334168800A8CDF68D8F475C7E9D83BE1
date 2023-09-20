class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


students1 = [Student("Kumara", "001", 3.6),Student("Yakneeswaran", "002", 3.7),Student("Vignesh", "003", 3.4),Student("Monish", "004", 3.8),]
students2 = [Student("Vallarasu", "005", 3.1),Student("preshanth", "006", 3.9),Student("Tamil selvan", "007", 3.5),Student("jeeva", "008", 3.8),]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

print("Students 1:\n")
for student in sorted_students1:
    print(f"{student.name} ({student.roll_number}): CGPA - {student.cgpa}")

print("\nStudents 2:\n")
for student in sorted_students2:
    print(f"{student.name} ({student.roll_number}): CGPA - {student.cgpa}")
