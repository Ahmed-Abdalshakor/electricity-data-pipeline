import json
from pathlib import Path

import pandas as pd


def transform_data():
    # Input file
    input_file = Path(
        "data/raw/egypt_electricity_demand_monthly.json"
    )

    # Output directory
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Output file
    output_file = output_dir / "egypt_electricity_demand_monthly.csv"

    # Read raw JSON
    with open(input_file, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    # Extract actual records
    records = raw_data["data"]

    # Convert to DataFrame
    df = pd.DataFrame(records)

    # Select required columns
    df = df[
        [
            "entity",
            "entity_code",
            "date",
            "demand_twh",
        ]
    ]

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Add year and month
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    # Sort by date
    df = df.sort_values("date")

    # Remove duplicate dates
    df = df.drop_duplicates(subset=["date"])

    # Check missing values
    print("Missing values:")
    print(df.isnull().sum())

    # Save processed data
    df.to_csv(output_file, index=False)

    print("\nTransformation completed successfully!")
    print(f"Processed data saved to: {output_file}")
    print(f"Number of records: {len(df)}")

    return output_file