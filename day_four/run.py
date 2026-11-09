class SolutionProblemFour:

    def __init__(self, problem_input: str, part: int = 1):
        self.problem_input = problem_input
        self.part = part
        self.data = self.parse_input()

    def part_one(self):
        participants = {}
        for data_line in self.problem_input.split('\n'):
            data_line = data_line.split(' ')
            id = data_line[0].replace('id=', '')
            comp_time = int(data_line[3].replace('time=', ''))
            if not participants.get(id):
                participants[id] = 0
            participants[id] += comp_time
        sorted_values = [
            v * i
            for i, (k, v) in enumerate(
                sorted(participants.items(), key=lambda item: item[1]),
                start=1
            )
        ]
        return sorted_values

    def part_two(self):
        participants = {}
        for data_line in self.problem_input.split('\n'):
            data_line = data_line.split(' ')
            id = data_line[0].replace('id=', '')
            comp_time = int(data_line[3].replace('time=', ''))
            if not participants.get(id):
                participants[id] = [0,0]
            participants[id][0] += 1
            participants[id][1] += comp_time
        sorted_values = [
            total_time * i
            for i, (k, (count, total_time)) in enumerate(
                sorted(
                    participants.items(),
                    key=lambda item: (-item[1][0], item[1][1])
                ),
                start=1
            )
        ]
        return sorted_values

    def part_three(self):
        data_map = defaultdict(lambda: defaultdict(dict))

        for line in self.problem_input.strip().splitlines():
            if not line:
                continue
            parts = line.split()
            user_id = int(parts[0].replace('id=', ''))
            quest = int(parts[1].replace('quest=', ''))
            part = int(parts[2].replace('part=', ''))
            comp_time = int(parts[3].replace('time=', ''))
            data_map[quest][part][user_id] = comp_time

        participants_points = defaultdict(int)

        for quest in sorted(data_map.keys()):
            cumulative_times = defaultdict(int)

            for part in sorted(data_map[quest].keys()):
                eligible_users = {}
                for user_id, time_taken in data_map[quest][part].items():
                    if part == 1 or user_id in cumulative_times:
                        cumulative_times[user_id] += time_taken
                        eligible_users[user_id] = cumulative_times[user_id]
                sorted_by_time = sorted(eligible_users.items(), key=lambda item: item[1])
                max_points = 50 * part
                current_rank = 1
                prev_time = None

                for i, (user_id, total_time) in enumerate(sorted_by_time):
                    if total_time != prev_time:
                        current_rank = i + 1
                        prev_time = total_time
                    pts = max(0, max_points - (current_rank - 1))
                    participants_points[user_id] += pts
        sorted_final = sorted(participants_points.items(), key=lambda item: item[1], reverse=True)

        checksum_values = []
        current_final_rank = 1
        prev_score = None

        for i, (user_id, score) in enumerate(sorted_final):
            if score != prev_score:
                current_final_rank = i + 1
                prev_score = score

            checksum_values.append(score * current_final_rank)

        return checksum_values

    def parse_input(self):
        if self.part == 1:
            return self.part_one()
        elif self.part == 2:
            return self.part_two()
        elif self.part == 3:
            return self.part_three()
        else:
            raise ValueError


    def solve_problem(self):
        print(sum(self.data))
