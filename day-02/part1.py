def read_input() -> list:
    """
    The input contains two parts, i.e. the direction and magnitude, so we split on the newline and
    then split on the space to have every instruction separate.
    """
    with open("input.txt", "r") as f:
        return [(x[0], int(x[1])) for x in (line.split() for line in f.read().strip().split("\n"))]


def get_product_position_depth(commands: list) -> int:
    """
    First identify the direction and then add or subtract the magnitude from the corresponding position.
    """
    pos, dep = 0, 0
    for command in commands:
        if command[0] == "forward":
            pos += command[1]
        elif command[0] == "down":
            dep += command[1]
        else:
            dep -= command[1]
    return pos * dep


if __name__ == "__main__":
    vals = read_input()
    print(f"Multiplication: {get_product_position_depth(vals)}")
    # 1604850
