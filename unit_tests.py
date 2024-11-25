import pytest
from group import Group
from student import Student

def test_add_student():
    #Given
    group = Group("Test Group")
    student = Student("Jan", "Kowalski", 1)
    #When
    group.add_student(student)
    #Then
    assert student in group.attendance_list
    assert group.attendance_list[student] == 0

def test_mark_student_attendance():
    #Given
    group = Group("Test Group")
    student = Student("Anna", "Kowalska", 2)
    group.add_student(student)
    #When
    group.mark_student_attendance(student, present=True)
    #Then
    assert group.attendance_list[student] == 1

def test_edit_attendance():
    #Given
    group = Group("Test Group")
    student = Student("Adam", "Nowak", 3)
    group.add_student(student)
    group.mark_student_attendance(student, present=True)
    #When
    group.edit_attendance(student, present=False)
    #Then
    assert group.attendance_list[student] == 0

def test_import_data(tmp_path):
    #Given
    data = "Jan Kowalski 1\nAnna Kowalska 2"
    test_file = tmp_path / "students.txt"
    test_file.write_text(data)
    #When
    group = Group("Test Group")
    group.import_data(str(test_file))
    #Then
    assert len(group.attendance_list) == 2
    assert any(student.student_id == 1 for student in group.attendance_list.keys())
    assert any(student.student_id == 2 for student in group.attendance_list.keys())

def test_export_data(tmp_path):
    #Given
    group = Group("Test Group")
    student1 = Student("Jan", "Kowalski", 1)
    student2 = Student("Anna", "Kowalska", 2)
    group.add_student(student1)
    group.add_student(student2)
    export_file = tmp_path / "attendance.txt"
    #When
    group.export_data(str(export_file))
    #Then
    exported_data = export_file.read_text()
    assert "Jan Kowalski 1" in exported_data
    assert "Anna Kowalska 2" in exported_data

def test_display_attendance(capsys):
    #Given
    group = Group("Test Group")
    student = Student("Jan", "Kowalski", 1)
    group.add_student(student)
    group.mark_student_attendance(student, present=True)
    #When
    group.display_attendance()
    #Then
    captured = capsys.readouterr()
    assert "Attendance for group: Test Group" in captured.out
    assert "Jan Kowalski 1: Present" in captured.out
