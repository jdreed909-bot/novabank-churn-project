import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "novabank_customer_retention_synthetic.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

def profile_data(df):
    print("=== Preview ===")
    print(df.head(), "\n")

    print("=== Shape ===")
    print(df.shape, "\n")

    print("=== Data Types & Missing Values ===")
    print(df.info(), "\n")

    print("=== Summary Statistics ===")
    print(df.describe(include="all"))

if __name__ == "__main__":
    df = load_data()
    profile_data(df)
