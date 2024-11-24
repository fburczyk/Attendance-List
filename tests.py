import unittest
from student import Student
from group import Group
import os


class SaveTest(unittest.TestCase):
    def test_save(self):
        # Given
        test_group1 = Group("Test Group 1")
        test_student1 = Student("John", "Doe", 12345)
        test_student2 = Student("Jane", "Smith", 54321)
        test_group1.add_student(test_student1)
        test_group1.add_student(test_student2)
        test_group1.mark_student_attendance(test_student1, True)
        test_group1.mark_student_attendance(test_student2, False)

        # When
        test_group1.export_data("test_group1")

        # Then
        self.assertTrue(os.path.exists("test_group1.txt"))

        # When
        with open("test_group1.txt", "r") as file:
            content = file.readlines()

        # Want
        expected_content = [
            f"{test_student1} - Present\n",
            f"{test_student2} - Absent\n"
        ]

        # Then
        self.assertEqual(content, expected_content)  # add assertion here

        os.remove("test_group1.txt")


class ImportTest(unittest.TestCase):
    def test_import(self):
        # Given
        test_group2 = Group("Test Group 2")

        # When
        test_group2.import_data("test_group2.txt")

        expected_content = {
            Student("John", "Doe", 12345): 0,
            Student("Jane", "Smith", 54321): 0
        }

        # Then
        self.assertDictEqual(test_group2.attendance_list, expected_content)


class StudentTests(unittest.TestCase):
    def test_student_creation(self):
        # When
        student = Student("John", "Doe", 12345)

        # Then
        self.assertEqual(student.first_name, "John")
        self.assertEqual(student.last_name, "Doe")
        self.assertEqual(student.student_id, 12345)

    def test_student_update(self):
        # Given
        student = Student("John", "Doe", 12345)

        # When
        student.update_info("Johnny", "Doe")

        # Then
        self.assertEqual(student.first_name, "Johnny")
        self.assertEqual(student.last_name, "Doe")

    def test_student_equality(self):
        # Given
        student1 = Student("John", "Doe", 12345)
        student2 = Student("Jane", "Smith", 12345)

        # Then
        self.assertTrue(student1 == student2)

    def test_student_inequality(self):
        # Given
        student1 = Student("John", "Doe", 12345)
        student2 = Student("Jane", "Smith", 54321)

        # Then
        self.assertFalse(student1 == student2)


class AttendanceTests(unittest.TestCase):
    def test_mark_attendance(self):
        # Given
        test_group = Group("Test Group")
        student1 = Student("John", "Doe", 12345)
        student2 = Student("Jane", "Smith", 54321)
        test_group.add_student(student1)
        test_group.add_student(student2)

        # When
        test_group.mark_student_attendance(student1, True)
        test_group.mark_student_attendance(student2, False)

        # Then
        self.assertEqual(test_group.attendance_list[student1], 1)
        self.assertEqual(test_group.attendance_list[student2], 0)

    def test_edit_attendance(self):
        # Given
        test_group = Group("Test Group")
        student1 = Student("John", "Doe", 12345)
        student2 = Student("Jane", "Smith", 54321)
        test_group.add_student(student1)
        test_group.add_student(student2)
        test_group.mark_student_attendance(student1, True)
        test_group.mark_student_attendance(student2, False)

        # When
        test_group.edit_attendance(student1, False)
        test_group.edit_attendance(student2, True)

        # Then
        self.assertEqual(test_group.attendance_list[student1], 0)
        self.assertEqual(test_group.attendance_list[student2], 1)


if __name__ == '__main__':
    unittest.main()
