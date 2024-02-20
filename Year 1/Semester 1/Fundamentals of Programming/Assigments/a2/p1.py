#sort selection

import random

def print_numbers(Numbers_list, numbers_of_numbers_to_be_generated):
    print("The numbers of the list are:")
    for i in range(0, numbers_of_numbers_to_be_generated):
        print(Numbers_list[i], end=" ")
    print("\n")

def generate_numbers(Numbers_list, numbers_of_numbers_to_be_generated) :
    for i in range(0, numbers_of_numbers_to_be_generated):
        random_number = random.randint(1, 100)
        Numbers_list.append(random_number)

    print_numbers(Numbers_list, numbers_of_numbers_to_be_generated)


def selection_sort(Numbers_list, number_steps):
    counter_steps = 0
    for i in range(len(Numbers_list)):
        min_index = i
        counter_steps += 1

        for j in range(i + 1, len(Numbers_list)):
            if Numbers_list[min_index] > Numbers_list[j]:
                min_index = j

        Numbers_list[i], Numbers_list[min_index] = Numbers_list[min_index], Numbers_list[i]

        if  counter_steps % number_steps == 0:
            print_numbers(Numbers_list, numbers_of_numbers_to_be_generated)

def shell_sort(Numbers_list, number_steps):
    counter_steps = 0
    interval = len(Numbers_list) // 2

    while interval > 0:
        counter_steps += 1
        for i in range(interval, len(Numbers_list)):
            next_minimum_value = Numbers_list[i]
            j = i
            while j >= interval and Numbers_list[j -interval] > next_minimum_value:
                Numbers_list[j] = Numbers_list[j - interval]

                counter_steps += 1
                if counter_steps % number_steps == 0:
                    print_numbers(Numbers_list, numbers_of_numbers_to_be_generated)

                j -= interval

            Numbers_list[j] = next_minimum_value
        interval //= 2



if __name__ == '__main__':
    numbers_of_numbers_to_be_generated = int(input("How many numbers to be generated?"))

    Numbers_list = []
    generate_numbers(Numbers_list, numbers_of_numbers_to_be_generated)

    number_steps = int(input("After how many steps would you like to see the results for the first algo(Selection)"))

    selection_sort(Numbers_list, number_steps)

    random.shuffle(Numbers_list)

    print("The new list after shuffling! : ")
    print_numbers(Numbers_list, numbers_of_numbers_to_be_generated)

    number_steps = int(input("After how many steps would you like to see the results for the second algo(Shell)"))

    shell_sort(Numbers_list, number_steps)

    print_numbers(Numbers_list, numbers_of_numbers_to_be_generated)