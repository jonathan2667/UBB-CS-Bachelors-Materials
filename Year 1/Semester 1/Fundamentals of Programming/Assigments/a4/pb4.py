#PROBLEM NUMBER 4

# Given a grid of numbers, find maximum length Snake sequence and print it.
# If multiple snake sequences exists with the maximum length, print any one of them.
#
# A snake sequence is made up of adjacent numbers in the grid such that for each number,
# the number on the right or the number below it is +1 or -1 its value.
#
# For example, if you are at location (x, y) in the grid, you can either move right i.e. (x, y+1) if that number is ± 1 or move down
# i.e. (x+1, y) if that number is ± 1.
#

def print_intermediate_results_of_dynamic_programming_matrix(dynamic_programming_matrix_maximum_length_of_snake_sequence):
    print("Intermediate result DP:\n")
    for i in range(number_rows_matrix + 1):
        print("")
        for j in range(number_columns_matrix + 1):
            print(dynamic_programming_matrix_maximum_length_of_snake_sequence[i][j], end ="")

    print("\n")

def find_longest_snake_sequence_using_dynamic_programming(initial_matrix_snake, number_rows_of_matrix, number_columns_of_matrix):
    visited_previous_positions_of_matrix = {}
    dynamic_programming_matrix_for_maximum_length_of_snake_sequence = [[1 for _ in range(number_columns_of_matrix + 1)]
                                  for _ in range(number_rows_of_matrix + 1)]   #

    max_length, coordinate_position_of_maximum_length = 0, (0, 0)

    for i in range(number_rows_of_matrix + 1):
        for j in range(number_columns_of_matrix + 1):
            left_position_in_snake_matrix, up_positon_in_snake_matrix = 0, 0
            previous_position = "initial"

            if i > 0 and verify_if_is_adjacent_element(initial_matrix_snake, i, j, i - 1, j):
                up_positon_in_snake_matrix = dynamic_programming_matrix_for_maximum_length_of_snake_sequence[i - 1][j]
            if j > 0 and verify_if_is_adjacent_element(initial_matrix_snake, i, j, i, j - 1):
                left_position_in_snake_matrix = dynamic_programming_matrix_for_maximum_length_of_snake_sequence[i][j - 1]

            if up_positon_in_snake_matrix!= 0 and up_positon_in_snake_matrix >= left_position_in_snake_matrix:
                previous_position = f"{i - 1} {j}"
            elif left_position_in_snake_matrix != 0:
                previous_position = f"{i} {j - 1}"

            current_position_in_snake_matrix = f"{i} {j}"
            visited_previous_positions_of_matrix[current_position_in_snake_matrix] = previous_position
            dynamic_programming_matrix_for_maximum_length_of_snake_sequence[i][j] = dynamic_programming_matrix_for_maximum_length_of_snake_sequence[i][j] + max(up_positon_in_snake_matrix, left_position_in_snake_matrix)

            if dynamic_programming_matrix_for_maximum_length_of_snake_sequence[i][j] >= max_length:
                max_length = dynamic_programming_matrix_for_maximum_length_of_snake_sequence[i][j]
                coordinate_position_of_maximum_length = (i, j)

            print_intermediate_results_of_dynamic_programming_matrix(dynamic_programming_matrix_for_maximum_length_of_snake_sequence)

    snake_values_represented_in_initial_matrix, snake_positions_coordinates = reconstruct_snake_path_for_dynamic_programming(initial_matrix_snake, visited_previous_positions_of_matrix, coordinate_position_of_maximum_length)
    return snake_values_represented_in_initial_matrix, snake_positions_coordinates


def verify_if_is_adjacent_element(initial_matrix_that_contains_snake_path, coordinates_i1, coordinates_j1, coordinates_i2, coordinates_j2):
    return coordinates_i1 > 0 and abs(initial_matrix_that_contains_snake_path[coordinates_i1][coordinates_j1] - initial_matrix_that_contains_snake_path[coordinates_i2][coordinates_j2]) == 1

def reconstruct_snake_path_for_dynamic_programming(matrix_reconstruction_path, visited_previous_positions_of_matrix, coordinate_position_of_maximum_length):
    snake_values_represented_in_initial_matrix = []
    snake_positions_coordinates = []
    snake_values_represented_in_initial_matrix.append(matrix_reconstruction_path[coordinate_position_of_maximum_length[0]][coordinate_position_of_maximum_length[1]])
    check_if_found = 'found'
    current_position = f"{coordinate_position_of_maximum_length[0]} {coordinate_position_of_maximum_length[1]}"

    while check_if_found == 'found':
        if visited_previous_positions_of_matrix[current_position] == 'initial':
            snake_positions_coordinates.insert(0, current_position)
            check_if_found = 'end'
            continue

        current_indices = visited_previous_positions_of_matrix[current_position].split()
        x_axix_indice = int(current_indices[0])
        y_axis_indice = int(current_indices[1])
        snake_values_represented_in_initial_matrix.insert(0, matrix_reconstruction_path[x_axix_indice][y_axis_indice])
        snake_position = f"{x_axix_indice} {y_axis_indice}"
        snake_positions_coordinates.insert(0, current_position)
        current_position = visited_previous_positions_of_matrix[current_position]

    return snake_values_represented_in_initial_matrix, snake_positions_coordinates


def findSnakeSequence_non_optimized_version(initial_matrix_snake):
    def verify_if_is_adjacent_element(i_current_coordonate, y_current_coordonate, prev_value):
        return 0 <= i_current_coordonate < len(initial_matrix_snake) and\
               0 <= y_current_coordonate < len(initial_matrix_snake[0]) and\
               abs(initial_matrix_snake[i_current_coordonate][y_current_coordonate] - prev_value) == 1

    def depth_first_search_from_coordinate_x_y(coordinate_x, coordinate_y, current_sequence_path, path):
        nonlocal max_snake_sequence_length, snake_sequence_path

        if current_sequence_path > max_snake_sequence_length:
            max_snake_sequence_length = current_sequence_path
            snake_sequence_path = path[:]

        for direction_x, direction_y in [(0, 1), (1, 0)]:
            new_coordinate_x, new_coordinate_y = coordinate_x + direction_x, coordinate_y + direction_y

            if verify_if_is_adjacent_element(new_coordinate_x, new_coordinate_y, initial_matrix_snake[coordinate_x][coordinate_y]):
                depth_first_search_from_coordinate_x_y(new_coordinate_x, new_coordinate_y, current_sequence_path + 1,
                                                       path + [(new_coordinate_x, new_coordinate_y, initial_matrix_snake[new_coordinate_x][new_coordinate_y])])

    max_snake_sequence_length = 0
    snake_sequence_path = []

    for i in range(len(initial_matrix_snake)):
        for j in range(len(initial_matrix_snake[0])):
            depth_first_search_from_coordinate_x_y(i, j, 1, [(i, j, initial_matrix_snake[i][j])])

    return max_snake_sequence_length, snake_sequence_path

if __name__ == "__main__":
    initial_matrix_snake = [[9, 6, 5, 2],
                            [8, 7, 6, 5],
                            [7, 3, 1, 6],
                            [1, 1, 10, 7]]


    print("\nNON OPTIMIZED SOLUTION:\n")
    max_snake_sequence_length, snake_sequence_path = findSnakeSequence_non_optimized_version(initial_matrix_snake)
    print("Maximum length of Snake sequence is:", max_snake_sequence_length - 1)
    print("Snake sequence is:")
    for x, y, value in snake_sequence_path:
        print(f"{value} ({x}, {y})")



    print("\nDP SOLUTION:\n\n")

    number_rows_matrix = 3
    number_columns_matrix = 3
    maximum_length_snake_sequence = find_longest_snake_sequence_using_dynamic_programming(initial_matrix_snake, number_rows_matrix, number_columns_matrix)
    for i in range(len(maximum_length_snake_sequence[0])):
        print(maximum_length_snake_sequence[0][i], ",", maximum_length_snake_sequence[1][i].split())

    print("\nMaximum length of Snake sequence is:", len(maximum_length_snake_sequence[0]) - 1)



#A5 - pb 2, 13