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

if __name__ == '__main__':
    unittest.main()
