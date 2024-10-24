from student import Student


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.attendance_list = {}

    def add_student(self, student: Student):
        """Add student to the group with attendance set to 0."""
        self.attendance_list[student] = 0

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

    def display_attendance(self):
        """Display the attendance list for all students."""
        print(f"Attendance for group: {self.group_name}")
        for student, attendance in self.attendance_list.items():
            status = "Present" if attendance == 1 else "Absent"
            print(f"{student}: {status}")

            