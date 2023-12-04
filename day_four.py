class DayFour:
    def __init__(self):
        self._card_piles = None

    @property
    def card_piles(self):
        if self._card_piles is None:
            with open("inputs/day_four.txt") as f:
                self._card_piles = []
                lines = f.read()
                for line in lines.splitlines():
                    [_, cards] = line.split(":")
                    [winning_numbers, card_vals] = cards.split("|")
                    self._card_piles.append(
                        [1, winning_numbers.split(), card_vals.split()]
                    )

        return self._card_piles

    def total_points(self):
        total_points = 0
        total_copies = 0
        for i in range(len(self.card_piles)):
            copies, winning_nums, card_nums = self.card_piles[i]
            total_copies += copies

            w = set(winning_nums)
            c = set(card_nums)

            winners = len(w.intersection(c))
            points = 2 ** (winners - 1) if winners > 0 else 0
            total_points += points

            for j in range(
                min(i + 1, len(self.card_piles)),
                min(i + winners + 1, len(self.card_piles)),
            ):
                self.card_piles[j][0] += copies

        return [total_points, total_copies]


day_four = DayFour()
[part_one_result, part_two_result] = day_four.total_points()
print(part_one_result)
print(part_two_result)
