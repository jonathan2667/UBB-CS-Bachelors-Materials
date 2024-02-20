import sqlite3
from sqlite3 import Error
from src.domain.student import Student
from src.repository.MemoryRepository import MemoryRepository


class DataBaseRepository(MemoryRepository):
    def __init__(self, db_path="students.sqlite"):
        super(DataBaseRepository, self).__init__()
        self._db_path = db_path
        self._stack_of_all_operations_done_to_student_list = []
        self._connection = self._create_connection_to_database()
        self._create_table()

    def _create_connection_to_database(self):
        connection_to_database = None
        try:
            connection_to_database = sqlite3.connect(self._db_path)
        except Error as exception_name:
            return exception_name
        return connection_to_database

    def _execute_query(self, query):
        cursor = self._connection.cursor()
        try:
            cursor.execute(query)
            self._connection.commit()
        except Error as exception_name:
            raise exception_name(exception_name)

    def _create_table(self):
        create_students_tabel = """
      CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        gr INTEGER
      );
      """
        self._execute_query(create_students_tabel)

    def _execute_read_query(self, query):
        cursor = self._connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def add_new_student(self, new_student: Student, student_not_already_added_to_list: bool):
        check_existing_id = self._execute_read_query("SELECT * from students WHERE id=" + str(new_student.id))
        if len(check_existing_id) == 0:
            add_student = "INSERT INTO students (id, name, gr) VALUES (" + str(
                new_student.id) + ", '" + new_student.name + "', " + str(new_student.group) + ")"
            self._execute_query(add_student)
            delete_student = ["DELETE * from students WHERE id=" + str(new_student.id)]
            self._stack_of_all_operations_done_to_student_list.append(delete_student)

    def get_list_with_all_students(self):
        sql_select_querry = "SELECT * from students"
        select_students = self._execute_read_query(sql_select_querry)
        return select_students

    def filter_students_according_to_group(self, group: int):
        undo_operations = []
        sql_select_querry = "SELECT * from students WHERE gr=" + str(group)
        select_students = self._execute_read_query(sql_select_querry)
        for student_object in select_students:
            undo_operations.append("INSERT INTO students (id, name, gr) VALUES " + str(student_object) + ")")
        select_students_query = "DELETE FROM students WHERE gr = " + str(group)
        self._execute_query(select_students_query)
        self._stack_of_all_operations_done_to_student_list.append(undo_operations)

    def undo_last_operation(self):
        if len(self._stack_of_all_operations_done_to_student_list) > 0:
            operations_stack_without_last_element = self._stack_of_all_operations_done_to_student_list[-1]
            for current_operation in operations_stack_without_last_element:
                print(current_operation)
                self._execute_query(current_operation)