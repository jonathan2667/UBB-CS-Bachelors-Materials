from dataclasses import dataclass

@dataclass
class Student:
    _student_unique_id: int
    _student_name: str
    _student_group: int

    @property
    def id(self):
        return self._student_unique_id

    @property
    def name(self):
        return self._student_name

    @property
    def group(self):
        return self._student_group

    def __str__(self):
        return str(self.id) + " " + self.name + str(self.group)