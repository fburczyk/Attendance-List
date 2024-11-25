import pytest
import os
from student import Student
from group import Group


def test_student_initialization():
    #Test initialization of a Student object
    student = Student("John", "Smith", 1)
    assert student.first_name == "John"
    assert student.last_name == "Smith"
    assert student.student_id == 1
    assert str(student) == "John Smith 1"


def test_student_equality():
    #Test equality of Student objects based on student_id.
    student1 = Student("John", "Smith", 1)
    student2 = Student("Jane", "Black", 1)
    student3 = Student("Alice", "Brown", 3)

    assert student1 == student2
    assert student1 != student3

def test_update_info():
    #Test updating Student information.
    student = Student("John", "Smith", 1)
    student.update_info("Jonathan", "Smith")
    assert student.first_name == "Jonathan"
    assert student.last_name == "Smith"
@pytest.fixture
def setup_group():
    #Setting up new group of students.
    group = Group("Comp_Sci_24")
    student1 = Student("John", "Smith", 1)
    student2 = Student("Jane", "Black", 2)
    group.add_student(student1)
    group.add_student(student2)
    return group, student1, student2


def test_add_student(setup_group):
    #Test adding a student to the Group.
    group, student1, student2 = setup_group
    assert student1 in group.attendance_list
    assert student2 in group.attendance_list
    assert group.attendance_list[student1] == 0
    assert group.attendance_list[student2] == 0


def test_mark_student_attendance(setup_group):
    #Test marking a student's attendance.
    group, student1, student2 = setup_group
    group.mark_student_attendance(student1, True)
    group.mark_student_attendance(student2, False)
    assert group.attendance_list[student1] == 1
    assert group.attendance_list[student2] == 0


def test_update_student_in_group(setup_group):
    #Test updating student information within the group.
    group, student1, _ = setup_group
    group.update_student_in_group(student1, "Jonathan", "Smith")
    assert student1.first_name == "Jonathan"
    assert student1.last_name == "Smith"


def test_edit_attendance(setup_group):
    #Test editing a student's attendance.
    group, student1, _ = setup_group
    group.edit_attendance(student1, True)
    assert group.attendance_list[student1] == 1
    group.edit_attendance(student1, False)
    assert group.attendance_list[student1] == 0


def test_import_data():
    #Test importing students from a file.
    group = Group("Comp_Sci_24")
    file_name = "students.txt"

    with open(file_name, "w") as file:
        file.write("Alice Johnson 3\nBob Brown 4\n")

    group.import_data(file_name)
    os.remove(file_name)

    new_student1 = Student("Alice", "Johnson", 3)
    new_student2 = Student("Bob", "Brown", 4)

    assert new_student1 in group.attendance_list
    assert new_student2 in group.attendance_list
    assert group.attendance_list[new_student1] == 0
    assert group.attendance_list[new_student2] == 0


def test_export_data(setup_group):
    #Test exporting attendance to a file.
    group, student1, student2 = setup_group

    group.mark_student_attendance(student1, True)
    group.mark_student_attendance(student2, False)

    filename = "test_attendance_list.txt"
    group.export_data(filename)

    with open(filename, "r") as file:
        content = file.read()
        assert "John Smith 1 - Present" in content
        assert "Jane Black 2 - Absent" in content

    os.remove(filename)