class Student:
    def __init__(self, first_name: str, last_name: str, student_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.student_id}'

    def __eq__(self, other):
        """Check equality between two Student objects based on their id."""
        return self.student_id == other.student_id

    def __hash__(self):
        """Allows to use student object as dict key"""
        return hash(self.student_id)

    def update_info(self, first_name: str, last_name: str):
        """Update student info"""
        self.first_name = first_name
        self.last_name = last_name


