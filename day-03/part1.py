def read_input() -> list:
    with open("input.txt", "r") as f:
        return [x for x in f.read().strip().split("\n")]


def get_mcb(vals: list) -> list:
    bit_count = [sum(int(num[i]) for num in vals) for i in range(len(vals[0]))]
    return [1 if count >= (len(vals) - count) else 0 for count in bit_count]


def get_power_consumption(vals: list) -> int:
    mcb = get_mcb(vals)
    gamma = "".join(["1" if bit else "0" for bit in mcb])
    epsilon = "".join(["0" if bit else "1" for bit in mcb])
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    vals = read_input()
    print(f"Power consumption: {get_power_consumption(vals)}")
    # 852500
