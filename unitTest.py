import pytest
import os
from student import Student
from group import Group


# Tests for Student Class
def test_student_initialization():
    """Test student initialization."""
    student = Student("John", "Doe", 12345)
    assert student.first_name == "John"
    assert student.last_name == "Doe"
    assert student.student_id == 12345
    assert str(student) == "John Doe 12345"


def test_student_equality():
    """Test student equality based on student_id."""
    student1 = Student("John", "Doe", 12345)
    student2 = Student("Jane", "Smith", 12345)
    student3 = Student("Alice", "Brown", 67890)
    assert student1 == student2  # Same student_id
    assert student1 != student3  # Different student_id


def test_student_hashing():
    """Test student objects as dictionary keys."""
    student1 = Student("John", "Doe", 12345)
    student2 = Student("Jane", "Smith", 12345)
    student3 = Student("Alice", "Brown", 67890)

    attendance = {student1: "Present", student3: "Absent"}
    assert attendance[student2] == "Present"  # Same student_id as student1
    assert attendance[student3] == "Absent"


def test_update_info():
    """Test updating student info."""
    student = Student("John", "Doe", 12345)
    student.update_info("Jonathan", "Doe")
    assert student.first_name == "Jonathan"
    assert student.last_name == "Doe"


# Tests for Group Class
@pytest.fixture
def setup_group():
    """Fixture to set up a group and sample students."""
    group = Group("Computer Science 2024")
    student1 = Student("John", "Doe", 12345)
    student2 = Student("Jane", "Smith", 54321)
    group.add_student(student1)
    group.add_student(student2)
    return group, student1, student2


def test_add_student(setup_group):
    """Test adding a student to the group."""
    group, student1, student2 = setup_group
    assert student1 in group.attendance_list
    assert student2 in group.attendance_list
    assert group.attendance_list[student1] == 0
    assert group.attendance_list[student2] == 0


def test_mark_student_attendance(setup_group):
    """Test marking student attendance."""
    group, student1, student2 = setup_group
    group.mark_student_attendance(student1, True)
    group.mark_student_attendance(student2, False)
    assert group.attendance_list[student1] == 1
    assert group.attendance_list[student2] == 0


def test_update_student_in_group(setup_group):
    """Test updating a student's information."""
    group, student1, _ = setup_group
    group.update_student_in_group(student1, "Jonathan", "Doe")
    assert student1.first_name == "Jonathan"
    assert student1.last_name == "Doe"


def test_edit_attendance(setup_group):
    """Test editing student attendance."""
    group, student1, _ = setup_group
    group.edit_attendance(student1, True)
    assert group.attendance_list[student1] == 1
    group.edit_attendance(student1, False)
    assert group.attendance_list[student1] == 0


def test_import_data():
    """Test importing students from a file."""
    group = Group("Computer Science 2024")
    file_name = "students.txt"

    # Create a mock import file
    with open(file_name, "w") as file:
        file.write("Alice Johnson 67890\nBob Brown 98765")

    group.import_data(file_name)
    os.remove(file_name)

    new_student1 = Student("Alice", "Johnson", 67890)
    new_student2 = Student("Bob", "Brown", 98765)

    assert new_student1 in group.attendance_list
    assert new_student2 in group.attendance_list
    assert group.attendance_list[new_student1] == 0
    assert group.attendance_list[new_student2] == 0


def test_export_data(setup_group):
    """Test exporting attendance data to a file."""
    group, student1, student2 = setup_group

    # Mark attendance for the students
    group.mark_student_attendance(student1, True)
    group.mark_student_attendance(student2, False)

    filename = "test_attendance_list.txt"
    group.export_data(filename)

    # Verify the file was created and contains the correct data
    with open(filename, "r") as file:
        content = file.read()
        assert "John Doe 12345 - Present" in content
        assert "Jane Smith 54321 - Absent" in content
    os.remove(filename)