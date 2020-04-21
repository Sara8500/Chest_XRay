import pandas as pd
import argparse


def parse_arguments():
    print('\nParse arguments')

    parser = argparse.ArgumentParser()
    parser.add_argument('--training_dataset', type=str, default=None,
                        help='path to training the dataset')
    parser.add_argument('--test_dataset', type=str, default=None,
                        help='path to test dataset')
    parser.add_argument('--csv_metadata', type=str, default=None,
                        help='path to csv meta')

    arguments = parser.parse_args()
    return arguments


args = parse_arguments()

summary = pd.read_csv(args.csv_metadata)
print(summary.head())
print(summary.Label.unique())
