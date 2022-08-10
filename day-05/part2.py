from part1 import read_input, count_crossings


def get_overlaps(vals: list) -> int:
    return count_crossings(vals, allow_diagonal=True)


if __name__ == "__main__":
    vals = read_input()
    print(f"No. of points of overlaps: {get_overlaps(vals)}")
    # 22364
