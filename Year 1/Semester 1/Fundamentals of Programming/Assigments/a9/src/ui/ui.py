from src.services.student_service import StudentService
from src.services.discipline_service import DisciplineService
from src.services.grade_service import GradeService
from src.services.UndoService import UndoService

MANAGE_STUDENT = "1"
MANAGE_DISCIPLINES = "2"
GRADE_STUDENT = "3"
SEARCH_STUDENT = "4"
SEARCH_DISCIPLINE = "5"
DISPLAY_STATISTICS = "6"
UNDO = "7"
REDO = "8"
EXIT = "9"

ADD_STUDENT = "1"
UPDATE_INFORMATION_ABOUT_STUDENT = "2"
REMOVE_STUDENT = "3"
LIST_STUDENTS = "4"

ADD_DISCIPLINE = "1"
UPDATE_INFORMATION_ABOUT_DISCIPLINE = "2"
REMOVE_DISCIPLINE = "3"
LIST_DISCIPLINES = "4"

DISPLAY_GRADES = "1"
ADD_GRADE = "2"

SEARCH_BY_ID = "1"
SEARCH_BY_NAME = "2"

DISPLAY_FAILING_STUDENTS = "1"
DISPLAY_BEST_STUDENTS = "2"
DISPLAY_DISCIPLINES_WITH_AT_LEAST_ONE_GRADE = "3"

ID = 0
AVERAGE = 1

class UI:
    def __init__(self, repository):
        self.undo_service = UndoService()
        self.__student_service = StudentService(repository, self.undo_service)
        self.__discipline_service = DisciplineService(repository, self.undo_service)
        self.__grade_service = GradeService(repository, self.undo_service)
        self.__grade_service.generate_random_grades(self.__student_service.get_all_student_ids(), self.__discipline_service.get_all_discipline_ids())

    def print_ui(self):
        try:
            while True:
                print("Choose one of the following options: ")
                print("1. Manage students")
                print("2. Manage disciplines")
                print("3. Grade a student")
                print("4. Search for students")
                print("5. Search for disciplines")
                print("6. Display statistics")
                print("7. Undo")
                print("8. Redo")
                print("9. Exit")

                option_menu = input("Choose your option: ")

                if option_menu == MANAGE_STUDENT:
                    print("1. Add a student")
                    print("2. Update information about the student")
                    print("3. Remove student")
                    print("4. List all students")

                    option_submenu = input("Choose your option: ")
                    if option_submenu == ADD_STUDENT:
                        id = int(input("What is the ID of the student? "))
                        name = input("What is the name of the student? ")
                        self.__student_service.add_student(id, name)
                    elif option_submenu == UPDATE_INFORMATION_ABOUT_STUDENT:
                        id = int(input("What is the ID of the student? "))
                        name = input("What is the name of the student? ")
                        self.__student_service.update_student(id, name)
                    elif option_submenu == REMOVE_STUDENT:
                        id = int(input("What is the ID of the student? "))
                        self.__grade_service.delete_gades_based_on_student(id)
                        self.__student_service.delete_student(id)
                    elif option_submenu == LIST_STUDENTS:
                        students = self.__student_service.get_all_students()
                        for student in students:
                            print(student)
                    else:
                        print("Input not valid!")

                elif option_menu == MANAGE_DISCIPLINES:
                    print("1. Add a discipline")
                    print("2. Update information about the discipline")
                    print("3. Remove discipline")
                    print("4. List all disciplines")

                    option_submenu = input("Choose your option: ")
                    if option_submenu == ADD_DISCIPLINE:
                        id = int(input("What is the ID of the discipline? "))
                        name = input("What is the name of the discipline? ")
                        self.__discipline_service.add_discipline(id, name)
                    elif option_submenu == UPDATE_INFORMATION_ABOUT_DISCIPLINE:
                        id = int(input("What is the ID of the discipline? "))
                        name = input("What is the name of the discipline? ")
                        self.__discipline_service.update_discipline(id, name)
                    elif option_submenu == REMOVE_DISCIPLINE:
                        id = int(input("What is the ID of the discipline? "))
                        self.__grade_service.delete_grades_based_on_discipline(id)
                        self.__discipline_service.delete_discipline(id)
                    elif option_submenu == LIST_DISCIPLINES:
                        disciplines = self.__discipline_service.get_all_disciplines()
                        for discipline in disciplines:
                            print(discipline)
                    else:
                        print("Input not valid!")

                elif option_menu == GRADE_STUDENT:
                    print("1. Display all the grades")
                    print("2. Add a grade")

                    option_submenu = input("Choose your option: ")
                    if option_submenu == DISPLAY_GRADES:
                        grades = self.__grade_service.get_all_grades()
                        for grade in grades:
                            print(grade)

                    elif option_submenu == ADD_GRADE:
                        discipline_id = int(input("What is the ID of the discipline?"))
                        self.__discipline_service.check_if_discipline_is_valid(discipline_id)

                        student_id = int(input("What is the ID of the student?"))
                        self.__student_service.check_if_student_is_valid(student_id)

                        grade_value = float(input("What is the grade of the student?"))
                        self.__grade_service.add_grade(discipline_id, student_id, grade_value)

                        grades = self.__grade_service.get_all_grades()
                        for grade in grades:
                            print(grade)

                elif option_menu == SEARCH_STUDENT:
                    print("1. Search student based on id")
                    print("2. Search student based on name")

                    option_submenu = input("Chooose your option")
                    if option_submenu == SEARCH_BY_ID:
                        id = int(input("What is the id of the student?"))
                        students = self.__student_service.search_student_based_on_id(id)
                        for student in students:
                            print(student)
                    elif option_submenu == SEARCH_BY_NAME:
                        name = input("What is the name of the student?")
                        students = self.__student_service.search_student_based_on_name(name)
                        for student in students:
                            print(students)
                    else:
                        print("Input non-valid")

                elif option_menu == SEARCH_DISCIPLINE:
                    print("1. Search discipline based on id")
                    print("2. Search discipline based on name")
                    option_submenu = input("Choose your option: ")

                    if option_submenu == SEARCH_BY_ID:
                        id = int(input("What is the ID of the discipline? "))
                        disciplines = self.__discipline_service.search_discipline_based_on_id(id)
                        for disc in disciplines:
                            print(disc)
                    elif option_submenu == SEARCH_BY_NAME:
                        name = input("What is the name of the discipline? ")
                        disciplines = self.__discipline_service.search_discipline_based_on_name(name)
                        for discipline in disciplines:
                            print(discipline)
                    else:
                        print("Your input is not valid")

                elif option_menu == DISPLAY_STATISTICS:
                    print("1. Display all the students that are failing at one or more disciplines")
                    print("2. Display the best students, based on aggregate average")
                    print("3. Display all the disciplines based on the grades received by the students")
                    option_submenu = input("Choose your option: ")

                    if option_submenu == DISPLAY_FAILING_STUDENTS:
                        failing_students = self.__grade_service.failing_students()
                        for object in failing_students:
                            print(self.__student_service.get_student_by_id(object[ID][ID]).name, self.__discipline_service.get_discipline_by_id(object[ID][AVERAGE]).name, object[AVERAGE])
                    elif option_submenu == DISPLAY_BEST_STUDENTS:
                        best_students = self.__grade_service.best_students()
                        for student in best_students:
                            print(self.__student_service.get_student_by_id(student), best_students[student])
                    elif option_submenu == DISPLAY_DISCIPLINES_WITH_AT_LEAST_ONE_GRADE:
                        descending_average_disciplines = self.__grade_service.descending_avg_disciplines()
                        for desc in descending_average_disciplines:
                            print(self.__discipline_service.get_discipline_by_id(desc), descending_average_disciplines[desc])
                    else:
                        print("Your input is not valid")
                elif option_menu == UNDO:
                    self.undo_service.undo()
                elif option_menu == REDO:
                    self.undo_service.redo()
                elif option_menu == EXIT:
                    return
                else:
                    print("Your input is not valid")
        except Exception as ex:
            print(ex)
