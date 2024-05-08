""" Data Preprocessing Script for Car Price Prediction Dataset """

from typing import List

import pandas as pd


class DataTransformer:
    """Abstract Data Transformer Class"""

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs):
        """
        Fit the transformer to the data.

        :param features: The input data
        :param labels: The target data
        :param kwargs: Additional arguments
        """
        raise NotImplementedError

    def transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Transform the input data.

        :param features: The input data
        :param labels: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        raise NotImplementedError

    def fit_transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Fit the transformer to the data and transform the input data.

        :param features: The input data
        :param labels: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        self.fit(features=features, labels=labels, **kwargs)
        return self.transform(features=features, labels=labels, **kwargs)


class TransformPipeline:
    """Class to chain multiple data transformations together"""

    def __init__(self, transformations: List[DataTransformer]):
        self.transformations = transformations

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs):
        """
        Fit each transformation in the pipeline

        :param features: The input data
        :param labels: The target data
        :param kwargs: Additional arguments
        """
        features = features.copy()
        for layer in self.transformations:
            features = layer.fit_transform(features, labels=labels, **kwargs)

    def transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Apply each transformation in the pipeline to the input data

        :param features: The input data
        :param labels: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        features = features.copy()
        for layer in self.transformations:
            features = layer.transform(features, labels=labels, **kwargs)
        return features

    def fit_transform(
        self, features: pd.DataFrame, labels: pd.DataFrame = None, **kwargs
    ) -> pd.DataFrame:
        """
        Fit and transform the input data using the pipeline

        :param features: The input data
        :param labels: The target data
        :param kwargs: Additional arguments
        :return: The transformed data
        """
        features = features.copy()
        for layer in self.transformations:
            features = layer.fit_transform(features, labels=labels, **kwargs)
        return features
