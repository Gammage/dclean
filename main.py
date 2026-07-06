import pandas as pd
import argparse

def clean_data(df):
    return df.drop_duplicates()

def summarise_data(df):
    print(df.shape)
    print(df.columns)
    print(df.isnull().sum())
    print(df.describe())   

def main(file_path, info, clean):
    
    df = pd.read_csv(file_path)

    if clean:
        df = clean_data(df)

    if info:
        summarise_data(df)

    output_file = "cleaned_" + file_path.split("/")[-1]
    df.to_csv(output_file, index=False)
    print(f"saved{output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to the CSV file")
    parser.add_argument("--info", action="store_true", help="summarises the file")
    parser.add_argument("--clean", action="store_true", help="removes duplicates and other dirty data")

    args = parser.parse_args()
    main(args.file, args.info, args.clean)


