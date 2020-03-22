

class LevelStats:

    def __init__(self):
        self.infected_total = 0
        self.infected_by_player = 0
        self.died = 0
        self.killed_by_player = 0
        self.recovered = 0
        self.level_time_ms = 0
        self.end_reason = None