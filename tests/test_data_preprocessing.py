import pandas as pd

from src.data_preprocessing import clean_total_charges


def test_clean_total_charges_converts_values_and_blanks():
    raw_data = pd.DataFrame(
        {
            "TotalCharges": ["29.85", " ", "1889.5"],
            "tenure": [1, 0, 34],
        }
    )

    cleaned_data = clean_total_charges(raw_data)

    assert cleaned_data["TotalCharges"].dtype == "float64"
    assert cleaned_data["TotalCharges"].tolist()[0] == 29.85
    assert pd.isna(cleaned_data["TotalCharges"].tolist()[1])
    assert cleaned_data["TotalCharges"].tolist()[2] == 1889.5

    # The original input must remain unchanged.
    assert raw_data["TotalCharges"].tolist()[1] == " "