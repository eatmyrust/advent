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

def day_seven():
    lines = open("advent/inputs/day_7_test.txt").read().split("\n")
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