import pandas as pd


def to_dataframe(data):

    return pd.DataFrame(data)


def export_csv(df):

    return df.to_csv(index=False).encode("utf-8")
