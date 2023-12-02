class DayTwo:
    def __init__(self):
        self._input = None
        self._max_cubes = {"red": 12, "green": 13, "blue": 14}

    @property
    def input(self):
        if self._input is None:
            with open("inputs/day_two.txt") as f:
                self._input = f.read()
        return self._input

    def get_max_cubes(self, plays):
        result = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for p in plays:
            cubes = p.split(",")
            for c in cubes:
                [num_str, color] = c.split()
                curr_max = result.get(color, 0)
                num = int(num_str)
                if num > curr_max:
                    result[color] = num

        return result

    def game_results(self):
        total_ids = 0
        total_powers = 0
        for line in self.input.splitlines():
            [game_info, plays] = line.split(":")
            [_, game_id] = game_info.split()
            rounds = plays.split(";")

            max_cubes = self.get_max_cubes(rounds)

            is_valid_game = True
            round_power = 1

            for k, v in max_cubes.items():
                round_power *= v
                if is_valid_game:
                    is_valid_game = v <= self._max_cubes[k]

            if is_valid_game:
                total_ids += int(game_id)

            total_powers += round_power

        return [total_ids, total_powers]


day_two = DayTwo()

[part_one_result, part_two_result] = day_two.game_results()
print(part_one_result)  # 3059
print(part_two_result)
