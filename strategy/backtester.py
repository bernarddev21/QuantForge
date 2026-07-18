class Backtester:

    def run(self, df):

        trades = []

        in_position = False
        entry_price = 0

        for _, row in df.iterrows():

            if (
                row["ma20"] > row["ma50"]
                and not in_position
            ):

                entry_price = row["close"]
                in_position = True

            elif (
                row["ma20"] < row["ma50"]
                and in_position
            ):

                exit_price = row["close"]

                pnl = (
                    exit_price - entry_price
                ) / entry_price

                trades.append(pnl)

                in_position = False

        return trades