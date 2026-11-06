class SolutionProblemTwo:

    def __init__(self, problem_input: list[int], part: int = 1):
        self.problem_input = problem_input
        self.part = part
        self.ranks = self.get_ranks()

    def part_2(self, alloys_map: dict) -> dict:
        for k in alloys_map.keys():
            new_set = set()
            for i in alloys_map[k]:
                new_set.update(alloys_map[i])
            alloys_map[k].update(new_set)
        return alloys_map

    def part_3_backtrack(self, alloys_map: dict, new_set: set, key: int) -> set:
        if len(alloys_map[key]) == 0:
            return new_set
        new_set.update(alloys_map[key])
        for k in alloys_map[key]:
            self.part_3_backtrack(alloys_map, new_set, k)
        return new_set

    def part_3(self, alloys_map: dict):
        for k in alloys_map.keys():
            new_set = set()
            new_set = self.part_3_backtrack(alloys_map, new_set, k)
            alloys_map[k].update(new_set)
        return alloys_map


    def get_ranks(self):
        ranks = []
        for l in self.problem_input.split('\n'):
            alloys_map = {}
            for e in l.split(' '):
                key = ''
                value = ''
                if '<' in e:
                    key = e[2]
                    value = e[0]
                if '>' in e:
                    key = e[0]
                    value = e[2]
                if alloys_map.get(key, None) is None:
                    alloys_map[key] = set()
                if alloys_map.get(value, None) is None:
                    alloys_map[value] = set()
                alloys_map[key].add(value)
            if self.part == 2:
                alloys_map = self.part_2(alloys_map)
            if self.part == 3:
                alloys_map = self.part_3(alloys_map)
            sorted_keys = sorted(
                alloys_map.keys(),
                key=lambda k: len(alloys_map[k]),
                reverse=True
            )
            result_int = int("".join(str(k) for k in sorted_keys))
            ranks.append(result_int)
        return ranks

    def solve_problem(self):

        print(sum(self.ranks))

p1 = SolutionProblemTwo(prob_input_part_1)
p1.solve_problem()

p2 = SolutionProblemTwo(prob_input_part_2, 2)
p2.solve_problem()

p3 = SolutionProblemTwo(prob_input_part_3, 3)
p3.solve_problem()
