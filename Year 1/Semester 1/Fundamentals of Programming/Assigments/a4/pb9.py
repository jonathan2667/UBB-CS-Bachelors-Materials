def has_common_digit(number1, number2):
    number_of_digits_first_number = set(str(number1))
    for digit in str(number2):
        if digit in number_of_digits_first_number:
            return True
    return False

def backtrack_iterative_to_find_subsets_with_ascending_order_and_same_digit(input_list):
    number_elements = len(input_list)
    iterative_subsets_results = []
    stack_iterative_backtracking_to_find_subsets_with_ascending_order_and_same_digit = [] #stack

    stack_iterative_backtracking_to_find_subsets_with_ascending_order_and_same_digit.append((0, []))

    while stack_iterative_backtracking_to_find_subsets_with_ascending_order_and_same_digit:
        index_current_iteration, current_subset = stack_iterative_backtracking_to_find_subsets_with_ascending_order_and_same_digit.pop()

        if len(current_subset) >= 2:
            if all(has_common_digit(current_subset[i], current_subset[i + 1]) for i in range(len(current_subset) - 1)):
                iterative_subsets_results.append(current_subset)

        for i in range(index_current_iteration, number_elements):
            if not current_subset or input_list[i] > current_subset[-1]:
                stack_iterative_backtracking_to_find_subsets_with_ascending_order_and_same_digit.append((i + 1, current_subset + [input_list[i]]))

    return iterative_subsets_results


def backtrack_recursive_to_find_subsets_with_ascending_order_and_same_digit(subset_generated, start_index, input_list, result_found_subsets):
    if len(subset_generated) >= 2 and all(has_common_digit(subset_generated[i], subset_generated[i + 1]) for i in range(len(subset_generated) - 1)):
        result_found_subsets.append(subset_generated[:])

    for i in range(start_index, len(input_list)):
        subset_generated.append(input_list[i])
        backtrack_recursive_to_find_subsets_with_ascending_order_and_same_digit(subset_generated, i + 1, input_list, result_found_subsets)
        subset_generated.pop()


def generate_subsets_with_backtracking_recursive_with_ascending_order_and_same_digit(input_list):
    recursive_subsets = []
    backtrack_recursive_to_find_subsets_with_ascending_order_and_same_digit([], 0, input_list, recursive_subsets)
    return recursive_subsets

if __name__ == "__main__":
    print("Iterative Backtracking:")
    input_list = [12, 23, 45, 67, 33, 78, 89]
    result_subsets = backtrack_iterative_to_find_subsets_with_ascending_order_and_same_digit(input_list)
    for subset in result_subsets:
        print(subset)

    print("Recursive Backtracking:")
    input_list = [12, 23, 45, 67, 33, 78, 89]
    result_subsets = generate_subsets_with_backtracking_recursive_with_ascending_order_and_same_digit(input_list)
    for subset in result_subsets:
        print(subset)
