class SolutionProblemThree:

    def __init__(self, problem_input: str, part: int = 1):
        self.problem_input = problem_input
        self.part = part
        self.data = self.parse_input()

    def part_one_parsing(self, line: str):
        return line.replace("ISO-", "").replace(" ", "")

    def part_two_parsing(self, line: str):
        lines = line.replace("ISO-", "").split(" ")

        len_one = len(lines[0])
        len_two = len(lines[1])

        i = 0
        j = len_one
        new_int = ""

        while i < len_two:
            if j == 0:
                j = len_one

            new_int = f"{lines[0][j - 1]}{new_int}"
            j -= 1
            i += 1

        return f"{new_int}{lines[1]}"

    def part_three_prepare_strings(self, lines: list[str]) -> str:
        len_one = len(lines[0])
        len_two = len(lines[1])

        i = 0
        j = len_one
        new_int = ""

        while i < len_two:
            if j == 0:
                j = len_one

            new_int = f"{lines[0][j - 1]}{new_int}"
            j -= 1
            i += 1

        return f"{new_int}{lines[1]}"

    def part_three_calc(self, nline: str) -> int:
        half = len(nline) // 2
        exponent = half - 1

        ans = 0

        for i in range(half):
            num_one = int(nline[i]) ** exponent
            num_two = int(nline[i + half])

            ans += num_one * num_two
            exponent -= 1

        return ans

    def part_three_parsing(self, line: str):
        lines = line.replace("ISO2-", "").split(" ")
        original_lines = self.part_three_prepare_strings(lines)
        original_ans = self.part_three_calc(original_lines)
        candidate = int(lines[1]) - 1
        while candidate >= 0:
            candidate_lines = [
                lines[0],
                str(candidate)
            ]
            new_lines = self.part_three_prepare_strings(candidate_lines)
            new_ans = self.part_three_calc(new_lines)
            if original_ans == new_ans:
                return "-1"

            candidate -= 1
        return original_lines

    def parse_input(self) -> list[int]:
        ans = []

        for line in self.problem_input.splitlines():
            if self.part == 1:
                nline = self.part_one_parsing(line)

            elif self.part == 2:
                nline = self.part_two_parsing(line)

            elif self.part == 3:
                nline = self.part_three_parsing(line)

            if nline == "-1":
                continue

            if self.part == 3:
                ans.append(self.part_three_calc(nline))
            else:
                # Common calculation for parts 1 and 2.
                half = len(nline) // 2
                exponent = half - 1

                r = 0

                for i in range(half):
                    num_one = int(nline[i]) ** exponent
                    num_two = int(nline[i + half])

                    r += num_one * num_two
                    exponent -= 1

                ans.append(r)

        return ans

    def solve_problem(self):
        print(sum(self.data))
