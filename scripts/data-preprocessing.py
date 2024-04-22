from typing import List
import argparse
import os
import re

import pandas as pd


class DataTransformer:
    def fit(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs) -> None:
        pass

    def transform(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs) -> pd.DataFrame:
        pass

    def fit_transform(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs) -> pd.DataFrame:
        self.fit(X=X, y=y, **kwargs)
        return self.transform(X=X, y=y, **kwargs)


class TransformPipeline:
    def __init__(self, transformations: List[DataTransformer]):
        self.transformations = transformations

    def fit(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        X = X.copy()
        for layer in self.transformations:
            X = layer.fit_transform(X, y=y, **kwargs)

    def transform(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        X = X.copy()
        for layer in self.transformations:
            X = layer.transform(X, y=y, **kwargs)
        return X

    def fit_transform(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        X = X.copy()
        for layer in self.transformations:
            X = layer.fit_transform(X, y=y, **kwargs)
        return X


class NormalizeUrl(DataTransformer):
    def __init__(self, column: str = 'region_url'):
        self.column = column

    def transform(self, X: pd.DataFrame, **kwargs) -> pd.DataFrame:
        X = X.copy()
        X[self.column] = X[self.column].apply(self.normalize_region_url)
        return X

    @staticmethod
    def normalize_region_url(url: str) -> str:
        results = re.search('https?://([A-Za-z_0-9.-]+).*', url)
        if results:
            return results.group(1)
        return url


class DropNonImputable(DataTransformer):
    def __init__(self, non_imputable_cols: List[str]):
        self.non_imputable_cols = non_imputable_cols

    def transform(self, X: pd.DataFrame, **kwargs) -> pd.DataFrame:
        X = X.copy()
        for column_name in self.non_imputable_cols:
            X = X[X[column_name].notna()]
        return X


class DropColumns(DataTransformer):
    def __init__(self, columns: List[str]):
        self.columns = columns

    def transform(self, X: pd.DataFrame, **kwargs) -> pd.DataFrame:
        X = X.copy()
        return X.drop(columns=self.columns)


def main():
    # constants we defined from data analysis
    drop_columns = [
        'url', 'region', 'title_status', 'VIN', 'image_url',
        'description', 'county', 'posting_date'
    ]
    non_imputable_columns = [
        'condition', 'cylinders', 'fuel', 'transmission',
        'drive', 'size', 'type', 'manufacturer', 'lat', 'long'
    ]

    # whole data preprocessing pipeline
    pipeline = TransformPipeline([
        DropColumns(drop_columns),
        DropNonImputable(non_imputable_columns),
        NormalizeUrl()
    ])

    # control script via console
    parser = argparse.ArgumentParser(
        prog='DataPreprocessor',
        description='Drops too ambiguous columns, '
                    'Drop rows with non-imputable values '
                    'and Normalize urls'
    )
    parser.add_argument(
        'filename',
        type=str,
        help='Input file path'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='output.csv',
        help='Output file path'
    )
    parser.add_argument(
        '-l', '--limit',
        type=int,
        default=None,
        help='Limit on the output number of rows'
    )

    # parse arguments & preprocess
    args = parser.parse_args()

    # read data & determine limit
    df = pd.read_csv(args.filename)
    if args.limit is None:
        args.limit = df.shape[0]

    # apply transformations and slice
    transformed = pipeline.fit_transform(df)
    transformed = transformed.iloc[:args.limit]

    # save transformed data & make directories if required
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    transformed.to_csv(args.output, index=False)


if __name__ == '__main__':
    main()
