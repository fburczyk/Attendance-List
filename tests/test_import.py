import unittest
from student import Student
from group import Group


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


if __name__ == '__main__':
    unittest.main()
