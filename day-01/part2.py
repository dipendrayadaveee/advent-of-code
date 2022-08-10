from part1 import read_input


def get_count_sliding_windows(values: list) -> int:
    """
    For the part 2, instead of taking the value itself we take the sum of
    the next three values while iterating from 1 until length - 2.
    """
    return sum(values[i + 3] + values[i + 2] + values[i + 1] > values[i + 2] + values[i + 1] + values[i]
               for i in range(len(values) - 3))


if __name__ == "__main__":
    vals = read_input()
    print(f"Sums greater than previous sums: {get_count_sliding_windows(vals)}")
    # 1618

