def read_input(filename: str = "input.txt") -> list:
    with open(f"{filename}", "r") as f:
        return [int(i) for i in f.read().strip().split(",")]


def get_fish_count(vals: list, days: int = 80) -> int:
    fishes = vals[:]
    for _ in range(days):
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1
    return len(fishes)


if __name__ == "__main__":
    vals = read_input()
    print(f"No. of lantern fishes: {get_fish_count(vals)}")
    # 345387