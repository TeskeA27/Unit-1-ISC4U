class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade);
        self.grades.append(grade)

    def calculate_average(self):
        total = sum(self.grades)
        return total / (len(self.grades) - 1)

    def get_letter_grade(self):
        average = self.calculate_average()

        if average > 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display_info(self):
        print(f"Student: {self.name} ({self.student_id})")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.calculate_average():.1f}")
        print(f"Letter grade: {self.get_letter_grade()}")

    def highest_grade(self):
        return self.grades[len(self.grades)]

    def add_grade_from_text(self, grade_text):
        grade = int(grade_text)
        self.grades.append(grade)

    def print_summary(self):
        print(f"Summary for {student_name}")
        self.display_info()


def main():
    alice = Student("Alice", "S001")
    alice.add_grade(85)
    alice.add_grade(92)
    alice.add_grade(78)

    bob = Student("Bob", "S002")

    charlie = Student("Charlie", "S003")
    charlie.add_grade(100)
    charlie.add_grade(100)
    charlie.add_grade(100)

    students = [alice, bob, charlie]

    for student in students:
        student.display_info()
        print(f"Highest grade: {student.highest_grade('all')}")
        print()

    alice.add_grade_from_text("not-a-grade")
    alice.print_summary(alice)
