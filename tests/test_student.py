import unittest
from student import Student


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


if __name__ == '__main__':
    unittest.main()
