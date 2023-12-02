class DayOne:
    def __init__(self):
        self._input = None
        self._digit_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

    @property
    def input(self):
        if self._input is None:
            with open("inputs/day_one.txt") as f:
                self._input = f.read()
        return self._input

    def convert_to_number(self, input):
        input_lst = list(input)

        for i in range(len(input_lst)):
            match input_lst[i:]:
                case ["o", "n", "e", *_]:
                    input_lst[i] = self._digit_map["one"]
                case ["t", "w", "o", *_]:
                    input_lst[i] = self._digit_map["two"]
                case ["t", "h", "r", "e", "e", *_]:
                    input_lst[i] = self._digit_map["three"]
                case ["f", "o", "u", "r", *_]:
                    input_lst[i] = self._digit_map["four"]
                case ["f", "i", "v", "e", *_]:
                    input_lst[i] = self._digit_map["five"]
                case ["s", "i", "x", *_]:
                    input_lst[i] = self._digit_map["six"]
                case ["s", "e", "v", "e", "n", *_]:
                    input_lst[i] = self._digit_map["seven"]
                case ["e", "i", "g", "h", "t", *_]:
                    input_lst[i] = self._digit_map["eight"]
                case ["n", "i", "n", "e", *_]:
                    input_lst[i] = self._digit_map["nine"]
        return input_lst

    def run_calibration(self, ignore_words):
        total_calibration = 0

        for line in self.input.splitlines():
            chars = line if ignore_words else self.convert_to_number(line)
            candidates = []
            for c in chars:
                if c.isdigit():
                    candidates.append(int(c))
            line_calibration = candidates[0] * 10 + candidates[-1]
            total_calibration += line_calibration

        return total_calibration


dayOne = DayOne()

part_one_cal = dayOne.run_calibration(True)
print(f"part one: {part_one_cal}")  # 54697

part_two_cal = dayOne.run_calibration(False)
print(f"part two: {part_two_cal}")
