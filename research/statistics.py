import pandas as pd


class StatisticsEngine:

    def calculate_returns(self, candles):

        df = pd.DataFrame(
            candles,
            columns=[
                "timestamp",
                "open",
                "high",
                "low",
                "close",
                "volume"
            ]
        )

        df["return"] = df["close"].pct_change()

        return df

    def add_features(self, df):

        # 20-period moving average
        df["ma20"] = df["close"].rolling(20).mean()

        # 50-period moving average
        df["ma50"] = df["close"].rolling(50).mean()

        # 20-period rolling volatility
        df["volatility20"] = (
            df["return"]
            .rolling(20)
            .std()
        )

        return df