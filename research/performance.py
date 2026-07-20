class PerformanceEngine:

    def analyse(self, trades):

        if len(trades) == 0:
            return {
                "trades": 0,
                "win_rate": 0,
                "average_return": 0,
                "total_return": 0,
                "best_trade": 0,
                "worst_trade": 0
            }

        wins = [trade for trade in trades if trade > 0]

        return {
            "trades": len(trades),
            "win_rate": len(wins) / len(trades),
            "average_return": sum(trades) / len(trades),
            "total_return": sum(trades),
            "best_trade": max(trades),
            "worst_trade": min(trades)
        }