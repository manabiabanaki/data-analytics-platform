import pandas as pd

def process(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    if 'value' in df.columns:
        print("Mean value:", df['value'].mean())
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    process("raw-data/data.csv", "processed-data/processed_data.csv")
