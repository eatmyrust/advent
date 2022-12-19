def day_one():
    elf_calories = open("advent/inputs/day_1.txt").read().split("\n\n")

    print("----------------DAY ONE----------------")

    split_individual_cals = [split_cal_group.split("\n") for split_cal_group in elf_calories]
    summed_individual_cals = [sum([int(cal) for cal in split_cal_group if cal != ""]) for split_cal_group in split_individual_cals]
    summed_individual_cals.sort()

    print(f"Part 1: {summed_individual_cals[-1]}\nPart 2: {sum(summed_individual_cals[-3:])}")


def day_two():
    rps_games = open("advent/inputs/day_2.txt").read().split("\n")

    print("----------------DAY TWO----------------")

    rps_values = {"X": 1, "Y": 2, "Z": 3}
    rps_opponent_values = {"A": 1, "B": 2, "C": 3}
    winning_values = {"A": "Y", "B": "Z", "C": "X"}
    losing_values = {"A": "Z", "B": "X", "C": "Y"}
    equal_values = {"A": "X", "B": "Y", "C": "Z"}

    scores = [(rps_values[game[2:3]] + (6 if winning_values[game[0:1]] == game[2:3] else 3 if equal_values[game[0:1]] == game[2:3] else 0)) for game in rps_games if game != ""]
    updated_scores = [(rps_opponent_values[game[0:1]] + 3 if game[2:3] == "Y" else rps_values[winning_values[game[0:1]]] + 6 if game[2:3] == "Z" else rps_values[losing_values[game[0:1]]]) for game in rps_games if game != ""]

    print(f"Part 1: {sum(scores)}\nPart 2: {sum(updated_scores)}")


def day_three():
    rucksack_contents = open("advent/inputs/day_3.txt").read().split("\n")

    print("----------------DAY THREE----------------")
    print("Part 1:", sum([
        (
            ord(set(rucksack[0:len(rucksack)//2]).intersection(set(rucksack[len(rucksack)//2:len(rucksack)])).pop()) -
            (38 if ord(set(rucksack[0:len(rucksack)//2]).intersection(set(rucksack[len(rucksack)//2:len(rucksack)])).pop()) < 91
            else 96)
        )
            for rucksack
            in rucksack_contents
    ]))
    print("Part 2: ", sum([
        (
            ord(set(rucksack).intersection(set(rucksack_contents[i+1])).intersection(set(rucksack_contents[i+2])).pop()) -
            (38 if ord(set(rucksack).intersection(set(rucksack_contents[i+1])).intersection(set(rucksack_contents[i+2])).pop()) < 91
            else 96)
        )
            for i, rucksack
            in enumerate(rucksack_contents) if i % 3 == 0
        ]))


def day_four():
    cleanup_sections = open("advent/inputs/day_4.txt").read().split("\n")

    print("----------------DAY FOUR----------------")
    print("PART 1: ", sum([
        (1 if
            set(range(int(cleanup[0].split("-")[0]),int(cleanup[0].split("-")[1])+1)).issubset(set(range(int(cleanup[1].split("-")[0]),int(cleanup[1].split("-")[1])+1)))
            or set(range(int(cleanup[1].split("-")[0]),int(cleanup[1].split("-")[1])+1)).issubset(set(range(int(cleanup[0].split("-")[0]),int(cleanup[0].split("-")[1])+1)))
            else 0)
            for cleanup
            in [section.split(",") for section in cleanup_sections]
        ]))
    print("PART 2: ", sum([
        (1 if
            len(set(range(int(cleanup[0].split("-")[0]),int(cleanup[0].split("-")[1])+1)).intersection(set(range(int(cleanup[1].split("-")[0]),int(cleanup[1].split("-")[1])+1)))) > 0
            else 0)
            for cleanup
            in [section.split(",") for section in cleanup_sections]
        ]))


def day_five(part_one):
    stack, steps = tuple(open("advent/inputs/day_5.txt").read().split("\n\n"))

    stack_tracker = [
        [
            stack[(int(stack[-2:-1])*row*4)+(column*4+2)-1:(int(stack[-2:-1])*row*4)+(column*4+2)]
            for row
            in range(len(stack.split("\n"))-1)
            if stack[(int(stack[-2:-1])*row*4)+(column*4+2)-1:(int(stack[-2:-1])*row*4)+(column*4+2)] != " "
        ]
        for column
        in range(int(stack[-2:-1]))
    ]
    step_tracker = [[int(step_nums) for i, step_nums in enumerate(step.split()) if i%2 != 0] for step in steps.split("\n")]
    for step in step_tracker:
        if part_one:
            for _ in range(step[0]):
                stack_tracker[step[2]-1] = stack_tracker[step[1]-1][:1] + stack_tracker[step[2]-1]
                stack_tracker[step[1]-1] = stack_tracker[step[1]-1][1:]
        else:
            stack_tracker[step[2]-1] = stack_tracker[step[1]-1][:step[0]] + stack_tracker[step[2]-1]
            stack_tracker[step[1]-1] = stack_tracker[step[1]-1][step[0]:]
    answer = ""
    for stack in stack_tracker:
        answer += stack[0]

    print(f"{'Part 1:' if part_one else 'Part 2:'}", answer)


def day_six(marker_len):
    input = open("advent/inputs/day_6.txt").read()
    for i in range(len(input)):
        if len(set(input[i:i+marker_len])) == marker_len:
            print(i+marker_len)
            break


def nested_set(dic: dict, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value

def dir_size_adder(dic: dict, answers: list, part_two: bool):
    current_count = 0
    for value in dic.values():
        if isinstance(value, dict):
            nested_dir_size = dir_size_adder(value, answers, part_two)
            current_count += nested_dir_size if not part_two else 0
        else:
            current_count += value
    if part_two or current_count <= 100000:
        answers.append(current_count)
    return current_count

def find_dir_to_delete(dic: dict, answer: list, free_up_space: int):
    current_count = 0
    for value in dic.values():
        if isinstance(value, dict):
            current_count += find_dir_to_delete(value, answer, free_up_space)
        else:
            current_count += value
    if current_count > free_up_space and answer[0] - free_up_space > current_count - free_up_space:
        answer.pop()
        answer.append(current_count)
    return current_count

def day_seven():
    print("----------------DAY SEVEN----------------")
    lines = open("advent/inputs/day_7.txt").read().split("\n")
    current_path = []
    directory_structure = {}
    for line in lines:
        split_line = line.split()
        if split_line[1] == "cd":
            if split_line[2] != "..":
                current_path.append(split_line[2])
                nested_set(directory_structure, current_path, {})
                pass
            else:
                current_path.pop()
                pass
        elif split_line[0] != "dir" and line[0] != "$":
            current_file = current_path + [split_line[1]]
            nested_set(directory_structure, current_file, int(split_line[0]))
    answers = []
    dir_size_adder(directory_structure, answers, False)
    print(f"Part One: {sum(answers)}")

    total_size = []
    dir_size_adder(directory_structure, total_size, True)
    free_up_size = 30000000 - (70000000 - sum(total_size))
    answer_holder = [70000000]
    find_dir_to_delete(directory_structure, answer_holder, free_up_size)
    print(answer_holder[0])


def traverse_rows(row_split, start_element, matrix, visible_trees):
    for i, row in enumerate(matrix[1:-1]):
        tallest_tree = row[start_element]
        for j, row_element in enumerate(row[row_split[0]:row_split[1]:row_split[2]]):
            if row_element > tallest_tree:
                if start_element == 0:
                    column_index = j
                else:
                    column_index = len(row[row_split[0]:row_split[1]:row_split[2]]) - 1 - j
                tallest_tree = row_element
                visible_trees[i][column_index] = 1

def traverse_columns(column_split, start_element, matrix, visible_trees):
    for i, column_start in enumerate(matrix[start_element][1:-1]):
        tallest_tree = column_start
        for j, row in enumerate(matrix[column_split[0]:column_split[1]:column_split[2]]):
            if row[1:-1][i] > tallest_tree:
                if start_element == 0:
                    row_index = j
                else:
                    row_index = len(matrix[column_split[0]:column_split[1]:column_split[2]]) - 1 - j
                tallest_tree = row[1:-1][i]
                visible_trees[row_index][i] = 1

def calculate_scenic_ranking(matrix, scenic_ranking):
    for i, row in enumerate(matrix[1:-1]):
        visible_trees = 0
        for j, row_element in enumerate(row[1:-1]):
            for element in row[j::-1]:
                visible_trees+=1
                if element >= row_element:
                    break
            scenic_ranking[i][j]*=visible_trees
            visible_trees = 0
            for element in row[j+2::]:
                visible_trees += 1
                if element >= row_element:
                    break
            scenic_ranking[i][j]*=visible_trees
            visible_trees = 0
            for element in matrix[i::-1]:
                visible_trees += 1
                if element[j+1] >= row_element:
                    break
            scenic_ranking[i][j]*=visible_trees
            visible_trees = 0
            for element in matrix[i+2::]:
                visible_trees += 1
                if element[j+1] >= row_element:
                    break
            scenic_ranking[i][j]*=visible_trees
            visible_trees = 0


def day_eight():
    print("----------------DAY EIGHT----------------")
    grid = open("advent/inputs/day_8.txt").read().split("\n")
    matrix = [[int(row_item) for row_item in row] for row in grid]
    visible_trees = [[0 for _ in row[1:-1]] for row in grid[1:-1]]
    print(len(visible_trees[0]), len(visible_trees))
    permitter = len(matrix[0]) + len(matrix[-1]) + (len(matrix)-2)*2
    traverse_rows((1, -1, 1), 0, matrix, visible_trees)
    traverse_rows((-2, 0, -1), -1, matrix, visible_trees)
    traverse_columns((1, -1, 1), 0, matrix, visible_trees)
    traverse_columns((-2, 0, -1), -1, matrix, visible_trees)
    print(f"Part One: {sum([sum(row) for row in visible_trees])+permitter}")
    scenic_ranking = [[1 for _ in row[1:-1]] for row in grid[1:-1]]
    calculate_scenic_ranking(matrix, scenic_ranking)
    print(f"Part Two: {max([max(row) for row in scenic_ranking])}")


def calculate_next_pos(head_position, tail_position):
    x_distance = head_position[0] - tail_position[0]
    y_distance = head_position[1] - tail_position[1]
    if abs(x_distance) == 1 and abs(y_distance) == 1:
        return tail_position
    if abs(x_distance) > 1 and abs(y_distance) > 1:
        if x_distance < 0:
            new_tail_x = tail_position[0] - 1
        else:
            new_tail_x = tail_position[0] + 1
        if y_distance < 0:
            new_tail_y = tail_position[1] - 1
        else:
            new_tail_y = tail_position[1] + 1
        return (new_tail_x, new_tail_y)
    if abs(x_distance) > 1:
        if x_distance < 0:
            new_tail_x = tail_position[0] - 1
        else:
            new_tail_x = tail_position[0] + 1
        if abs(y_distance) > 0:
            new_tail_y = tail_position[1] + y_distance
        else:
            new_tail_y = tail_position[1]
        tail_position = (new_tail_x, new_tail_y)
        return tail_position
    if abs(y_distance) > 1:
        if y_distance < 0:
            new_tail_y = tail_position[1] - 1
        else:
            new_tail_y = tail_position[1] + 1
        if abs(x_distance) > 0:
            new_tail_x = tail_position[0] + x_distance
        else:
            new_tail_x = tail_position[0]
        tail_position = (new_tail_x, new_tail_y)
        return tail_position
    return tail_position

def day_nine(part_one):
    moves = open("advent/inputs/day_9.txt").read().split("\n")
    head_position = (0, 0)
    middle_positions = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    tail_position = (0, 0)
    tail_has_been = {(0,0)}
    for move in moves:
        direction, steps = tuple(move.split())
        for _ in range(int(steps)):
            if direction == "D":
                head_position = (head_position[0], head_position[1] - 1)
            elif direction == "U":
                head_position = (head_position[0], head_position[1] + 1)
            elif direction == "R":
                head_position = (head_position[0] + 1, head_position[1])
            else:
                head_position = (head_position[0] - 1, head_position[1])
            if part_one:
                tail_position = calculate_next_pos(head_position, tail_position)
            else:
                middle_positions[0] = calculate_next_pos(head_position, middle_positions[0])
                for i, position in enumerate(middle_positions[1::]):
                    middle_positions[i+1] = calculate_next_pos(middle_positions[i], position)
                tail_position = calculate_next_pos(middle_positions[-1], tail_position)
            tail_has_been.add(tail_position)
    print(f"{'Part One:' if part_one else 'Part Two:'} {len(tail_has_been)}")


def day_ten():
    instructions = open("advent/inputs/day_10.txt").read().split("\n")
    # check_cycle = [20, 60, 100, 140, 180, 220]
    # total_strength = 0
    current_cycle = 0
    x = 1
    screen = ""
    for instruction in instructions:
        if abs(current_cycle-x) <= 1:
            screen = screen + "#"
        else:
            screen = screen + "."
        current_cycle += 1
        if current_cycle%40 == 0:
            # total_strength += current_cycle*x
            screen = screen + "\n"
            current_cycle = 0
        if len(instruction.split()) == 1:
            continue
        else:
            if abs(current_cycle-x) <= 1:
                screen = screen + "#"
            else:
                screen = screen + "."
            current_cycle += 1
            if current_cycle%40 == 0:
                # total_strength += current_cycle*x
                screen = screen + "\n"
                current_cycle = 0
            x += int(instruction.split()[1])
    print(screen)


def main():
    day_one()
    day_two()
    day_three()
    day_four()

    print("----------------DAY FIVE----------------")
    day_five(True)
    day_five(False)

    print("----------------DAY SIX----------------")
    day_six(4)
    day_six(14)

    day_seven()
    day_eight()

    print("----------------DAY NINE----------------")
    day_nine(True)
    day_nine(False)