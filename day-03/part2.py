from part1 import read_input, get_mcb


def reduce_reports(reports: list, invert: bool = False) -> int:
    for i in range(0, len(reports[0])):
        mcb = get_mcb(reports)[i]
        bit = str(mcb if not invert else 1 - mcb)
        reports = [rep for rep in reports if rep[i] == bit]
        if len(reports) == 1:
            break
    return int(reports[0], 2)


def get_life_support_rating(vals: list) -> int:
    oxy_gr = reduce_reports(vals[:])  # oxygen generator rating
    co2_sr = reduce_reports(vals[:], invert=True)  # CO2 scrubber rating
    return oxy_gr * co2_sr


if __name__ == "__main__":
    vals = read_input()
    print(f"Power consumption: {get_life_support_rating(vals)}")
    # 1007985
