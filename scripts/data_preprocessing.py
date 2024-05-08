""" Data Preprocessing Script for Car Price Prediction Dataset """

import argparse
import os
import re

from typing import List

import pandas as pd

# Constants we defined from data analysis
DROP_COLUMNS = [
    "url",
    "region",
    "title_status",
    "VIN",
    "image_url",
    "description",
    "county",
    "posting_date",
    "model",
]

NON_IMPUTABLE_COLUMNS = [
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
    "odometer",
]


class DataTransformer:
    """Abstract Data Transformer Class"""

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        """
        Fit the transformer to the data.

        :param x: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        """
        raise NotImplementedError

    def transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Transform the input data.

        :param x: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        raise NotImplementedError

    def fit_transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Fit the transformer to the data and transform the input data.

        :param x: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        self.fit(x=x, y=y, **kwargs)
        return self.transform(x=x, y=y, **kwargs)


class TransformPipeline:
    """Class to chain multiple data transformations together"""

    def __init__(self, transformations: List[DataTransformer]):
        self.transformations = transformations

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        """
        Fit each transformation in the pipeline

        :param x: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        """
        x = x.copy()
        for layer in self.transformations:
            x = layer.fit_transform(x, y=y, **kwargs)

    def transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Apply each transformation in the pipeline to the input data

        :param x: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        x = x.copy()
        for layer in self.transformations:
            x = layer.transform(x, y=y, **kwargs)
        return x

    def fit_transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Fit and transform the input data using the pipeline

        :param x: The input data
        :param y: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        x = x.copy()
        for layer in self.transformations:
            x = layer.fit_transform(x, y=y, **kwargs)
        return x


class NormalizeUrl(DataTransformer):
    """Transformer that extracts the domain from the given column"""

    def __init__(self, column: str = "region_url"):
        self.column = column

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Extracts the domain from the given column

        :param x: The input data
        :return: The transformed data
        """
        x = x.copy()
        x[self.column] = x[self.column].apply(self.extract_domain_url)
        return x

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

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Drops rows with non-imputable values in the specified columns

        :param x: The input data
        :return: The transformed data
        """
        x = x.copy()
        for column_name in self.non_imputable_cols:
            x = x[x[column_name].notna()]
        return x


class DropColumns(DataTransformer):
    """Transformer that drops the specified columns"""

    def __init__(self, columns: List[str]):
        self.columns = columns

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Drops the specified columns

        :param x: The input data
        :return: The transformed data
        """
        x = x.copy()
        return x.drop(columns=self.columns)


class ApplyTransform(DataTransformer):
    """Transformer that applies transformation function to given column"""

    def __init__(self, column_name: str, transform_function):
        self.column = column_name
        self.transform_function = transform_function

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Transforms specified column by given transform function

        :param x: The input data
        :return: The transformed data
        """
        x = x.copy()
        x[self.column] = x[self.column].apply(self.transform_function)
        return x


class FillNa(DataTransformer):
    """Fill missing values in a given column"""

    def __init__(self, column_name: str, value):
        self.column = column_name
        self.value = value

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Fills missing values in a `self.column` as `self.value`

        :param x: The input data
        :return: The transformed data
        """
        x = x.copy()
        x[self.column] = x[self.column].fillna(self.value)
        return x


class QuantileFilter(DataTransformer):
    """Filter rows based on quantile values of a column"""

    def __init__(self, column_name: str, lower_quantile: float, upper_quantile: float):
        self.column = column_name
        self.lower_quantile = lower_quantile
        self.upper_quantile = upper_quantile

        self.lower_bound = None
        self.upper_bound = None

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        self.lower_bound = x[self.column].quantile(self.lower_quantile)
        self.upper_bound = x[self.column].quantile(self.upper_quantile)

    def transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        if not self.lower_bound or not self.upper_bound:
            raise ValueError("Bounds not set. Call fit before transform")

        x = x.copy()
        return x[
            (x[self.column] >= self.lower_bound) & (x[self.column] <= self.upper_bound)
        ]


class DropIfEqual(DataTransformer):
    """Drop rows where a value in a column is equal to a specified value"""

    def __init__(self, column_name: str, value):
        self.column = column_name
        self.value = value

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, x: pd.DataFrame, y: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        x = x.copy()
        return x[x[self.column] != self.value]


def main():
    """Main function for console script to preprocess data"""

    # Preprocessing pipeline definition
    pipeline = TransformPipeline(
        [
            DropColumns(DROP_COLUMNS),
            FillNa(column_name="paint_color", value="unspecified"),
            DropNonImputable(NON_IMPUTABLE_COLUMNS),
            DropIfEqual(column_name="price", value=0),
            QuantileFilter(
                column_name="price", lower_quantile=0.05, upper_quantile=0.95
            ),
            NormalizeUrl(),
            ApplyTransform(column_name="year", transform_function=int),
            ApplyTransform(column_name="odometer", transform_function=int),
        ]
    )

    # Control script via console
    parser = argparse.ArgumentParser(
        prog="DataPreprocessor",
        description="""
            Preprocesses the car price prediction dataset.

            The script performs the following operations:
                - Drops unnecessary columns,
                - Fills missing values with imputable values,
                - Drops rows if price is 0,
                - Filters out price outliers,
                - Extracts domain from region_url,
                - Converts year and odometer columns to integers,
        """,
    )
    parser.add_argument(
        "filename",
        type=str,
        help="Input file path",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output file path",
        default="output.csv",
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
