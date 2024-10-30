from student import Student


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.attendance_list = {}

    def add_student(self, student: Student):
            """Add student to the group with attendance set to 0."""
            self.attendance_list[student] = 0

    def update_student_info (self, student: Student):
        """Check if student exists based on id and update data"""
        if student.student_id in self.attendance_list:
            existing_student = self.attendance_list[student.student_id]
            existing_student.first_name = student.first_name
            existing_student.last_name = student.last_name

    def mark_student_attendance(self, student: Student, present: bool):
        """Mark student attendance as present or not."""
        if present:
            self.attendance_list[student] = 1
        else:
            self.attendance_list[student] = 0

    def edit_attendance(self, student: Student, present: bool):
        """Edit student attendance."""
        if student in self.attendance_list:
            if present:
                self.attendance_list[student] = 1
            else:
                self.attendance_list[student] = 0
        else:
            print(f"Student {student} not found in group.")

    def import_data(self,filename):
        """Import students from file."""
        try:
            with open(filename, "r") as file:
                for line in file:
                    student_data = line.strip().split()
                    if len(student_data) == 3:
                        first_name, last_name, student_id = student_data[0], student_data[1], int(student_data[2])
                        student = Student(first_name, last_name, student_id)
                        self.add_student(student)
            print(f"Successfully imported students from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def export_data(self,filename):
        """Checking if file is a .txt file"""
        if not filename.endswith('.txt'):
            filename += '.txt'
        """Export attendance list to file."""
        with open(filename, "w") as file:
            for student in self.attendance_list:
                file.write(f"{student}\n")
        print(f"Successfully exported attendance to {filename}")

    def display_attendance(self):
        """Display the attendance list for all students."""
        print(f"Attendance for group: {self.group_name}")
        for student, attendance in self.attendance_list.items():
            status = "Present" if attendance == 1 else "Absent"
            print(f"{student}: {status}")

            