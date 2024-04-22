""" Data Preprocessing Script for Car Price Prediction Dataset """

import argparse
import os
import re

from typing import List

import pandas as pd

# pylint: disable=C0103
# because sklearn format for ML
# See:
# https://github.com/scikit-learn/scikit-learn/blob/872124551/sklearn/preprocessing/_data.py#L851


class DataTransformer:
    """Abstract Data Transformer Class"""

    def fit(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        """
        Fit the transformer to the data.

        :param X: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        """
        raise NotImplementedError

    def transform(
        self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Transform the input data.

        :param X: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        raise NotImplementedError

    def fit_transform(
        self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Fit the transformer to the data and transform the input data.

        :param X: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        self.fit(X=X, y=y, **kwargs)
        return self.transform(X=X, y=y, **kwargs)


class TransformPipeline:
    """Class to chain multiple data transformations together"""

    def __init__(self, transformations: List[DataTransformer]):
        self.transformations = transformations

    def fit(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        """
        Fit each transformation in the pipeline

        :param X: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        """
        X = X.copy()
        for layer in self.transformations:
            X = layer.fit_transform(X, y=y, **kwargs)

    def transform(
        self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Apply each transformation in the pipeline to the input data

        :param X: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        X = X.copy()
        for layer in self.transformations:
            X = layer.transform(X, y=y, **kwargs)
        return X

    def fit_transform(
        self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Fit and transform the input data using the pipeline

        :param X: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        X = X.copy()
        for layer in self.transformations:
            X = layer.fit_transform(X, y=y, **kwargs)
        return X


class NormalizeUrl(DataTransformer):
    """Transformer that extracts the domain from the given column"""

    def __init__(self, column: str = "region_url"):
        self.column = column

    def fit(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Extracts the domain from the given column

        :param X: The input data
        :return: The transformed data
        """
        X = X.copy()
        X[self.column] = X[self.column].apply(self.extract_domain_url)
        return X

    @staticmethod
    def extract_domain_url(url: str) -> str:
        """
        Extracts the domain from the given url

        :param url: The input url
        :return: The domain of the url
        """
        results = re.search("https?://([A-Za-z_0-9.-]+).*", url)
        if results:
            return results.group(1)
        return url


class DropNonImputable(DataTransformer):
    """Transformer that drops rows with non-imputable values in the specified columns"""

    def __init__(self, non_imputable_cols: List[str]):
        self.non_imputable_cols = non_imputable_cols

    def fit(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Drops rows with non-imputable values in the specified columns

        :param X: The input data
        :return: The transformed data
        """
        X = X.copy()
        for column_name in self.non_imputable_cols:
            X = X[X[column_name].notna()]
        return X


class DropColumns(DataTransformer):
    """Transformer that drops the specified columns"""

    def __init__(self, columns: List[str]):
        self.columns = columns

    def fit(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Drops the specified columns

        :param X: The input data
        :return: The transformed data
        """
        X = X.copy()
        return X.drop(columns=self.columns)


class ApplyTransform(DataTransformer):
    """Transformer that applies transformation function to given column"""

    def __init__(self, column_name: str, transform_function):
        self.column = column_name
        self.transform_function = transform_function

    def fit(self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, X: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Transforms specified column by given transform function

        :param X: The input data
        :return: The transformed data
        """
        X = X.copy()
        X[self.column] = X[self.column].apply(self.transform_function)
        return X


def main():
    """Main function for console script to preprocess data"""
    # Constants we defined from data analysis
    drop_columns = [
        "url",
        "region",
        "title_status",
        "VIN",
        "image_url",
        "description",
        "county",
        "posting_date",
    ]

    non_imputable_columns = [
        "condition",
        "cylinders",
        "fuel",
        "transmission",
        "drive",
        "size",
        "type",
        "manufacturer",
        "lat",
        "long",
    ]

    # Whole data preprocessing pipeline
    pipeline = TransformPipeline(
        [
            DropColumns(drop_columns),
            DropNonImputable(non_imputable_columns),
            NormalizeUrl(),
            ApplyTransform(column_name='year', transform_function=lambda a: int(a))
        ]
    )

    # Control script via console
    parser = argparse.ArgumentParser(
        prog="DataPreprocessor",
        description="Drops too ambiguous columns, "
        "Drop rows with non-imputable values "
        "and Normalize urls",
    )
    parser.add_argument("filename", type=str, help="Input file path")
    parser.add_argument(
        "-o", "--output", type=str, default="output.csv", help="Output file path"
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        default=None,
        help="Limit on the output number of rows",
    )

    # Parse arguments & preprocess
    args = parser.parse_args()

    # Read data & determine limit
    df = pd.read_csv(args.filename)
    if args.limit is None:
        args.limit = df.shape[0]

    # Apply transformations and slice
    transformed = pipeline.fit_transform(df)
    transformed = transformed.iloc[: args.limit]

    # Save transformed data & make directories if required
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    transformed.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
