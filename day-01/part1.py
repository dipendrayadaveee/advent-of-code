def read_input() -> list:
    """
    The input data consists of a string of ints which we can split on
    the newline character and then convert the individual elements to int.
    """
    with open("input.txt", "r") as f:
        return [int(line) for line in f.read().strip().split("\n")]


def get_count(values: list) -> int:
    """
    The first part was just a matter of iterating over the list of items, starting
    from 1 and checking whether the last value was lower.
    """
    return sum(values[i + 1] > values[i] for i in range(len(values) - 1))


if __name__ == "__main__":
    vals = read_input()
    print(f"Measurements larger than previous measurements: {get_count(vals)}")
    # 1581
