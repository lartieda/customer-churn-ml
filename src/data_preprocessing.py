"""Reusable data-cleaning functions for the churn project."""

import pandas as pd


def clean_total_charges(frame: pd.DataFrame) -> pd.DataFrame:
    """
    Return a copy with TotalCharges converted to numeric values.

    Blank or invalid values are converted to missing values (NaN) so that
    the machine-learning preprocessing pipeline can impute them later.
    """

    cleaned = frame.copy()

    cleaned["TotalCharges"] = pd.to_numeric(
        cleaned["TotalCharges"],
        errors="coerce",
    )

    return cleaned