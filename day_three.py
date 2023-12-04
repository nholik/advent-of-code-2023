from math import log10, floor
from collections import defaultdict


class DayThree:
    def __init__(self):
        self._matrix = None
        self._directions = {(-1, 0), (-1, 1), (-1, -1), (1, 0), (1, 1), (1, -1)}
        self._gears = defaultdict(set)

    @property
    def matrix(self):
        if self._matrix is None:
            with open("inputs/day_three.txt") as f:
                self._matrix = []
                lines = f.read()
                for line in lines.splitlines():
                    self._matrix.append(list(line))

        return self._matrix

    def is_valid(self, row, col):
        return (
            0 <= row
            and row < len(self.matrix)
            and 0 <= col
            and col < len(self.matrix[0])
        )

    def is_symbol(self, row, col):
        if not self.is_valid(row, col):
            return False

        return self.matrix[row][col] != "." and not self.matrix[row][col].isdigit()

    def is_schematic_part(self, num, row, col):
        num_len = floor(log10(num) + 1) - 1
        start_row = row
        start_col = col - num_len
        is_sp = False

        for c in range(start_col, col + 1):
            for dx, dy in self._directions:
                check_r, check_c = row + dx, c + dy

                if self.is_symbol(check_r, check_c):
                    symbol = self.matrix[check_r][check_c]
                    if symbol == "*":
                        self._gears[(check_r, check_c)].add(
                            (num, check_r, check_c, row, col)
                        )
                    is_sp = True

        if self.is_symbol(start_row, start_col - 1):
            symbol = self.matrix[start_row][start_col - 1]
            if symbol == "*":
                self._gears[(start_row, start_col - 1)].add(
                    (num, start_row, start_col - 1, row, col)
                )
            is_sp = True

        if self.is_symbol(start_row, col + 1):
            symbol = self.matrix[start_row][col + 1]
            if symbol == "*":
                self._gears[(start_row, col + 1)].add(
                    (num, start_row, col + 1, row, col)
                )
            is_sp = True

        return is_sp

    def sum_part_numbers(self):
        total_parts = 0
        total_rows = len(self.matrix)
        total_cols = len(self.matrix[0])

        for row in range(0, total_rows):
            curr_num = 0
            for col in range(0, total_cols):
                entry = self.matrix[row][col]
                if entry.isdigit():
                    curr_num *= 10
                    curr_num += int(entry)

                    if col == total_cols - 1 and self.is_schematic_part(
                        curr_num, row, col
                    ):
                        total_parts += curr_num
                elif not entry.isdigit() and curr_num > 0:
                    if self.is_schematic_part(curr_num, row, col - 1):
                        total_parts += curr_num
                    curr_num = 0

        total_gear_product = 0

        for k, v in self._gears.items():
            if len(v) == 2:
                f = v.pop()
                s = v.pop()
                p = f[0] * s[0]
                total_gear_product += p

        return [total_parts, total_gear_product]


day_three = DayThree()
[part_one_result, part_two_result] = day_three.sum_part_numbers()
print(part_one_result)
print(part_two_result)
