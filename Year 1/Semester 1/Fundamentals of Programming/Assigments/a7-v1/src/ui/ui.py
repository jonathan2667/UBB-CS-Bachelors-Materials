from src.services.StudentService import StudentService

ADD_STUDENT = "1"
DISPLAY_STUDENT = "2"
REMOVE_STUDENT_FROM_GROUP = "3"
UNDO_LAST_OPERATION = "4"
EXIT = "5"
UI_STATEMENT = """
            1. Add a student
            2. Display all students
            3. Filter students by group. All the students from that respective group will be deleted
            4. Undo the last operation you have performed
            5. Exit the application
            """

class UI:
    def __init__(self, repo):
        self._student_service = StudentService(repo)

    def print_ui(self):
        while True:
            print(UI_STATEMENT)
            option = input("Choose your option: ")

            if option == ADD_STUDENT:
                id = int(input("What is the ID of the student? "))
                name = input("What is the name of the student? ")
                group = int(input("In which group is the student? "))
                self._student_service.add_student(id, name, group, True)

            elif option == DISPLAY_STUDENT:
                students = self._student_service.get_all_students()
                for stud in students:
                    print(stud)

            elif option == REMOVE_STUDENT_FROM_GROUP:
                group = int(input("Which group would you like to remove? "))
                self._student_service.filter_students(group)

            elif option == UNDO_LAST_OPERATION:
                self._student_service.undo_last_operation()

            elif option == EXIT:
                print("Goodbye")
                return
            else:
                print("Your input is not valid")