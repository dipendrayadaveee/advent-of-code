from part1 import read_input, Draws


def get_final_score(draws: Draws, fields: list) -> int:
    while draws.draws_left:
        play_fields = [field for field in fields if not field.winner]
        if len(play_fields) == 1:
            break

        num = draws.draw()
        for field in play_fields:
            field.draw(num)

    last = play_fields[0]
    while not last.winner:
        last.draw(draws.draw())
    return last.calculate_score()


if __name__ == "__main__":
    draws, fields = read_input()
    print(f"Final score: {get_final_score(draws, fields)}")
    # 11377
