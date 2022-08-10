from part1 import read_input


def get_fish_count(vals: list, days: int = 256) -> int:
    fishes = [vals.count(i) for i in range(9)]
    for _ in range(days):
        tmp = fishes[0]
        fishes = fishes[1:] + [tmp]
        fishes[6] += tmp
    return sum(fishes)


if __name__ == "__main__":
    vals = read_input()
    print(f"No of lantern fishes: {get_fish_count(vals)}")
