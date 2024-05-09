""" Data Preprocessing Script for Car Price Prediction Dataset """

import argparse
import os

import pandas as pd

from preprocess.modules import TransformPipeline
from preprocess.transformers import (
    DropColumns,
    FillNa,
    DropNonImputable,
    DropIfEqual,
    QuantileFilter,
    NormalizeUrl,
    ApplyTransform,
)

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


def main():
    """Main function for console script to preprocess data"""

    # Preprocessing pipeline definition
    pipeline = TransformPipeline(
        [
            DropColumns(DROP_COLUMNS),
            DropNonImputable(NON_IMPUTABLE_COLUMNS),
            DropIfEqual(column_name="price", value=0),
            QuantileFilter(
                column_name="price", lower_quantile=0.05, upper_quantile=0.95
            ),
            NormalizeUrl(),
            ApplyTransform(column_name="year", transform_function=int),
            ApplyTransform(column_name="odometer", transform_function=int),
            FillNa(column_name="paint_color", value="unspecified"),
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
    dataframe = pd.read_csv(args.filename)

    if args.limit is None:
        args.limit = dataframe.shape[0]

    # Apply transformations and slice
    transformed = pipeline.fit_transform(dataframe)
    transformed = transformed.iloc[: args.limit]

    # Save transformed data & make directories if required
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    transformed.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
