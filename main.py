from ping_game_theory_25 import Strategy, StrategyTester, Move, History, HistoryEntry


class Bot(Strategy):
    def __init__(self) -> None:
        self.author_netid = ""
        self.strategy_name = ""
        self.stretegy_desc = ""

    def begin(self) -> Move:
        return Move.ROCK

    def turn(self, history: History) -> Move:
        return Move.ROCK


tester = StrategyTester(Bot)
tester.run()
