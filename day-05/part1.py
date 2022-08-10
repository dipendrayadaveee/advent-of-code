def read_input(filename: str = "input.txt") -> list:
    with open(f"{filename}", "r") as f:
        lines = [line.split(" -> ") for line in f.read().strip().split("\n")]
    return [[(int(s[0]), int(s[1])) for s in (x.split(",") for x in line)] for line in lines]


def count_crossings(vals: list, allow_diagonal: bool = False) -> int:
    segments = dict()
    for val in vals:
        x_1, x_2, y_1, y_2 = val[0][0], val[1][0], val[0][1], val[1][1]
        x_dir = 1 if x_1 < x_2 else -1 if x_1 > x_2 else 0
        y_dir = 1 if y_1 < y_2 else -1 if y_1 > y_2 else 0
        dist = max(abs(x_2 - x_1), abs(y_2 - y_1))
        cond = True if allow_diagonal else (x_dir == 0 or y_dir == 0)
        tmp = [(x_1 + n * x_dir, y_1 + n * y_dir) for n in range(dist + 1) if cond]

        for segment in tmp:
            if segment not in segments:
                segments[segment] = 1
            else:
                segments[segment] += 1

    return sum(1 for x in segments if segments[x] > 1)


def get_overlaps(vals: list) -> int:
    return count_crossings(vals)


if __name__ == "__main__":
    vals = read_input()
    print(f"No. of points of overlaps: {get_overlaps(vals)}")
    # 7468
