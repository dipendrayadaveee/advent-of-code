from part1 import read_input


def final_product_horizontal_depth(commands: list) -> int:
    position, depth, aim = 0, 0, 0
    for com in commands:
        if com[0] == "forward":
            position += com[1]
            depth += aim * com[1]
        elif com[0] == "down":
            aim += com[1]
        else:
            aim -= com[1]
    return position * depth


if __name__ == "__main__":
    vals = read_input()
    print(f"Multiplication: {final_product_horizontal_depth(vals)}")
    # 1685186100
