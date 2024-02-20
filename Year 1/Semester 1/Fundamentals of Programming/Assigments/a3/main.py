import random
import time

def print_numbers(Numbers_list, numbers_to_generate):
    print("The numbers of the list are:")
    for i in range(0, numbers_to_generate):
        print(Numbers_list[i], end=" ")
    print("\n")

def generate_numbers(Numbers_list, numbers_to_be_generated) :
    for i in range(0, numbers_to_be_generated):
        random_number = random.randint(1, 100)
        Numbers_list.append(random_number)

def selection_sort(Numbers_list):
    for i in range(len(Numbers_list)):
        min_index = i

        for j in range(i + 1, len(Numbers_list)):
            if Numbers_list[min_index] > Numbers_list[j]:
                min_index = j

        Numbers_list[i], Numbers_list[min_index] = Numbers_list[min_index], Numbers_list[i]

def shell_sort(Numbers_list):
    interval = len(Numbers_list) // 2
    while interval > 0:
        for i in range(interval, len(Numbers_list)):
            temp = Numbers_list[i]
            j = i
            while j >= interval and Numbers_list[j -interval] > temp:
                Numbers_list[j] = Numbers_list[j - interval]

                j -= interval

            Numbers_list[j] = temp
        interval //= 2

def check_time_selection_sort(Numbers_list, numbers_to_generate, length_array_gets_doubled):
    start_time = time.time()

    selection_sort(Numbers_list)

    end_time = time.time();

    print(length_array_gets_doubled, end_time - start_time)

    generate_numbers(Numbers_list, length_array_gets_doubled)

def check_time_shell_sort(Numbers_list, numbers_to_generate, length_array_gets_doubled):
    start_time = time.time()

    shell_sort(Numbers_list)

    end_time = time.time();

    print(length_array_gets_doubled, end_time - start_time)

    generate_numbers(Numbers_list, length_array_gets_doubled)

def best_case_selection_sort(Numbers_list, numbers_to_generate):
    print("for best case in selection sort, the list needs to be sorted at the beggining")

    length_array_gets_doubled = numbers_to_generate
    for i in range(0, 5):
        length_array_gets_doubled = length_array_gets_doubled * 2
        Numbers_list.sort()  # for best case, the list needs to be sorted at the beggining'
        check_time_selection_sort(Numbers_list, numbers_to_generate, length_array_gets_doubled)

def best_case_shell_sort(Numbers_list, numbers_to_generate):
    print("\nfor best case in shell sort, the list needs to be sorted at the beggining")

    length_array_gets_doubled = numbers_to_generate

    for i in range(0, 5):
        length_array_gets_doubled = length_array_gets_doubled * 2
        Numbers_list.sort()  # for best case, the list needs to be sorted at the beggining
        check_time_shell_sort(Numbers_list, numbers_to_generate, length_array_gets_doubled)


def best_case_both_algos(Numbers_list, numbers_to_generate):
    best_case_selection_sort(Numbers_list, numbers_to_generate)
    best_case_shell_sort(Numbers_list, numbers_to_generate)


def average_case_selection_sort(Numbers_list, numbers_to_generate):
    print("for average case in selection sort, the list needs to be partially sorted")
    length_array_gets_doubled = numbers_to_generate

    for i in range(0, 5):
        length_array_gets_doubled = length_array_gets_doubled * 2
        Numbers_list = sorted(Numbers_list[:len(Numbers_list) // 2]) + Numbers_list[
                                                                       len(Numbers_list) // 2:]  # we sort half
        check_time_selection_sort(Numbers_list, numbers_to_generate, length_array_gets_doubled)

def average_case_shell_sort(Numbers_list, numbers_to_generate):
    print("\nfor average case in shell sort, the list needs to be partially sorted")

    length_array_gets_doubled = numbers_to_generate

    for i in range(0, 5):
        length_array_gets_doubled = length_array_gets_doubled * 2
        Numbers_list = sorted(Numbers_list[:len(Numbers_list) // 2]) + Numbers_list[
                                                                       len(Numbers_list) // 2:]  # we sort half
        check_time_shell_sort(Numbers_list, numbers_to_generate, length_array_gets_doubled)

def average_case_both_algos(Numbers_list, numbers_to_generate):
    average_case_selection_sort(Numbers_list, numbers_to_generate)
    average_case_shell_sort(Numbers_list, numbers_to_generate)


def worst_case_selection_sort(Numbers_list, numbers_to_generate):
    print("for worst case in selection sort, the list needs to be reverse sorted")

    length_array_gets_doubled = numbers_to_generate

    for i in range(0, 5):
        length_array_gets_doubled = length_array_gets_doubled * 2
        Numbers_list.sort(reverse=True)  # for best case, the list needs to be sorted at the beggining
        check_time_selection_sort(Numbers_list, numbers_to_generate, length_array_gets_doubled)

def worst_case_shell_sort(Numbers_list, numbers_to_generate):
    print("\nfor worst case in shell sort, the list needs to be reverse sorted")

    length_array_gets_doubled = numbers_to_generate

    for i in range(0, 5):
        length_array_gets_doubled = length_array_gets_doubled * 2
        Numbers_list.sort(reverse=True)  # for best case, the list needs to be sorted at the beggining
        check_time_shell_sort(Numbers_list, numbers_to_generate, length_array_gets_doubled)


def worst_case_both_algorithms(Numbers_list, numbers_to_generate):
    worst_case_selection_sort(Numbers_list, numbers_to_generate)
    worst_case_shell_sort(Numbers_list, numbers_to_generate)

if __name__ == '__main__':
    case_sorting = int(input("Press 1 for for the best case, 2 for the average case and 3 for the worst case!"))
    numbers_to_generate = int(input("Choose the list lenght for the first list. The next 4 will each double every time."))

    Numbers_list = []
    generate_numbers(Numbers_list, numbers_to_generate)
    print_numbers(Numbers_list, numbers_to_generate)

    if case_sorting == 1:
        best_case_both_algos(Numbers_list, numbers_to_generate)
    elif case_sorting == 2:
        average_case_both_algos(Numbers_list, numbers_to_generate)
    else:
        worst_case_both_algo(Numbers_list, numbers_to_generate)