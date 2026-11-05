class SolutionProblemOne:

    def __init__(self, part: int, problem_input: list[int]):
        self.part = part
        self.problem_input = problem_input
        self.squares = self.generate_squares()

    def generate_squares(self):
        squares = [0]
        if self.part == 1:
            squares.extend([i*i for i in range(0,self.problem_input[-1]) if
                    i*i <= self.problem_input[-1] * 1.1])
        elif self.part == 2:
            squares.extend([(i * i) - (i - 2) * (i - 2)  for i in range(3, self.problem_input[-1]) if
                    (i * i) - (i - 2) * (i - 2) <= self.problem_input[-1] * 1.1])
        else:
            raise ValueError
        return squares

    def solve_problem(self):
        total_needed = 0
        for pines in self.problem_input:
            if pines in self.squares:
                continue
            for j in range(1, len(self.squares)):
                if self.squares[j-1] < pines < self.squares[j]:
                    total_needed += self.squares[j] - pines
        print(total_needed)


p1 = SolutionProblemOne(1, prob_input_part_1)
p1.solve_problem()

p2 = SolutionProblemOne(2, prob_input_part_2)
p2.solve_problem()
