class SolutionProblemSix:

    def __init__(self, problem_input: str, part: int):
        self.problem_input = problem_input
        self.part = part
        self.data = self.parse_input()
        self.seen = set()
        self.counter = 0

    def parse_input(self) -> dict:

        data = {}
        if self.part == 1 or 3:
            for row in self.problem_input.split('\n'):
                key = row.split(':')[0]
                values = row.split(':')[1].split(',')
                data[key] = values
                for v in values:
                    if not data.get(v):
                        data[v] = []
        if self.part == 2:
            for row in self.problem_input.split('\n'):
                key = row.split(':')[0]
                values = row.split(':')[1].split(',')
                if not data.get(key):
                    data[key] = []
                for v in values:
                    if not data.get(v):
                        data[v] = []
                    data[v].append(key)
        return data

    def solve(self, current: str) -> None:
        # parts 1 and 2
        self.seen.add(current)
        for k in self.data[current]:
            if k not in self.seen:
                self.solve(k)

    def solve_three(self, current: str) -> None:
        # part three
        self.seen.add(current)
        for k in self.data[current]:
            if k not in self.seen:
                if 'NULL' in k:
                    self.counter += 1
                self.solve_three(k)

    def part_one(self):
        self.solve('NULL')
        print(len(self.seen) - 1)

    def part_two(self):
        self.solve('NULL')
        print(len(self.seen) - 1)

    def part_three(self):
        ans = 0
        for k in self.data.keys():
            self.counter = 0
            self.seen = set()
            self.solve_three(k)
            if self.counter > 1:
                ans += 1
        print(f"Total: {ans}")
