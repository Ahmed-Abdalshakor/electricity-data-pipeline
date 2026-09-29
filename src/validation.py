import pandas as pd


def validate_data(file_path):
    print("\nRunning data quality checks...")

    df = pd.read_csv(file_path)

    # Check 1: Empty dataset
    if df.empty:
        raise ValueError("Validation failed: dataset is empty")

    # Check 2: Missing values
    if df.isnull().any().any():
        missing_values = df.isnull().sum()
        raise ValueError(
            f"Validation failed: missing values found:\n{missing_values}"
        )

    # Check 3: Duplicate dates
    if df["date"].duplicated().any():
        raise ValueError(
            "Validation failed: duplicate dates found"
        )

    # Check 4: Invalid demand values
    if (df["demand_twh"] <= 0).any():
        raise ValueError(
            "Validation failed: invalid demand values found"
        )

    # Check 5: Required columns
    required_columns = {
        "entity",
        "entity_code",
        "date",
        "demand_twh",
        "year",
        "month",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Validation failed: missing columns: {missing_columns}"
        )

    print("Data quality checks passed!")

    return True