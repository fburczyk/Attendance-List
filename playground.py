from group import Group
from student import Student


def test_group_attendance():
    # Create a new group
    group = Group("Computer Science 2024")

    # Add students manually
    student1 = Student("John", "Doe", 12345)
    student2 = Student("Jane", "Smith", 54321)
    group.add_student(student1)
    group.add_student(student2)

    # Display initial attendance
    print("Initial attendance:")
    group.display_attendance()

    # Mark attendance
    print("\nMarking attendance...")
    group.mark_student_attendance(student1, True)
    group.mark_student_attendance(student2, False)

    # Display updated attendance
    print("\nUpdated attendance after marking:")
    group.display_attendance()

    # Export attendance to file
    group.export_data("test_group2.txt")

    # Update student info
    print("\nUpdating student info for John Doe...")
    group.update_student_in_group(student1, "Jonathan", "Doe")

    # Display updated attendance with new student info
    print("\nAttendance after updating student info:")
    group.display_attendance()

    # Import data (assuming "students.txt" exists with students formatted as "First Last ID")
    print("\nImporting students from 'students.txt'...")
    group.import_data("students.txt")

    # Display attendance after import
    print("\nAttendance after import:")
    group.display_attendance()


# Run test
test_group_attendance()
