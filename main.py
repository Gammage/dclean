import pandas as pd
import argparse

def main(file_path):
    
    df = pd.read_csv(file_path)

    df = df.drop_duplicates()

    output_file = "cleaned_" + file_path.split("/")[-1]
    df.to_csv(output_file, index=False)
    print(f"dropped duplicates, output {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to the CSV file")

    args = parser.parse_args()
    main(args.file)
