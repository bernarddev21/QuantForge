class SignalEngine:

    def moving_average_signal(self, df):

        latest = df.iloc[-1]

        if latest["ma20"] > latest["ma50"]:
            return "BUY"

        elif latest["ma20"] < latest["ma50"]:
            return "SELL"

        return "HOLD"