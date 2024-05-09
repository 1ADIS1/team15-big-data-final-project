""" Script for implemented transformers """

import re
from typing import List

import pandas as pd

from preprocess.modules import DataTransformer


class NormalizeUrl(DataTransformer):
    """Transformer that extracts the domain from the given column"""

    def __init__(self, column: str = "region_url"):
        self.column = column

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Extracts the domain from the given column

        :param features: The input data
        :return: The transformed data
        """
        features = features.copy()
        features[self.column] = features[self.column].apply(self.extract_domain_url)
        return features

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

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Drops rows with non-imputable values in the specified columns

        :param features: The input data
        :return: The transformed data
        """
        features = features.copy()
        for column_name in self.non_imputable_cols:
            features = features[features[column_name].notna()]
        return features


class DropColumns(DataTransformer):
    """Transformer that drops the specified columns"""

    def __init__(self, columns: List[str]):
        self.columns = columns

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Drops the specified columns

        :param features: The input data
        :return: The transformed data
        """
        features = features.copy()
        return features.drop(columns=self.columns)


class ApplyTransform(DataTransformer):
    """Transformer that applies transformation function to given column"""

    def __init__(self, column_name: str, transform_function):
        self.column = column_name
        self.transform_function = transform_function

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Transforms specified column by given transform function

        :param features: The input data
        :return: The transformed data
        """
        features = features.copy()
        features[self.column] = features[self.column].apply(self.transform_function)
        return features


class FillNa(DataTransformer):
    """Fill missing values in a given column"""

    def __init__(self, column_name: str, value):
        self.column = column_name
        self.value = value

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Fills missing values in a `self.column` as `self.value`

        :param features: The input data
        :return: The transformed data
        """
        features = features.copy()
        features[self.column] = features[self.column].fillna(self.value)
        return features


class QuantileFilter(DataTransformer):
    """Filter rows based on quantile values of a column"""

    def __init__(self, column_name: str, lower_quantile: float, upper_quantile: float):
        self.column = column_name
        self.lower_quantile = lower_quantile
        self.upper_quantile = upper_quantile

        self.lower_bound = None
        self.upper_bound = None

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs):
        self.lower_bound = features[self.column].quantile(self.lower_quantile)
        self.upper_bound = features[self.column].quantile(self.upper_quantile)

    def transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        if not self.lower_bound or not self.upper_bound:
            raise ValueError("Bounds not set. Call fit before transform")

        features = features.copy()
        return features[
            (features[self.column] >= self.lower_bound)
            & (features[self.column] <= self.upper_bound)
        ]


class DropIfEqual(DataTransformer):
    """Drop rows where a value in a column is equal to a specified value"""

    def __init__(self, column_name: str, value):
        self.column = column_name
        self.value = value

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs):
        pass

    def transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        features = features.copy()
        return features[features[self.column] != self.value]
