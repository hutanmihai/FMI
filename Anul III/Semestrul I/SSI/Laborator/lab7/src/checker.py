def get_output_lines() -> list:
    with open("output.txt", "r") as r:
        lines = [x.replace("\n", "") for x in r.readlines()][1:]
        lines = [x.split("::::: ")[1] for x in lines]
    return lines


def get_output_test_lines() -> list:
    with open("output_test.txt", "r") as r:
        lines = [x.replace("\n", "") for x in r.readlines()][1:]
        lines = [x.split("::::: ")[1] for x in lines]
    return lines


if __name__ == '__main__':
    lines = get_output_lines()
    test_lines = get_output_test_lines()
    used = set(test_lines)
    has_collisions = False
    for line in lines:
        if line in used:
            has_collisions = True
            print(line + " has a collision")
        used.add(line)
    if has_collisions:
        print("Collisions found")
    else:
        print("No collisions found")
