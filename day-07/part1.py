def read_input(filename: str = "input.txt") -> list:
    with open(f"{filename}", "r") as f:
        return [int(x) for x in f.read().strip().split(",")]


def calculate_distances(positions):
    return [[abs(p - r) for p in positions] for r in range(min(positions), max(positions) + 1)]


def get_fuel_expenditure(vals: list) -> int:
    return min(sum(distance) for distance in calculate_distances(vals))


if __name__ == "__main__":
    vals = read_input()
    print(f"Fuel expenditure: {get_fuel_expenditure(vals)}")
